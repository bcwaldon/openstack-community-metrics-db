import sqlalchemy
import sqlalchemy.orm

import ocm.models as models


class API(object):
    def __init__(self, db_url, debug=False):
        self.engine = sqlalchemy.create_engine(db_url, echo=debug)

    @property
    def session(self):
	maker = sqlalchemy.orm.sessionmaker(bind=self.engine)
        session = maker()
        return session

    def get_commits(self):
       return self.session.query(models.Commit).all() 
