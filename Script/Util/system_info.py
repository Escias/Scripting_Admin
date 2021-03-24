import psutil
import datetime
import platform
import socket
from getmac import get_mac_address as gma


def get_ip_client():
    '''
    Get mac address
    :return: mac address
    '''
    ip_client = gma()
    return ip_client


def get_cpu_info():
    '''
    Get cpu information
    :return: dictionary with cpu informations
    '''
    if get_system_os() == "Windows":
        temperature = "Not Supported"
    elif get_system_os() == "Linux":
        temperature = psutil.sensors_temperatures(fahrenheit=False)
    else:
        print("[WARN] Cannot access temperature!")

    cpu = {'cpu_percent': psutil.cpu_percent(interval=1),
           'cpu_count': psutil.cpu_count(),
           'cpu_temperature': temperature,
           'cpu_frequency': psutil.cpu_freq().current}
    return cpu


def get_ram_info():
    '''
    Get memory (ram) information
    :return: dictionary with ram informations
    '''
    ram = {'ram_usage': psutil.virtual_memory().percent}
    return ram


def get_disk_info():
    '''
    Get disk information
    :return: dictionary with disk informations
    '''
    disk = {'disk_usage': psutil.disk_usage('/').percent}
    return disk


def get_network_info():
    '''
    Get network information
    :return: dictionary with network informations
    '''
    network = {'network_bytes_sent': psutil.net_io_counters(pernic=False, nowrap=True).bytes_sent,
               'network_bytes_receive': psutil.net_io_counters(pernic=False, nowrap=True).bytes_recv,
               'network_packets_sent': psutil.net_io_counters(pernic=False, nowrap=True).packets_sent,
               'network_packets_receive': psutil.net_io_counters(pernic=False, nowrap=True).packets_recv}

    return network


def get_sensors_info():
    '''
    Get sensors information
    :return: dictionary with sensors informations
    '''
    try:
        sensor = ""
        sensor = {'sensor_battery': psutil.sensors_battery().percent}
    except (AttributeError, TypeError):
        print('[WARN] User has no battery !')
        return sensor


def get_system_info():
    '''
    Get system information
    :return: dictionary with system informations
    '''
    system = {'system_boot_time': datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")}
    return system


def get_system_os():
    platform.system()
    return platform.system()
