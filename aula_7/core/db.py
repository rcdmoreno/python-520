import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext.declarative

engine = sqlalchemy.create_engine(
    'sqlite:///projeto.db',
    echo=True
)

Base =  sqlalchemy.ext.declarative.declarative_base()

Session = sqlalchemy.orm.sessionmaker(bind=engine)