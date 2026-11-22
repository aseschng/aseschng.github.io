"""Build the website (PreTeXt look) from Markdown.

    pip install markdown pyyaml
    python build.py            # writes the site to _site/
    python build.py --serve    # build, then preview at http://localhost:8000

content/ holds one Markdown file per chapter (1-intro1.md, 2-SpeechLab.md, ...):
  - text before the first `##` is the chapter's introduction
  - `## Title {: #page_name }`  starts a section; it becomes its own page, page_name.html
  - `### Title`                  starts a subsection inside that section
Numbers (2.1, 2.1.3 ...), the Contents sidebar and Prev/Up/Next are generated.
"""
import datetime as dt
import functools
import html as htmllib
import http.server
import re
import shutil
import sys
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).parent
CONTENT, OUT = ROOT / "content", ROOT / "_site"
TEMPLATE = (ROOT / "theme" / "page.html").read_text(encoding="utf-8")
SITE_TITLE = "Chng Eng Siong"
SGT = dt.timezone(dt.timedelta(hours=8), "SGT")   # Singapore time (GitHub's servers run on UTC)
TODAY = dt.datetime.now(SGT).strftime("%d %B %Y, %H:%M SGT").lstrip("0")


# ---------------------------------------------------------------- reading
def slug(text):
    return re.sub(r"[^A-Za-z0-9]+", "_", text).strip("_") or "s"


def split_heading(line):
    """'## Title {: #id data-count=x }' -> (title, id, attrs)"""
    m = re.match(r"#+\s+(.*?)\s*(\{:(.*?)\})?\s*$", line)
    title, attrs = m.group(1), (m.group(3) or "")
    hid = re.search(r"#([\w-]+)", attrs)
    return title, (hid.group(1) if hid else None), attrs


def read_chapters():
    chapters = []
    files = [p for p in CONTENT.glob("*.md") if re.match(r"\d+-", p.name)]   # 1-intro1.md, 2-SpeechLab.md, ...
    for path in sorted(files, key=lambda p: int(p.name.split("-")[0])):
        text = path.read_text(encoding="utf-8")
        _, fm, body = text.split("---", 2)
        meta = yaml.safe_load(fm)
        chap = {"title": meta["title"], "id": meta.get("id") or slug(meta["title"]),
                "intro": "", "sections": []}
        cur_sec = cur_sub = None
        buf = []

        def flush():
            target = cur_sub if cur_sub else (cur_sec if cur_sec else chap)
            target["intro" if target is not cur_sub else "body"] = "\n".join(buf)

        for line in body.splitlines():
            if line.startswith("## ") or line.startswith("### "):
                flush()
                buf = []
                title, hid, attrs = split_heading(line)
                if line.startswith("## "):
                    cur_sec = {"title": title, "id": hid or slug(title), "intro": "", "subs": []}
                    cur_sub = None
                    chap["sections"].append(cur_sec)
                else:
                    cur_sub = {"title": title, "id": hid or slug(title), "body": "", "attrs": attrs}
                    (cur_sec or chap.setdefault("_orphans", {"subs": []}))["subs"].append(cur_sub)
            else:
                buf.append(line)
        flush()
        chapters.append(chap)
    return chapters


def count_lists(chapters):
    """Count top-level items in lists under headings tagged data-count=NAME."""
    counts = {}
    for c in chapters:
        for s in c["sections"]:
            for sub in s["subs"]:
                m = re.search(r"data-count=([\w-]+)", sub["attrs"])
                if m:
                    counts[m.group(1)] = len(re.findall(r"^(\d+\.|[-*]) ", sub["body"], re.M))
    return counts


# ---------------------------------------------------------------- markdown -> PreTeXt-style HTML
def sidebyside(text):
    """::: sidebyside 85% 15%  panel  +++  panel  :::"""
    def repl(m):
        widths = m.group(1).split()
        panels = m.group(2).split("\n+++\n")
        cells = "".join(
            f'<div class="sbspanel" style="width:{widths[i] if i < len(widths) else "50%"};justify-content:center;">'
            f"{render(p, boxed_images=False)}</div>"
            for i, p in enumerate(panels)
        )
        return f'\n<div class="sidebyside"><div class="sbsrow" style="margin-left:0%;margin-right:0%;">{cells}</div></div>\n'

    return re.sub(r"^::: *sidebyside *([^\n]*)\n(.*?)\n:::\s*$", repl, text, flags=re.S | re.M)


def list_classes(html):
    """PreTeXt list styles: 1. a. i. for ol, disc/circle/square for ul."""
    ol_styles, ul_styles = ["decimal", "lower-alpha", "lower-roman"], ["disc", "circle", "square"]
    out, depth, pos = [], 0, 0
    alpha_next = False
    for m in re.finditer(r"<!-- list: a -->|<(/?)(ol|ul)>", html):
        out.append(html[pos:m.start()])
        pos = m.end()
        if m.group(0).startswith("<!--"):
            alpha_next = True
            continue
        closing, tag = m.group(1), m.group(2)
        if closing:
            depth -= 1
            out.append(f"</{tag}>")
        else:
            style = (ol_styles if tag == "ol" else ul_styles)[min(depth, 2)]
            if alpha_next and tag == "ol":
                style, alpha_next = "lower-alpha", False
            out.append(f'<{tag} class="{style}">')
            depth += 1
    out.append(html[pos:])
    return "".join(out)


def links_and_code(html):
    def link(m):
        attrs, text = m.group(1), m.group(2)
        href = re.search(r'href="([^"]*)"', attrs).group(1)
        if re.match(r"^(https?:|mailto:|ftp:)", href):
            inner = text if "<code" in text else f"<code>{text}</code>"
            return f'<a class="external" href="{href}" target="_blank">{inner}</a>'
        return f'<a href="{href}" class="internal">{text}</a>'

    html = re.sub(r"<a ([^>]*)>(.*?)</a>", link, html, flags=re.S)
    return html.replace("<code>", '<code class="code-inline tex2jax_ignore">')


def images(html, boxed):
    def img(m):
        src = re.search(r'src="([^"]*)"', m.group(0)).group(1)
        tag = f'<img src="{src}" style="width: 100%; height: auto;" alt="">'
        if not boxed:
            return tag
        return f'<div class="image-box" style="width: 100%; margin-left: 0%; margin-right: 0%;">{tag}</div>'

    return re.sub(r"<img [^>]*>", img, html)


def render(text, boxed_images=True):
    text = sidebyside(text)
    html = markdown.markdown(text, extensions=["attr_list", "md_in_html", "tables", "sane_lists"])
    return images(links_and_code(list_classes(html)), boxed_images)


# ---------------------------------------------------------------- page assembly
def heading(kind, tag, number, title, hide_type=True):
    cls = "heading hide-type" if hide_type else "heading"
    return (f'<{tag} class="{cls}">\n<span class="type">{kind}</span> <span class="codenumber">{number}</span> '
            f'<span class="title">{htmllib.escape(title, quote=False)}</span>\n</{tag}>')


def summary_links(items):
    lis = "".join(f'<li><a href="{u}"><span class="codenumber">{n}</span> <span class="title">{t}</span></a></li>'
                  for n, t, u in items)
    return f'<nav class="summary-links"><ul>{lis}</ul></nav>'


def build():
    chapters = read_chapters()
    counts = count_lists(chapters)

    def fill(s):
        s = re.sub(r"\{\{count:([\w-]+)\}\}", lambda m: str(counts.get(m.group(1), "?")), s)
        return s.replace("{{updated}}", TODAY)

    # list of pages in reading order: (file, title, up-file, content-html, active-id)
    pages = []
    book_items = [(i, c["title"], c["id"] + ".html") for i, c in enumerate(chapters, 1)]
    pages.append({"file": "default.html", "title": SITE_TITLE, "up": None, "active": None,
                  "html": f'<section class="book" id="default">{summary_links(book_items)}</section>'})

    for ci, c in enumerate(chapters, 1):
        cfile = c["id"] + ".html"
        body = f'<section class="chapter" id="{c["id"]}">' + heading("Chapter", "h2", ci, c["title"], False)
        body += f'<a href="{cfile}" class="permalink">¶</a>'
        intro = render(fill(c["intro"])) if c["intro"].strip() else ""
        if intro:
            body += f'<section class="introduction" id="introduction-{ci}">{intro}</section>'
        if c["sections"]:
            body += summary_links([(f"{ci}.{si}", s["title"], s["id"] + ".html")
                                   for si, s in enumerate(c["sections"], 1)])
        body += "</section>"
        pages.append({"file": cfile, "title": c["title"], "up": "default.html", "active": c["id"], "html": body})

        for si, s in enumerate(c["sections"], 1):
            sfile = s["id"] + ".html"
            body = f'<section class="section" id="{s["id"]}">' + heading("Section", "h2", f"{ci}.{si}", s["title"])
            body += f'<a href="{sfile}" class="permalink">¶</a>'
            sintro = render(fill(s["intro"])) if s["intro"].strip() else ""
            if s["subs"]:
                if sintro:
                    body += f'<section class="introduction" id="introduction-{s["id"]}">{sintro}</section>'
                for bi, b in enumerate(s["subs"], 1):
                    body += (f'<section class="subsection" id="{b["id"]}">'
                             + heading("Subsection", "h3", f"{ci}.{si}.{bi}", b["title"])
                             + render(fill(b["body"])) + "</section>")
            else:
                body += sintro
            body += "</section>"
            pages.append({"file": sfile, "title": s["title"], "up": cfile, "active": s["id"], "html": body})

    toc = toc_html(chapters)
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    version = dt.datetime.now().strftime("%Y%m%d%H%M%S")
    for i, p in enumerate(pages):
        prev = pages[i - 1]["file"] if i > 0 else None
        nxt = pages[i + 1]["file"] if i + 1 < len(pages) else None
        page_toc = toc
        if p["active"]:
            page_toc = page_toc.replace(f'data-scroll="{p["active"]}"', f'data-scroll="{p["active"]}" class="active"', 1)
        html = (TEMPLATE.replace("{{title}}", htmllib.escape(p["title"]))
                .replace("{{site_title}}", SITE_TITLE)
                .replace("{{buttons_top}}", nav_buttons(prev, p["up"], nxt, top=True))
                .replace("{{buttons_bottom}}", nav_buttons(prev, p["up"], nxt, top=False))
                .replace("{{toc}}", page_toc)
                .replace("{{content}}", p["html"])
                .replace("{{updated}}", TODAY)
                .replace("{{version}}", version))
        (OUT / p["file"]).write_text(html, encoding="utf-8")
    (OUT / "index.html").write_text(
        '<!DOCTYPE html><html><head><meta charset="UTF-8">'
        '<meta http-equiv="refresh" content="0; URL=\'default.html\'"></head><body></body></html>', encoding="utf-8")
    print(f"built {len(pages)} pages into {OUT}")

    images = ROOT / "images" if (ROOT / "images").exists() else ROOT.parent / "images"
    shutil.copytree(images, OUT / "images")
    shutil.copytree(ROOT / "theme", OUT / "theme", ignore=shutil.ignore_patterns("page.html"))
    (OUT / ".nojekyll").write_text("")


def toc_html(chapters):
    out = []
    for ci, c in enumerate(chapters, 1):
        link = (f'<a href="{c["id"]}.html" data-scroll="{c["id"]}"><span class="codenumber">{ci}</span> '
                f'<span class="title">{c["title"]}</span></a>')
        subs = "".join(f'<li><a href="{s["id"]}.html" data-scroll="{s["id"]}">{s["title"]}</a></li>'
                       for s in c["sections"])
        out.append(f'<li class="link">{link}' + (f"<ul>{subs}</ul>" if subs else "") + "</li>")
    return '<nav id="toc"><ul>' + "".join(out) + "</ul></nav>"


def nav_buttons(prev, up, nxt, top):
    def btn(cls, href, label, bid):
        idattr = f' id="{bid}"' if top else ""
        if href:
            return f'<a{idattr} class="{cls} button toolbar-item" href="{href}" title="{label}">{label}</a>'
        return f'<span{idattr} class="{cls} button toolbar-item disabled">{label}</span>'

    b = (btn("previous-button", prev, "Prev", "previousbutton") + btn("up-button", up, "Up", "upbutton")
         + btn("next-button", nxt, "Next", "nextbutton"))
    return f'<span class="threebuttons">{b}</span>' if top else b


if __name__ == "__main__":
    build()
    if "--serve" in sys.argv:
        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(OUT))
        print("Preview at http://localhost:8000  (Ctrl+C to stop)")
        http.server.ThreadingHTTPServer(("", 8000), handler).serve_forever()
