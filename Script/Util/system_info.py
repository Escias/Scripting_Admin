import psutil
import datetime
import socket
from getmac import get_mac_address as gma


def get_ip_client():
    '''

    :return:
    '''
    ip_client = gma()
    return ip_client


def get_cpu_info():
    '''

    :return:
    '''
    cpu = {'cpu_percent': psutil.cpu_percent(interval=1),
           'cpu_count': psutil.cpu_count(),
           'cpu_frequency': psutil.cpu_freq().current}
    return cpu


def get_ram_info():
    '''

    :return:
    '''
    ram = {'ram_usage': psutil.virtual_memory().percent}
    return ram


def get_disk_info():
    '''

    :return:
    '''
    disk = {'disk_usage': psutil.disk_usage('/').percent}
    return disk


def get_network_info():
    network = {'network_bytes_sent': psutil.net_io_counters(pernic=False, nowrap=True).bytes_sent,
               'network_bytes_receive': psutil.net_io_counters(pernic=False, nowrap=True).bytes_recv,
               'network_packets_sent': psutil.net_io_counters(pernic=False, nowrap=True).packets_sent,
               'network_packets_receive': psutil.net_io_counters(pernic=False, nowrap=True).packets_recv}
    return network


def get_sensors_info():
    sensor = {'sensor_battery': psutil.sensors_battery().percent}
    return sensor


def get_system_info():
    system = {'system_boot_time': datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")}
    return system
