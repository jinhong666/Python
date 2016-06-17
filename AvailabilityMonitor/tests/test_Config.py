import unittest,AmConfig.appconf,AmConfig.domainconfig

class TestConfigReader(unittest.TestCase):
    def test_readappconf(self):
        conf = AmConfig.appconf.AppConf("Conf/am.conf")
        self.assertIsNotNone(conf.MonitorInterval)

    def test_readdomainconf(self):
        conf = AmConfig.domainconfig.DomainConf("Conf/webapi.conf")
        self.assertIsNotNone(conf.DomainName)
        self.assertTrue(len(conf.SrcIpList) > 0)
        self.assertTrue(len(conf.UrlDic) > 0)

if __name__ == '__main__':
    unittest.main()

