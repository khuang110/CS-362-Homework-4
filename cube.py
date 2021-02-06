# Calculate volume of a cube to run unit test on
# By: Kyle Huang

def calc_cube(x,y,z):
    return x * y * z

if __name__=="__main__":
    x = input("Enter length")
    y = input("Enter Width")
    z = input("Enter Height")

    print("Volume of cube is: %d"% calc_cube(x,y,z))
