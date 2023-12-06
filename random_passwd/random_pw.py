# -*- coding: utf-8 -*-
import sys
import string
import argparse
from random import choice


def get_random_password(length=16):
    """
    Get Random Password
    :param length: Default Length 16
    :return:
    """
    punctuation = r"$^+_-&"
    return "".join(choice(string.ascii_letters + string.digits + punctuation) for _ in range(length))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Random Password', description='Generate Random Password')
    try:
        parser.add_argument('-c', '--count', type=int, nargs='?', const=16,
                            help='Random password digits (16 by default)')
        args = parser.parse_args()
        if args.count:
            print(get_random_password(args.count))
        else:
            print(get_random_password())
    except Exception as e:
        print(e)
        sys.exit(0)
