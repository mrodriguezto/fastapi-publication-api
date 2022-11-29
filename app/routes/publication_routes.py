'''Publication Routes'''
from typing import Optional
from fastapi import APIRouter, Depends, File, UploadFile, Form

from app.middlewares.auth import get_token_payload
from app.schemas.token_schema import TokenData
from app.schemas.publication_schema import Publication
from app.services.publication_service import PublicationService

publications_router = APIRouter()


@publications_router.post("/publications", tags=["Publications"])
async def post_publication(
    title: str = Form(...),
    content: str = Form(...),
    payload: TokenData = Depends(get_token_payload),
    file: Optional[UploadFile] = File(...)
):
    '''Endpoint to create a publication'''
    file_readed = await file.read()
    await PublicationService.create_publication(payload, title, content, file_readed)
    return {"msg": "Publication created successfully"}


@publications_router.delete("/publications/{id}", tags=["Publications"])
async def delete_publication(id: str, payload: TokenData = Depends(get_token_payload)):
    '''Endpoint to delete a publication by id'''
    message = await PublicationService.delete_publication(id, payload.id)
    return {"msg": message}


@publications_router.get("/publications/{id}/id", tags=["Publications"], response_model=Publication)
async def get_publication(id: str):
    '''Endpoint to get a publication by id'''
    return await PublicationService.get_publication(id)


@publications_router.get("/publications", tags=["Publications"], response_model=list[Publication])
async def get_publications(skip: int = 0, limit: int = 5):
    '''Endpoint to get all publications'''
    return await PublicationService.get_publications(skip, limit)


@publications_router.get("/publications/hashtags", tags=["Publications"], response_model=list[Publication])
async def get_publications_by_hashtag(skip: int = 0, limit: int = 5, hashtag: str = None):
    '''Endpoint to get all publications by hashtag'''
    return await PublicationService.get_publications_by_hashtag(skip, limit, hashtag)
