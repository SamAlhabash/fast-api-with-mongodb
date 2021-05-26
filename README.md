# fast-api-with-mongodb
A basic template for Fast API with mongoDB. 

---
**NOTE**

This template is still currently under development. It works as is, but it needs a few optimizations and refactoring. 

---


## Installation

Use the package manager [pipenv](https://pypi.org/project/pipenv/) to install dependencies.

```bash
pipenv install
```

## Usage

After activating your virtual environment, Run: 
```bash
python main.py
```

and then go to [localhost:8000/swagger](http://localhost:8000/swagger) to view the auto-generated docs.

![Example Image of openAPI docs](https://github.com/SamAlhabash/fast-api-with-mongodb/blob/main/github_docs/swagger-example.png?raw=true)

## TODO 
* Add Authentication 
* Refactor MongoDBConnections to allow different Database names
* Design and implement a MongoDB Query Builder. 
* Design and run tests. 

## Created with [FastAPI](https://fastapi.tiangolo.com/)
Fast API is one of the fastest python frameworks available for creating web APIs quickly. You can check them out at the [docs](https://fastapi.tiangolo.com/)

## License
[MIT](https://choosealicense.com/licenses/mit/)
