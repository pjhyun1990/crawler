from datetime import datetime
from urllib.request import Request, urlopen
import ssl

def crawling(url='',encoding = 'utf-8'):
    try:

        ssl._create_default_https_context = ssl._create_unverified_context
        request = Request(url)

        resp = urlopen(request)

        try:
            receive = resp.read()  # euc-kr
            result = receive.decode(encoding)

        except UnicodeDecodeError:
            result = receive.decode(encoding, 'replace')
        print('%s : success for request(%s)' %(datetime.now(), url))
        return result

    except Exception as e:
        print('%s : %s' % (e, datetime.now()))


