from flask_env import MetaFlaskEnv


class Configuration(metaclass=MetaFlaskEnv):
    PROPERTY_1 = 'value'
    PROPERTY_2 = 10.1
    PROPERTY_3 = 20
    PROPERTY_4 = 'hello'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/db'