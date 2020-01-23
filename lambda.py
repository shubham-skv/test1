'''def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst
d=[i*j for i in range(10) for j in range(10)]
print(d)
'''
lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = [i+j+k+f for i in lowercase for j in lowercase for k in digits for f in digits]
print(answer[1:100])
