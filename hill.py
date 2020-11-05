import random
def printboard(b):
  for i in b:
    print(' '.join(i))
def randomconfig(n):
  b = []
  s = []
  c =[]
  for i in range(n):
    s.append(random.randint(0, n-1))
    c =[]
    for j in range(n):
      if j==s[i]:
        c.append('Q')
      else:
        c.append('-')
    b.append(c)
  return b, s
def genboard(s, N):
  b=[]
  for i in range(N):
    c=[]  
    for j in range(N):
      if j==s[i]:
        c.append('Q')
      else:
        c.append('-')
    b.append(c)
  return b
def opobj(b, s, n):
  attack = 0
  for i in range(n):
    row = i-1
    col = s[i]
    while row>=0:
      if b[row][col]== 'Q':
        break 
      row -=1
    if row>=0:
      if b[row][col]== 'Q':
        attack+=1
    row =i+1
    col =s[i]
    while row<n:
      if b[row][col]== 'Q':
        break 
      row +=1
    if row <n :
      if b[row][col]== 'Q':
        attack+=1
    col = s[i]-1 
    row = i-1
    while row >=0 and col >=0 :
      if b[row][col]== 'Q':
        break 
      row -=1
      col -=1
    if row >=0 and col >=0:
      if b[row][col]== 'Q':
        attack+=1

    col =s[i]+1
    row = i+1
    while row <n and col <n:
      if b[row][col]== 'Q':
        break 
      row +=1
      col +=1
    if row <n and col <n:
      if b[row][col]== 'Q':
        attack+=1

    col = s[i]-1
    row = i+1
    while col >=0 and row <n :
      if b[row][col]== 'Q':
        break 
      row +=1
      col -=1
    if col >=0 and row <n :
      if b[row][col]== 'Q':
        attack+=1

    col = s[i]+1
    row=i-1
    while col <n and row >=0 :
      if b[row][col]== 'Q':
        break 
      row -=1
      col +=1
    if col <n and row >=0 :
      if b[row][col]== 'Q':
        attack+=1
  return int(attack/2)
def getneigh(s, n):
  opb = []
  ops =[]
  ops = s
  opb = genboard(ops,n)
  opob = opobj(opb,ops,n)
  nei =[]
  neistate = s
  nei = genboard(neistate, N)
  for i in range(N):
    for j in range(N):
      if j != s[i]:
        neistate[i]=j
        nei[i][j]='Q'
        nei[i][s[i]]='-'
        temp = opobj(nei, neistate, n)
        if temp<=opob:
          opob = temp
          ops = neistate
          opb = genboard(ops, n)
        nei[i][neistate[i]]='-'
        neistate[i] = s[i]
        nei[i][s[i]]='Q'
  return ops, opb   
def hillclimbing(board, state,N):
  nei =[]
  neistate = state
  nei = genboard(neistate, N)
  while True:
    state = neistate
    board = genboard(state, N)
    neistate, nei = getneigh(neistate,N)
    
    if  neistate == state:
      printboard(board)
      break
    elif opobj(board, state, N)==opobj(nei, neistate, N):
      neistate[random.randint(0, N-1)] = random.randint(0,N-1)
      nei = genboard(neistate, N)
  
N = int(input("Enter the size of board"))
board = []
state = []
board, state = randomconfig(N)
hillclimbing(board, state,N)

