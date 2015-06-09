#-*- coding:utf-8 -*- 
__author__ = 'BING'

import urllib2
import sys
import socket

class GetPic():
    def __init__(self, url):
        self.picurl = url
    def get_pic(self):
        socket.setdefaulttimeout(2)
        url = self.picurl
        if not url.startswith('http://'):
            url = 'http://'+url
        try:
            req = urllib2.urlopen(url)
            return req
        except:
            return False