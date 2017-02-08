## coding:UTF-8

from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as par
from os import makedirs
import os.path, time, re

# すでにダウンロードしたファイルを記憶
exit_files = {}

# HTML内にあるリンクを全て抽出する
def enum_links(html, base):
    soup = BeautifulSoup(html, "html.parser")
    # CSSのリンクを抽出
    links = soup.select("link[rel='stylesheet']")
    # その他のリンク(aタグ)を抽出
    links += soup.select("a[href]")
    # リンク部分(href)のみ抽出して絶対パスに変換、それをリストにまとめたものを返す.
    return [par.urljoin(base, a.attrs["href"]) for a in links]

# ファイルをダウンロードし保存する
def download_file(url):
    o = par.urlparse(url)
    savepath = "./" + o.netloc + o.path
    if re.search(r"/$", savepath):
        savepath += "index.html"
    savedir = os.path.dirname(savepath)
    if os.path.exists(savepath): return savepath
    if not os.path.exists(savedir):
        print("mkdir:", savedir)
        makedirs(savedir)
    try:
        print("download:", url)
        req.urlretrieve(url, savepath)
        time.sleep(1)
        return savepath
    except:
        print("ダウンロード失敗")
        return None

# HTMLを解析してダウンロードする
def analize_html(url, root_url):
    savepath = download_file(url)
    if savepath is None or savepath in exit_files: return
    exit_files[savepath] = True
    print("analize_html:",url)
    # HTML内のリンクを抽出
    html = open(savepath, "r", encoding="UTF-8").read()
    links = enum_links(html, url)
    for link_url in links:
        # 内部参照のもののみ処理(root_urlが冒頭に現れたかどうかで判断)
        if link_url.find(root_url) is not 0:
            # CSSはレイアウトが崩れる恐れが有るのでダウンロードするがそれ以外はスルー
            if not re.search(r".css$", link_url): continue
        # リンク先がHTML(新しいページ)か確認
        if re.search(r".(html|htm)$", link_url):
            # 再帰する
            analize_html(link_url, root_url)
            # 次のリンクの処理へ戻る
            continue
        # それ以外のファイルはダウンロード
        else:
            download_file(link_url)

def main():
    url = "http://docs.python.jp/3.3/library/"
    analize_html(url, url)

if __name__ == "__main__":
    main()
