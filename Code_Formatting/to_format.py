

class MyClass:

    @staticmethod
    def display_info(name: str, age: int , description: str = None) -> str:
        return f"Name: {name} + Age: {age} + Description: {description}"

def add_numbers(num1: int,
                num2: int) -> int:
    return num1 + num2;

text = "This is some text."

letters = (
    "aplha",
    "beta",
    "gamma",
    "delta"
)

greek_alphabet = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota", "kappa", "lambda", "mu", "nu", "xi", "omicron", "pi", "rho", "sigma", "tau", "upsilon", "phi", "chi", "psi", "omega"]


import sys
sys.stdout.write("This is printed, but it might be buffered\n")
sys.stdout.flush()


if __name__ == "__main__":
    print(MyClass.display_info('ABCD', 100))
    print(add_numbers(304,
                500)) # no newline at EOF