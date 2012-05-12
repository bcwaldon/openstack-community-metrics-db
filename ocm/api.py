import sqlalchemy
import sqlalchemy.orm

import ocm.models


class API(object):
    def __init__(self, db_url, debug=False):
        self.engine = sqlalchemy.create_engine(db_url, echo=debug)

    @property
    def session(self):
	maker = sqlalchemy.orm.sessionmaker(bind=self.engine)
        session = maker()
        return session

    def get_commits(self, author_id=None, company_id=None, repository_id=None, 
            start=None, end=None):
        query = self.session.query(ocm.models.Commit)
        query = query.options(sqlalchemy.orm.joinedload('author'))

        if author_id:
            query = query.filter(ocm.models.Commit.author_id == author_id)
        
        if repository_id:
            query = query.filter(
                      ocm.models.Commit.repository_id == repository_id)
        
        if start:
            query = query.filter(ocm.models.Commit.date >= start)

        if end:
            query = query.filter(ocm.models.Commit.date <= end)

        commits = query.all()

        if company_id:
            commits = filter(lambda ci: company_id in \
                    [co.id for co in ci.author.companies], commits)

        return commits

    def get_repositories(self):
        return self.session.query(ocm.models.Repository).all()

    def get_people(self):
        return self.session.query(ocm.models.Person).all()
