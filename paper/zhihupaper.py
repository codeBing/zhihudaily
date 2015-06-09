# -*-coding:utf-8-*-
__author__ = 'BING'
import requests,json,re

class apiUse(object):
    def __init__(self):
        self.getLatestApi = 'http://news-at.zhihu.com/api/4/news/latest'
        self.getNewApi = 'http://news-at.zhihu.com/api/4/news/'
        self.getBeforeApi = 'http://news.at.zhihu.com/api/4/news/before/'
        #headers信息
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT'
        self.headrs = {'User-Agent':self.user_agent}

    def access(self,url):
        self.mystr = requests.get(url,headers = self.headrs)
        return json.loads(self.mystr.text)

    def getLateset(self):
        return self.access(self.getLatestApi)

    def getNews(self, _id):
        return self.access(self.getNewApi+str(_id))

    def getBefore(self, date):
        return self.access(self.getBeforeApi+str(date))

class singelNews(object):
    def __init__(self,api,_id):
        self.data = api.getNews(_id)

    def getbody(self):
        return self.data['body']

    def gettitle(self):
        return self.data['title']

    def getimage(self):
        return self.data['image']

    def getid(self):
        return self.data['id']

    def getcss(self):
        return self.data['css']

class latestNews():
    def __init__(self,api):
        self.data = api.getLateset()

    def getdate(self):
        return self.data['date']

    def getimage(self,index):
        return self.data['stories'][index].get('images')

    def gettitle(self,index):
        return self.data['stories'][index].get('title')

    def getid(self,index):
        return self.data['stories'][index].get('id')

    def getstories(self):
        self.data['stories'] = getLargeImg(self.data['stories'])
        return self.data['stories']

    def getnum(self):
        return len(self.data['stories'])

class beforeNews(object):
    def __init__(self,api,date):
        self.data = api.getBefore(date)

    def getstories(self):
        getLargeImg(self.data['stories'])
        return self.data['stories']

def getLargeImg(stories):
    api = apiUse()
    for story in stories:
        print int(story.get('id'))
        singelnews = singelNews(api, int(story.get('id')))
        try:
            story['images'][0] = singelnews.getimage()
        except KeyError:
            story['images'][0] = ''
    return [i for i in stories if not i['images'][0] == '']