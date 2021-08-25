
# Bruteforce wrong approach
def fib(n):
	if n == 0 or n == 1 :
		return n
	else:
		return fib(n-1) + fib(n-2)


print(fib(0),fib(1),fib(2),fib(3),fib(4),fib(5),fib(6),fib(7),fib(8),fib(9),fib(10),fib(11))


# why this is wrong ? 
# because it will on calculating the same thing again and again and no caching 
# What is its time complexity ? 
# > exponential 2^n

def fib2(n,cache):
	if n == 0 or n == 1:
		return n
	
	if n in cache:
		return cache[n]
	
	ret =  fib2(n-1,cache) + fib2(n-2,cache)
	cache[n] =  ret
	return ret

cache = {}
print(fib2(0,cache),fib2(1,cache),fib2(2,cache),fib2(3,cache),fib2(4,cache),fib2(5,cache),fib2(6,cache),fib2(7,cache),fib2(8,cache),fib2(9,cache),fib2(10,cache),fib2(11,cache))




