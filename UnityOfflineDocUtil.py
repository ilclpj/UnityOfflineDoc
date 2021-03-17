#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import shutil
import time

import bs4
import re
from bs4 import UnicodeDammit

def write_xml(text, out_path):
    # print(text)
    # text = text.encode("utf-8")
    # dammit = UnicodeDammit(text, ["utf-8"], smart_quotes_to="html")
    # print(dammit.unicode_markup)
    # UnicodeDammit(markup, ["windows-1252"], smart_quotes_to="html").unicode_markup
    with open(out_path, mode='w', encoding='utf-8') as f:
        f.write(text)

def filter_html(html_path, out_path):
    with open(html_path, "rb") as f:
        text = str(f.read(), encoding="utf-8")
        text = re.sub(u"&quot;", "'", text)

        soup = bs4.BeautifulSoup(text, features="lxml")
        for elem in soup.select('link'):
            if "href" in elem.attrs and elem.attrs["href"].find("google") != -1:
                elem.extract()

        for elem in soup.select('script'):
            if len(elem) > 0 and elem.contents[0].find("google") != -1:
                elem.extract()

        for elem in soup.select('iframe'):
            if "src" in elem.attrs and elem.attrs["src"].find("google") != -1:
                elem.extract()

        write_xml(soup.prettify(), out_path)

        # text = str(f.read(), encoding="utf-8")
        # text = re.sub(u"&quot;", u"----", text)

def handle_common_dir(dir_path, out_dir):
    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)

    shutil.copytree(dir_path, out_dir)

def filter_dir(dir_path, out_dir):
    print("处理文件夹: [{}] ----------------> ".format(dir_path))

    old_time = time.time()

    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)

    os.makedirs(out_dir)

    docdata = os.path.join(dir_path, "docdata")
    if os.path.exists(docdata):
        shutil.copytree(docdata, os.path.join(out_dir, "docdata"))

    limit = 1000000
    base_count = 200
    flag = 0

    for root, dirs, files in os.walk(dir_path):
        length = min(limit, len(files))

        for index, name in enumerate(files):
            if name.find(".html") == -1:
                continue

            path = os.path.join(root, name)
            out_path = os.path.join(out_dir, name)
            # print("-----> filter file: \"{}\"".format(name))

            if flag > base_count and ((flag % base_count) == 0 or (index == length - 1)):
                print("正在处理第: {}个文件".format(flag))

            try:
                flag = flag + 1
                filter_html(path, out_path)
            except Exception as e:
                print("执行出错: " + str(e))

            if index == length - 1:
                break

    print("----> 执行耗时: {}".format(time.time() - old_time))

# ---------------------------------------------------------------------------

print("开始执行, 请等待!")

source_dir = "D:/Personal/learn/unity/Documents/2017.1"
out_dir = os.path.join(source_dir, "out")

# 处理公共部分
staticFiles_source_dir = os.path.join(source_dir, "StaticFiles")
uploads_source_dir = os.path.join(source_dir, "uploads")

staticFiles_out_dir = os.path.join(out_dir, "StaticFiles")
uploads_out_dir = os.path.join(out_dir, "uploads")

handle_common_dir(staticFiles_source_dir, staticFiles_out_dir)
handle_common_dir(uploads_source_dir, uploads_out_dir)

# ---------------------------------------------------------------------------

# 处理手册
manual_source_dir = os.path.join(source_dir, "Manual")
manual_out_dir = os.path.join(out_dir, "Manual")

filter_dir(manual_source_dir, manual_out_dir)

# ---------------------------------------------------------------------------

# 处理脚本API
script_source_dir = os.path.join(source_dir, "ScriptReference")
script_out_dir = os.path.join(out_dir, "ScriptReference")

filter_dir(script_source_dir, script_out_dir)