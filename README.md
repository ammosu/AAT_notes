# AAT 課程筆記

代數自動機理論（Algebraic Automata Theory）手寫課程筆記的文字版：半群、自由半群、自動機、群半自動機與句法近環。

| 檔案 | 說明 |
|---|---|
| `index.html` | 可直接用瀏覽器開啟的網頁版，左上角可切換「中文／原文」，數學式由 KaTeX 渲染（需連網載入 KaTeX） |
| `AAT_notes_zh.md` | 中文翻譯版 Markdown |
| `AAT_notes.md` | 原文（英文）轉錄版 Markdown |
| `build.py` | 由兩份 Markdown 重新產生 `index.html` |

## 重新產生網頁

```bash
pip install markdown
python -X utf8 build.py
```

## 說明

- 內容由 16 張手寫掃描頁（AAT001–AAT016）轉錄，依頁碼排列。
- `[?]` 表示原稿無法辨識之處；「（註：…）」為轉錄時加上的更正或說明。
- 第 14、15 頁的近環運算表已依定義用程式重新計算核對。
