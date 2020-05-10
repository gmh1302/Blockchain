from PIL import Image
import hashlib  # Hash로 변환하기 위한 모듈
import numpy as np
import requests

def hash_change(text): # text에 대한 Hash를 생성하는 함수
    sha = hashlib.sha256() # Hash 값을 생성
    sha.update((text.encode())) # index, timestamp, data, previous_hash를 가지고 새로운 Hash를 생성
    return sha.hexdigest() # Hash를 16진수로 변경 → 이 값은 문자열이다!


def pixel_list(fname, size = 16):
    img = Image.open(fname) # 이미지 열기
    img = img.convert('L')  #그레이스케일 변환
    img = img.resize((size,size),Image.ANTIALIAS)       # 리사이즈하기
    pixel_data = img.getdata()      # 픽셀데이터 가져오기
    pixels = np.array(pixel_data)       # Numpy 배열로 변환하기
    pixels = pixels.reshape((size,size))        # 2차원 배열로 변환하기
    avg = pixels.mean() # 평균 구하기
    diff = 1 * (pixels > avg)   # 평균보다 크면 1, 작으면 0으로 변환하기
    return diff


def np2hash(ahash,text): # 이진수를 16진수 Hash 값으로 변환
    bhash = []
    for nl in ahash.tolist():
        sl = [str(i) for i in nl]
        s2 = "".join(sl)
        i = int(s2, 2)  # 이진수를 정수로 변환
        bhash.append("%04x" % i)
    return hash_change(("".join(bhash) + hash_change(text)))