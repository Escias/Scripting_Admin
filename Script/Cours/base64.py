import binascii


def string_to_list(str):
    '''
    Convert string to list
    :param str:
    :return:
    '''
    li = []
    li[:0] = str
    print(li)
    return li


def to_ascii(li_str):
    '''
    Convert each element of string to ASCII
    :param li_str:
    :return:
    '''
    li = []
    for elem in li_str:
        li.append(ord(elem))
    print(li)
    return li


def to_binary(li_ascii):
    '''
    Convert each element (ascii) of list to binary
    :param li_ascii:
    :return:
    '''
    li = []
    for elem in li_ascii:
        li.append(bin(elem)[2:])
    print(li)
    return li


def frame_list(li_binary):
    '''
    Crop each element of list to 8 position
    :param li_binary:
    :return:
    '''
    li = []
    for elem in li_binary:
        li.append(elem.zfill(8))
    print(li)
    return li


def list_to_string(li):
    '''
    Convert list to String
    :param li:
    :return:
    '''
    print(''.join(li))
    return ''.join(li)


def bloc(srt, n):
    '''
    Cut the string into list of element of length n
    :param srt:
    :param n:
    :return:
    '''
    li = []
    for i in range(0, len(srt), n):
        li.append(srt[i:i + n])
    print(li)
    return li


def last_bloc(li_bloc):
    '''
    Crop each element of list to 6 position
    :param li_bloc:
    :return:
    '''
    li = []
    for elem in li_bloc:
        while len(elem) < 6:
            elem = elem.ljust(6, '0')
        li.append(elem)
    print(li)
    return li


def to_decimal(li_binary):
    '''
    convert each element (binary) of list to decimal
    :param li_binary:
    :return:
    '''
    li = []
    for elem in li_binary:
        li.append(int(elem, 2))
    print(li)
    return li


def to_base64(li_decimal):
    '''
    Convert decimal to base64 character
    :param li_decimal:
    :return:
    '''
    li = []
    for elem in li_decimal:
        li.append(chr(elem+65))
    print(li)
    return li


def multiple_4(str64):
    while len(str64) % 4 != 0:
        str64 += '='
    print(str64)
    return str64
