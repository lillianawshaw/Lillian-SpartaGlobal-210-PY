from GCS import *

list_blobs(bucket_name="pythongrab")

text = download_blob_content(bucket_name="pythongrab", source_blob_name="Ideas")
print(str(text))