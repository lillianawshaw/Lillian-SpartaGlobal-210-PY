import os
from google.cloud import storage
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "seraphic-jet-379316-7f41a3c9cfe7.json"
def list_blobs(bucket_name):
    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name)
    for blob in blobs:
        print(blob.name)


def download_blob_content(bucket_name, source_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(
        source_blob_name)
    content = blob.download_as_string()
    return content
