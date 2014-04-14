import unittest

from tests import lumpia_client


def suite():
    suite = unittest.TestSuite()
    suite.addTest(lumpia_client.suite())
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')