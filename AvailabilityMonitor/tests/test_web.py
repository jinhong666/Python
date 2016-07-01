import unittest,WebAccess.webaccesser


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self._url = '/yicheapp/getappconfigs/?appid=1'
        self._ip = '59.151.102.138'
        self._host = 'api.ycapp.yiche.com'

    def test_webaccess(self):
        webAccesser = WebAccess.webaccesser.WebAccesser()
        webAccesser.SetDomainName(self._host)
        webAccesser.SetUserAgent("bitauto.application : api monitor")
        webAccesser.SetWebIp('59.151.102.138')
        jsonData = webAccesser.RequestUrl(self._url)
        self.assertTrue(len(jsonData) > 0)


if __name__ == '__main__':
    unittest.main()
