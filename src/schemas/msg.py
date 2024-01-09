from pydantic import BaseModel


class Massage(BaseModel):
    msg: str
