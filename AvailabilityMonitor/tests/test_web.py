import unittest
from WebAccess.webaccesser import WebAccesser


class TestWeb(unittest.TestCase):
    def setUp(self):
        self._url = 'http://api.ycapp.yiche.com/yicheapp/getappconfigs/?appid=1'
        self._ip = '59.151.102.138'

    def test_webaccess(self):
        webAccesser = WebAccesser(self._url)
        webAccesser.SetUserAgent("bitauto.application : api monitor")
        #webAccesser.SetDomainIp(self._ip)
        jsonData = webAccesser.Request()
        self.assertTrue(len(jsonData) > 0)

    def test_fullUrl(self):
        fullUrl = "http://www.ora.com:80/goodparts/test?q#fragment"
        wa = WebAccesser(fullUrl)
        self.assertEqual(wa.Protocol,'http')
        self.assertEqual(wa.DonmainName,'www.ora.com')
        self.assertEqual(wa.Port,80)
        self.assertEqual(wa.Path,'/goodparts/test')
        self.assertEqual(wa.QueryString,'q')

