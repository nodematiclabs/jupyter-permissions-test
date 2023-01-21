from google.cloud import bigquery

GCP_PROJECT = "PLACEHOLDER"
BQ_DATASET = "PLACEHOLDER"

client = bigquery.Client()

# Create the BigQuery dataset
dataset_id = f"{GCP_PROJECT}.{BQ_DATASET}"
dataset = bigquery.Dataset(dataset_id)
dataset.location = "US"
try:
    dataset = client.create_dataset(dataset, timeout=30)  # Make an API request.
    print("Created dataset {}.{}".format(client.project, dataset.dataset_id))
except exceptions.Conflict:
    print("Dataset already exists - choose a new name if the dataset is not under your control")
    pass