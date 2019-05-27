import pandas as pd
from google.colab import auth
from google.cloud import bigquery


class BQ:
    def __init__(self, project_id, wait=True):
        self.wait = wait
        self.project_id = project_id
        auth.authenticate_user()
        self.client = bigquery.Client(project_id)

    def get(self, query):
        return pd.read_gbq(query, project_id=self.project_id, dialect='standard')

    def wait_job(self, job):
        job.result() if self.wait == True else False
        return job

    def table_ref(self, path):
        dataset_name, table_name = path.split('.')
        return self.client.dataset(dataset_name).table(table_name)

    def run(self, **args):
        job_config = bigquery.QueryJobConfig()
        job_config.destination = args['destination']
        job_config.create_disposition = 'CREATE_IF_NEEDED'
        job_config.write_disposition = 'WRITE_TRUNCATE' # WRITE_TRUNCATE or WRITE_APPEND
        job_config.use_legacy_sql = False
        job_config.allow_large_results = True
        job = self.client.query(args['query'], job_config=job_config)
        return self.wait_job(job)

    def create_table(self, query, table_path):
        table_ref = self.table_ref(table_path)
        create_job = self.run(query = query, destination=table_ref)
        return self.wait_job(create_job)

    def export_csv(self, table_path, destination_uri):
        table_ref = self.table_ref(table_path)
        extract_job = self.client.extract_table(table_ref, destination_uri, location='US')
        return self.wait_job(extract_job)

    def delete_table(self, table_path):
        table_ref = self.table_ref(table_path)
        self.client.delete_table(table_ref)