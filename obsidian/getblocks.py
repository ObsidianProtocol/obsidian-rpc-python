from obsidian import Obsidiand
import json

#one of the seed nodes
rpc_host = '209.97.174.174'
rpc_port = 11898

#instantiate the TurtleCoind python request class

obsidiand = Obsidiand(rpc_host, rpc_port)

#Call for the response
#possible commands:
#look at obsidiand.py
def read():
    latestHeight = obsidiand.get_height()["height"] -1
    return obsidiand.get_blocks(latestHeight)
