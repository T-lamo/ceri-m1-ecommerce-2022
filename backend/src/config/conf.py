from pydantic import BaseSettings
class Settings(BaseSettings):
    DATABASE_ADDRESS: str = ""
    DATABASE_USER: str =""
    DATABASE_PASSWORD: str = ""
    DATABASE_NAME: str=""
    ALGOLIA_APP_ID: str =""
    ALGOLIA_KEY: str = ""
