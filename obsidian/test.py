from obsidian import Obsidiand


#one of the seed nodes
rpc_host = '209.97.174.174'
rpc_port = 57576

#instantiate the TurtleCoind python request class
obsidiand = Obsidiand(rpc_host, rpc_port)


#Call for the response
response = obsidiand.get_block_count()
print(response)
