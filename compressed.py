# Minified version of the main.py code.
# Readable version of this code is at the main.py code.
a=False
Z=ValueError
L=list
R='red'
Q=int
J='yellow'
G=True
D='bold'
C=print
A=range
import numpy as H
from termcolor import colored as B
def U(board,col):return board[0][col]==0
def O(board,col):
	for B in A(5,-1,-1):
		if board[B][col]==0:return B
def P(board,row,col,piece):board[row][col]=piece
def I(board,piece):
	E=piece;D=board
	for B in A(4):
		for C in A(6):
			if D[C][B]==E and D[C][B+1]==E and D[C][B+2]==E and D[C][B+3]==E:return G
	for B in A(7):
		for C in A(3):
			if D[C][B]==E and D[C+1][B]==E and D[C+2][B]==E and D[C+3][B]==E:return G
	for B in A(4):
		for C in A(3):
			if D[C][B]==E and D[C+1][B+1]==E and D[C+2][B+2]==E and D[C+3][B+3]==E:return G
	for B in A(4):
		for C in A(3,6):
			if D[C][B]==E and D[C-1][B+1]==E and D[C-2][B+2]==E and D[C-3][B+3]==E:return G
def K(window,piece):
	C=piece;A=window;B=0;D=1
	if C==1:D=2
	if A.count(C)==4:B+=100
	elif A.count(C)==3 and A.count(0)==1:B+=5
	elif A.count(C)==2 and A.count(0)==2:B+=2
	if A.count(D)==3 and A.count(0)==1:B-=4
	return B
def T(board,piece):
	G=piece;F=board;E=0;H=[Q(A)for A in L(F[:,3])];I=H.count(G);E+=I*3
	for B in A(6):
		J=[Q(A)for A in L(F[B,:])]
		for C in A(4):D=J[C:C+4];E+=K(D,G)
	for C in A(7):
		M=[Q(A)for A in L(F[:,C])]
		for B in A(3):D=M[B:B+4];E+=K(D,G)
	for B in A(3):
		for C in A(4):D=[F[B+A][C+A]for A in A(4)];E+=K(D,G)
	for B in A(3):
		for C in A(4):D=[F[B+3-A][C+A]for A in A(4)];E+=K(D,G)
	return E
def Y(board):A=board;return I(A,1)or I(A,2)or len(S(A))==0
def V(board,depth,alpha,beta,maximizingPlayer):
	N=depth;M=None;E=beta;D=alpha;A=board;L=S(A);R=Y(A)
	if N==0 or R:
		if R:
			if I(A,2):return M,0x5af3107a4000
			elif I(A,1):return M,-0x9184e72a000
			else:return M,0
		else:return M,T(A,2)
	if maximizingPlayer:
		B=-H.Inf;F=H.random.choice(L)
		for C in L:
			Q=O(A,C);J=A.copy();P(J,Q,C,2);K=V(J,N-1,D,E,a)[1]
			if K>B:B=K;F=C
			D=max(D,B)
			if D>=E:break
		return F,B
	else:
		B=H.Inf;F=H.random.choice(L)
		for C in L:
			Q=O(A,C);J=A.copy();P(J,Q,C,1);K=V(J,N-1,D,E,G)[1]
			if K<B:B=K;F=C
			E=min(E,B)
			if D>=E:break
		return F,B
def S(board):
	B=[]
	for C in A(7):
		if U(board,C):B.append(C)
	return B
def W(board):
	F=board;E=' '
	for G in A(6):
		for H in A(7):
			if F[G][H]==0:C(B('□','blue'),end=E)
			elif F[G][H]==1:C(B('■',R),end=E)
			else:C(B('■',J),end=E)
		C()
	C(B('0 1 2 3 4 5 6',J,attrs=[D]))
def E():
	b='Player 1';T='=';N='white';M='green';L='[Info]';F='\n';A=H.zeros((6,7));S=a;X=0;W(A)
	while not S:
		if X==0:
			try:
				E=Q(input(F+B(b,R,attrs=[D])+' make your selection (0-6): '));C(F)
				if E<0 or E>6:raise Z('Invalid column!')
				if U(A,E):
					K=O(A,E);P(A,K,E,1);W(A);C(F+T*50);C(B(L,M,attrs=[D]),B(f": {B(b,R,attrs=[D])} placed a piece in column {E}, row {chr(5-K+ord('A'))}.",N,attrs=[D]));C(T*50+F)
					if I(A,1):C(F+B(L,M,attrs=[D]),B(': Player 1 (You) wins!',N,attrs=[D]));S=G;break
					X=1
				else:C(F+B('[Warning]',J,attrs=[D]),B(': Column is full! Choose another column.',N,attrs=[D]))
			except Z as c:C(F+B('[Error]',R,attrs=[D]),B(':',N,attrs=[D]),c)
		else:
			E,d=V(A,5,-H.Inf,H.Inf,G)
			if U(A,E):
				K=O(A,E);P(A,K,E,2);W(A);C(F+T*50);C(B(L,M,attrs=[D]),f": {B('Player 2',J,attrs=[D])} placed a piece in column {E}, row {chr(5-K+ord('A'))}.");C(T*50)
				if I(A,2):C(F+B(L,M,attrs=[D]),f": {B('Player 2 (AI)',J,attrs=[D])} wins!");S=G;break
				X=0
			if Y(A):C(F+B(L,M,attrs=[D]),B(": It's a tie!",N,attrs=[D]));S=G
E()
