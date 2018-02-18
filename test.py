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

def transE2C(srcStr):
	ans=transTX.transTX(content.strip(),'en','zh')
	return ans


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


f1 = open("/Users/luozepeng/Desktop/testtgt.md", "wt")
f1.write(ans)
time.sleep(5)
f1.close()