## coding: UTF-8
from bs4 import BeautifulSoup

def main():
    # 解析する対象を生成(本来はwebページから抽出される箇所)
    html = """
    <html><body>
        <h1 id="title">スクレイピングとは？</h1>
        <p>webページを解析して</p>
        <p id="body">任意の箇所を抽出すること</p>
    </body></html>
    """
    # BeautifulSoupのインスタンスを生成(htmlのパーサーを指定する事で区切られる)
    soup = BeautifulSoup(html, "html.parser")

    # 任意の箇所を抽出！！
    h1 = soup.html.body.h1
    p1 = soup.html.body.p
    p2 = p1.next_sibling.next_sibling

    # テキスト表示(文字列を取り出す。)
    print("h1:" + h1.string)
    print("p:" + p1.string)
    print("p:" + p2.string)

    # findメソッドを使うとid名を指定することで任意の箇所から取り出すことが可能
    print("title:" + soup.find(id="title").string)
    print("body:" + soup.find(id="body").string)

    # find_allメソッドで複数のタグを一括で抽出できる
    ptags = soup.find_all("p")
    for p in ptags:
        print(p.string)

if __name__ == "__main__":
    main()
