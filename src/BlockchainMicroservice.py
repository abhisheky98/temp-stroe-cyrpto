from web3 import Web3
from web3 import Web3, EthereumTesterProvider
from eth_tester import EthereumTester
w3 = Web3(EthereumTesterProvider())
w3.is_connected()


class BlockchainMicroservice:
    def __init__(self, node_url, contract_address, contract_abi):
        self.web3 = Web3(Web3.HTTPProvider(node_url))
        self.contract = self.web3.eth.contract(address=contract_address, abi=contract_abi)

    def transfer_usdt(self, sender, receiver, amount):
        # Send USDT transaction using Web3.py
        tx_hash = self.contract.functions.transfer(receiver, amount).transact({'from': sender})
        return tx_hash
