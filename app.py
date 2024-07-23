from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import FileResponse
from typing import Annotated

from utils.aws_s3 import upload_to_s3
from model.db import create_message, all_message

app = FastAPI()

@app.get("/")
def index():
    return FileResponse("./static/index.html")

@app.post("/api/message")
async def upload(content: Annotated[str, Form()], image: UploadFile):
    try:
        s3_obj_name = upload_to_s3(image.file)
        create_message(content, s3_obj_name)
        return {"ok": True}
    except Exception as e:
        print(e)

@app.get("/api/message")
def get_all_message():
    data = all_message()
    if not data:
        return {"data": None}
    cloudFront_url = "https://d1gfnocndlguhy.cloudfront.net"
    for item in data:
        item["image"] = cloudFront_url + "/" + item["image"]
    return {"data": data}
        
    
