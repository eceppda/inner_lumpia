from couchdb.mapping import Document, TextField, ViewField


class User(Document):

    type = TextField()
    username = TextField()
    password = TextField()
    email = TextField()
    by_name = ViewField('users', '''
        function(doc) {
            if(doc.type !== null && doc.type == "User") {
	            emit(doc._id, doc);
	        }
        }''')

    def __init__(self, username, password, email, id=None, **values):

        super(User, self).__init__(id, **values)
        self.username = username
        self.password = password
        self.email = email
        self.type = 'User'
