## coding: UTF-8

from bs4 import BeautifulSoup

def main():
    html = """
    <html><body>
    <div id="meigen">
        <h1>名言たち</h1>
        <ul class="items">
            <li>汝の心に教えよ、心に学ぶな</li>
            <li>謙虚な人は誰からも好かれる</li>
            <li>ねだるな、さすれば与えられん</li>
        </ul>
    </div>
    </body><html>
    """

    soup = BeautifulSoup(html, "html.parser")

    # CSSクエリを用いて抽出可能
    print("h1:" + soup.select_one("div#meigen > h1").string)

    # リストのような複数要素を含むものの抽出例
    for i, item in enumerate(soup.select("div#meigen > ul.items > li")):
        print(str(i+1)+"番目の名言:" + item.string)

if __name__ == "__main__":
    main()
