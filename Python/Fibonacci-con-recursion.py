result = 0
last = 0
then = 1
k = 0
def fibo(last,then,k):
    if (k == 10):
        return
    result = last + then
    last = then
    then = result
    k+=1
    print(result)
    fibo(last,then,k)

fibo(0,1, k)
