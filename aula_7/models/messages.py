import core.db
import sqlalchemy

class Message(core.db.Base):

    __tablename__ = 'tb_messages'
    
    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True
    )
    conteudo = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=False,
    )
    user = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey(
            'tb_users.id'
        )
    )