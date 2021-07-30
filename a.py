#-*- coding:utf8 -*-
from gevent import monkey; monkey.patch_all()
from urllib import request
import gevent


def test(url):
    print('Get: %s' % url)
    response = request.urlopen(url)
    content = response.read().decode('utf8')
    print('%d bytes received from %s.' % (len(content), url))


if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(test, 'http://httpbin.org/ip'),
        gevent.spawn(test, 'http://httpbin.org/uuid'),
        gevent.spawn(test, 'http://httpbin.org/user-agent')
    ])
