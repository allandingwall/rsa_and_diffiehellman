import rsa_functions as rsa
import secrets

# Set bit length of primes (default is 1024 bits)
prime_bit_length = pow(2,10)

# Generating prime number for p
print(f"Generating {prime_bit_length} bit prime for p:")
p = rsa.find_prime(prime_bit_length)
print(f"p = {p}\n")
# Generating random number for g
print(f"Generating {prime_bit_length} bit random number for g: ")
g = secrets.randbits(prime_bit_length)
print(f"g = {g}\n\n")

# Generating Alice's private key (prime)
print(f"Generating Alice's private key - {prime_bit_length} bit prime number:")
alice_private = rsa.find_prime(prime_bit_length)
print(f"Alice private = {alice_private}\n")
# Generating Alice's public key =  g^(Alice's Private Key) mod p
print(f"Generating Alice's public key - g^(Alice's Private Key) mod p")
alice_public = pow(g, alice_private, p)
print(f"Alice public = {alice_public}\n\n")

# Generating Bob's private key (prime)
print(f"Generating Bob's private key - {prime_bit_length} bit prime number:")
bob_private = rsa.find_prime(prime_bit_length)
print(f"Bob private = {bob_private}\n")
# Generating Bob's public key =  g^(Bob's Private Key) mod p
print(f"Generating Bob's public key - g^(Bob's Private Key) mod p")
bob_public = pow(g, bob_private, p)
print(f"Bob public = {bob_public}\n\n")

# Generating shared keys
print("Generating Alice's shared key - (Bob's Public Key)^(Alice's Private Key) mod p")
alice_common_key = pow(bob_public, alice_private, p)
print(f"Alice shared key = {alice_common_key}\n")
print("Generating Bob's shared key - (Alice's Public Key)^(Bob's Private Key) mod p")
bob_common_key = pow(alice_public, bob_private, p)
print(f"Bob shared key = {bob_common_key}\n")

# Checking that Alice's shared key == Bob's shared key
print("Check if shared keys are equivalent:")
print(alice_common_key == bob_common_key)

