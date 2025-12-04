try:
    f = open("demofile.txt","w")
    try:
        f.write("I am MacOS")
    except:
        print("Something went wrong when writing to the code")
    finally:
        f.close()
except:
        print("Something when wrong when opening the file")

        