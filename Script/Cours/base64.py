def string_to_list(str):
    li = []
    li[:0] = str
    print(li)
    to_ascii(li)
    return li


def to_ascii(cha):
    li = []
    for c in cha:
        li.append(ord(c))
    print(li)
    to_binary(li)
    return li


def to_binary(cha):
    li = []
    for c in cha:
        li.append(bin(c).replace('b', ''))
    print(li)
    # frame_list(li)
    list_to_string(li)
    return li


def frame_list(cha):
    li = []
    for c in cha:
        li.append('0'+c)
    print(li)
    list_to_string(li)
    return li


def list_to_string(cha):
    print(''.join(cha))
    bloc(''.join(cha), 6)
    return ''.join(cha)


def bloc(cha, n):
    li = []
    for i in range(0, len(cha), n):
        li.append(cha[i:i+n])
    print(li)
    last_bloc(li)
    return li


def last_bloc(cha):
    li = []
    for c in cha:
        while len(c) < 6:
            c = c + '0'
        li.append(c)
    print(li)
    to_decimal(li)
    return li


def to_decimal(cha):
    li = []
    for c in cha:
        li.append(int(c, 2))
    print(li)
    to_base64(li)
    return li


def to_base64(cha):
    li = []
    for c in cha:
        li.append(chr(c))
    print(li)
    return li


