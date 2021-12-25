from simplecrypt import decrypt, DecryptionException


def crack(encrypted, pass_list):
    for passwd in pass_list:
        try:
            print(passwd + ": '" + decrypt(passwd, encrypted).decode('utf8') + "'")
            return
        except DecryptionException as e:
            print(e.args)


if __name__ == '__main__':
    with open("encrypted.bin", "rb") as inp:
        with open("passwords.txt") as pass_ipn:
            crack(inp.read(), [x.strip() for x in pass_ipn.readlines()])
