import os
import geojson

from opensearchpy import OpenSearch, helpers


INDEX_NAME = "geo_example"
GEO_JSON_FILE_PATH = f"{os.path.dirname(__file__)}/test_data/geojson.json"


def delete_index(client: OpenSearch):
    if client.indices.exists(index=INDEX_NAME):
        result = client.indices.delete(index=INDEX_NAME)
        print(result)


def create_index(client: OpenSearch):
    result = client.indices.create(index=INDEX_NAME, body={
        "mappings": {
            "properties": {
                "geometry": {
                    "type": "geo_shape"
                }
            }
        }
    })

    print(result)


def geojson_to_es(gj: geojson):
    for feature in gj['features']:
        yield feature


def index_geojson(client: OpenSearch):
    with open(GEO_JSON_FILE_PATH) as f:
        gj = geojson.load(f)
        features = ({
            "_index": INDEX_NAME,
            "_source": feature,
        } for feature in geojson_to_es(gj))

        helpers.bulk(client, features)


if __name__ == '__main__':
    client = OpenSearch(host="localhost", port=9200)
    delete_index(client=client)
    create_index(client=client)
    index_geojson(client=client)
