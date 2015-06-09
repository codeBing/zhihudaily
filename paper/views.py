__author__ = 'BING'
from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from zhihupaper import apiUse,singelNews,latestNews,beforeNews
import re
from getPic import GetPic

def home(request):
    api = apiUse()
    news = latestNews(api)
    count = news.getnum()
    stories = news.getstories()
    return render_to_response('home.html',{'count':count, 'stories':stories})

def story(request, id):
    api = apiUse()
    singelnews = singelNews(api, int(id))
    title = singelnews.gettitle()
    body = singelnews.getbody()
    image = singelnews.getimage()
    body = replaceUrl(body)
    body = replaceImg(body, image)
    return render_to_response('story.html', {'title': title, 'body': body})

def ajax_morestory(request, date):
    api = apiUse()
    beforenews = beforeNews(api, date)
    stories = beforenews.getstories()
    return render_to_response('ajax_morestory.html', { 'stories': stories})

def replaceImg(body, image):
    pattern = re.compile('<div class=\"img-place-holder\"><\/div>',re.DOTALL)
    replaceStr = r'<div class="img-wrap"><img src="/imgurl/url=%s" alt></div>' % image
    return pattern.sub(replaceStr, body)

def replaceUrl(body):
    pattern = re.compile(r'src=\"', re.DOTALL)
    replaceStr = r'src="/imgurl/url='
    return pattern.sub(replaceStr, body)

def get_pic(request, url):
    url = url[4:]
    getpic = GetPic(url)
    req = getpic.get_pic()
    pic = req.read()
    return HttpResponse(pic)