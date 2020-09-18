<p align="center">
    <img alt="SVG Blob from Blobmaker" src="./images/blob.svg" width="100" />
</p>
<h1 align="center" style="color:#9EF0F0;">
    NGR
</h1>

![master](https://github.com/LuisBrime/ngr/workflows/master/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

FastAPI project example made for deployment with AWS Lambda.
\
## Run locally 💻 
1. Install dev dependencies with Makefile

This will install dependencies found at `requirements-dev.txt` and `requirements.txt`.
```bash
make install-dev
```
1. Install an ASGI server, for example [Uvicorn](http://www.uvicorn.org/):
```bash
pip install uvicorn
```
3. Run the server locally:

This will run the API locally and if you change anything in the code reload it.
```bash
uvicorn ngr.main:app --reload
```
\
## Structure 📁 
```
.
├── ngr/
  ├── api/
    ├── v1/
      ├── bodies.py
  ├── db/
      ├── data.json
      ├── db.py
  ├── main.py
├── tests/
  ├── api/
  ├── conftest.py  
```
- **`ngr/`**: Contains all the FastAPI source code.
  - **`api/`**: Contains the API routes, within the folder `v1` contains the files for the routes of the API's first version.
  - **`db/`**: Contains handler for the fake DB. All data is contained on `data.json` generated with [JSON-Generator](https://www.json-generator.com/).
- **`tests/`**: Contains all the tests for the source code, it mimics the structure of `ngr`.

\
## Commands 🛠 
This project uses a Makefile to easily run commands for installation, format, lint, etc.
- **`make venv`**: Generates a Python `venv` so you can install dependencies without making Python go crazy. Note that after running you need to run `source venv/bin/activate` to activate it.
- **`make install`**: Installs all core dependencies of the project located in `requirements.txt`.
- **`make install-dev`**: Installs all dependencies required to run project locally and run the tests, as well as core dependencies.
- **`make test`**: Installs dependencies, lints and runs tests for the project.
- **`make format`**: Formats all the files on the project using [isort](https://pycqa.github.io/isort/) and [black](https://black.readthedocs.io/en/stable/).
- **`make lint`**: Lints project using [flake8](https://flake8.pycqa.org/en/latest/) and checks format.
- **`make clean`**: Cleans all cached files and folders.

\
## Deploy to Lambda 🚀 
Follow my tutorial on Medium.
