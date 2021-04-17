import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    UPLOAD_FOLDER = ('./uploads') or '.uploads'
    ALLOWED_EXTENSIONS = {'.jpg', '.png'}
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgres://wptqqyofwjbysb:d42eff0cc5cd007c8793d57253aca731cdbb9cd4a3804badedc28275ab1e0296@ec2-54-161-239-198.compute-1.amazonaws.com:5432/df4pt6b9p4qbdk'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed

class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False