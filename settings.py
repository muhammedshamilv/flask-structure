from dotenv import load_dotenv
import os

load_dotenv()

database = os.getenv("DATABASE_URL")
