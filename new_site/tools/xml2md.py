"""One-time converter: PreTeXt XML (old site) -> Markdown chapters (new site).

Usage: python tools/xml2md.py <folder-with-old-xml> content/

Keeps the original structure: one Markdown file per chapter, `##` = section (its own
page, file name = the section's xml:id), `###` = subsection.
"""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

XML_ID = "{http://www.w3.org/XML/1998/namespace}id"
CHAPTERS = ["intro1.xml", "speechLab.xml", "Teaching.xml", "FundingList.xml"]
COUNT_IDS = {"countGraduatedPhD": "past-phd", "countGraduatedMEng": "past-meng"}
COUNT_HEADINGS = {"Past_PhD_Students": "past-phd", "Past_MEng_Students": "past-meng"}

TARGET = {}   # xml:id -> "page.html" or "page.html#anchor"


def ws(s):
    return re.sub(r"\s+", " ", s or "")


def inline(e):
    out = ws(e.text)
    for ch in e:
        out += inline_el(ch) + ws(ch.tail)
    return out


def inline_el(ch):
    t = ch.tag
    if t == "url":
        txt = inline(ch).strip().replace("`", "") or ch.get("href")
        href = ch.get("href", "").strip()
        if href and not re.match(r"^[a-z]+:", href):
            href = "https://" + href
        return f"[{txt}]({href})"
    if t == "c":
        return f"`{inline(ch).strip()}`"
    if t == "em":
        return f"*{inline(ch).strip()}*"
    if t == "alert":
        return f"**{inline(ch).strip()}**"
    if t == "xref":
        ref = ch.get("ref")
        txt = inline(ch).strip()
        if ref in COUNT_IDS:
            return f"{txt.rstrip('=').strip()}= {{{{count:{COUNT_IDS[ref]}}}}}"
        return f"[{txt or ref.replace('_', ' ')}]({TARGET.get(ref, '#' + ref)})"
    if t == "image":
        return f"![]({ch.get('source', '').lstrip('./')})"
    return inline(ch)


def lst(e, depth):
    ordered = e.tag == "ol"
    lines = []
    if ordered and e.get("label", "1").strip().startswith("a") and depth == 0:
        lines.append("<!-- list: a -->\n")
    pad = "    " * depth
    for li in e.findall("li"):
        text, subs = ws(li.text), []
        for ch in li:
            if ch.tag in ("ol", "ul"):
                subs.append(lst(ch, depth + 1))
            elif ch.tag == "p":
                text += " " + ws(ch.text)
                for sub in ch:
                    if sub.tag in ("ol", "ul"):
                        subs.append(lst(sub, depth + 1))
                    elif sub.tag == "p":
                        for inner in sub:
                            if inner.tag in ("ol", "ul"):
                                subs.append(lst(inner, depth + 1))
                        text += " " + inline(ET.fromstring("<p/>")) if False else " " + ws(sub.text) + "".join(
                            inline_el(i) + ws(i.tail) for i in sub if i.tag not in ("ol", "ul"))
                    else:
                        text += inline_el(sub)
                    text += ws(sub.tail)
            else:
                text += inline_el(ch)
            text += ws(ch.tail)
        text += ws(li.tail)                      # stray text written just after </li>
        lines.append(f"{pad}{'1.' if ordered else '-'} {text.strip()}")
        lines.extend(subs)
    return "\n".join(lines)


def blocks(e):
    out = []
    for ch in e:
        t = ch.tag
        if t in ("title", "section", "subsection"):
            continue
        if t in ("introduction", "stack"):
            out.append(blocks(ch))
        elif t == "sidebyside":
            widths = (ch.get("widths") or "50% 50%").split()
            panels = [blocks_of([p]) for p in ch]
            out.append(f"::: sidebyside {' '.join(widths)}\n" + "\n\n+++\n\n".join(panels) + "\n:::")
        elif t == "p":
            out.append(blocks_of([ch]))
        elif t in ("ol", "ul"):
            out.append(lst(ch, 0))
        elif t == "image":
            out.append(inline_el(ch))
        else:
            txt = inline(ch).strip()
            if txt:
                out.append(txt)
    return "\n\n".join(x for x in out if x)


def blocks_of(els):
    out = []
    for ch in els:
        if ch.tag in ("ol", "ul"):
            out.append(lst(ch, 0))
            continue
        if ch.tag == "image":
            out.append(inline_el(ch))
            continue
        buf = ws(ch.text)
        for sub in ch:
            if sub.tag in ("ol", "ul", "p", "sidebyside", "image"):
                if buf.strip():
                    out.append(buf.strip())
                if sub.tag in ("ol", "ul"):
                    out.append(lst(sub, 0))
                elif sub.tag == "p":           # paragraph nested inside a paragraph
                    out.append(blocks_of([sub]))
                else:
                    out.append(blocks(ET.Element("x")) if False else (inline_el(sub) if sub.tag == "image" else blocks_wrap(sub)))
                buf = ""
            else:
                buf += inline_el(sub)
            buf += ws(sub.tail)
        if buf.strip():
            out.append(buf.strip())
    return "\n\n".join(out)


def blocks_wrap(el):
    w = ET.Element("wrap"); w.append(el)
    return blocks(w)


def heading(e, level, xid):
    title = ws(e.findtext("title")).strip()
    attrs = [f"#{xid}"]
    if xid in COUNT_HEADINGS:
        attrs.append(f"data-count={COUNT_HEADINGS[xid]}")
    return "#" * level + f" {title} {{: {' '.join(attrs)} }}"


def main(src, dst):
    src, dst = Path(src), Path(dst)
    dst.mkdir(parents=True, exist_ok=True)
    roots = [ET.parse(src / f).getroot() for f in CHAPTERS]

    # pass 1: give every section/subsection an id the way PreTeXt does
    # (global counters: section-8, subsection-2, ...) and record link targets
    nsec = nsub = 0
    for root in roots:
        TARGET[root.get(XML_ID)] = root.get(XML_ID) + ".html"
        for sec in root.findall("section"):
            nsec += 1
            sid = sec.get(XML_ID) or f"section-{nsec}"
            sec.set(XML_ID, sid)
            TARGET[sid] = sid + ".html"
            for sub in sec.findall("subsection"):
                nsub += 1
                bid = sub.get(XML_ID) or f"subsection-{nsub}"
                sub.set(XML_ID, bid)
                TARGET[bid] = f"{sid}.html#{bid}"

    for n, root in enumerate(roots, 1):
        cid = root.get(XML_ID)
        parts = [f"---\ntitle: {ws(root.findtext('title')).strip()}\nid: {cid}\n---"]
        intro = blocks(root)
        if intro:
            parts.append(intro)
        for sec in root.findall("section"):
            parts.append(heading(sec, 2, sec.get(XML_ID)))
            body = blocks(sec)
            if body:
                parts.append(body)
            for sub in sec.findall("subsection"):
                parts.append(heading(sub, 3, sub.get(XML_ID)))
                body = blocks(sub)
                if body:
                    parts.append(body)
        text = "\n\n".join(parts) + "\n"
        text = re.sub(r"Last Updated: [^\n]*", "Last Updated: {{updated}}", text)
        text = re.sub(r"This web page was produced using \[PreTeXt\]\([^)]*\)",
                      "This web page is generated from Markdown, in the style of [PreTeXt](https://pretextbook.org/index.html)", text)
        name = f"{n}-{cid}.md"
        (dst / name).write_text(text, encoding="utf-8")
        print("wrote", dst / name)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
