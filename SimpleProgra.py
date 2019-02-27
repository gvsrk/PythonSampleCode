def isPrime(n):
    if n<=1:
        return False
    for temp in range(2,n):
        if n % temp == 0:
            return False
        else: 
            return True
    print('Im in isPrime')
# commented 
  
n=5

if isPrime(n):
    print(f'{n} is prime')
else:
    print(f'{n} is not prime')
    
def printnos():
    for i in range(1,10):
        print(i,'   ','--')
        
printnos()