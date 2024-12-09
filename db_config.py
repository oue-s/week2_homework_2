import datetime
import os
from dotenv import load_dotenv
from peewee import Model, IntegerField, CharField, TextField, TimestampField
from playhouse.db_url import connect

# .envの読み込み
load_dotenv(override=True)

db = connect(os.environ.get("DATABASE"))


# メッセージのモデル
class Message(Model):
    """Message Model"""

    id = IntegerField(primary_key=True)  # idは自動で追加されるが明示
    name = CharField()
    age = IntegerField()
    pub_date = TimestampField(default=datetime.datetime.now())  # 何も指定しない場合は現在時刻が入る

    class Meta:
        database = db
        table_name = "messages"


db.create_tables([Message])
