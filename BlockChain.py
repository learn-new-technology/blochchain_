from Block import Block

class BlockChain:
    def __init__(self, difficulty):
        genesis_block = Block('0000', {'is_genesis': True})
        self.chain = [genesis_block]
        self.difficulty = difficulty
    
    def get_last_block(self):
        return self.chain[len(self.chain) - 1]

    def add_block(self, data):
        last_block = self.get_last_block()
        new_block = Block(last_block.block_hash, data)
        new_block.mine(self.difficulty)
        # print(f"New block: {new_block.previous_block_hash} --- data: {new_block.data} --- block_hash: {new_block.block_hash} --- {new_block.time}")
        self.chain.append(new_block)
    
    def is_valid(self):
        for item in range(1, len(self.chain)):
            current_chain = self.chain[item]
            prev_block = self.chain[item - 1]
            # block_hash_before_mine = current_chain.mine(self.difficulty)
            # if current_chain.block_hash != block_hash_before_mine:
            #     return False
            if current_chain.previous_block_hash != prev_block.block_hash:
                return False
        return True
