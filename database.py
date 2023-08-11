from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://qhceykvr:VcmJgJKWHEw9QMxmdjRRK_zUBmU97_GD@satao.db.elephantsql.com/qhceykvr"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
