from google.cloud import aiplatform

GCP_PROJECT = "PLACEHOLDER"
GCP_REGION = "PLACEHOLDER"
EXPERIMENT_NAME = "PLACEHOLDER"

# Vertex AI initialization
aiplatform.init(
    project=GCP_PROJECT,
    location=GCP_REGION,
    experiment=EXPERIMENT_NAME,
)