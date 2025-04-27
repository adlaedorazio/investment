from blockchain import Blockchain, Block
import time

def main():

    #Initialize Blockchain
    blockchain = Blockchain()
    
    #Add blocks to the Blockchain
    blockchain.add_block(Block(
        index=1,
        timestamp=time.time(),
        data="First block after Genesis",
        previous_hash=blockchain.chain[-1].hash
    ))
    blockchain.add_block(Block(
        index=2,
        timestamp=time.time(),
        data="Second block after Genesis",
        previous_hash=blockchain.chain[-1].hash
    ))

    #Print out the Blockchain
    for idx, block in enumerate(blockchain.chain):
        print(f"Block {idx}:")
        print(f"Hash: {block.hash}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Data: {block.data}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Nonce: {block.nonce}")
        print("-" * 30)

if __name__ == "__main__":
    main()
