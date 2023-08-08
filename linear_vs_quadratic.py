def linear_function(n):
    """Represents the function: f(n) = 100n"""
    return 100 * n

def quadratic_function(n):
    """Represents the function: f(n) = n²"""
    return n ** 2

# Sample values
sample_values = [10, 25, 50, 75, 100, 150, 200, 300]

print("For given sample values of n:")
print("n\t100n\t\tn^2")
print("-------------------------")
for n in sample_values:
    print(f"{n}\t{linear_function(n)}\t\t{quadratic_function(n)}")
