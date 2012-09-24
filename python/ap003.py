# Shamefully copied off some google search...

def highest_prime_factor(n):
   if n == 2:
      return 2
   if not n % 2:
      return highest_prime_factor(n/2)
   for x in xrange(3,int(n ** 0.5 + 1),2):
      if not n % x:
         return highest_prime_factor(n/x)
   return n

print(highest_prime_factor(600851475143))