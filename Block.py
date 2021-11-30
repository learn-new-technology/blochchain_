import hashlib
import json
from datetime import datetime

class Block:
    def __init__(self, previous_block_hash, data):
        self.previous_block_hash = previous_block_hash  # previous block hash
        self.data = data        # data request
        self.mine_var = 0
        self.time = datetime.now()
        self.block_hash = self.hash_block() # hash block
        # self.block_data = self._data()  # show data with data format

    def hash_block(self):
        return hashlib.sha256((
            self.previous_block_hash + str(self.time) + json.dumps(self.data) + str(self.mine_var)
        ).encode()).hexdigest()

    # def _data(self):
    #     return f"previous_block_hash: {self.previous_block_hash} --- data: {self.data} --- block_hash: {self.block_hash} --- {self.time}"

    def mine(self, difficulty):
        assert difficulty >= 1
        prefix = '0' * difficulty
        while not self.block_hash.startswith(prefix):
            self.block_hash = self.hash_block()
            self.mine_var += 1
        print("++++++++++++++++++++++++++++")
        print ("after " + str(self.mine_var) + " iterations found nonce: "+ self.block_hash)
        return self.block_hash
