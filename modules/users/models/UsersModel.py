from mongoengine import Document, StringField, DateTimeField
import json, datetime, pytz

tz_1 = pytz.timezone("America/Sao_Paulo")

class UserModel(Document):
    name = StringField(required=True,  max_length=100)
    document = StringField(required=True, max_length=15, unique=True)
    address = StringField(required=True, max_length=60)
    created_date = DateTimeField(default=datetime.datetime.now(tz_1))
    

    def to_dict(self):
        return {
            "name": self.name,
            "document":self.document,
            "address":self.address,
            "created_date":self.created_date
        }

    def to_json(self):
        return json.dump(self.to_dict()); 
