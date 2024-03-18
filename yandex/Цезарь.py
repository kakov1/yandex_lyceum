alphabet_up = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_low = list(alphabet_up.lower())
alphabet_up = list(alphabet_up)


def encrypt_caesar(msg, *args, shift=3):
    message = ''
    if len(args) != 0:
        shift = args[0]
    if shift >= 32:
        while shift >= 32:
            shift -= 32
    elif shift <= -32:
        while shift <= -32:
            shift += 32
    for i in msg:
        if i in alphabet_up:
            if alphabet_up.index(i) + shift > 31:
                message += alphabet_up[alphabet_up.index(i) + shift - 32]
            else:
                message += alphabet_up[alphabet_up.index(i) + shift]
        elif i in alphabet_low:
            if alphabet_low.index(i) + shift > 31:
                message += alphabet_low[alphabet_low.index(i) + shift - 32]
            else:
                message += alphabet_low[alphabet_low.index(i) + shift]
        else:
            message += i
    return message


def decrypt_caesar(msg, *args, shift=3):
    if len(args) == 0:
        return encrypt_caesar(msg, -shift)
    else:
        return encrypt_caesar(msg, -args[0])
