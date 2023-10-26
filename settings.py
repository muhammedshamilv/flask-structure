from dotenv import load_dotenv
import os

load_dotenv()

database = os.getenv("DATABASE_URL")
secret_key = os.getenv("SECRET_KEY")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
