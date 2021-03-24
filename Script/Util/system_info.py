import psutil
import datetime
import socket


def get_cpu_info():
    '''

    :return:
    '''
    cpu = {'cpu_percent': psutil.cpu_percent(interval=1),
           'cpu_count': psutil.cpu_count(),
           'cpu_frequency': psutil.cpu_freq()}
    return cpu


def get_ram_info():
    '''

    :return:
    '''
    ram = {'ram_usage': psutil.virtual_memory()}
    return ram


def get_disk_info():
    '''

    :return:
    '''
    disk = {'disk_partitions': psutil.disk_partitions(),
            'disk_usage': psutil.disk_usage('/')}
    return disk


def get_network_info():
    network = {'network_io_counter': psutil.net_io_counters(pernic=False, nowrap=True),
               'network_address': psutil.net_if_addrs()}
    return network


def get_sensors_info():
    sensor = {'sensor_temp': psutil.sensors_battery()}
    return sensor


def get_system_info():
    system = {'system_boot_time': datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")}
    return system


def get_ip_client():
    '''

    :return:
    '''
    host = socket.gethostname()
    ip_client = socket.gethostbyname(host)
    return ip_client
