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
        print('[WARN] Cannot access temperature!')

    cpu = {'cpu_percent': psutil.cpu_percent(interval=1),
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
    uptime = str(datetime.timedelta(seconds=time.mktime(d.timetuple()) - psutil.boot_time()))
    system = {'system_uptime': str('"{}"'.format(uptime))}
    return system


def get_system_os():
    platform.system()
    return platform.system()


def get_mac_address():
    '''
    Get mac address
    :return: mac address
    '''
    mac_address = gma()
    return str('"{}"'.format(mac_address))
