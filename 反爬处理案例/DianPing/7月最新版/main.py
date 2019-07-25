# -*- coding: utf-8 -*-
# __author__ = "zok"  362416272@qq.com
# Date: 2019-07-25  Python: 3.7

"""
调用例子
"""

from font import ParseFontClass

# 这里需要传入页面中包含字体链接的 css 网址

pf = ParseFontClass('http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/8945b511eb964a95fe071d4852a7ef03.css')

# 此处为页面上加密的 新华路 三个字

print(pf.parse_ttf('&#xe2cc;'))
print(pf.parse_ttf('&#xed59;'))
print(pf.parse_ttf('&#xe169;'))
