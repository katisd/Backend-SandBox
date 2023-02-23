from fastapi import APIRouter, Body
from typing import Union, Optional
from pydantic import BaseModel

router = APIRouter(
    prefix="/std",
    tags=["std"],
    responses={404: {"description": "Not found"}},
)


@router.get("/1/foo/true")
def show_item1():
    return {"msg": "order"}
