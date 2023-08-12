from pprint import PrettyPrinter
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
import pandas as pd
import numpy as np

bucket = "covid19JSON"
org = "my-org"
token = "DxwfAGZ_EBz_P22uwa_yWqO-QujNmTgu740itD0qzMq19kIv4UTvdjKcRJ38SMWySRdmM3tuPRZSSmCb_z_wYw=="
# Store the URL of your InfluxDB instance
url = "https://luis-influxdb.duckdns.org/"


def prepare_influxdb_comms(url, token, org):
    client = InfluxDBClient(
        url=url,
        token=token,
        org=org
        # debug=True
    )

    write_client = client.write_api(write_options=SYNCHRONOUS)

    return write_client


def send_to_influxdb(df, write_client):
    for row_idx, row in df.iterrows():
        loaded = [{
            "measurement": "Test2",
            "tags": {"Country": row[2]},
            "fields": {
                "Country_code": row[1],
                "Cumulative_cases": row[3]
            }
        }]
    printer = PrettyPrinter()
    printer.pprint(loaded)
        # write_client.write(bucket=bucket, record=loaded)


def csv_to_json():

    df = pd.read_csv('C:/Users/luisp/Desktop/docker_portainer_prometheus_grafana/write_influxDB/WHO-COVID-19-global-data.csv')
    df.drop(
        ['WHO_region', 'New_cases', 'New_deaths', 'Cumulative_deaths'],
        axis=1,
        inplace=True
        )
    df['Date_reported'] = pd.to_datetime(df['Date_reported'])
    df = df[df['Date_reported'] == '2023-08-09']
    df['Country_code'].replace(' ', np.nan, inplace=True)
    df.dropna(inplace=True)
    # df.set_index(['Date_reported'], inplace=True)
    # print(df.head())

    return df


write_client = prepare_influxdb_comms(url, token, org)
df = csv_to_json()
send_to_influxdb(df, write_client)
