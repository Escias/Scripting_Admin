import psutil
import datetime
import time
import platform
from getmac import get_mac_address as gma


def get_cpu_info():
    '''
    Get cpu information
    :return: dictionary with cpu informations
    '''
    if get_system_os() == 'Windows':
        temperature = 'Not Supported'
    elif get_system_os() == 'Linux':
        temperature = psutil.sensors_temperatures(fahrenheit=False)
    else:
        temperature = ''
    cpu = {'cpu_percent': psutil.cpu_percent(interval=1),
           'cpu_frequency': psutil.cpu_freq().current}
    if temperature != "":
        cpu["cpu_temperature"] = temperature
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
               'network_packets_receive': psutil.net_io_counters(pernic=False, nowrap=True).packets_recv,
               'network_error_in': psutil.net_io_counters(pernic=False, nowrap=True).errin,
               'network_error_out': psutil.net_io_counters(pernic=False, nowrap=True).errout,
               'network_packets_drop_in': psutil.net_io_counters(pernic=False, nowrap=True).dropin,
               'network_packets_drop_out': psutil.net_io_counters(pernic=False, nowrap=True).dropout,
               }
    return network


def get_system_info():
    '''
    Get system information
    :return: dictionary with system informations
    '''
    s = str(datetime.datetime.now())[:-7]
    d = datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
    uptime = float(time.mktime(d.timetuple()) - psutil.boot_time())
    system = {'system_uptime': uptime}
    return system


def get_system_os():
    platform.system()
    return platform.system()


def get_mac_address():
    '''
    Get mac address
    :return: mac address
    '''
    address = gma().replace(':', '')
    return address


def add_before_in_string(srt, insert, to_replace):
    '''
    Insert a value before specified value in string
    :param srt: string to modify
    :param insert: value to insert
    :param to_replace: value to replace
    :return: modified string
    '''
    srt = srt.replace(to_replace, insert + to_replace)
    return srt


def format_uptime(uptime):
    '''
    Change format of date to fit with influxDB
    :param uptime: date to format
    :return: formatted date
    '''
    time = uptime.split(':')
    new_uptime = '{}H{}m{}s'.format(time[0], time[1], time[2])
    return new_uptime
