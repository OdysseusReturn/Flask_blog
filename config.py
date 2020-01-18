class Configuration(object):
    DEBUG = True
    SQL_ALCHEMY_TRACK_MODIFICATIONS = False
    SQL_ALCHEMY_URI = 'mysql+mysqlconnector://root:12345678@localhost/test1'
    SQLALCHEMY_BINDS = True
