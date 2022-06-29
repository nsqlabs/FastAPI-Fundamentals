from datetime import datetime
from pydantic import BaseModel
from typing import Text, Optional
from uuid import uuid4 as uuid


class Post(BaseModel):
    id: Optional[str] = uuid()
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()  # default value
    published_at: Optional[datetime]
    published: Optional[bool] = False


class UpdatePostPayload(BaseModel):
    title: Optional[str]
    content: Optional[Text]