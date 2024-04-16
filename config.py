from pydantic import BaseModel, SecretStr

class TelegramConfig(BaseModel):
    token: SecretStr
