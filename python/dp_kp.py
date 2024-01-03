import sys

from knapsack import knapsack

class dp(knapsack):
    def __init__(self, filename):
        knapsack.__init__(self, filename)
        
    def DP(self, solution):
        # Renaming things to keep track of them wrt. names used in algorithm
        v = self.item_values;
        wv = self.item_weights;
        n = self.Nitems
        W = self.Capacity
        
        # the dynamic programming function for the knapsack problem
        # the code was adapted from p17 of http://www.es.ele.tue.nl/education/5MC10/solutions/knapsack.pdf

        # v array holds the values / profits / benefits of the items
        # wv array holds the sizes / weights of the items
        # n is the total number of items
        # W is the constraint (the weight capacity of the knapsack)
        # solution: True in position n means pack item number n+1. False means do not pack it.
        
        # V and Keep should be 2d arrays for use in the dynamic programming solution
        # The are both of size (n + 1)*(W + 1)
        
        # Initialise V and keep
        # ADD CODE HERE
        y = n + 1
        x = W + 1
        V = [[None for i in range(x)] for j in range(y)]
        keep = [[None for i in range(x)] for j in range(y)] #keeping track of the items
        # Set the values of the zeroth row of the partial solutions table to False
        # ADD CODE HERE
        
        for w in range(0,W+1):
            V[0][w] = 0
        for i in range(0,y):
            V[i][0] = 0

        # main dynamic programming loops, adding on item at a time and looping through weights from 0 to W
        # ADD CODE HERE
        for i in range(1,y): #loop of item
            for w in range(1,x): #loop of weight
                wi = wv[i]
                if(wi <= w) and (v[i] + V[i - 1][w - wi] > V[i - 1][w]): #max solution 
                    V[i][w] = v[i] + V[i - 1][w - wi]
                    keep[i][w] = 1
                else:
                    V[i][w] = V[i - 1][w]
                    keep[i][w] = 0
        


        # now discover which iterms were in the optimal solution
        # ADD CODE HERE
        K = W
        for i in range(n,0,-1):
            if (keep[i][K] == 1):
                solution[i] = True
                K = K - wv[i]


    #    for i in V:
    #        for r in i:
    #            print(r, end = " ") 
    #        print()
        print(V[n][W]) 
        return V[n][W]
        
knapsk = dp(sys.argv[1])
solution = [False]*(knapsk.Nitems + 1)
knapsk.DP(solution);
knapsk.check_evaluate_and_print_sol(solution)
