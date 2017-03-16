import re
import requests

def getHTMLTest(url):
	try:
		r = requests.get(url, timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""

def parsePage(ilt, html):
	try:
		plt = re.findall(r'<strong>58.00</strong>', html)
		#最后我实在是找不到解决的办法了，试着用老师的源码，结果成功了，最终弄明白是浏览器的原因
		#以后查看页面源码再也不用这个了，改用Firefox
		print(plt)
		tlt = re.findall(r'</span>\n*?\n<span', html)
		for i in range(len(plt)):
			price = plt[i]
			title = tlt[i]
			ilt.append([price, title])
	except:
		print("")

def printGoodList(ilt):
	tplt = "{:4}\t{:8}\t{:16}"
	print(tplt.format("序号", "价格", "商品名称"))
	count = 0
	for g in ilt:
		count += 1
		print(tplt.format(count, g[0], g[1]))

def main():
	goods = "书包"
	depth = 2
	start_url = 'http://s.taobao.com/search?' + goods +'&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.50862.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170316&bcoffset=1&ntoffset=1&p4ppushleft=1%2C48'
	infoList = []
	for i in range(depth):
		try:
			url = start_url + '&s=' + str(44*i)
			html = getHTMLTest(url)
			parsePage(infoList, html)
		except:
			continue
	printGoodList(infoList)

if __name__ == "__main__":
	main()