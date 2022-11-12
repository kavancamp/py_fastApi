from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class Post(BaseModel):
  title: str 
  content: str
  published: bool = True
  rating: Optional[int] = None


#@ = decorator

@app.get("/")
def root():
  return {"message": "Hello World!!!"}

@app.get("/posts")
def get_posts():
  return {"data": "This is your posts"}
  
@app.post("/post")
def create_posts(post: Post):
  print(post)
  print(post.dict())
  return {"data": post}
