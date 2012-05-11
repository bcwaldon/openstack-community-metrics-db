
import sqlalchemy
import sqlalchemy.ext.declarative


Base = sqlalchemy.ext.declarative.declarative_base()


class Commit(Base):
    __tablename__ = 'scmlog'
    id = sqlalchemy.Column(sqlalchemy.Integer(11), primary_key=True)
    rev = sqlalchemy.Column(sqlalchemy.Text())
    committer_id = sqlalchemy.Column(sqlalchemy.Integer(11))
    author_id = sqlalchemy.Column(sqlalchemy.Integer(11))
    date = sqlalchemy.Column(sqlalchemy.DateTime())
    message = sqlalchemy.Column(sqlalchemy.Text())
    rev = sqlalchemy.Column(sqlalchemy.Integer(1))
    repository_id = sqlalchemy.Column(sqlalchemy.Integer(11))
