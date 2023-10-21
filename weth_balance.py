from web3 import Web3
import os

endpoints = {'ethereum': os.environ.get('ETHEREUM_RPC')}

contract_address = {'ethereum': '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'}

contract_abi =[
    {
        "inputs":[{"internalType":"address","name":"account","type":"address"}],
        "name":"balanceOf",
        "outputs":[{"internalType":"uint256","name":"","type":"uint256"}],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "constant": True,
        "inputs": [{"name": "","type": "address"},{"name": "","type": "address"}],
        "name": "allowance",
        "outputs": [{"name": "","type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

def getWETHbalance(address, address_allowance='0xb8e4526e0da700e9ef1f879af713d691f81507d8'):

    weth_balance = {}

    for key, value in contract_address.items():
        web3 = Web3(Web3.HTTPProvider(endpoints[key]))
        address = web3.to_checksum_address(address)
        address_allowance = web3.to_checksum_address(address_allowance)

        contract = web3.eth.contract(web3.to_checksum_address(
            value), abi=contract_abi)

        try:
            balance_in_wei = contract.functions.balanceOf(address).call()
            balance_in_eth = balance_in_wei / 1E18
        except:
            balance_in_eth = 0.15

        try:
            balance_allowed_in_wei = contract.functions.allowance(address,address_allowance).call()
            balance_allowed_in_eth = web3.from_wei(balance_allowed_in_wei, 'ether')
        except:
            balance_allowed_in_eth = 0

        
        weth_balance[key] = balance_in_eth
        weth_balance['allowed_balance'] = balance_allowed_in_eth

    return weth_balance
