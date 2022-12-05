# .envの設定で flask とコマンドを打つとこのファイルを実行する設定にしてある

from flask import Flask
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
import datetime
# from marshmallow import fields, Schema

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")

db = SQLAlchemy(app) 
migrate = Migrate(app, db)

class TodoListModel(db.Model):
    """
    Todo List Model
    """

    # table name
    __tablename__ = 'todo_list'

    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(128), nullable=False)
    comment = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.task = data.get('task')
        self.comment = data.get('comment')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def __repr__(self):
        return '<id {}>'.format(self.id)


# class TodoListSchema(Schema):
#     id = fields.Int(dump_only=True)
#     task = fields.Str(required=True)
#     comment = fields.Str(required=True)
#     created_at = fields.DateTime(dump_only=True)
#     modified_at = fields.DateTime(dump_only=True)
