'''Service for managing publications'''
import os
import cloudinary
import cloudinary.uploader

from dotenv import load_dotenv
from fastapi import HTTPException

from app.database.config import connect_database
from app.models.publication import Publication

load_dotenv()
connect_database()

cloudinary.config(
    cloud_name=os.getenv('CLOUD_NAME'),
    api_key=os.getenv('API_KEY'),
    api_secret=os.getenv('API_SECRET'),
    secure=True
)


class PublicationService:
    '''
    Class with methods to manage publication operations
    '''
    @staticmethod
    async def create_publication(author, title, content, file):
        '''
        Creates a new publication.

        Parameters:
            author (str): The author of the publication.
            title (str): The title of the publication.
            content (str): The content of the publication.
            file (UploadFile): The file of the publication.
        '''

        upload_result = cloudinary.uploader.upload(
            file, folder="kisaragi_publications")

        url = upload_result["url"]
        public_id = upload_result["public_id"]

        hashtags = list({hashtag.strip("#")
                        for hashtag in content.split() if hashtag.startswith("#")})

        new_publication = Publication(
            title=title,
            content=content,
            author_id=author.id,
            img_url=url,
            img_public_id=public_id,
            hashtags=hashtags
        )
        new_publication.save()

    @staticmethod
    async def delete_publication(publication_id, author_id):
        '''
        Deletes a publication by its id.

        Parameters:
            publication_id (str): The id of the publication.
            author_id (str): The id of the author.
        '''
        publication_obj = Publication.objects(
            id=publication_id,
            author_id=author_id
        ).first()
        
        if publication_obj is not None:
            cloudinary.uploader.destroy(publication_obj.img_public_id)
            publication_obj.delete()
            return "Publication deleted successfully"

        raise HTTPException(status_code=400, detail="Publication not found")

    @staticmethod
    async def get_publication(publication_id):
        '''
        Gets only one publication based on its id.

        Parameters:
            publication_id (str): The id of the publication.
        '''
        publication_obj = Publication.objects(
            id=publication_id,
        ).first()

        if publication_obj is not None:
            print(publication_obj.hashtags)
            return publication_obj.to_json()

        raise HTTPException(status_code=400, detail="Publication not found")

    @staticmethod
    async def get_publications(skip, limit):
        '''
        Gets all publications.

        Parameters:
            skip (int): The number of publications to skip.
            limit (int): The number of publications to return.
        '''
        publication_objs = Publication.objects().limit(limit).skip(skip)
        publications = []
        publications = list(
            map(lambda publication_obj: publication_obj.to_json(), publication_objs))
        return publications

    @staticmethod
    async def get_publications_by_hashtag(skip, limit, hashtag):
        '''
        Gets all publications by hashtag.

        Parameters:
            skip (int): The number of publications to skip.
            limit (int): The number of publications to return.
            hashtag (str): The hashtag to search.
        '''
        publication_objs = Publication.objects(
            hashtags__in=[hashtag]).limit(limit).skip(skip)
        publications = []
        publications = list(
            map(lambda publication_obj: publication_obj.to_json(), publication_objs))
        return publications
