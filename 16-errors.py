try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")

# how to throw an error
if x < 0:
    raise Exception("Sorry, no numbers below zero")
# raise TypeError("Only integers are allowed")
