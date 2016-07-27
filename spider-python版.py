# coding:UTF-8
import urllib2,urllib
from urllib import unquote
import re
import sys
#import base64
from bs4 import BeautifulSoup
import simplejson as json

class baikesearch(object):
	def __init__(self):
		super(baikesearch,self).__init__()
	def search(self,keyword,page=10):
	    list=[]
            for x in range(page):
                i=x*10 #暂时爬取10页为限
                reprStr = repr(keyword).replace(r'\x', '%')
		url='http://baike.baidu.com/search/none?word='+reprStr[1:-1]+'&pn='+str(i)+'&rn=10'
                request=urllib2.Request(url)
                response=urllib2.urlopen(request).read()
		soup = BeautifulSoup(response,"lxml")
                tag1=soup.find_all('a', attrs={'class':'result-title'})
                for tag in tag1 :
                        list.append(tag.get('href'))
            #for i in list:
                #print i
            return(list)
        def analysis(self,list):
            result=[]
            for iurl in list:
                request=urllib2.Request(iurl)
                response=urllib2.urlopen(request).read()
                soup = BeautifulSoup(response,"lxml")
                result.append(soup.h1.string.encode("utf-8"))
            return(result)
        def bsearch(self,soup,response):
            result=[]
            p=re.compile(r'<h2 class="title-text"><span class="title-prefix">.+</span>(.+)</h2>')
            m=p.findall(response)
            for x in m:
                a=unquote(x)
                result.append(a)
            return(result)
		
		
		
if __name__ == '__main__':
	keyword=sys.argv[1]
        baikesearch=baikesearch()
        reprStr = repr(keyword).replace(r'\x', '%')
	url='http://baike.baidu.com/item/'+reprStr[1:-1]
        request=urllib2.Request(url)
        response=urllib2.urlopen(request).read()
        soup = BeautifulSoup(response,"lxml")
        tag1=soup.find_all('h1')
        tag2= (tag1[0].get_text().encode("utf-8"))
        if (len(tag2)!=45):
            bresult=baikesearch.bsearch(soup,response)
            atitle=u'词条标签:'
            print atitle.encode("utf-8")
            for i in set(bresult):
                print i
        else:
            title=u'搜索到以下相关词条：'
            print title.encode("utf-8")
            result=[]
            aresult=[]
            result=baikesearch.search(keyword)
            aresult=baikesearch.analysis(result)
            #f=open("result.txt","w")
            for i in set(aresult):
                print i
        