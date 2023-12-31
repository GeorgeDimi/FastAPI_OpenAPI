# generated by fastapi-codegen:
#   filename:  pet_shop_api.json
#   timestamp: 2023-10-27T17:17:38+00:00

from __future__ import annotations

from typing import List, Optional, Union

from fastapi import FastAPI

from models import Error, NewPet, Pet

app = FastAPI(
    title='PetStoreAPI',
    version='1.0.0',
    description='A sample API that uses a petstore as an example to demonstrate features\nin the OpenAPI 3.0 specification',
    termsOfService='http://swagger.io/terms/',
    contact={
        'name': 'Swagger API Team',
        'url': 'http://swagger.io',
        'email': 'apiteam@swagger.io',
    },
    license={
        'name': 'Apache 2.0',
        'url': 'https://www.apache.org/licenses/LICENSE-2.0.html',
    },
    servers=[{'url': 'http://petstore.swagger.io/api'}],
)


@app.get('/pets', response_model=List[Pet], responses={'default': {'model': Error}})
def find_pets(
    tags: Optional[List[str]] = None, limit: Optional[int] = None
) -> Union[List[Pet], Error]:
    pass


@app.post('/pets', response_model=Pet, responses={'default': {'model': Error}})
def add_pet(body: NewPet) -> Union[Pet, Error]:
    pass


@app.get('/pets/{id}', response_model=Pet, responses={'default': {'model': Error}})
def find_pet_by_id(id: int) -> Union[Pet, Error]:
    pass


@app.delete('/pets/{id}', response_model=None, responses={'default': {'model': Error}})
def delete_pet(id: int) -> Union[None, Error]:
    pass
