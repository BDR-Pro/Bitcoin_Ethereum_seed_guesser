import itertools
from web3 import Web3
from eth_account import Account
Account.enable_unaudited_hdwallet_features()
Infura_Project_ID = "https://mainnet.infura.io/v3/b677748c1ffc433297bd45713df59aa9"

# Replace these with your 12 seed words
seed_words = ["Day", "follow", "hill", "cattle", "planet", "few", "boil", "alert", "cover", "satisfy", "faith"]

# Function to check if a seed phrase is valid (you'll need to implement this)
def is_valid_seed(seed_phrase):
    # Replace this with your validation logic
    # Return True if the seed phrase is valid, otherwise return False

    # Replace this with your actual mnemonic (12 or 24 words)
    mnemonic = seed_phrase.lower()
    
    # Initialize a Web3 connection to the Ethereum mainnet
    w3 = Web3(Web3.HTTPProvider(Infura_Project_ID))
    # Derive the Ethereum address from the mnemonic
    try:

        account = Account.from_mnemonic(mnemonic)
        # Derive the Ethereum private key from the mnemonic
        private_key = Account.from_mnemonic(mnemonic).privateKey.hex()
        # Convert the private key into an Ethereum account
        account = Account.privateKeyToAccount(private_key)
        # Derive the Ethereum address from the account
        address = account.address
        # Check the balance of the address
        balance_wei = w3.eth.get_balance(address)
        balance_eth = w3.fromWei(balance_wei, 'ether')
        # Print the results
        print(f'Mnemonic: {mnemonic}')
        print(f'Private Key: {private_key}')
        print(f'Address: {address}')
        print(f'Balance (ETH): {balance_eth}')
        return balance_eth > 0
    except ValueError:
            print("Invalid seed phrase")
            return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False
    
# Generate permutations of the seed words
permutations = itertools.permutations(seed_words)
counter = 0
for perm in permutations:
    seed_attempt = " ".join(perm)
    print(seed_attempt)
    counter += 1
    print(counter)
    if is_valid_seed(seed_attempt):
        print("Found a valid seed phrase:", seed_attempt)
        break

print(counter)