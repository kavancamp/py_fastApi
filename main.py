from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from random import randrange



app = FastAPI()

class Post(BaseModel):
  title: str 
  content: str
  published: bool = True
  rating: Optional[int] = None

my_posts =[{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "Favorite Foods", "content": "I like pizza", "id": 2}]

#@ = decorator

@app.get("/")
def root():
  return {"message": "Hello World!!!"}

@app.get("/posts")
def get_posts():
  return {"data": my_posts}
  
@app.post("/post")
def create_posts(post: Post):
  post_dict = post.dict()
  post_dict['id'] = randrange(0, 1000000)
  my_posts.append()
  return {"data": post_dict}
