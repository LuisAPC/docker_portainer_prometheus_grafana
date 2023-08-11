import json
import pandas as pd
from pprint import PrettyPrinter
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "covid19CSV"
org = "my-org"
token = "SImrhiZiUkCvDsxI_U9J_Gg_kch8RDm15Ux7zx7g2Sjudwlbhj0ej80yhHnPOl2zvG-5qpI7X7xuMzNeRE3osg=="
# Store the URL of your InfluxDB instance
url = "https://luis-influxdb.duckdns.org/"

client = InfluxDBClient(
    url=url,
    token=token,
    org=org
    # debug=True
)
write_client = client.write_api(write_options=SYNCHRONOUS)

# 1st way of creating json file
# loaded = json.loads(
#     '{"measurement": "test10", "tags": {"Ort": "Rxxxx"}, "fields": {"temp1": 2.6, "hum1": 66.0, "temp2": 2.3, "hum2": 81.0, "temp3": 22.0, "hum3": 32.0}}')

# 2nd way of creating json file
# loaded = [{
#     "measurement": "test11",
#     "tags": {"Ort": "Rxxxx"},
#     "fields": {
#         "temp1": 2.6,
#         "hum1": 66.0,
#         "temp2": 2.3,
#         "hum2": 81.0,
#         "temp3": 22.0,
#         "hum3": 32.0
#     }
# }]

df = pd.read_csv('C:/Users/luisp/Desktop/docker_portainer_prometheus_grafana/write_influxDB/csvtest.csv')
# df.set_index(['_time'], inplace=True)


for row_idx, row in df.iterrows():
    # for row in rows:
    #     print(row)
    print(row)
    loaded = [{
        "measurement": "testB",
        "tags": {"Host": row[2]},
        "fields": {
            "time": row[0],
            "region": row[1],
            "host": row[2],
            "usage_user": row[3],
        }
    }]
    # printer = PrettyPrinter()
    # printer.pprint(loaded)
    # write_client.write(bucket=bucket, record=loaded)
