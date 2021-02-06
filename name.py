# Make a full name as input to run unit test on
# By: Kyle Huang

def name(first, last):
    if not isinstance(first, str) or not isinstance(last, str):
        raise TypeError("Does not contain string")
    else:
        return first + " " + last


if __name__=="__main__":
    print(name("Kyle", "Huang"))

