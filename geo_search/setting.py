import os
import geojson

from elasticsearch import Elasticsearch, helpers


INDEX_NAME = "geo_example"
GEO_JSON_FILE_PATH = f"{os.path.dirname(__file__)}/test_data/geojson.json"


def delete_index(es: Elasticsearch):
    if es.indices.exists(index=INDEX_NAME):
        result = es.indices.delete(index=INDEX_NAME)
        print(result)


def create_index(es: Elasticsearch):
    result = es.indices.create(index=INDEX_NAME, body={
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


def index_geojson(es: Elasticsearch):
    with open(GEO_JSON_FILE_PATH) as f:
        gj = geojson.load(f)
        features = ({
            "_index": INDEX_NAME,
            "_source": feature,
        } for feature in geojson_to_es(gj))

        helpers.bulk(es, features)


if __name__ == '__main__':
    es = Elasticsearch(host="localhost", port=9200)
    delete_index(es=es)
    create_index(es=es)
    index_geojson(es=es)
