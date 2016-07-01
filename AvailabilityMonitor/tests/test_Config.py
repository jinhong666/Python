import unittest,AmConfig.appconf,AmConfig.domainconfig,os

class TestConfigReader(unittest.TestCase):
    def test_readappconf(self):
        conf = AmConfig.appconf.AppConf(self._mainConfig)
        self.assertIsNotNone(conf.MonitorInterval)
        conf.ReadDomainConfig(self._configPath)
        self.assertTrue(len(conf.DomainConfs) > 1)

    def test_readdomainconf(self):
        conf = AmConfig.domainconfig.DomainConf(self._domainConfig)
        self.assertIsNotNone(conf.DomainName)
        self.assertTrue(len(conf.SrcIpList) > 0)
        self.assertTrue(len(conf.UrlDic) > 0)


    def setUp(self):
        self._startPath = os.path.split(os.path.realpath(__file__))[0]
        self._configPath = os.path.join(self._startPath,"../Conf")
        self._mainConfig = os.path.join(self._configPath,"am.conf")
        self._domainConfig = os.path.join(self._configPath,"DomainConf/webapi.conf")


if __name__ == '__main__':
    unittest.main()

