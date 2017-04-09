# -*- coding: utf-8 -*-
'''
Created on 5 Mar 2017

@author: rf
'''
import base64
import datetime
import time
import urlparse

import re

REGEXP_HOST = re.compile("(?<=Host: ).*")
REGEXP_REQUEST = re.compile("(?P<METHOD>(GET|POST|HEAD|PUT|DELETE|OPTIONS|TRACE|CONNECT|PATCH)) (?P<RESSOURCE>.*) HTTP/1.1")
REGEXP_COOKIE = re.compile("(?<=Cookie: ).*") 
REGEXP_AUTH = re.compile("(?<=Authorization: ).*")
REGEXP_POSTDATA = re.compile("(?<=\n\n).+")

REGEXP_HEADERS = dict() 
REGEXP_HEADERS_SUPPORTED = [
"Accept",
"Accept-Charset",
"Accept-Encoding",
"Accept-Language",
"Accept-Datetime",
"Cache-Control",
"Content-Type",
"Date",
"Expect",
"From",
"If-Match",
"If-Modified-Since",
"If-None-Match",
"If-Range",
"If-Unmodified-Since",
"Max-Forwards",
"Origin",
"Pragma",
"Proxy-Authorization",
"Range",
"Referer",
"TE",
"User-Agent",
"Upgrade",
"Via",
"Warning",
"X-Requested-With",
"DNT",
"X-Forwarded-For",
"X-Forwarded-Host",
"X-Forwarded-Proto",
"Front-End-Https",
"X-Http-Method-Override",
"X-ATT-DeviceId",
"X-Wap-Profile",
"Proxy-Connection",
 "Upgrade-Insecure-Requests"]

 
for h in REGEXP_HEADERS_SUPPORTED:
    REGEXP_HEADERS[h] = re.compile("(?<=%s: ).*" % h)
    


class NotSupportedException(Exception):
    pass

class Module(object):
    def __init__(self, request= "", addBurpProxy=False):
        self.request = request
        self.result = ""
        self.indent = ""
        self.addHeader()
        self.extensions = ""
        self.addBurpProxy = addBurpProxy
        
    def name(self):
        return "Request2Requests"
    
    def match(self, text):
        count= 0
        for s in REGEXP_HEADERS_SUPPORTED:
            count+= text.count(s)
        score= count*0.2
        return score

    def process(self, text):
        self.request= text
        return self.transform()
        
    def addLine(self, line, indentAfter=0):
        if self.result == "":
            self.result = self.result + self.indent + line
        else:
            self.result = self.result + "\n" + self.indent + line
        if indentAfter == 1:
            self.indent = self.indent + "\t"
        if indentAfter == -1 and len(self.indent) > 0:
            self.indent = self.indent[:-1]
            
    def addNewLine(self):
        self.addLine("")

    def addHeader(self):
        self.addLine("#!/usr/bin/python")
        self.addLine("# -*- coding: utf-8 -*-")
        self.addLine("'''")
        self.addLine("Created on %s" % datetime.datetime.fromtimestamp(int(time.time())).strftime("%d.%m.%Y %H:%M:%S"))
        self.addLine("@author request2requests")
        self.addLine("'''")
        self.addLine("import requests")
        self.addNewLine()
        self.addLine("if __name__ == '__main__':", 1)
        
    def addTrailer(self):
        self.addNewLine()
        self.addLine("#result.status_code")
        self.addLine("#result.headers")
        self.addLine("#result.text")
        
        
    def addRequestMethod(self):
        self.reqMethod = REGEXP_REQUEST.search(self.request).group("METHOD")
        if self.reqMethod in ["TRACE", "CONNECT", "PATCH"]:
            raise NotSupportedException("reqMethod %s not supported." % self.reqMethod)
    
    def addRequestURL(self):
        reqRessource = REGEXP_REQUEST.search(self.request).group("RESSOURCE")
        reqHost = REGEXP_HOST.search(self.request).group(0)
        reqURL = reqHost + reqRessource
        self.addLine("protocol='http://'")
        self.addLine("reqURL=protocol+'%s'" % reqURL)
        self.addNewLine()
        return reqURL
    
    def addHeaders(self):
        self.headers = dict()
        for KEY, REGEXP_H in REGEXP_HEADERS.iteritems():
            search = REGEXP_H.search(self.request)
            if search:
                value = search.group(0)
                self.headers[KEY] = value
        
        if len(self.headers) > 0:
            self.addLine("headers=%s" % str(self.headers))
            self.addNewLine()
            self.extensions += ", headers=headers"
    
    def addCookies(self):
        search = REGEXP_COOKIE.search(self.request)
        if search:
            reqCookieData = search.group(0)
            reqCookies = dict() 
            for c in reqCookieData.split("; "):
                item = c.split("=")
                reqCookies[item[0]] = item[1]
            self.addLine("cookies=%s" % str(reqCookies))
            self.addNewLine()
            self.extensions += ", cookies=cookies" 
            
    def addAuth(self):
        search = REGEXP_AUTH.search(self.request)
        if search:
            reqAuth = search.group(0)
            if "Basic" in reqAuth:
                credentials = base64.b64decode(reqAuth.split(" ")[1]).split(":")
                self.addLine("authUser='%s'" % credentials[0])
                self.addLine("authPass='%s'" % credentials[1])
                self.addLine("from requests.auth import HTTPBasicAuth")
                self.addLine("auth=HTTPBasicAuth(authUser, authPass)")
            elif "Digest" in reqAuth:
                self.addLine("authUser=''")
                self.addLine("authPass=''")
                self.addLine("from requests.auth import HTTPDigestAuth")
                self.addLine("auth=HTTPDigestAuth(authUser, authPass)")
            elif "OAuth" in reqAuth:
                self.addLine("auth=OAuth1('APP_KEY','APP_SECRET','USER_TOKEN','USER_TOKEN_SECRET')")
            else:
                self.addLine("#Unknown Auth-Algorithm")
                self.addLine("#auth=HTTPBasicAuth(authUser, authPass)")
            
            self.addNewLine()
            self.extensions += ", auth=auth" 
    
    def addData(self):
        if self.reqMethod == "POST":
            search = REGEXP_POSTDATA.search(self.request)
            if search:
                reqPostData = search.group(0)
                reqPost = dict(urlparse.parse_qsl(reqPostData))
                self.addLine("#postdata=%s" % str(reqPost))
                self.addLine("postdata=dict()")
                for k, v in reqPost.iteritems():
                    self.addLine("postdata['%s']='%s'" % (k, v))
                self.addNewLine()
                self.extensions += ", data=postdata"
    
    def addProxy(self):
        if self.addBurpProxy:
            self.extensions += ", proxies={'http': '127.0.0.1:8080', 'https':'127.0.0.1:8080'}"
    
    def addRequest(self):
        self.addLine("result = requests.%s(reqURL%s)" % (self.reqMethod.lower(), self.extensions))
    
    def transform(self):
        self.addRequestMethod()
        self.addRequestURL()
        self.addHeaders()
        self.addCookies()
        self.addAuth()
        self.addData()
        self.addProxy()
        self.addRequest()
        self.addTrailer()
        
        return self.result