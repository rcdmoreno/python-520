import datetime

import sqlalchemy

#nome_do_banco = input('Digite o nome do Banco: ')

engine = sqlalchemy.create_engine(
    #'sqlite:///{}.db'.format(nome_do_banco),
    'sqlite:///Financial.db',
    echo=True
)

metadata = sqlalchemy.MetaData(bind=engine)

users_table = sqlalchemy.Table(
    'tb_users',
    metadata,
    sqlalchemy.Column(
        'id',
        sqlalchemy.Integer,
        primary_key=True
    ),
    sqlalchemy.Column(
        'name',
        sqlalchemy.String(50),
        index=True
    ),
    sqlalchemy.Column(
        'age',
        sqlalchemy.Integer,
        nullable=False
    ),
    sqlalchemy.Column(
        'password',
        sqlalchemy.String        
    ),
    sqlalchemy.Column(
        'created_at',
        sqlalchemy.DateTime,
        default=datetime.datetime.now
    ),
    sqlalchemy.Column(
        'updated_at',
        sqlalchemy.DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now
    ))

addresses_table = sqlalchemy.Table(
    'tb_Addresses',
    metadata,
    sqlalchemy.Column(
        'id',
        sqlalchemy.Integer,
        primary_key =True
    ),
    sqlalchemy.Column(
        'name',
        sqlalchemy.String(100),
        nullable=False
    ))

if __name__ == '__main__':

    metadata.create_all(engine)