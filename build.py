"""Convert AAT_notes_zh.md + AAT_notes.md -> index.html (中文/原文切換; math rendered by KaTeX).

Usage: python -X utf8 build.py
Requires: pip install markdown
"""
import html
import re
from pathlib import Path

import markdown

ROOT = Path(__file__).parent


def convert(src, prefix):
    """Markdown (with $...$ math) -> (body_html, toc_html)."""
    # 1. Protect math from the Markdown parser (underscores, asterisks, backslashes).
    maths = []

    def stash(m):
        maths.append(m.group(0))
        return f"MATHTOKEN{len(maths) - 1:05d}X"

    # Skip fenced code blocks while stashing math.
    parts = re.split(r"(```.*?```)", src, flags=re.S)
    for i, p in enumerate(parts):
        if p.startswith("```"):
            continue
        p = re.sub(r"\$\$.+?\$\$", stash, p, flags=re.S)
        p = re.sub(r"(?<!\\)\$[^$\n]+?\$", stash, p)
        parts[i] = p
    protected = "".join(parts)

    # 2. Markdown -> HTML. Heading ids are prefixed per language so they stay unique.
    counter = iter(range(10**6))
    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "toc", "sane_lists"],
        extension_configs={"toc": {"toc_depth": "2",
                                   "slugify": lambda v, s: f"{prefix}-{next(counter)}"}})
    body = md.convert(protected)
    toc = md.toc

    # 3. Restore math (HTML-escaped; KaTeX auto-render reads text nodes).
    restore = lambda m: html.escape(maths[int(m.group(1))], quote=False)
    body = re.sub(r"MATHTOKEN(\d{5})X", restore, body)
    toc = re.sub(r"MATHTOKEN(\d{5})X", restore, toc)

    # Wrap tables so wide ones scroll on small screens.
    body = body.replace("<table>", '<div class="tbl"><table>').replace("</table>", "</table></div>")
    return body, toc, len(maths)


body_en, toc_en, n_en = convert((ROOT / "AAT_notes.md").read_text(encoding="utf-8"), "en")
body_zh, toc_zh, n_zh = convert((ROOT / "AAT_notes_zh.md").read_text(encoding="utf-8"), "zh")

TEMPLATE = """<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AAT 課程筆記</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}],throwOnError:false,ignoredTags:['script','noscript','style','textarea','pre','code']});"></script>
<style>
:root {
  --bg: #fbfaf7; --fg: #1f2328; --muted: #6a6f76; --accent: #b4532a;
  --line: #e3dfd6; --code: #f2efe8; --quote: #f6f1e7;
}
@media (prefers-color-scheme: dark) {
  :root { --bg: #16181c; --fg: #e6e6e3; --muted: #9aa0a6; --accent: #e8915f;
          --line: #2e3238; --code: #22262c; --quote: #1f2329; }
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { margin: 0; background: var(--bg); color: var(--fg);
  font: 17px/1.75 "Noto Serif TC", "Source Han Serif TC", Georgia, "PMingLiU", serif; }
.layout { display: grid; grid-template-columns: 240px minmax(0, 1fr); max-width: 1200px; margin: 0 auto; }
nav { position: sticky; top: 0; height: 100vh; overflow-y: auto; padding: 32px 16px 32px 24px;
  border-right: 1px solid var(--line); font: 14px/1.6 system-ui, "Microsoft JhengHei", sans-serif; }
nav .brand { font-weight: 700; color: var(--accent); margin-bottom: 12px; letter-spacing: .05em; }
nav ul { list-style: none; margin: 0; padding: 0; }
nav li { margin: 2px 0; }
nav a { color: var(--muted); text-decoration: none; display: block; padding: 2px 6px; border-radius: 4px; }
nav a:hover { color: var(--fg); background: var(--code); }
main { padding: 40px 48px 120px; min-width: 0; }
h1 { font-size: 2rem; margin: 0 0 .5em; color: var(--accent); }
h2 { font-size: 1.35rem; margin: 2.4em 0 .8em; padding-bottom: .3em; border-bottom: 2px solid var(--line);
  font-family: system-ui, "Microsoft JhengHei", sans-serif; }
h3 { font-size: 1.1rem; margin: 1.8em 0 .6em; font-family: system-ui, "Microsoft JhengHei", sans-serif; }
hr { border: 0; border-top: 1px dashed var(--line); margin: 3em 0; }
strong { color: var(--accent); font-weight: 700; }
blockquote { margin: 1em 0; padding: .6em 1em; background: var(--quote); border-left: 4px solid var(--accent);
  color: var(--muted); border-radius: 0 6px 6px 0; }
blockquote p { margin: .3em 0; }
pre { background: var(--code); padding: 12px 16px; border-radius: 6px; overflow-x: auto;
  font: 14px/1.5 ui-monospace, Consolas, "MingLiU", monospace; }
.tbl { overflow-x: auto; margin: 1em 0; }
table { border-collapse: collapse; font-size: .95em; }
th, td { border: 1px solid var(--line); padding: 4px 10px; text-align: center; white-space: nowrap; }
th { background: var(--code); }
.katex-display { overflow-x: auto; overflow-y: hidden; padding: 4px 0; }
@media (max-width: 860px) {
  .layout { display: block; }
  nav { position: static; height: auto; border-right: 0; border-bottom: 1px solid var(--line); padding: 16px; }
  nav ul { columns: 2; }
  main { padding: 24px 16px 80px; }
  body { font-size: 16px; }
}
.lang-switch { display: flex; gap: 4px; margin-bottom: 16px; }
.lang-switch button { flex: 1; padding: 6px 0; border: 1px solid var(--line); background: transparent;
  color: var(--muted); border-radius: 6px; cursor: pointer; font: inherit; }
.lang-switch button[aria-pressed="true"] { background: var(--accent); border-color: var(--accent); color: #fff; }
body[data-lang="en"] [data-lang-only="zh"], body[data-lang="zh"] [data-lang-only="en"] { display: none; }
@media print { nav { display: none; } .layout { display: block; } }
</style>
</head>
<body data-lang="zh">
<div class="layout">
<nav>
  <div class="brand">AAT 筆記目錄</div>
  <div class="lang-switch">
    <button type="button" data-set-lang="zh">中文</button>
    <button type="button" data-set-lang="en">原文</button>
  </div>
  <div data-lang-only="zh">__TOC_ZH__</div>
  <div data-lang-only="en">__TOC_EN__</div>
</nav>
<main>
<div data-lang-only="zh" lang="zh-Hant">
__BODY_ZH__
</div>
<div data-lang-only="en" lang="en">
__BODY_EN__
</div>
</main>
</div>
<script>
(function () {
  var buttons = document.querySelectorAll('[data-set-lang]');
  function setLang(lang) {
    document.body.setAttribute('data-lang', lang);
    buttons.forEach(function (b) { b.setAttribute('aria-pressed', b.dataset.setLang === lang); });
    try { localStorage.setItem('aat-lang', lang); } catch (e) {}
  }
  var saved = null;
  try { saved = localStorage.getItem('aat-lang'); } catch (e) {}
  setLang(saved === 'en' ? 'en' : 'zh');
  buttons.forEach(function (b) {
    b.addEventListener('click', function () { setLang(b.dataset.setLang); window.scrollTo(0, 0); });
  });
})();
</script>
</body>
</html>
"""

out = (TEMPLATE.replace("__TOC_ZH__", toc_zh).replace("__TOC_EN__", toc_en)
       .replace("__BODY_ZH__", body_zh).replace("__BODY_EN__", body_en))
(ROOT / "index.html").write_text(out, encoding="utf-8")
print(f"index.html written: {len(out):,} chars, math blocks en={n_en} zh={n_zh}")
