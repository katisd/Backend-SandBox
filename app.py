from fastapi import FastAPI, Body

# for type hinting
from typing import Optional, Union

# for type validation
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def index():
    return {"data": {"name": "Saurabh"}}


# path param &post request
@app.post("/blog/{blog_code}", status_code=201)
def post_blog(blog_code: int):
    return {"data": f"Blog {blog_code} is created"}


# query param& default value
@app.get("/blog/", status_code=200)
def get_blog(blog_code: int = 1):
    return {"data": "Content of blog " + str(blog_code)}


# union type & optional type & default value
# union will parse the value to the first type in the list if possible
@app.get("/items/", status_code=200)
def get_items(item_id: int, q: Optional[Union[int, str, None]] = None):
    return {"item_id": item_id, "q": q}


# BaseModel for type validation (BaseModdel always in "body")
class Blog(BaseModel):
    title: str
    body: str = "default body"
    published: Optional[bool]


@app.post("/blog/", status_code=201)
def create_blog(blog: Blog):
    return {
        "data": f"Blog is created with title as {blog.title} and body as {blog.body} and published as {blog.published}"
    }


# BaseModel with path param
@app.post("/flower/{flower_code}", status_code=200)
def get_flower_in_blog(flower_code: int, blog: Blog):
    return {"flower_code": flower_code, "blog": blog}


# BaseModel with query param

# query param will be in body
# example Body:
# {
#     "dessert_code":1,
#     "blog":{"title":"sample_title"}
# }
@app.post("/dessert", status_code=200)
def get_dessert_in_blog(blog: Blog, dessert_code: int = Body()):
    return {"dessert_code": dessert_code, "blog": blog.title}


# or simply in params is doable
@app.post("/dessert", status_code=200)
def get_dessert_in_blog(blog: Blog, dessert_code: int):
    return {"dessert_code": dessert_code, "blog": blog.title}


# cl => uvicorn {fileName}:{moduleName(when call FastAPI)} --reload => uvicorn app:app --reload
# if not work use :python -m uvicorn app:app --reload
