from apscheduler.schedulers.blocking import BlockingScheduler
from Script.Util.database import iterate_for_database
from Script.Util.system_info import get_cpu_info, get_ram_info, get_disk_info, get_network_info, \
    get_system_info, get_mac_address


def main():
    '''
    Main function of application
    :return: None
    '''
    cpu_info = get_cpu_info()
    ram_info = get_ram_info()
    disk_info = get_disk_info()
    network_info = get_network_info()
    system_info = get_system_info()
    mac_address = get_mac_address()
    info = [cpu_info,
            ram_info,
            disk_info,
            network_info,
            system_info]
    iterate_for_database(info, mac_address)


if __name__ == '__main__':
    main()
    scheduler = BlockingScheduler()
    scheduler.add_job(main, 'interval', seconds=5)
    scheduler.start()
