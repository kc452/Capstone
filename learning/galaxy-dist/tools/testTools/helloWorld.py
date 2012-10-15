from sys import argv

outName = argv[1]
fOut = open(outName, "w")
fOut.write("Hello World!\n")
fOut.close()
