import os
from dotenv import load_dotenv

load_dotenv()

context = os.getenv('context', 'bstack')
userName = os.getenv('bstack_userName', 'sofiatuvykina_pkVzJY')
accessKey = os.getenv('bstack_accessKey', '4UNCy5QxoqBxy4yLLJag')