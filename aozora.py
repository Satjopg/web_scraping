## coding: UTF-8

from bs4 import BeautifulSoup
import urllib.request as req

def get_aozora(url):
    return worklist_extraction(data=req.urlopen(url))

def worklist_extraction(data):
    soup = BeautifulSoup(data, "html.parser")
    return soup.select("ol:nth-of-type(1) > li")

def main():
    aozora_url = "http://www.aozora.gr.jp/index_pages/person148.html#sakuhin_list_1"
    for index, li in enumerate(get_aozora(aozora_url)):
        a = li.a
        if a is not None:
            print(str(index+1)+":"+a.string)

if __name__ == "__main__":
    main()
