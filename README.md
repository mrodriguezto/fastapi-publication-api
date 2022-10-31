# Publications API

Social network where you can share your thoughts and sell or buy whatever you want. This API
handles publications and commentaries. It uses token-based authentication which are provided
by the Users API.
Made with FastAPI and MongoDB.

## Features

- Token authentication
- Publication operations
- Commentary operations

## Install project

```bash
python -m venv env
pip install -r requirements.txt
uvicorn --port 5000 --host 127.0.0.1 main:app --reload
```
