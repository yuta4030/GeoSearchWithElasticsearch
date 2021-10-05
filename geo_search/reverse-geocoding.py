import json

from opensearchpy import OpenSearch


INDEX_NAME = "geo_example"

client = OpenSearch(host="localhost", port=9200)

target = [[7.0, 7.0], [7.0, 7.0]]
result = client.search(index=INDEX_NAME, body={
    "query": {
        "bool": {
            "must": {
                "match_all": {}
            },
            "filter": {
                "geo_shape": {
                    "geometry": {
                        "shape": {
                            "type": "envelope",
                            "coordinates": target
                        },
                        "relation": "intersects"
                    }
                }
            }
        }
    }
})

print(json.dumps(result["hits"]["hits"]))
