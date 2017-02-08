## coding: UTF-8

from bs4 import BeautifulSoup

def main():
    html = """
    <ul id="bible">
        <li id="ge">Genesis</li>
        <li id="ex">Exodus</li>
        <li id="le">Leviticus</li>
        <li id="nu">Number</li>
        <li id="de">Deuteronomy</li>
    </ul>
    """
    soup = BeautifulSoup(html, "html.parser")
    # 指定したCSSセレクターから要素を取り出して表示する無名関数
    css_select = lambda q:print(soup.select_one(q).string)
    # Numberを取り出す例８つ
    css_select("#nu")
    css_select("li#nu")
    css_select("ul > li#nu")
    css_select("#bible #nu")
    css_select("#bible > #nu")
    css_select("ul#bible > li#nu")
    css_select("li[id='nu']")
    css_select("li:nth-of-type(4)")

    html = """
    <html><body>
    <div id="main-goods" role="page">
        <h1>フルーツや野菜</h1>
        <ul id="fr-list">
            <li class="red green" data-lo="jp">リンゴ</li>
            <li class="purple" data-lo="us">ブドウ</li>
            <li class="yellow" data-lo="us">レモン</li>
            <li class="yellow" data-lo="jp">オレンジ</li>
        </ul>
        <ul id="ve-list">
            <li class="white green" data-lo="jp">大根</li>
            <li class="red green" data-lo="us">パプリカ</li>
            <li class="black" data-lo="jp">ナス</li>
            <li class="black" data-lo="us">アボカド</li>
            <li class="white" data-lo="cn">レンコン</li>
        </ul>
    </div>
    </body></html>
    """
    soup=BeautifulSoup(html, "html.parser")
    css_select("ul#ve-list > li:nth-of-type(4)")
    cond = { "class":"black", "data-lo":"us" }
    print(soup.find(id="ve-list").find("li", cond).string)

if __name__ == "__main__":
    main()
