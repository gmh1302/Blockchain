import os, sys
import hashlib

def getHash(path, blocksize=65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


# sys.argv[0]은 입력받은 값 중에서 파이썬 프로그래밍 이름인 md5_hash.py
# sys.argv[1]은 1번째 옵션
# sys.argv[2]는 2번쨰 옵션

file = "Blockchain/md5_hash.py"

print(file)

if os.path.exists(file):
    fileHash = getHash(file)
    print(fileHash)
else:
    print('%s is not a valid path, please verify' % file)
    sys.exit()
