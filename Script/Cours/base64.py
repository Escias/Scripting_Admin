def string_to_list(str):
    li = []
    li[:0] = str
    print(li)
    return li


def to_ascii(cha):
    li = []
    for c in cha:
        li.append(ord(c))
    print(li)
    return li


def to_binary(cha):
    li = []
    for c in cha:
        li.append(bin(c))
    print(li)
    return c


def frame_list(cha):
    li = []
    for c in cha:
        li.append('0'+c)
    print(li)
    return li


def list_to_string(cha):
    print(''.join(cha))
    return ''.join(cha)


def bloc(cha, n):
    li = []
    for i in range(0, len(cha), n):
        li.append(cha[i:i+n])
    return li


def last_bloc(cha):
    li = []
    for c in cha:
        while len(c) < 6:
            c = c + '0'
        li.append(c)
    return li



