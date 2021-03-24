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


def send_info_to_DB(category, host, value_type, value):
    data = '{},host={} {}={}'.format(category, host, value_type, value)
    write_api.write(bucket, org, data)
