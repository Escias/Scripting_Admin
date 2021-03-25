from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('token')
org = 'anis.bastide@edu.itescia.fr'
bucket = "anis.bastide's Bucket"
client = InfluxDBClient(url=os.getenv('URL'), token=token)
write_api = client.write_api(write_options=SYNCHRONOUS)


def iterate_for_database(info, address):
    print(address)
    for data in info:
        for value in data:
            print('{} : {}'.format(value, data[value]))
            send_info_to_DB('device', address, value, data[value])


def send_info_to_DB(category, host, value_type, value):
    data = '{},host={} {}={}'.format(category, host, value_type, value)
    write_api.write(bucket, org, data)
