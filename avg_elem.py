# Calcualte the average of elements in a list
# By: Kyle Huang

# Function to calculate the average of elements in a list
def avg_list(l):
    if isinstance(l, list) and len(l) != 0:
        for i in l:
            if isinstance(i, str):
                raise TypeError("Must be integer list")
        return float(sum(l)/len(l))
    else:
        return 0


