import itertools
from bitcoinlib.wallets import Wallet
from bitcoinlib.mnemonic import Mnemonic
import hashlib
import random
import string


# Replace these with your 12 seed words
seed_words = ["Day", "follow", "hill", "cattle", "planet", "few", "boil", "alert", "cover", "satisfy", "faith"]



def generate_random_string(length):
    # Define the characters you want to include in the random string
    characters = string.ascii_letters + string.digits  # You can add more characters if needed

    # Use random.choices() to generate a random string
    random_string = ''.join(random.choices(characters, k=length))

    return random_string


# Function to check if a seed phrase is valid (you'll need to implement this)
def is_valid_seed(seed_phrase):
    # Replace this with your validation logic
    # Return True if the seed phrase is valid, otherwise return False
    # Replace this with your actual mnemonic (12 or 24 words)
    mnemonic = seed_phrase.lower()
    if len(mnemonic) != 32:
        mnemonic = hashlib.sha256(mnemonic.encode()).digest()

    # Derive the Bitcoin addresses from the mnemonic

    m = Mnemonic('english') # Default language is 'english'
    w = Wallet.create(generate_random_string(9), keys=mnemonic, network='bitcoin') 
    key = w.get_key()
    address = key.address
    balance = w.balance()
    print(f'Mnemonic: {seed_phrase}')
    print(f'Bitcoin Address: {address}')
    print(f'Balance (BTC): {balance}')
    
    return balance>0 # You may want to check the balance here, similar to Ethereum




# Generate permutations of the seed words
permutations = itertools.permutations(seed_words)
permutations = list(permutations)
counter = 0
for perm in reversed(permutations):
    seed_attempt = " ".join(perm)
    counter += 1
    if is_valid_seed(seed_attempt):
        print("Found a valid seed phrase:", seed_attempt)
        break
    print(counter)

print("Done!")