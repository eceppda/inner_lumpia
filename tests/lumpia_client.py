import unittest
from couchdb import http, client
from tests import testutil


class ServerTestCase(testutil.TempDatabaseMixin, unittest.TestCase):

    def test_exists(self):
        self.assertTrue(client.Server(client.DEFAULT_BASE_URL))
        self.assertFalse(client.Server('http://localhost:9999'))

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ServerTestCase, 'test'))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
