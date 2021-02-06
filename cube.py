# Calculate volume of a cube to run unit test on
# By: Kyle Huang

# Function to calculate volume of cube
def calc_cube(x):
    try:
        x = float(x)
        return abs(x * x * x)
    except ValueError:
        return "Undefined, Value Error"
    except TypeError:
        return "Undefined, Type Error"


if __name__=="__main__":
    x = input("Enter side length: ")
    print("Volume of cube is: ", calc_cube(x))
