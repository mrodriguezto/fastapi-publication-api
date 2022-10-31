from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


tags_metadata = [{
  "name": "Publications",
  "description": "Manage user publications"
},{
  "name": "Commentaries",
  "description": "Manage commentaries on publications"
}]

origins = ["*"]

app = FastAPI(
  title="API Publications Kisaragi",
  description="REST API to manage users publications on Kisaragi",
  version="0.0.1",
  open_api_tags=tags_metadata
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
