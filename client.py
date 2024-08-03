import boto3
import os
from time import sleep

def upload_files(bucket_name):
    s3 = boto3.client('s3')
    files = {
        "project.txt": 1024,  # 1KB
        "temp.txt": 1024,  # 1KB
        "project_new.txt": 1024,  # 1KB
        "temporary_data.txt": 2560,  # 2.5KB
        "project_new_new.txt": 1024,  # 1KB
        "real_temporary_data.txt": 2048  # 2KB
    }

    # upload file
    for file_name, size in files.items():
        with open(file_name, 'wb') as f:
            f.write(os.urandom(size))  

        # upload to s3
        with open(file_name, 'rb') as f:
            s3.upload_fileobj(f, bucket_name, file_name)
            print(f"Uploaded {file_name} to {bucket_name}")

        os.remove(file_name)
        sleep(60)

upload_files("s3bucketprojectstack-sourceadfc1803-du1kudua6l79")

