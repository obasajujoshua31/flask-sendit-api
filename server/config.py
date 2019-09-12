import os

class Config(object):
    DEBUG = False
    FLASK_ENV = os.environ.get("FLASK_ENV")
    APP_SETTINGS = os.environ.get('APP_SETTINGS')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    CSRF_ENABLED = True

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True

class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL')
    DEBUG = True

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
