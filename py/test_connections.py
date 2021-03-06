from amqp import Connection
from datetime import datetime
from elasticsearch import Elasticsearch
from memcache import Client, SERVER_MAX_KEY_LENGTH, SERVER_MAX_VALUE_LENGTH
import os
import psycopg2
from time import sleep
import unittest


class TestMemcache(unittest.TestCase):
    def test_elastic_connection(self):
        # wait until elastic will start
        sleep(8)

        print('ELASTIC_PORT_9200_TCP_ADDR')
        print(os.environ.get('ELASTIC_PORT_9200_TCP_ADDR'))
        print('ELASTIC_PORT_9200_TCP_PORT')
        print(os.environ.get('ELASTIC_PORT_9200_TCP_PORT'))
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

    def test_postgres_connection(self):
        print('POSTGRES_PORT_5432_TCP_ADDR')
        print(os.environ.get('POSTGRES_PORT_5432_TCP_ADDR'))
        print('POSTGRES_PORT_5432_TCP_PORT')
        print(os.environ.get('POSTGRES_PORT_5432_TCP_PORT'))
        conn = psycopg2.connect(host=os.environ.get('POSTGRES_PORT_5432_TCP_ADDR'),
                                user="postgres",
                                password="secret",
                                port=os.environ.get('POSTGRES_PORT_5432_TCP_PORT'))
        self.assertEqual(conn.closed, False)
        conn.close()
        self.assertEqual(conn.closed, True)

    def test_rabbitmq_conection(self):
        print('RABBITMQ_PORT_5672_TCP_ADDR')
        print(os.environ.get('RABBITMQ_PORT_5672_TCP_ADDR'))
        print('RABBITMQ_PORT_5672_TCP_PORT')
        print(os.environ.get('RABBITMQ_PORT_5672_TCP_PORT'))
        # BROKER_URL = 'amqp://guest:guest@localhost:5672//'
        conn = Connection(host='{}:{}'.format(
            os.environ.get('RABBITMQ_PORT_5672_TCP_ADDR'),
            os.environ.get('RABBITMQ_PORT_5672_TCP_PORT')))
        self.assertIsNotNone(conn.connection)
        conn.close()
        self.assertIsNone(conn.connection)

    def test_volume_connection(self):
        print('os.listdir("/webapp")')
        print(os.listdir("/webapp"))
        self.assertTrue('hello.world.txt' in os.listdir("/webapp"))
