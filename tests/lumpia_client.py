import unittest
from couchdb import client
from couchdb.design import ViewDefinition
from documents.user import User
from tests import testutil


class ServerTestCase(testutil.TempDatabaseMixin, unittest.TestCase):

    def setUp(self):
        super(ServerTestCase, self).setUp()

        self.dbname, db = self.temp_db()

        ViewDefinition.sync_many(self.db, [User.by_name])

    def test_exists(self):
        self.assertTrue(client.Server(client.DEFAULT_BASE_URL))
        self.assertFalse(client.Server('http://localhost:9999'))

    def test_tmpdb(self):
        self.assertIsNotNone(self.dbname)
        self.assertIsNotNone(self.db)

    def test_user_view(self):
        user1 = User()
        user1.username = 'aaa'
        user1.password = 'aaa'
        user1.email = 'aaa@one.com'
        user1.type = 'User'
        user2 = User()
        user2.username = 'bbb'
        user2.password = 'bbb'
        user2.email = 'bbb@one.com'
        user2.type = 'User'
        user1.store(self.db)
        user2.store(self.db)
        assert user1.id is not None
        assert user2.id is not None
        assert user1.type == 'User'

        users = User.by_name(self.db)
        assert users.total_rows == 2


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ServerTestCase, 'test'))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
