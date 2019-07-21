class Node1:
  def __init__(self,Ai):
    self.value=Ai
    self.right=None
    self.left=None

def insert(root,Ai):
  if root is None:
    root=Node1(data)
  elif root.value > Ai:
    if root.left is None:
      root.left=Node1(Ai)
    else:
      insert(root.left,Ai)
  elif root.value < Ai:
    if root.right is None:
      root.right=Node1(Ai)
    else:
      insert(root.right,Ai)

def LCA(root,L_val,R_val):
  if root is None:
    return None
  elif L_val > root.value and R_val > root.value:
    return(LCA(root.right,L_val,R_val))
  elif L_val < root.value and R_val < root.value:
    return (LCA(root.left,L_val,R_val))
  else:
    return root.value

num=int(input())
val=list(map(eval,input().split()))
u,v=map(eval,input().split())
R=Node1(val[0])
for i in range(1,num):
  insert(R,val[i])
print(LCA(R,u,v))
