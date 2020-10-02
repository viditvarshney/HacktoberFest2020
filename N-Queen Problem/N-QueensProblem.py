def N_Queens(l, m, br, N):
  # checking for column m
  for p in range(1, l):
    if(br[p][m] == 1):
      return True

  # checking upper right diagonal
  p = l-1
  q = m+1
  while (p>=1 and q<=N):
    if (br[p][q] == 1):
      return True
    p=p+1
    q=q+1

  # checking upper left diagonal
  p = l-1
  q = m-1
  while (p>=1 and q>=1):
    if (br[p][q] == 1):
      return True
    p=p-1
    q=q-1

  return False

def Problem_Solution(row, n, N, br):
  if (n==0):
    return True

  for m in range(1, N+1):
    if(not(N_Queens(row, m, br, N))):
      br[row][m] = 1

      if (Problem_Solution(row+1, n-1, N, br)):
        return True

      br[row][m] = 0 #backtracking
  return False

if __name__ == '__main__':
  br = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

  Problem_Solution(1, 4, 4, br)

  #printing the matix
  for i in range(1, 5):
      print(br[i][1:])