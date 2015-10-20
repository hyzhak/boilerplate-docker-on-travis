from datetime import datetime
from elasticsearch import Elasticsearch
import os


def test_connection():
    print('ELASTIC_PORT_9200_TCP_ADDR')
    print(os.environ.get('ELASTIC_PORT_9200_TCP_ADDR'))
    print('ELASTICSEARCH_PORT_9200_TCP_ADDR')
    print(os.environ.get('ELASTICSEARCH_PORT_9200_TCP_ADDR'))
    print('ELASTIC_PORT_9200_TCP_PORT')
    print(os.environ.get('ELASTIC_PORT_9200_TCP_PORT'))
    print('ELASTICSEARCH_PORT_9200_TCP_PORT')
    print(os.environ.get('ELASTICSEARCH_PORT_9200_TCP_PORT'))
    es = Elasticsearch([{'host': os.environ.get('ELASTIC_PORT_9200_TCP_ADDR'),
                         'port': os.environ.get('ELASTIC_PORT_9200_TCP_PORT')}])
    es.index(index="my-index", doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})
