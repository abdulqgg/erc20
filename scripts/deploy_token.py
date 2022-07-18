from scripts.helpful_scripts import get_account
from brownie import OurToken
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")

def deploy_token():
    account = get_account()
    ourToken = OurToken.deploy(
        initial_supply,
        {"from": account}
    )
    print(ourToken.name())


def main():
    deploy_token()