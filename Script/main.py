from Script.Util.system_info import get_cpu_info


def main():
    '''

    :return:
    '''
    cpu = get_cpu_info()
    for value in cpu:
        print('{} : {}'.format(value, cpu[value]))


if __name__ == '__main__':
    main()
