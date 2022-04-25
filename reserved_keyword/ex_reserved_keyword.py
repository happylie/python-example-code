#!/usr/bin/env python
# -*- coding: utf-8 -*-
import platform
from keyword import kwlist


def check_kwlist(word):
    if word in kwlist:
        return True
    return False


if __name__ == '__main__':
    word1 = 'def'
    word2 = 'defa'
    print('파이썬 버전은? : {version}'.format(version=platform.python_version()))
    print('"{word}"는 파이썬 예약어 인가요? : {check}'.format(word=word1, check=check_kwlist(word1)))
    print('"{word}"는 파이썬 예약어 인가요? : {check}'.format(word=word2, check=check_kwlist(word2)))
