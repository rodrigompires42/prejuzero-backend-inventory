import sys

from dotenv import dotenv_values

env_variables = dotenv_values(".env")


DB_URL = env_variables["DB_URL"]
DB_NAME = env_variables["DB_NAME"]
