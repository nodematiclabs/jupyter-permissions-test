from google.cloud import storage

GCP_REGION = "PLACEHOLDER"
GCP_BUCKET = "PLACEHOLDER"

storage_client = storage.Client()

try:
    bucket = storage_client.bucket(GCP_BUCKET)
    bucket.storage_class = "STANDARD"
    new_bucket = storage_client.create_bucket(bucket, location=GCP_REGION)
except exceptions.Conflict:
    print("Bucket already exists - choose a new name if the bucket is not under your control")
    pass