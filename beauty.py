from bs4 import BeautifulSoup


def beautySoup(text):
    bt = None
    try:
      bt = BeautifulSoup(text, "lxml")
    except:
      bt = BeautifulSoup(text, "html")
    return bt
