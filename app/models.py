# generated by fastapi-codegen:
#   filename:  .\open_api\pet_shop_api.json
#   timestamp: 2023-10-27T17:17:38+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class NewPet(BaseModel):
    name: str
    tag: Optional[str] = None


class Error(BaseModel):
    code: int
    message: str


class Pet(NewPet):
    id: int
