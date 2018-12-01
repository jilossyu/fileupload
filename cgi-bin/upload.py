#!/usr/bin/env python
# coding: utf-8

import cgi
import cgitb; cgitb.enable()
import os, sys

print "Content-Type: text/html; charset=utf-8"

UPLOAD_DIR = "./img"

# フォーマット文字の作成
html_body = """
<html><body>
%s
</body></html>"""

def save_uploaded_file (upload_dir):
    form = cgi.FieldStorage()
    if not form.has_key("file"):
        print html_body % form.getvalue('foo', 'ファイルを入力してください')
        return
    fileitem = form["file"]
    if not fileitem.file:
        print html_body % form.getvalue('foo', 'ファイルを入力してください')
        return

    fout = file (os.path.join(upload_dir, "test_" + os.path.basename(fileitem.filename)), 'wb')
    while 1:
        chunk = fileitem.file.read(100000)
        if not chunk: break
        fout.write (chunk)
    fout.close()
    print html_body % form.getvalue('foo', '送信しました')

save_uploaded_file(UPLOAD_DIR)
