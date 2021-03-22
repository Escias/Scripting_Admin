from Script.Cours.base64 import string_to_list, to_ascii, to_binary, frame_list, list_to_string, bloc, last_bloc, \
    to_decimal, to_base64, multiple_4


def main(li):
    string_to_list(li)


if __name__ == '__main__':
    to_list = string_to_list('ABCDE')
    list_ascii = to_ascii(to_list)
    list_binary = to_binary(list_ascii)
    frame = frame_list(list_binary)
    to_string = list_to_string(frame)
    bloc = bloc(to_string, 6)
    lbloc = last_bloc(bloc)
    list_decimal = to_decimal(lbloc)
    list_base64 = to_base64(list_decimal)
    str_base64 = list_to_string(list_base64)
    multiple_4(str_base64)
