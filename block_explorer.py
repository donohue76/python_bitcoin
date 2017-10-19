# import blockchain library
from blockchain import blockexplorer

# get a particular block
block = blockexplorer.get_block("00000000000000000010639dfd78a2e9eea1bb4c6ef0f079c1e715101165d07b")

print(block.fee)
print(block.size)
print(block.transactions)