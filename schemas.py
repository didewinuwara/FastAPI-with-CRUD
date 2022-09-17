from pydantic import BaseModel


class Item(BaseModel):
    task: str
    class Config:
        schema_extra = {
            "example": {
                "task": "Add your task name",
            }
        }
