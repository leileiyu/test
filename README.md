## 协程

参考文档：
https://zhuanlan.zhihu.com/p/104918655
https://zhuanlan.zhihu.com/p/108900759
https://blog.csdn.net/qq_39147299/article/details/107874929

```python
import gevent
from gevent import monkey
import time

# 打补丁，可以让gevent识别所有耗时操作，以便自动切换
monkey.patch_all()


def task(name):
    for i in range(5):
        print(name, '在执行任务')
        time.sleep(1)  # 如果不打monkey补丁，需要用gevent.sleep(0.5)


if __name__ == '__main__':
    # 创建协程
    g1 = gevent.spawn(task, 'xiaoming')
    g2 = gevent.spawn(task, 'hong')

    # join，让主线程等到（相当于执行耗时操作）
    g1.join()
    g2.join()
```

```python
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
```