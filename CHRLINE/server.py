# -*- coding: utf-8 -*-
import json, requests, urllib

class Server(object):
    _session        = requests.session()
    timelineHeaders = {}
    Headers         = {}

    def __init__(self):
        self.Headers = {}
        self.timelineHeaders = {}
        self.channelHeaders = {}

    def parseUrl(self, path):
        return self.LINE_HOST_DOMAIN + path

    def urlEncode(self, url, path, params=[]):
        return url + path + '?' + urllib.parse.urlencode(params)

    def getJson(self, url, allowHeader=False, cHeaders={}):
        if allowHeader is False:
            return json.loads(self._session.get(url).text)
        else:
            if cHeaders != {}:
                return json.loads(self._session.get(url, headers=cHeaders).text)
            return json.loads(self._session.get(url, headers=self.Headers).text)

    def setHeadersWithDict(self, headersDict):
        self.Headers.update(headersDict)

    def setHeaders(self, argument, value):
        self.Headers[argument] = value

    def setTimelineHeadersWithDict(self, headersDict):
        self.timelineHeaders.update(headersDict)

    def setTimelineHeaders(self, argument, value):
        self.timelineHeaders[argument] = value

    def additionalHeaders(self, source, newSource):
        headerList={}
        headerList.update(source)
        headerList.update(newSource)
        return headerList

    def optionsContent(self, url, data=None, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.options(url, headers=headers, data=data)

    def postContent(self, url, data=None, files=None, headers=None, json=None):
        if headers is None:
            headers = self.Headers
        res = self._session.post(url, headers=headers, data=data, files=files, json=json)
        if 'x-ls' in res.headers:
            print(f"{url} -> {res.headers}")
        return res

    def getContent(self, url, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.get(url, headers=headers, stream=True)

    def deleteContent(self, url, data=None, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.delete(url, headers=headers, data=data)

    def putContent(self, url, data=None, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.put(url, headers=headers, data=data)