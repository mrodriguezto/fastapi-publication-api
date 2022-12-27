'''Publication Schemas'''
from datetime import date
from bson import ObjectId
from typing import List, Optional

from pydantic import BaseModel, validator

class Commentary(BaseModel):

    '''Commentary Schema'''

    commentary_id: str
    author_id: str
    commentary: str
    created_at: date

    @validator('commentary')
    def commentary_must_not_be_null(cls, v):
        if v is None:
            raise ValueError("Commentary must not be Null")
        return v.title()

    @validator("author_id")
    def author_id_must_be_object_id(cls, v):
        assert ObjectId.is_valid(v)
        return v


class Publication(BaseModel):

    '''Publication Schema'''
    
    publication_id: str
    title: str
    content: str
    author_id: str
    img_url: str
    hashtags: List[str]
    commentaries: Optional[List[Commentary]] = None
    created_at: date

    @validator('title')
    def title_must_not_be_null(cls, v):
        if v is None:
            raise ValueError("Title must not be Null")
        return v.title()

    @validator('content')
    def content_must_not_be_null(cls, v):
        if v is None:
            raise ValueError("Content must not be Null")
        return v.title()

    @validator("author_id")
    def author_id_must_be_object_id(cls, v):
        assert ObjectId.is_valid(v)
        return v
