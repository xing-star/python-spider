# _*_ coding: UTF-8 _*_
from urllib import request
import chardet
import io
import sys
# 改变标准输出的默认编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

if __name__ == "__main__":
    response = request.urlopen("http://fanyi.baidu.com/")
    html = response.read()
    charset = chardet.detect(html)
    html = html.decode(charset["encoding"])
    print (charset)
    print (html)
