import secrets
import random
 
def find_prime(n_bits):
    primes = open('primes.txt','r')
    for line in primes:
        first_1000_primes = line.split(',')
        first_1000_primes = [i.replace(' ','') for i in first_1000_primes] 
        first_1000_primes = [int(i) for i in first_1000_primes]

    def sieve(n):
        while True:
            prime_candidate = secrets.randbits(n)
            if prime_candidate < 2 ** (n-1):
                continue

            for prime in first_1000_primes:
                if prime_candidate % prime == 0:
                    break
            return prime_candidate

    def MillerRabin(mrc):
        maxDivisionsByTwo = 0
        ec = mrc-1
        while ec % 2 == 0:
            ec >>= 1
            maxDivisionsByTwo += 1
        assert(2**maxDivisionsByTwo * ec == mrc-1)

        def trialComposite(round_tester):
            if pow(round_tester, ec, mrc) == 1:
                return False
            for i in range(maxDivisionsByTwo):
                if pow(round_tester, 2**i * ec, mrc) == mrc-1:
                    return False
            return True

        num_trials = 50
        for i in range(num_trials):
            round_tester = random.randrange(2, mrc)
            if trialComposite(round_tester):
                return False
        return True

    while True:
        p = (sieve(n_bits))
        if MillerRabin(p):
            break
    return p

def mod_inverse(x,y):
	def eea(a, b):
		if b == 0: return (1,0)
		(q,r) = (a//b,a%b)
		(s,t) = eea(b,r)
		return (t, s-(q*t) )

	inv = eea(x,y)[0]
	if inv < 1: inv += y
	return inv
