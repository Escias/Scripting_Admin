from influxdb_client import InfluxDBClient
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv("token")
org = "anis.bastide@edu.itescia.fr"
bucket = "anis.bastide's Bucket"

client = InfluxDBClient(url=os.getenv("URL"), token=token)

data = "mem,host=host1 used_percent=20"
client.write_api().write(bucket, org, data)