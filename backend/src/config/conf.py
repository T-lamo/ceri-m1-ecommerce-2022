from pydantic import BaseSettings
class Settings(BaseSettings):
    DATABASE_ADDRESS: str = ""
    DATABASE_USER: str =""
    DATABASE_PASSWORD: str = ""
    DATABASE_NAME: str=""
    ALGOLIA_APP_ID: str ="5JQ98FK7KJ"
    ALGOLIA_KEY: str = "69e0f0d5c62f30afa587322210d3b89a"
