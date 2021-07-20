def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
      
############

def fastfib(n, memo={}):
    """Assumes n is an int, memo used only by rescursive calls"""
    if n==1 or n==0:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastfib(n-2, memo) + fastfib(n-1, memo)
        memo[n] = result
        return result
 
for i in range(20):
    print('fib('+ str(i) +')=', fib(i))
print('=========')
for i in range(20):
    print(fastfib(i))
