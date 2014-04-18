from couchdb.mapping import Document, TextField, ViewField, ListField, DictField, Mapping
from pyramid.security import Allow, Deny


class User(Document):
    """
    Represents an application user, with authentication details and a list of words.
    Initialization requires a username, password, and email address. This is analogous to registering.
    """

    type = TextField()
    username = TextField()
    password = TextField()
    email = TextField()

    # TODO - change this back to a python view
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


class ACE(Document):
    """
    Represents an Access Control Entry.
    """

    action = TextField()
    principle = TextField()
    permissions = ListField(TextField())

    def get_ace(self):

        if self.action == 'Allow':
            return (Allow, self.principle, self.permissions)
        else:
            return (Deny, self.principle, self.permissions)

