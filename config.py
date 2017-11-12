class config:
    SECRET_KEY = 'HARD TO GUESS'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:digibird@localhost:3306/test?charset=utf8mb4'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True