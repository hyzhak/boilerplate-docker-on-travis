from datetime import datetime
from elasticsearch import Elasticsearch
from memcache import Client, SERVER_MAX_KEY_LENGTH, SERVER_MAX_VALUE_LENGTH
import os
import unittest


class TestMemcache(unittest.TestCase):
    def test_elastic_connection(self):
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

    def test_memcached_connection(self):
        # python-memcached
        print('MEMCACHED_PORT_11211_TCP_ADDR')
        print(os.environ.get('MEMCACHED_PORT_11211_TCP_ADDR'))
        print('MEMCACHED_PORT_11211_TCP_PORT')
        print(os.environ.get('MEMCACHED_PORT_11211_TCP_PORT'))

        mc = Client([
            os.environ.get('MEMCACHED_PORT_11211_TCP_ADDR')
        ], debug=1)

        mc.set('a_string', 'some random string')
        newval = mc.get('a_string')
        self.assertEqual(newval, 'some random string')

        mc.disconnect_all()
