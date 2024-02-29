import concurrent.futures
from runmain import Runmain
from con_reject import Con_rejecter
def function1():
    Con_rejecter()
    # Your code for function 1 here
    print("Function 1 executed")

def function2():
    Runmain()
    # Your code for function 2 here
    print("Function 2 executed")

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit both functions for execution
        future1 = executor.submit(function1)
        future2 = executor.submit(function2)

        # Wait for both functions to complete
        concurrent.futures.wait([future1, future2])
