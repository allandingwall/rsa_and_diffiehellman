import rsa_functions as rsa

# Set bit length of primes (default is 1024 bits)
prime_bit_length = pow(2,10)

# Finding primes (p & q)
p = rsa.find_prime(prime_bit_length)
print(f'p = {p}')
q = rsa.find_prime(prime_bit_length)
print(f'q = {q}')

# Calculating n and 𝜑(n)
n = p * q
t = n - (p + q) + 1
print(f'totient(n) = {t}')

# Choosing e (default 65537)
e = 65537
print(f'e = {e}')
print(f"PUBLIC KEY = (N - {hex(n)} // E - {hex(e)})")

# Calculating private key d
d = rsa.mod_inverse(e,t)
print(f'PRIVATE KEY = (D - {hex(d)})')

message = 10
c = pow(message,e, n) 
decrypted_message = pow(c,d,n)
print(message == decrypted_message)

