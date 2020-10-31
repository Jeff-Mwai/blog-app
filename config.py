import os


class Config:
    '''
    General configuration parent class
    '''
    pass



class ProdConfig(Config):
    '''
    Pruduction  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class TestConfig(Config):
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:KingJeffa00*@localhost/watchlist'
    DEBUG = True
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test': TestConfig
}