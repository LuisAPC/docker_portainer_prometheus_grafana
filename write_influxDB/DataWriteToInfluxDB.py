'''
docker exec -it influxdb /bin/bash
influx write -b <%= bucket %> -f path/to/example.csv
'''

import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

# Write data to InfluxDB with Python

bucket = "testbucket"
org = "my-org"
token = "FOsL9piX9Bl5GrkLovQRn3QocdyMl5i3q2Ig92sl7B22jbK21nfnSJtuki33WELYIXicgqVds9_spqtHtqzhTg=="
# Store the URL of your InfluxDB instance
url = "https://luis-influxdb.duckdns.org/"

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)

write_api = client.write_api(write_options=SYNCHRONOUS)

p = influxdb_client.Point("my_measurement").tag("location", "Prague").field("temperature", 15.0)
write_api.write(bucket=bucket, org=org, record=p)

# Query data from InfluxDB with Python

# query_api = client.query_api()

# query = ' from(bucket:"my-bucket")\
# |> range(start: -10m)\
# |> filter(fn:(r) => r._measurement == "my_measurement")\
# |> filter(fn: (r) => r.location == "Prague")\
# |> filter(fn:(r) => r._field == "temperature" )'

# result = query_api.query(org=org, query=query)
# results = []

# for table in result:
#     for record in table.records:
#         results.append((record.get_field(), record.get_value()))

# print(results)
