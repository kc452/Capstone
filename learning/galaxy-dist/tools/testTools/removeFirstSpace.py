from sys import argv

inName, outName = argv[1], argv[2]

fIn = open(inName, "r")
inStrings = fIn.readline().split(" ")
outString = "".join(inStrings)
fIn.close()

fOut = open(outName, "w")
fOut.write(outString)
fOut.close()
