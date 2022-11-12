from fastapi import FastAPI
from fastapi import Body

app = FastAPI()
#@ = decorator

@app.get("/")
def root():
  return {"message": "Hello World!!!"}

@app.get("/posts")
def get_posts():
  return {"data": "This is your posts"}
  
@app.post("/createposts")
def create_posts(payload: dict = Body):
  print(payload)
  return {"message": "successfully created posts"}
