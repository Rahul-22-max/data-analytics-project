from sqlalchemy import create_engine
from customer import Base

DATABASE_URL = "sqlite:///telco_churn.db"

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)

print("Tables created successfully!")