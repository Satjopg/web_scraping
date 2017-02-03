## coding: UTF-8
# urllibの中のrequestはwebサイトにあるデータにアクセスする機能を有する.
import urllib.request
import urllib.parse
import sys

# 接続情報を表示するapiを叩いて情報を表示.
def get_api_ip(url):
    # urlopenはapiの返り値をpythonのメモリ上に保存する(返り値はbinary)
    response = urllib.request.urlopen(url).read()
    text = response.decode("utf-8")
    print(text)

# 郵便番号をパラメータで送って住所を取得する。
def get_api_ad(url, params):
    data = urllib.request.urlopen(url).read()
    print(data.decode("UTF-8"))

# 100人一首からキーワードが含まれた歌を取得して表示する.
def get_api_hun(url, params):
    with urllib.request.urlopen(url) as data:
        print("「"+sys.argv[1]+"」"+"での検索結果")
        print(data.read().decode("UTF-8"))

def main():
    ip_url = "http://api.aoikujira.com/ip/ini"
    get_api_ip(ip_url)
    ad_url = "http://api.aoikujira.com/zip/xml/get.php"
    # fmt:返り値の形式の指定(json or xml)
    # zn:知りたい住所の郵便番号
    values = {
        "fmt":"xml",
        "zn":"1500042"
    }
    # パラメータに追加するためencode
    params = urllib.parse.urlencode(values)
    ad_url += "?" + params
    print("requestURL:"+ad_url)
    get_api_ad(ad_url, params)

    # コマンドライン引数はargv配列に格納されている.
    if len(sys.argv) <= 1:
        print("USAGE:$ dl-api.py (keyword)")
        sys.exit()
    search_word = sys.argv[1]
    hun_url = "http://api.aoikujira.com/hyakunin/get.php"
    query = {
        "fmt":"ini",
        "key":search_word
    }
    param = urllib.parse.urlencode(query)
    hun_url += "?" + param
    get_api_hun(hun_url, param)


if __name__ == '__main__':
    main()
