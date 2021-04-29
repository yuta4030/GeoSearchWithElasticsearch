# GeoSearchWithElasticsearch

How to use

``` bash
$ docker-compose up -d

# wait a secound

# create index and insert document made from geojson.json
$ poetry run python geo_search/setting.py
{'acknowledged': True, 'shards_acknowledged': True, 'index': 'geo_example'}

# check the reverse-geocoording
$ poetry run python geo_search/reverse-geocoording.py | jq .
[
  {
    "_index": "geo_example",
    "_type": "_doc",
    "_id": "nKoYHHkB1wUm2qq0Di9x",
    "_score": 1,
    "_source": {
      "type": "Feature",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              0,
              0
            ],
            [
              10,
              0
            ],
            [
              10,
              10
            ],
            [
              0,
              10
            ],
            [
              0,
              0
            ]
          ]
        ]
      },
      "properties": {
        "area_code": "01",
        "name": "ALL",
        "level": 1
      }
    }
  },
  {
    "_index": "geo_example",
    "_type": "_doc",
    "_id": "nqoYHHkB1wUm2qq0Di9y",
    "_score": 1,
    "_source": {
      "type": "Feature",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              0,
              10
            ],
            [
              10,
              10
            ],
            [
              10,
              5
            ],
            [
              0,
              5
            ],
            [
              0,
              10
            ]
          ]
        ]
      },
      "properties": {
        "area_code": "0102",
        "name": "B",
        "level": 2
      }
    }
  },
  {
    "_index": "geo_example",
    "_type": "_doc",
    "_id": "oqoYHHkB1wUm2qq0Di9y",
    "_score": 1,
    "_source": {
      "type": "Feature",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              5,
              5
            ],
            [
              10,
              5
            ],
            [
              10,
              10
            ],
            [
              5,
              10
            ],
            [
              5,
              5
            ]
          ]
        ]
      },
      "properties": {
        "area_code": "010202",
        "name": "B-2",
        "level": 3
      }
    }
  }
]

```