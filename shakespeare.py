from elasticsearch import Elasticsearch, AsyncElasticsearch
import asyncio
import pandas as pd
from io import StringIO


ELASTIC_PASSWORD = "changeme"
URL = "http://localhost:9200"

client = AsyncElasticsearch(
    URL,
    basic_auth=("elastic", ELASTIC_PASSWORD)
)


index_name = "shakespeare"

async def get_shakespeare_data():
    async with client:
        resp = await client.search(index=index_name, query={
            "match_all": {},
        })

        print("Got %d Hits:" % resp['hits']['total']['value'])

        for hit in resp['hits']['hits']:
            source = hit['_source']
            print(f"{source['@timestamp']} | {source['play_name']} | {source['line_number']} | {source['text_entry']}")

        return resp

result = asyncio.run(get_shakespeare_data())

print(result)