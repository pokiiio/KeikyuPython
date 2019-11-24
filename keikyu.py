# coding=utf-8

import urllib2
from HTMLParser import HTMLParser


def get_unko():
    # 京急運行情報のパーサー
    class KeikyuUnkoParser(HTMLParser):

        def __init__(self):
            HTMLParser.__init__(self)
            self.flag = False
            self.unko = ""

        # divタグで、classが"unko-panel"なものを探す
        def handle_starttag(self, tag, attrs):
            attrs = dict(attrs)
            if tag == "a" and "href" in attrs and attrs["href"] == "https://unkou.keikyu.co.jp/" and "target" in attrs and attrs["target"] == "_blank":
                self.flag = True

        # 上記の条件に合致するタグが発見できたら、そのタグで囲まれているdataを読み取る
        def handle_data(self, data):
            if self.flag:
                self.unko = self.unko + data

        # divタグ終了時に読み取り終了
        def handle_endtag(self, tag):
            self.flag = False

        # 読み取った運行情報を整形して返す
        def get_unko(self):
            return self.unko.replace("\n", "").replace("\r", "").decode("utf-8")

    # 京急の運行情報ページ
    url = "http://unkou.keikyu.co.jp/"

    # 運行情報ページを取得
    response = urllib2.urlopen(url)

    # パーサーに食わせる
    parser = KeikyuUnkoParser()
    parser.feed(response.read())

    # 諸々close()
    parser.close()
    response.close()

    # 運行情報を返す
    return parser.get_unko()
