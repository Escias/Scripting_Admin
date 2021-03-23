from influxdb_client import InfluxDBClient

token = "kcBQaDuqc66x4v-Vjz4diqSIe5mbSaAFp8oeH07uI0Mag81ZvFpHh3mb5QnbF_woUqHtRnuLYciR8mOk5BhNUg=="
org = "anis.bastide@edu.itescia.fr"
bucket = "anis.bastide's Bucket"

client = InfluxDBClient(url="https://eu-central-1-1.aws.cloud2.influxdata.com/", token=token)

data = "mem,host=host1 used_percent=20"
client.write_api().write(bucket, org, data)