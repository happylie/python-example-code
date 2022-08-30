#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import icnsutil

# 1. 이미지 파일을 icons 파일로 변환하기
org_file = './status.png'       # 원본 이미지 파일
icons_file = './AppIcon.icns'   # Apple icons 파일로 변환

imgtoicns = icnsutil.IcnsFile()
try:
    imgtoicns.add_media(file=org_file)
    imgtoicns.write(icons_file)
except Exception as err:
    print(err)
    sys.exit(0)

# 2. icons 파일에서 이미지 파일로 추출하기
org_file = './app.icns'   # 원본 Apple icons 파일로 변환
extract_dir = './'        # 추출 이미지 위치
try:
    img = icnsutil.IcnsFile(org_file)
    img.export(extract_dir, allowed_ext='png', recursive=True, convert_png=True)
except Exception as err:
    print(err)
    sys.exit(0)

# 3. icons 파일 정보 확인하기
# 3.1 description 함수 이용
org_file = './app.icns'         # Chrome Apple icons 파일
org_file1 = './AppIcon.icns'    # 제작한 Apple icons 파일
img_file = './status.png'       # 일반 이미지 파일

try:
    desc1 = icnsutil.IcnsFile.description(org_file)
    desc2 = icnsutil.IcnsFile.description(org_file1)
    desc3 = icnsutil.IcnsFile.description(img_file)
    print('desc1 description : {desc1}'.format(desc1=desc1))
    print('desc2 description : {desc2}'.format(desc2=desc2))
    print('desc3 description : {desc3}'.format(desc3=desc3))
except Exception as err:
    print(err)
    sys.exit(0)

# 3.2 verify 함수 이용
org_file = './app.icns'         # Chrome Apple icons 파일
org_file1 = './AppIcon.icns'    # 제작한 Apple icons 파일
img_file = './status.png'       # 일반 이미지 파일

try:
    desc1 = icnsutil.IcnsFile.verify(org_file)
    desc2 = icnsutil.IcnsFile.verify(org_file1)
    desc3 = icnsutil.IcnsFile.verify(img_file)
    print('desc1 verify : {desc1}'.format(desc1=list(desc1)))
    print('desc2 verify : {desc2}'.format(desc2=list(desc2)))
    print('desc3 verify : {desc3}'.format(desc3=list(desc3)))
except Exception as err:
    print(err)
    sys.exit(0)
