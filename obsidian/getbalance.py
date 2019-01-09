from walletd import Walletd

rpc_host = '209.97.174.174'
rpc_port = 11898

walletd = Walletd(rpc_host,rpc_port)

def read(address):
    return walletd.get_status()

print(read("XSDFyFytzFxDhiZBLutnC4BWDDqPevQLRRadqURdnK4fMagRDhLd4gphtHFMq4xxDDgiDSTxc7xj6bNscBf5YKue57hH7bwmTE"))
