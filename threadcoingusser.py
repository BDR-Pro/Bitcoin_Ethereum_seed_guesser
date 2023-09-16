import itertools
from bitcoinlib.wallets import Wallet
from bitcoinlib.mnemonic import Mnemonic
import hashlib
import random
import string
import multiprocessing

# Replace these with your 12 seed words
seed_words = ["follow", "hill", "planet", "few", "boil", "alert", "cover", "faith"]

def randomword(length=9):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# Function to check if a seed phrase is valid (you'll need to implement this)
def is_valid_seed(seed_phrase):
    # Replace this with your validation logic
    # Return True if the seed phrase is valid, otherwise return False
    # Replace this with your actual mnemonic (12 or 24 words)
    mnemonic = seed_phrase.lower()
    if len(mnemonic) != 32:
        mnemonic = hashlib.sha256(mnemonic.encode()).digest()

    # Create the wallet once
    m = Mnemonic('english')  # Default language is 'english'
    w = Wallet.create(randomword(), keys=mnemonic, network='bitcoin')
    key = w.get_key()
    address = key.address
    balance = w.balance()
    print(f'Mnemonic: {seed_phrase}')
    print(f'Bitcoin Address: {address}')
    print(f'Balance (BTC): {balance}')

    return balance > 0  # You may want to check the balance here, similar to Ethereum

def check_permutations(perms, solution, start, end):
    for i, perm in enumerate(perms[start:end]):
        seed_attempt = " ".join(perm)
        seed_attempt = solution + seed_attempt
        if is_valid_seed(seed_attempt):
            print("Found a valid seed phrase:", seed_attempt)
            return i + start  # Return the index of the valid seed
    return -1  # Indicate that no valid seed was found in this range

if __name__ == '__main__':
    solution = "Day cattle satisfy hotel "
    permutations = itertools.permutations(seed_words)
    permutations = list(permutations)
    num_processes = multiprocessing.cpu_count()  # Number of CPU cores
    chunk_size = len(permutations) // num_processes

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.starmap(check_permutations, [(permutations, solution, i * chunk_size, (i + 1) * chunk_size) for i in range(num_processes)])

    # Check the results to see if any valid seed was found
    for result in results:
        if result != -1:
            print(f"Valid seed found at index {result}")
            break

    print("Done!")
