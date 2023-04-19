from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

SQLALCHEMY_DATABASE_URL =   "postgresql://todo_authenticaion_user:PqD3zGFFSESOR9Fump9TJgTeVuVVwZ1c@dpg-cgvntequt4mc4k9i5fsg-a/todo_authenticaion"

# MYSQL Series
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:test1234!@127.0.0.1:3306/todoapp"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

# MYSQL Series
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL
# )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
