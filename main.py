from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World", "Version": "v1.0.0"}

@app.get("/user")
async def read_user():
    return {"user_id": "the current user"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)