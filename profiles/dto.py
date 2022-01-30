from pydantic import BaseModel

class Profile(BaseModel):
    arroba: str

    class Config:
        orm_mode = True
