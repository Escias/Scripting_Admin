import psutil
import datetime
import time
import socket
from getmac import get_mac_address as gma

from Script.Util.database import send_info_to_DB


def get_cpu_info():
    '''
    Get cpu information
    :return: dictionary with cpu informations
    '''
    cpu = {'cpu_percent': psutil.cpu_percent(interval=1),
           'cpu_frequency': psutil.cpu_freq().current}
    send_info_to_DB("cpu", "mac_anis", "cpu_utilisation", cpu["cpu_percent"])
    send_info_to_DB("cpu", "mac_anis", "cpu_frequency", cpu["cpu_frequency"])
    return cpu


def get_ram_info():
    '''
    Get memory (ram) information
    :return: dictionary with ram informations
    '''
    ram = {'ram_usage': psutil.virtual_memory().percent}
    send_info_to_DB("ram", "mac_anis", "ram_utilisation", ram["ram_usage"])
    return ram


def get_disk_info():
    '''
    Get disk information
    :return: dictionary with disk informations
    '''
    disk = {'disk_usage': psutil.disk_usage('/').percent}
    send_info_to_DB("disk", "mac_anis", "ram_utilisation", disk["disk_usage"])
    return disk


def get_network_info():
    '''
    Get network information
    :return: dictionary with network informations
    '''
    network = {'network_bytes_sent': psutil.net_io_counters(pernic=False, nowrap=True).bytes_sent,
               'network_bytes_receive': psutil.net_io_counters(pernic=False, nowrap=True).bytes_recv,
               'network_packets_sent': psutil.net_io_counters(pernic=False, nowrap=True).packets_sent,
               'network_packets_receive': psutil.net_io_counters(pernic=False, nowrap=True).packets_recv,
               'errin': psutil.net_io_counters(pernic=False, nowrap=True).errin,
               'errout': psutil.net_io_counters(pernic=False, nowrap=True).errout,
               'dropin': psutil.net_io_counters(pernic=False, nowrap=True).dropin,
               'dropout': psutil.net_io_counters(pernic=False, nowrap=True).dropout,
               }
    send_info_to_DB("network", "mac_anis", "bytes_sent", network["network_bytes_sent"])
    send_info_to_DB("network", "mac_anis", "bytes_received", network["network_bytes_receive"])
    send_info_to_DB("network", "mac_anis", "packets_sent", network["network_packets_sent"])
    send_info_to_DB("network", "mac_anis", "packets_received", network["network_packets_receive"])
    send_info_to_DB("network", "mac_anis", "errin", network["errin"])
    send_info_to_DB("network", "mac_anis", "errout", network["errout"])
    send_info_to_DB("network", "mac_anis", "dropin", network["dropin"])
    send_info_to_DB("network", "mac_anis", "dropout", network["dropout"])
    return network


def get_system_info():
    '''
    Get system information
    :return: dictionary with system informations
    '''
    s = str(datetime.datetime.now())[:-7]
    d = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
    uptime=str(datetime.timedelta(seconds=time.mktime(d.timetuple())-psutil.boot_time()))
    system = {'system_uptime': uptime}
    send_info_to_DB("device", "mac_anis", "uptime", system["system_uptime"])
    return system
