import os

from google.cloud import storage

# Replace '/path/to/your/keyfile.json' with the actual path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/owlery-v2.json"

storage_client = storage.Client()
bucket = storage_client.create_bucket("new_bucket")
print(f'Bucket "{bucket.name}" opened')

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f'File {source_file_name} uploaded to {destination_blob_name}')

def download_blob(bucket_name, source_blob_name, destination_file_name):
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print(f'Blob {source_blob_name} downloaded to {destination_file_name}')

def write_string_to_cloud(bucket_name, content, destination_blob_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_string(content)
    print(f'File {destination_blob_name} uploaded to {destination_blob_name}')

upload_blob('ibdifs', 'test_upload.txt', 'blobnameig')
