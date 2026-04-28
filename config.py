import os
from urllib.parse import quote_plus

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "9f3c2a7e1b8d4f6a0c5e9b2d7a1f4c8e6b3d0a9f2c7e1b5d4f6a8c2e7b1d9f3"

    BLOB_ACCOUNT = os.environ.get("BLOB_ACCOUNT") or "azureappsjensstore"
    BLOB_STORAGE_KEY = os.environ.get("BLOB_STORAGE_KEY") or "fiDrfgES4JD+O10qXlw7sbdI0lVZwp6VOi3cV3XwT+pio2j1PneyKF9sioN9+uaY2o0GPeza3EIx+AStLQYlmw=="
    BLOB_CONTAINER = os.environ.get("BLOB_CONTAINER") or "article-images"

    SQL_SERVER = os.environ.get("SQL_SERVER") or "azureapps-jens-sqlsrv.database.windows.net"
    SQL_DATABASE = os.environ.get("SQL_DATABASE") or "azureapps-cms-db"
    SQL_USER_NAME = os.environ.get("SQL_USER_NAME") or "azurejensadmin"
    SQL_PASSWORD = os.environ.get("SQL_PASSWORD") or "CMS4dmin"

    SQLALCHEMY_DATABASE_URI = (
        "mssql+pyodbc://"
        f"{SQL_USER_NAME}:{quote_plus(SQL_PASSWORD)}"
        f"@{SQL_SERVER}:1433/{SQL_DATABASE}"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###

    CLIENT_SECRET = os.environ.get("CLIENT_SECRET") or "MES8Q~3gqlUobVMmJ7ylw.yQnDm1uQU2KqnS4bFt"
    AUTHORITY = os.environ.get("AUTHORITY") or "https://login.microsoftonline.com/f958e84a-92b8-439f-a62d-4f45996b6d07"
    CLIENT_ID = os.environ.get("CLIENT_ID") or "6f4094f3-cc77-4e36-9f6a-862a685fe1f9"

    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]
    SESSION_TYPE = "filesystem"
    PREFERRED_URL_SCHEME = "https"
