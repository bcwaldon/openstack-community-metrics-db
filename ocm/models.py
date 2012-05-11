
import sqlalchemy
import sqlalchemy.ext.declarative


Base = sqlalchemy.ext.declarative.declarative_base()


class Person(Base):
    __tablename__ = 'people'
    id = sqlalchemy.Column(sqlalchemy.Integer(11), primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(255))
    email = sqlalchemy.Column(sqlalchemy.String(255))


class Company(Base):
    __tablename__ = 'companies'
    id = sqlalchemy.Column(sqlalchemy.Integer(11), primary_key=True)
    c_name = sqlalchemy.Column(sqlalchemy.String(255))


class PersonCompanyAffiliation(Base):
    __tablename__ = 'affiliation'
    id = sqlalchemy.Column(sqlalchemy.Integer(11), primary_key=True)
    company_id = sqlalchemy.Column(sqlalchemy.Integer(11),
                                   sqlalchemy.ForeignKey('companies.id'))
    people_id = sqlalchemy.Column(sqlalchemy.Integer(11),
                                   sqlalchemy.ForeignKey('people.id'))
    until = sqlalchemy.Column(sqlalchemy.DateTime())


class Repository(Base):
    __tablename__ = 'repositories'
    id = sqlalchemy.Column(sqlalchemy.Integer(11), primary_key=True)
    uri = sqlalchemy.Column(sqlalchemy.String(255))
    name = sqlalchemy.Column(sqlalchemy.String(255))
    type = sqlalchemy.Column(sqlalchemy.String(30))


class Commit(Base):
    __tablename__ = 'scmlog'
    id = sqlalchemy.Column(sqlalchemy.Integer(11), primary_key=True)
    rev = sqlalchemy.Column(sqlalchemy.Text())
    date = sqlalchemy.Column(sqlalchemy.DateTime())
    message = sqlalchemy.Column(sqlalchemy.Text())
    composed_rev = sqlalchemy.Column(sqlalchemy.Integer(1))
    committer_id = sqlalchemy.Column(sqlalchemy.Integer(11))

    author_id = sqlalchemy.Column(sqlalchemy.Integer(11),
                                  sqlalchemy.ForeignKey('people.id'))
    author = sqlalchemy.orm.relationship(Person, 
                                         primaryjoin=author_id == Person.id)

    repository_id = sqlalchemy.Column(sqlalchemy.Integer(11),
                                      sqlalchemy.ForeignKey('repositories.id'))
    repository = sqlalchemy.orm.relationship(Repository, 
            primaryjoin=repository_id == Repository.id)
