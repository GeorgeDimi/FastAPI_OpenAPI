# FastAPI_OpenAPI
An example project for generating a FastAPI Python server from an OpenApi file.


## Install requirements 

For generating the server from the OpenApi file we will need a generator. Here we use the <b>[fastapi-code-generator](https://github.com/koxudaxi/fastapi-code-generator)</b>

````
pip install fastapi-code-generator

````

To run the application we the will use Uvicorn package:

```
pip install unicorn
```

## Generate Server

To generate the server simply use the following command:

````
fastapi-codegen --input .\open_api\pet_shop_api.json --output app
````

After this you will found all the generated files (main.py and models.py) under the app folder.


## Run Server

To run the server just run:

````
cd app
uvicorn main:app --reload
````