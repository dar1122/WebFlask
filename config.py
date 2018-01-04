import os



basedir = os.path.abspath(os.path.dirname(__file__))


APP_STATIC_TXT = os.path.join(basedir,'static/txt')

class Config:
    @staticmethod
    def init_app(app):
        pass
class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True


Config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

