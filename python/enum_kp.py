import sys

from knapsack import knapsack

class enum_knapsack(knapsack):
    def __init__(self, filename):
        knapsack.__init__(self, filename)
        
    def enumerate(self):
        # Do an exhaustive search (aka enumeration) of all possible ways to pack
        # the knapsack.
        # This is achived by creating every "binary" solution vectore of length Nitems.
        # For each solution vector, its value and weight is calculated
        
        solution = [False]*(self.Nitems + 1) # (binary/ true/false) solution vectore representing items pack
        best_solution = [False]*(self.Nitems + 1) # (binary) solution veectore for best solution found
        j = 0
        percentage = 0.0
        total_sol = 2 ** self.Nitems
        ten = 0 # 10 percentage mark
        i = 0 #total solution count

        self.QUIET = True
        best_value = 0 # total value packed in the best solution
        while (not self.next_binary(solution, self.Nitems)):
            
            i += 1
            if (i > ten):
                sys.stdout.write('\r')
                sys.stdout.write("[%-10s] %d%%" % ('#' * j, round(percentage * 100)))
                sys.stdout.flush()
                j += 1
                percentage += 0.1
                ten = total_sol * percentage

            # calculates the value and weight and feasibility
            infeasible = self.check_evaluate_and_print_sol(solution)
            #PRINT OUT BEST SOLUTION

            if (infeasible == False):
                if (self.total_value >= best_value):
                    
                    best_value = self.total_value
                    best_solution = solution.copy()
        sys.stdout.write('\r')
        sys.stdout.write("[%-10s] %d%%" % ('#' * 11, round(percentage * 100)))
        sys.stdout.flush()
        print()
        
        print(best_solution)
        print(best_value)
        self.QUIET = False
        self.check_evaluate_and_print_sol(best_solution)

    def next_binary(self, sol, Nitems):
        # Called with a "binary" vector of length Nitmes, this
        # method "adds 1" to the vector, e.g. 0001 would turn to 0010.
        # If the string overflows, then the function returs True, else it returns False
        i = Nitems
        while (i > 0):
            if (sol[i]):
                sol[i] = False
                i = i -1
            else:
                sol[i] = True
                break
        if (i == 0):
            return True
        else:
            return False
        
            


knapsk = enum_knapsack(sys.argv[1])
knapsk.print_instance()
knapsk.enumerate()

