## coding: UTF-8

from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as par

def get_exchange_data(url, values):
    params = par.urlencode(values)
    return data_extraction(data=req.urlopen(url + "?" + params))

def data_extraction(data):
    soup = BeautifulSoup(data, "html.parser")
    # ソース見るとtdの.stoksPriceというクラスが対応してるからそこを取り出す
    return soup.select_one(".stoksPrice").string

def main():
    # yahoo!ファイナンスのURL
    finance_url = "http://stocks.finance.yahoo.co.jp/stocks/detail"
    # 円とドルの情報を知るためにパラメータを設定
    values = {"code":"USDJPY"}
    print("usd/jpy:" + get_exchange_data(finance_url, values) + "円")
    # 円とユーロの情報が知りたい時
    values["code"] = "EURJPY"
    print("eur/jpy:" + get_exchange_data(finance_url, values) + "円")
    values["code"] = "GBPJPY"
    print("gbp/jpy:" + get_exchange_data(finance_url, values) + "円")


if __name__ == "__main__":
    main()
