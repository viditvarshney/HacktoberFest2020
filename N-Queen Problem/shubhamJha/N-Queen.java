class Main
{ 

static int num = 4; 
static int k = 1; 
static void Solution(int dimension[][]) 
{ 
	System.out.printf("%d:\n", k++); 
	for (int i = 0; i < num; i++) 
	{ 
		for (int j = 0; j < num; j++) 
			System.out.printf(" %d ", dimension[i][j]); 
		System.out.printf("\n"); 
	} 
	System.out.printf("\n"); 
} 
static boolean isSafe(int dimension[][], int r, int c) 
{ 
	int i, j; 
	for (i = 0; i < c; i++) 
		if (dimension[r][i] == 1) 
			return false; 
	for (i = r, j = c; i >= 0 && j >= 0; i--, j--) 
		if (dimension[i][j] == 1) 
			return false; 
	for (i = r, j = c; j >= 0 && i < num; i++, j--) 
		if (dimension[i][j] == 1) 
			return false; 

	return true; 
} 

static boolean solveNQ(int dimension[][], int c) 
{ 
	if (c == num) 
	{ 
		Solution(dimension); 
		return true; 
	} 

	boolean res = false; 
	for (int i = 0; i < num; i++) 
	{ 
		if ( isSafe(dimension, i, c) ) 
		{ 
			dimension[i][c] = 1; 

			res = solveNQ(dimension, c + 1) || res; 

			dimension[i][c] = 0; 
		} 
	} 

	return res; 
} 


static void solve() 
{ 
	int dimension[][] = new int[num][num]; 

	if (solveNQ(dimension, 0) == false) 
	{ 
		System.out.printf("Solution does not exist"); 
		return ; 
	} 

	return ; 
} 

public static void main(String[] args) 
{ 
	solve(); 
} 
}