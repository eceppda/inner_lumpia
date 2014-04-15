from couchdb.mapping import Document, TextField, ViewField, ListField, DictField, Mapping


class User(Document):
    """
    Represents an application user, with authentication details and a list of words.
    Initialization requires a username, password, and email address. This is analogous to registering.
    """

    type = TextField()
    username = TextField()
    password = TextField()
    email = TextField()

    by_name = ViewField('users', '''
        function(doc) {
            if(doc.type !== null && doc.type == "User")
            {
	            emit(doc._id, doc);
	        }
        }''')

    words = ListField(DictField(
        Mapping.build(
            word=TextField(),
            typeofspeach=TextField(),
        )
    ))
