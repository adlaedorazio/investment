import hashlib
import time

class Block:
    #Every Block must have:
        #index: (int) what number block it is
        #previous_hash: (string) hash of the block before it
        #timestamp: (float) when it was created
        #data: (any type) payload for the block (could be transactions, etc.)
        #nonce: (int) number used for mining (Proof of Work)
        #hash: (string) the result of hashing all the above together
    
    def __init__(self, index, previous_hash, timestamp, data, nonce = 0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()
        
    def calculate_hash(self):
        #value combines all the important fields into one big long string.
        value = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        #hash the text inside of value (first encode it, then hash using SHA-256, then convert that hash into hex string)
        return hashlib.sha256(value.encode()).hexdigest()
    
class Blockchain:
    #The Blockchain is a LIST of blocks

    def __init__(self, difficulty = 4):
        self.chain = [self.create_genesis_block()]
        #The 'difficulty' is how hard it is to mine (how many leading zeros in the hash)
        self.difficulty = difficulty
        
    def create_genesis_block(self):
        #Create the first block with index 0 and previous hash '0'
        return Block(0, "0", time.time(), "Genesis Block")
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self, new_block):
        #set previous hash to the latest block's hash
        new_block.previous_hash = self.get_latest_block().hash
        #new_block.hash = new_block.calculate_hash() <-- RETRACTED ONCE I ADDED PROOF OF WORK
        new_block.hash = self.proof_of_work(new_block)
        self.chain.append(new_block)
        
    def proof_of_work(self, block):
        block.nonce = 0
        computed_hash = block.calculate_hash()
        #repeatedly try new nonce values until a valid hash is found
        while not computed_hash.startswith('0' * self.difficulty):
            block.nonce += 1
            #recalculate hash if number of zeros was incorrect
            computed_hash = block.calculate_hash()
        return computed_hash
    
    
            