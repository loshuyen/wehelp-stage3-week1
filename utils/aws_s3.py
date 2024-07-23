import os
import boto3
import dotenv
from uuid import uuid4

dotenv.load_dotenv()
aws_access_key_id = os.getenv("AWS_ACCESS_KEY")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

def upload_to_s3(file):
    try:
        s3_obj_name = str(uuid4()) + ".png"
        s3.upload_fileobj(file, "loshuyen-bucket", s3_obj_name)
        print("Upload Successful", s3_obj_name)
        return s3_obj_name
    except Exception as e:
        print(f"Upload Failed: {str(e)}")