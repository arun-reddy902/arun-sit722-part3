from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://sit722_postgresql_arun_user:8Xj1VmCY4OYjvB5bdEyuT1dTO87d3rfa@dpg-crp5f82j1k6c73c081g0-a.oregon-postgres.render.com/sit722_postgresql_arun" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
