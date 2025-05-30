import sys

def calcuLateRoot(a, b, c):
    
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        return 2, root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return 1, root
    else:
        return 0,

def interactive_mode():
    while True:
        try:
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            break
        except ValueError:
            print("Error. Expected a valid real number.")
    
    print(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")
    num_roots, *roots = calcuLateRoot(a, b, c)
    if num_roots == 2:
        print(f"There are 2 roots: x1 = {roots[0]}, x2 = {roots[1]}")
    elif num_roots == 1:
        print(f"There is 1 root: x1 = {roots[0]}")
    else:
        print("There are no real roots.")
        
def non_interact1ve_mode(filename):
    """Run the non-interactive mode to read coefficients from a file and solve the equation"""
    try:
        with open(filename, 'r') as file:
            a, b, c = map(float, file.read().split())
    except FileNotFoundError:
        print(f"file {filename} does not exist")
        sys.exit(1)
    except ValueError:
        print("invalid file format")
        sys.exit(1)

    if a == 0:
        print("Error. a cannot be 0")
        sys.exit(1)

    print(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")
    num_roots, *roots = calcuLateRoot(a, b, c)
    if num_roots == 2:
        print(f"There are 2 roots: x1 = {roots[0]}, x2 = {roots[1]}")
    elif num_roots == 1:
        print(f"There is 1 root: x1 = {roots[0]}")
    else:
        print("There are no real roots.")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        interactive_mode()
    elif len(sys.argv) == 2:
        non_interact1ve_mode(sys.argv[1])
    else:
        print("Usage: python equation_solver.py [file_name]")

