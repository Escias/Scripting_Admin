import string

def string_to_list(str):
    '''
    Convert string to list
    :param str: string
    :return: list
    '''
    li = []
    li[:0] = str
    print(li)
    return li


def to_ascii(li_str):
    '''
    Convert each element of list to ASCII
    :param li_str: list of string
    :return: list of ASCII
    '''
    li = []
    for elem in li_str:
        li.append(ord(elem))
    print(li)
    return li


def to_binary(li_ascii):
    '''
    Convert each element (ascii) of list to binary
    :param li_ascii: list of ascii
    :return: list of binary
    '''
    li = []
    for elem in li_ascii:
        li.append(bin(elem)[2:])
    print(li)
    return li


def frame_list(li_binary):
    '''
    Crop each element of list to 8 position
    :param li_binary: list of binary
    :return: list of rearranged binary element
    '''
    li = []
    for elem in li_binary:
        li.append(elem.zfill(8))
    print(li)
    return li


def list_to_string(li):
    '''
    Convert list to String
    :param li: list
    :return: string based on the list
    '''
    print(''.join(li))
    return ''.join(li)


def bloc(srt, n):
    '''
    Cut the string into list of element of length n
    :param srt: string
    :param n: length of each element to add to the list
    :return: list of rearranged string binary
    '''
    li = []
    for i in range(0, len(srt), n):
        li.append(srt[i:i + n])
    print(li)
    return li


def last_bloc(li_bloc):
    '''
    Crop each element of list to 6 position
    :param li_bloc: list of rearranged string binary
    :return: list of rearranged string binary
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
    :param li_binary: list of binary
    :return: list of decimal
    '''
    li = []
    for elem in li_binary:
        li.append(int(elem, 2))
    print(li)
    return li


def to_base64(li_decimal):
    '''
    Convert decimal to base64 character
    :param li_decimal: list of decimal
    :return: list of element encoded in base 64
    '''
    li = []
    for elem in li_decimal:
        # letter begin at 65 in ASCII list
        li.append(chr(elem+65))
    print(li)
    return li


def multiple_4(str64):
    '''
    change string to multiple of 4
    :param str64: string
    :return: string of length multiple of 4
    '''
    while len(str64) % 4 != 0:
        str64 += '='
    print(str64)
    return str64
