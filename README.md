<a name="readme-top"></a>

<br />
<div align="center">
  <h3 align="center">Publications API</h3>

  <p align="center">
    Social network where you can share your thoughts and sell or buy whatever you want.
    <br />
    <a href="https://github.com/mrodriguezto/fastapi-publication-api"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#features">Features</a></li>
        <li><a href="#tech-used">Tech used</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#documentation">Documentation</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

Social network where you can share your thoughts and sell or buy whatever you want. This API
handles publications and commentaries. It uses token-based authentication which are provided
by the Users API.

### Features

- Token authentication
- Publication operations
- Commentary operations

### Tech used
- Python
- MongoDB
- FastApi
- Cloudinary

## Getting Started

### Prerequisites
In order to get started and run the project you have to meet certain prerequisites:
- Python 3.8 or newer
- A MongoDB cluster
- A Cloudinary account

Next, create a `.env` file and fill the next fields
```properties
MONGODB_URI=<mongodb_uri>
SECRET_KEY=<jwt_secret>
ALGORITHM=<hashing_algorithm>
CLOUD_NAME=<cloudinary_cloud>
API_KEY=<cloudinary_public_key>
API_SECRET=<cloudinary_secret_key>
```

### Installation

First, create an environment and activate it
```bash
python -m venv env
./env/Scripts/Activate.ps1
```

Install the dependencies
```bash
python -m venv env
pip install -r requirements.txt
```

## Usage
Run the project with uvicorn
```bash
uvicorn --port 5000 --host 127.0.0.1 main:app --reload
```
If everything is in order you can now make requests to `localhost:5000`.

You can also check the documentation [here](https://documenter.getpostman.com/view/18270528/2s8YRmHCYa).

## Documentation
FastAPI comes with Swagger out of the box and generates the documentation for all your endpoints. 
You can check the generated documentation on `localhost:5000/docs`.



