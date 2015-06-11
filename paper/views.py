# -*-coding:utf-8-*-
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
    return render_to_response('home.html',{'stories':stories})

def mobile(request):
    api = apiUse()
    news = latestNews(api)
    topstories = news.gettopstories()
    stories = news.getmobilestories()
    return render_to_response('mobile.html',{'topstories':topstories, 'stories':stories})

def story(request, id):
    api = apiUse()
    singelnews = singelNews(api, int(id))
    title = singelnews.gettitle()
    body = singelnews.getbody()
    image = singelnews.getimage()
    source = singelnews.getsource()
    body = replaceUrl(body)
    body = replaceImg(body, image, title, source)
    return render_to_response('story.html', {'title': title, 'body': body})

def ajax_morestory(request, date):
    api = apiUse()
    beforenews = beforeNews(api, date)
    stories = beforenews.getstories()
    return render_to_response('ajax_morestory.html', { 'stories': stories})

def m_ajax_morestory(request, date):
    api = apiUse()
    beforenews = beforeNews(api, date)
    stories = beforenews.getmobilestories()
    return render_to_response('m_ajax_morestory.html', { 'stories': stories})

def replaceImg(body, image, title, source):
    pattern = re.compile('<div class=\"img-place-holder\"><\/div>',re.DOTALL)
    replaceStr = r'<div class="img-wrap"><h1 class="headline-title">%s</h1><span class="img-source">%s</span><img src="/imgurl/url=%s" alt></div>' % (title, source, image)
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