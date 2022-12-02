import requests
from web3 import Web3

# Set the target price and the amount of Ethereum to buy
target_price = 500
eth_to_buy = 100

# Set the private key of the Ethereum account to use for buying
private_key = "YOUR_PRIVATE_KEY_HERE"

# Import the Ethereum account using the private key
def import_account(pk):
    # Create a new Web3 instance
    w3 = Web3()

    # Import the Ethereum account using the private key
    account = w3.eth.account.privateKeyToAccount(pk)

    # Return the imported account
    return account

# Check the current price of Ethereum on Optimism
current_price = requests.get("https://optimism.com/ethereum/price").json()["price"]

# If the current price is equal to or greater than the target price, buy Ethereum
if current_price >= target_price:
    # Import the Ethereum account using the private key
    account = import_account(private_key)

    # Place the buy order for Ethereum with USDC
    buy_order = requests.post("https://optimism.com/ethereum/buy", data={"usdc": eth_to_buy * current_price, "from": account.address})

    # Print a success message if the order was placed successfully
    if buy_order.status_code == 200:
        print(f"Successfully bought {eth_to_buy} ETH for {current_price * eth_to_buy} USDC using account {account.address}!")
    else:
        print("Failed to place buy order. Check your API key and try again.")
else:
    print(f"Current price is {current_price}. Target price not reached.")
