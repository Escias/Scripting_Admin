import string

from Script.Cours.base64 import to_binary, list_to_string, bloc, to_decimal, frame_list, last_bloc


def decimal_to_ascii(decimal_list):
    for i in range(len(decimal_list)):
        decimal_list[i] = chr(decimal_list[i] + 65)
    print(decimal_list)
    return decimal_list


def remove_zero(binary_list):
    for i in range(len(binary_list)):
        while binary_list[i] == 0:
            binary_list[i] = binary_list[i][1:]
    print(binary_list)
    return binary_list


def stringToDecimal(base64_string):
    '''
    Convert decimal to base64 character
    :param li_decimal: list of decimal
    :return: list of element encoded in base 64
    '''
    li = []
    cleaned_string = removeEquals(base64_string)
    reverse_table64 = getReverseTable64()
    for elem in cleaned_string:
        li.append(reverse_table64[elem])
    print(li)

    binary_list = to_binary(li)
    frame = frame_list(binary_list, 6)
    binary_string = list_to_string(frame)
    print(type(binary_string))
    binary_string_without_zero_after = remove_zero_after(binary_string)
    binary_list_eight = bloc(binary_string_without_zero_after, 8)
    binary_list_six = last_bloc(binary_list_eight, 8)
    binary_list_without_zero = remove_zero(binary_list_six)
    decimal_list = to_decimal(binary_list_without_zero)
    char_list = decimal_to_ascii(decimal_list)
    print(list_to_string(char_list))
    return li


def remove_zero_after(binary_string):
    binary_string.rstrip("0")
    return binary_string


def removeEquals(str64):
    '''
    change string to multiple of 4
    :param str64: string
    :return: string of length multiple of 4
    '''
    string = str64.split("=")
    return string[0]


def getReverseTable64():
    table64 = {}
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    numbers = string.digits
    characters = uppercase_letters + lowercase_letters + numbers + "+/"
    for i in range(len(characters)):
        table64[characters[i]] = i
    return table64
