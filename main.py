#!/usr/bin/python
# coding=utf-8
#FILENAME : __main.py__ 
#DESCRIBE:

import alfred,urllib,urllib2,json,time

query = u'{query}'
url = 'http://api.acfun.tv/search?exact=1&channelIds=0&orderId=0&orderBy=1&pageNo=1&pageSize=10&'

query.strip(' ')

if u' ' in query:
    list = query.split(u' ')
    query = list[1]
    arg = list[0]
    if arg == 'new':
        url = 'http://api.acfun.tv/search?exact=1&channelIds=0&orderId=2&orderBy=1&pageNo=1&pageSize=10&'

get_url = url + urllib.urlencode({'query':query.encode('utf-8')})

json_str = urllib2.urlopen(get_url).read()
json_obj = json.loads(json_str[10:-1])

results = []
index = 1
format_str = '%Y-%m-%d %H:%M:%S'

for i in json_obj['contents']:
    link = 'http://www.acfun.tv/v/ac' + str(i['aid'])
    title = i['title']
    tim = time.localtime(int(str(i['releaseDate'])[:10]))
    dt = time.strftime(format_str, tim)
    subtitle = u'UP主:' + i['username'] + u' 时间' + dt
    subtitle = subtitle + u' 播放:' + str(i['views']) + u' 简介' + i['description']
    item = alfred.Item({'uid':index ,'arg': link},title,subtitle,('acfun.jpg',{'type': 'jpg'}))
    results.append(item)
    index += 1

alfred.write(alfred.xml(results))

