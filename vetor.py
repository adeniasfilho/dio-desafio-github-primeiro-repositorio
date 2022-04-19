N = [0,0,0,0,0,0,0,0,0,0]
x = int(input())
for i in range(10):
  N[i]=x
  x = x * 2
  print('N[{}] = {} '.format(i,N[i]))