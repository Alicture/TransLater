# *- coding:utf-8 *-
import transTX
import time
import requests
import html2text

'''
	transHTML2MD:
	markdown: str
'''
def transMD(weburl):
	h2t=html2text.HTML2Text()
	html = requests.get(weburl)
	htmltext=html.text.replace("\n"," ").replace("	"," ").replace("    "," ")
	h2t.body_width = 0
	markdown = h2t.handle(htmltext)
	return markdown
'''
	trans english 2 chinese
'''
def transE2C(srcStr):
	ans=transTX.transTX(srcStr.strip(),'en','zh')
	return ans

def download(url,Wtstr):
	f1 = open(url, "wt")
	f1.write(Wtstr)
	f1.close()

print(markdown)
f1 = open("/Users/luozepeng/Desktop/test.md", "wt")
f1.write(str(markdown))
time.sleep(5)
f1.close()


fo = open("/Users/luozepeng/Desktop/test.md", "rt")
content=fo.read()
fo.close()

# print(content)
time.sleep(3)
ans=transTX.transTX(content.strip(),'en','zh')
# time.sleep(5)
print(ans)
time.sleep(5)


