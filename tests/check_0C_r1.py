"""0C 第一輪的檢查：網頁有使用說明。"""
from checklib import check, read_source

src = read_source("ui.py")

check("0C-r1 有 HELP_TEXT", "HELP_TEXT = " in src, True)
check("0C-r1 說明含三種用法", all(w in src for w in ["撿到東西", "找東西", "認領："]), True)
check("0C-r1 網頁有顯示 HELP_TEXT", "gr.Markdown(HELP_TEXT)" in src, True)