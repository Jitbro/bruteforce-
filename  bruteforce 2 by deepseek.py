import itertools
import hashlib
import time

def crack_password(target_hash, max_length=4, charset=None):
    # Define a small character set for demonstration (lowercase + digits)
    charset = charset or string.ascii_lowercase + string.digits
    attempts = 0

    # Iterate over all possible password lengths up to max_length
    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            guess_hash = hashlib.sha256(guess.encode()).hexdigest()

            # Print progress (optional)
            if attempts % 1000 == 0:
                print(f"Attempts: {attempts}, Testing: {guess}")

            # Check if the hash matches
            if guess_hash == target_hash:
                print(f"\nPassword found: {guess}")
                print(f"Total attempts: {attempts}")
                return guess

    print("\nPassword not found within constraints.")
    return None

# Example usage (for educational purposes only)
if __name__ == "__main__":
    import string

    # Simulate a target password (SHA-256 hash of "abc123")
    target_password = input("")
    target_hash = hashlib.sha256(target_password.encode()).hexdigest()

    # Run the cracker with constraints (max_length=4)
    start_time = time.time()
    crack_password(target_hash, max_length=6, charset=string.ascii_lowercase + string.digits)
    end_time = time.time()

    print(f"Time elapsed: {end_time - start_time:.2f} seconds")