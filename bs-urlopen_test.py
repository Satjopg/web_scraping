## coding: UTF-8

from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as par

def get_api(url):
    return req.urlopen(url)

def main():
    ad_url = "http://api.aoikujira.com/zip/xml/get.php"
    values = {
        "fmt":"xml",
        "zn":"1500042"
    }
    params = par.urlencode(values)
    ad_url += "?" + params
    response = get_api(url=ad_url)
    soup = BeautifulSoup(response, "html.parser")
    print("都道府県:" + soup.find("ken").string)
    print("市区:" + soup.find("shi").string)
    print("町村:" + soup.find("cho").string)

if __name__ == "__main__":
    main()
