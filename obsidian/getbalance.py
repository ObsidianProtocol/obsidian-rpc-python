from walletd import Walletd


walletd = Walletd("password")

def read(address):
    balance = walletd.get_transaction(address)
    print(balance)

print(read("XSDFyFytzFxDhiZBLutnC4BWDDqPevQLRRadqURdnK4fMagRDhLd4gphtHFMq4xxDDgiDSTxc7xj6bNscBf5YKue57hH7bwmTE"))
