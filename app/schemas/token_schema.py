'''Schemas for the Token model'''

from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):

    '''Token schema'''
    
    access_token: str
    token_type: str


class TokenData(BaseModel):

    '''Token data schema'''

    id: Optional[str] = None
