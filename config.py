import os
from dotenv import load_dotenv

load_dotenv()

context = os.getenv('context', 'bstack')
userName = os.getenv('USER_NAME')
accessKey = os.getenv('ACCESS_KEY')
