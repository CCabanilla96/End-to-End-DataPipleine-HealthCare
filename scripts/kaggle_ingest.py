import os
import kagglehub

# Proxy configuration (if required)
#os.environ['HTTP_PROXY'] = ''http://username:password@cchproxy1234'
#os.environ['HTTPS_PROXY'] = ''http://username:password@cchproxy1234'

# Download dataset
path = kagglehub.dataset_download("prasad22/healthcare-dataset")

print("Path to dataset files:", path)

#python -m pip install kagglehub --proxy 'http://username:password@cchproxy1234'

#pip install pandas sqlalchemy psycopg2-binary --proxy 'http://username:password@cchproxy1234'
