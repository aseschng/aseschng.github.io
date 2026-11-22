# Website: Markdown → PreTeXt-style HTML

Replaces the old PreTeXt XML + xsltproc pipeline. The look, page names and numbering are the same as the old site (Contents sidebar, Prev / Up / Next, 2.1, 2.1.3 ...). Only the source format changed: you now edit Markdown, and a small Python script builds the pages.

## Updating the site

1. Edit the chapter file in `content/`:

   | File | Chapter |
   |---|---|
   | `content/1-intro1.md` | 1 Introduction |
   | `content/2-SpeechLab.md` | 2 Speech and Language Laboratory (lab, collaborators, staff, students, interns) |
   | `content/3-Teaching.md` | 3 Teaching Activities |
   | `content/4-FundlingList.md` | 4 Fundings |

2. Preview: `python build.py --serve`, then open http://localhost:8000 (first time only: `pip install markdown pyyaml`).
3. Commit and push. Once the GitHub workflow is switched on (see below), the live site updates by itself.

## How a chapter file is laid out

```markdown
---
title: Speech and Language Laboratory
id: SpeechLab                         ← the chapter's page name (SpeechLab.html)
---

Text here (before the first ##) is the chapter introduction.

## Current PhD and Graduate Students {: #my_Students }      ← section 2.4, its own page: my_Students.html

1. [Liu Changsong](https://linkedin.com/...), thesis title (PhD reg Aug 2026)
1. [Wu Mengjun](https://linkedin.com/...), ...

### Current MEng and Masters Program Students {: #my_MSAI_Students }   ← subsection 2.4.2
```

- Numbers (2.4, 2.4.2), the Contents sidebar and Prev / Up / Next are generated. Never type them.
- The `{: #name }` after a `##` heading sets the page's file name. Keep the existing ones so old links keep working; for a new section pick any short name.
- **Links:** `[text](https://...)` shows in the PreTeXt boxed style automatically.
- **Code-style words** (like the old `<c>`): put backticks around them, `` `ASR and LLM` ``.
- **Lists:** every item starts with `1.`; they are numbered automatically. A sub-list is indented 4 spaces and shows as a, b, c. To make a top-level list use a, b, c, put `<!-- list: a -->` on the line before it.
- **Images:** copy the file into the repository's `images/` folder and write `![](images/photo.jpg)`.
- **Text beside a picture** (the old `<sidebyside>`):

  ```
  ::: sidebyside 85% 15%
  Text on the left...

  +++

  ![](images/es2_small.jpg)
  :::
  ```

## Common updates

| Change | What to do |
|---|---|
| New Masters student | Add a line under `### Current MEng and Masters Program Students` in `2-SpeechLab.md` |
| New PhD student | Add a line under `## Current PhD and Graduate Students` |
| Student graduates | Move the line to `### Past PhD Students` or `### Past MEng`. The "supervised (PhD Students)= 28" count on the Introduction updates by itself. |
| New grant | Add a line under `## Current Fundings` in `4-FundlingList.md` |
| "Last Updated" date | Automatic (`{{updated}}`) |

## Files

- `build.py`: the generator
- `theme/page.html`: page layout (same HTML structure as the old PreTeXt pages, using the same PreTeXt stylesheets from pretextbook.org)
- `theme/custom.css`: put any of your own style tweaks here
- `tools/xml2md.py`: one-time converter used to migrate the old XML (kept for reference)
- `build-site.workflow.yml`: GitHub Action that builds and publishes the site

## Switching the live site over (once)

1. Copy `new_site/build-site.workflow.yml` to `.github/workflows/build-site.yml` at the repository root.
2. On GitHub: Settings → Pages → Source = **GitHub Actions**.
3. Run the workflow once from the Actions tab, check the site, then uncomment the `push:` trigger in the workflow.

The page names are the same as before (`default.html`, `intro1.html`, `my_Students.html` ...), so existing links and bookmarks keep working.
