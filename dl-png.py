## coding: UTF-8

import urllib.request

def get_png_retrieve(url, savename):
    urllib.request.urlretrieve(url, savename)
    print("保存しました.")

def get_png_open(url, savename):
    mem = urllib.request.urlopen(url).read()
    with open(savename, mode="wb") as f:
        f.write(mem)
        print("保存しました.")

def main():
    url = "http://uta.pw/shodou/img/28/214.png"
    savename = "test.png"
    #get_png_retrieve(url, savename)
    get_png_open(url, savename)

if __name__ == '__main__':
    main()
