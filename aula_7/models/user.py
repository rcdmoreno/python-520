import core.db
import sqlalchemy

class user(core.db.Base):

    __tablename__ = 'tb_users'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True
    )
    name = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=False,
    )
    email = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=False,
        unique=True
    )

    password = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=False
    )

    def say_hello(self):
        print('Hello, my name is ' + self.name)