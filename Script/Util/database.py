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
    '''
    iterate in list and dictionary
    :param info: list contain dictionary
    :param address: mac address of actuel computer
    :return: None
    '''
    for data in info:
        for value in data:
            send_info_to_DB('device', address, value, data[value])


def send_info_to_DB(category, host, value_type, value):
    '''
    Send data to the database InfluxDB
    :param category: category
    :param host: data sender
    :param value_type: type of value
    :param value: value of specific type
    :return: None
    '''
    data = '{},host={} {}={}'.format(category, host, value_type, value)
    write_api.write(bucket, org, data)
