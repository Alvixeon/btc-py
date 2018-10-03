#imports
import requests,lxml
from lxml import html
#end imports

#globals
global trm
#end globals

def Coin_Price(data):
        full_coin_name = convert(data)
        pageContent=requests.get("https://coinmarketcap.com/currencies/{0}/".format(full_coin_name))
        tree = html.fromstring(pageContent.content)
        final = tree.xpath('//*[@id="quote_price"]//text()')
        finstr = ''.join(final)
        return finstr
def convert(data):
        if data == "btc":return 'bitcoin'
        elif data == "eth":return 'ethereum'
        elif data == "ltc":return 'litecoin'
        elif data == "bch":return 'bitcoin-cash'
        elif data == "xmr":return 'monero'
        elif data == "neo":return 'neo'
        elif data == "sc":return 'siacoin'
        elif data == "xrp":return 'ripple'
        elif data == "dash":return 'dash'
        elif data == "xem":return 'nem'
        elif data == "bcc":return 'bitconnect'
        elif data == "miota":return 'iota'
        elif data == "doge":return 'dogecoin'
def supported():
	return ["btc", "eth", "ltc", "bch", "xmr","neo","sc","xrp","dash","xem","bcc","miota","doge"]
