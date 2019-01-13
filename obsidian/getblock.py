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
    return obsidiand.get_block(hash)
print(read("51328444820de47a1a3307104cadffbfddb8cd0b2a95f293cd91b17a53731ab9"))
