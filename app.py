import os
import html
from flask import Flask, jsonify
import pandas as pd
import json
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

app = Flask(__name__)

STORAGEACCOUNTURL="DefaultEndpointsProtocol=https;AccountName=pythonstorageaccountsg;AccountKey=ueHYjLQGkRfVCXAjDyDqMYCW5+Sf8duDJp+aSiHuWXHDo4yzS60919XwWZqwnYH8Axo+RyAJzUrGV+hm6uoKfw==;EndpointSuffix=core.windows.net"
CONTAINERNAME= "pythonblobstorecontainer"
BLOBNAME= "small_radio_json.json"

#download from blob
blob_service_client = BlobServiceClient.from_connection_string(STORAGEACCOUNTURL)
container_client = blob_service_client.get_container_client(CONTAINERNAME)
blob_client = container_client.get_blob_client(BLOBNAME)
streamdownloader = blob_client.download_blob()

fileReader = json.loads(streamdownloader.readall())
print(fileReader)

@app.route("/")
def test():
    return fileReader

if __name__ == '__main__':
    app.run(host='localhost', debug=True)
