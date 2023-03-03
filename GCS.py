import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "seraphic-jet-379316-7f41a3c9cfe7.json"

# client = storage.Client()
# bucket = client.get_bucket('pythongrab')
# blob = bucket.blob("Ideas")
# blob.upload_from_filename("BucketData.txt")


client = storage.Client()
bucket = client.get_bucket('pythongrab')
blob = bucket.blob("Ideas")
data = blob.download_as_string()
text = data.decode('utf-8')
print(text)

#file = open (filename)
#text = file.read()

#with open(filename) as file:
    #print (file.read())

#

