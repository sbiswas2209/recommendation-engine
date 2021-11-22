import os
from dotenv import load_dotenv
load_dotenv()
uri: str = os.environ.get("NEO4J_URI")
username: str = os.environ.get("NEO4J_USERNAME")
password: str = os.environ.get("NEO4J_PASSWORD")