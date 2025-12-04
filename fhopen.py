#f = open("/Users/dhruv29/Desktop/XYZ/CASE STUDY(CSF) 1.txt")
#print(f.read())
#print("\n ----------------------------------------------------------\n")
#with open("/Users/dhruv29/Desktop/XYZ/CASE STUDY(CSF) 1.txt") as f:
    #print(f.read())

#f = open("/Users/dhruv29/Desktop/XYZ/CASE STUDY(CSF) 1.txt")
#print(f.readline())
#f.close()

#with open("/Users/dhruv29/Desktop/XYZ/CASE STUDY(CSF) 1.txt") as f:
    #print(f.readline())
    #f.close()

#f = open("/Users/dhruv29/Desktop/XYZ/CASE STUDY(CSF) 1.txt")
#print(f.readlines())
#f.close()

with open("/Users/dhruv29/Desktop/XYZ/CASE STUDY(CSF) 1.txt") as f:
    print(f.readlines(3))
    f.close()

with open("/Users/dhruv29/Desktop/XYZ/CASE STUDY(CSF) 1.txt","w") as f:
    f.write("This is a new line added to the file.\n")

with open("/Users/dhruv29/Desktop/XYZ/CASE STUDY(CSF) 1.txt","a") as f:
    f.write("This line is appended to the file.\n")