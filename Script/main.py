from Script.Util.system_info import get_cpu_info, get_ram_info, get_disk_info, get_sensors_info, get_network_info, \
    get_system_info, get_ip_client


def main():
    '''
    Main function of application
    :return: None
    '''
    ip_client = get_ip_client()
    cpu_info = get_cpu_info()
    ram_info = get_ram_info()
    disk_info = get_disk_info()
    network_info = get_network_info()
    sensors_info = get_sensors_info()
    system_info = get_system_info()
    print(ip_client)
    for value in cpu_info:
        print('{} : {}'.format(value, cpu_info[value]))
    for value in ram_info:
        print('{} : {}'.format(value, ram_info[value]))
    for value in disk_info:
        print('{} : {}'.format(value, disk_info[value]))
    for value in network_info:
        print('{} : {}'.format(value, network_info[value]))
    for value in sensors_info:
        print('{} : {}'.format(value, sensors_info[value]))
    for value in system_info:
        print('{} : {}'.format(value, system_info[value]))


if __name__ == '__main__':
    main()
