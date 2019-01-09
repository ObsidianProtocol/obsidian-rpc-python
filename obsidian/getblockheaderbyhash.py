from obsidian import Obsidiand


#one of the seed nodes
rpc_host = '209.97.174.174'
rpc_port = 11898

#instantiate the TurtleCoind python request class

obsidiand = Obsidiand(rpc_host, rpc_port)

#Call for the response
#possible commands:
#look at obsidiand.py
def read(hash):
    print("The hash is " + str(hash))
    return obsidiand.get_block_header_by_hash(hash)
