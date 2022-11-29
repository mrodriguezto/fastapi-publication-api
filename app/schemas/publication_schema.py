'''Publication Schemas'''
from datetime import date
from typing import List, Optional

from pydantic import BaseModel


class Commentary(BaseModel):
    '''Commentary Schema'''
    commentary_id: str
    author_id: str
    commentary: str
    created_at: date


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
