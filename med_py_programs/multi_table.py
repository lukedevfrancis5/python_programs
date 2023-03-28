# prints multiplication table

def mult_table():
    for x in range(1, 11):
        for y in range(1, 11):
            # adds spaces so that columns are same width    
            print("{:3d}".format(x * y), end=" ")
        print() 
        

mult_table()