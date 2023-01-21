# Jupyter Notbook Permissions Tests (Vertex AI Workbench)

1. Setup a service account in Google Cloud Platform with permissions across Cloud Storage, BigQuery, and Vertex AI.  For example, apply the roles:
    1. Storage Admin
    1. BigQuery Admin
    1. Vertex AI Administrator
1. Create a Jupyter notebook using Vertex AI Workbench
1. In the notebook, run `bucket.py`, `dataset.py`, and `experiment.py` (replace `"PLACEHOLDER"`s with your values)
    1. You will need to install the Vertex AI SDK by running `pip install google-cloud-aiplatform` in a terminal, for the last example to work
    1. These are all serverless resources with low monthly cost, but in any case they should be deleted if/when they are not needed