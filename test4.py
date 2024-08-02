import requests

for text in open('1.json').read().replace('@', '').split('\n'):
    # print(text)
    print(requests.get('http://47.76.40.247:8014/joinChat?username=%s' % text).text)
