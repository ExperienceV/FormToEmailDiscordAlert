from pydantic import BaseModel

class form_model(BaseModel):
    name: str
    mail: str
    issue: str
    message: str