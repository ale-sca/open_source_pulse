from google.cloud import bigquery
client = bigquery.Client(project="open-source-pulse")
print("Connected to project:", client.project)

