import hashlib  # Hash로 변환하기 위한 모듈
import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash): # 블록 생성을 위한 초기화 메서드
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self): # Hash를 생성하는 함수
        sha = hashlib.sha256() # Hash 값을 생성
        sha.update((str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode()) # index, timestamp, data, previous_hash를 가지고 새로운 Hash를 생성
        return sha.hexdigest() # Hash를 16진수로 변경 → 이 값은 문자열이다!


def create_first_block(): # 첫 번째 블록을 생성하는 함수
    return Block(0, datetime.datetime.now(), "Genesis Block", "0")


def next_block(last_block): # 다음 블록을 생성하는 함수
    this_index = last_block.index + 1
    this_timestamp = datetime.datetime.now()
    this_data = "Hey!  I'm block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)


############################################################################


blockchain = [create_first_block()]
previous_block = blockchain[0]

num_of_blocks_to_add = int(input("원하는 블록 생성 갯수 : ")) # 생성하고 싶은 블록 갯수

for i in range(0, num_of_blocks_to_add) :
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    
    print(block_to_add.hash) # 인덱스 순서에 따른 블록의 Hash 값 출력
 
# print("Hash Value: {}\n".format(block_to_add.hash)) # 현재 블록(가장 마지막 블록)의 Hash 값 출력
