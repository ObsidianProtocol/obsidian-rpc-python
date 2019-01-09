from walletd import Walletd

rpc_host = '209.97.174.174'
rpc_port = 11898

walletd = Walletd(rpc_host,rpc_port)

def read():
    response = walletd.get_status()
    print(response)
print(read())
