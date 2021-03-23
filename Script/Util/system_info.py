import psutil


def get_cpu_info():
    '''

    :return:
    '''
    cpu = {'cpu_percent': psutil.cpu_percent(interval=1),
           'cpu_count': psutil.cpu_count(),
           'cpu_frequency': psutil.cpu_freq()}
    return cpu
