'''
PROGRAM TO CONVERT .gcode FILE TO ABAQUS .inp FILE
  (c) TB
The program considers only extruding paths. Rapid movements are neglected.
'''
import io
# File names
filenameGCode       = str('GCODEFILE.gcode')
filenameABAQUSinp   = str('FILAMENTFILE.inp')
filenameMaterial    = str('MATERIALFILE.inp')

# Set width of the microstructure
microWidth = float(0.3)

# Define orthotropic fiber properties
E1      = float(2690.0)
E2      = float(2130.0)
E3      = float(2260.0)
G12     = float(894.2)
G13     = float(916.7)
G23     = float(895.1)
NU12    = float(0.2653)
NU13    = float(0.2818)
NU23    = float(0.3037)
Alpha1  = float(76.0E-6)
Alpha2  = float(82.6E-6)
Alpha3  = float(82.6E-6)

#----------------- Read and rewrite points from GCode --------------------#
# Open file
with open(filenameGCode,'r') as file:
    data = []

    # Initialize coordinates
    X       = float(0.)
    Y       = float(0.)
    Z       = float(0.)

    # Read line by line
    for lines in file:
        if lines.startswith('G1 '):
        # Write lines containing points to data list
            data.append(lines)
        if lines.startswith('G0 '):
        # Write lines containing points to data list
            data.append(lines)

    # Read number of overall fibres (lines starting with G0), each fibre consists of printed paths defined by 'G1'
    countG0 = int()
    for lines in data:
        if lines.startswith('G0'):
            countG0 += 1
    numbFibres = countG0
    #print numbFibres

    # Write each fibre input into an own list:  Dictionary - 'fibreList'
    fibreList = {}
    for i in range(numbFibres):
        fibreList[i] = []

    countF = 0
    for lines in data:
        if lines.startswith('G0'):
            fibreList[countF].append(lines)
            countF += 1
        else:
            fibreList[countF-1].append(lines)

    # Initialize fibre coordinate dictionary
    fibreListCoor = {}
    for i in range(numbFibres):
        fibreListCoor[i] = []

    # Initialize new coordinate dictionary
    newCoorDict = {}
    for i in range(numbFibres):
        newCoorDict[i] = []

    # Initialize coordinate dictionary
    coordDict = {}
    for i in range(numbFibres):
        coordDict[i] = []

    # Get floats from strings in the dictionary
    for items in fibreList:
        coorList = fibreList[items]
        coordXYZ = []
        for line in coorList:
            # Split lines
            splitLine = line.split()
            # Number of items in split array
            NumbItem = len(splitLine)
            for item in splitLine:
                if 'X' in item:
                    if item.startswith('X'):
                        X = float(item[1:])
                    else:
                        pass

            for item in splitLine:
                if 'Y' in item:
                    if item.startswith('Y'):
                        Y = float(item[1:])
                    else:
                        pass

            for item in splitLine:
                if 'Z' in item:
                    if item.startswith('Z'):
                        Z = float(item[1:])
                    else:
                        pass

            # Append X,Y,Z to new dictionary   LOOP:  line
            newCoorList = [X, Y, Z]

            # Append newCoordList to new dictionary
            newCoorDict[items].append(newCoorList)

    # Delete multiple coordinates
    for i in range(len(newCoorDict)):
        for j in range(len(newCoorDict[i])-1):
            if (newCoorDict[i][j-1] == newCoorDict[i][j]):
                pass
                #del newCoorDict[i][j]

    # Delete single coordinates (non extruding nozzle movement)
    for i in range(len(newCoorDict)):
        if (len(newCoorDict[i]) == 1):
            del newCoorDict[i]
        else:
            pass

    # Actualize number of fibres
    numbFibres = len(newCoorDict)

    # Write X,Y,Z coordinates in different lists
    Ncount = 0
    Xnodes = list()
    for i in newCoorDict:
        for j in range(len(newCoorDict[i])):
            Xnodes.append(newCoorDict[i][j][0])
    Ynodes = list()
    for i in newCoorDict:
        for j in range(len(newCoorDict[i])):
            Ynodes.append(newCoorDict[i][j][1])
    Znodes = list()
    for i in newCoorDict:
        for j in range(len(newCoorDict[i])):
            Znodes.append(newCoorDict[i][j][2])

    # Get layer height
    def getLayerHeight(Znodes):
        for i in range(3, len(Znodes)):
            if (Znodes[i] != Znodes[i-1]):
                layerHeight = Znodes[i] - Znodes[i-1]
                break
            else:
                pass
        return layerHeight

    # Rewrite dictionary keys
    def rewriteDict(newCoorDict):
        count = -1
        actCoorDict = newCoorDict
        for k in actCoorDict:
            count += 1
            actCoorDict[count] = actCoorDict.pop(k)
        return actCoorDict

    # Call rewritten coordinate dictionary
    actCoorDict = rewriteDict(newCoorDict)

    # Get list with number of layer for each fibre
    def getLayerNumber(newCoorDict):
        countL = 0
        layerList = []
        actCoorDict = rewriteDict(newCoorDict)
        # Write Layer number to layerList
        countL = 1
        for i in range(1,len(actCoorDict)):
            layerList.append(countL)
            if (actCoorDict[i][0][2] == actCoorDict[i-1][0][2]):
                pass
            else:
                countL += 1
        layerList.append(countL)
        return layerList

    # Call layer number
    layerList = getLayerNumber(newCoorDict)

    # Get list including the number of elements for each fibre
    def getElementsFromFibre(actCoorDict):
        elementList = []
        for i in actCoorDict:
            elementNumb = len(actCoorDict[i])-1
            elementList.append(elementNumb)
        return elementList

    elementList = getElementsFromFibre(actCoorDict)

    # Get list containing the number of elements of each layer
    def getSetNumber(layerList,elementList):
        listNumb = []
        countE = elementList[0]
        for i in range(1,len(layerList)):
            if (layerList[i] == layerList[i-1]):
                countE += elementList[i]
            else:
                listNumb.append(countE)
                countE += elementList[i]
        listNumb.append(countE)
        return listNumb

    listNumb = getSetNumber(layerList,elementList)

    # Check the number of nodes
    def checkNodes(newCoorDict):
        numberOfNodes = 0
        for i in newCoorDict:
            for j in newCoorDict[i]:
                numberOfNodes += 1
        return numberOfNodes

    def checkFibres(newCoorDict):
        numberOfFibres = 0
        for i in newCoorDict:
            numberOfFibres += 1
        return numberOfFibres

    layerHeight = getLayerHeight(Znodes)

    area = layerHeight * microWidth

#---------------- Create Abaqus input file ------------------#
with io.FileIO(filenameABAQUSinp,"w") as outFile:
    outFile.write("*Heading\n")
    outFile.write("** Job name: SimpleTestModelStraightWeave Model name: Weave\n")
    outFile.write("** Generated by: Abaqus/CAE 2017\n")
    outFile.write("*Preprint, echo=NO, model=NO, history=NO, contact=NO\n")
    outFile.write("**\n")
    outFile.write("** PARTS\n")
    outFile.write("**\n")
    outFile.write("*Part, name=Beam\n")

    # Write Master nodes to output file
    counter     =   0           # Returns the actual node number
    entries     =   0           # Number of entries in masterNodes
    masterNodes =  [1]          # Array including master node numbers: First node initialized
    # Write nodes
    outFile.write("*Node\n")

    # Write nodes to the file
    for i in range(len(Xnodes)):
        counter = counter + 1
        outFile.write("  %7d,  %10.3f,  %10.3f,  %10.3f\n" % ( counter , Xnodes[i], Ynodes[i], Znodes[i] ) )

    # Write elements to the file
    outFile.write("*Element, type=B31\n")
    countE = 0
    countN = 0
    for i in actCoorDict:
        for nodes in range(len(actCoorDict[i])-1):
            countN += 1
            countE += 1
            outFile.write("%7d, %7d, %7d\n" % ( countE , countN , countN+1 ) )
        countN += 1

    # Create different Element sets
    for i in range(len(listNumb)-1):
        # Print Element set
        outFile.write('*Elset, elset=LAYER_%s_PRINTED, generate\n' %(i+1) )
        outFile.write('%6d, %6d,  1\n' % (listNumb[i]+1,listNumb[i+1]) )

    # Create node set
    outFile.write("*Nset, nset=ALL, generate\n")
    outFile.write(" 1, %7d,  1\n" % ( len(Xnodes) ) )
    outFile.write("*Nset, nset=SECTION, generate\n")
    outFile.write(" 1, %7d,  1\n" % (len(Xnodes)))
    outFile.write("*Elset, elset=SECTION, generate\n")
    outFile.write(" 1, %7d,  1\n" %(countE) )

    # Write layer sections
    for i in range(len(listNumb)-1):
        outFile.write('** Section: Section-%s-SECTION\n' %(i+1) )
        outFile.write('*Solid Section, elset=LAYER_%s_PRINTED, material=FIBERMATERIAL%s\n' %(i+1, i+1) )
        outFile.write("%s,\n" %(area))

    outFile.write("*End Part\n")
    outFile.write("**\n")
    outFile.write("**\n")
    outFile.write("** ASSEMBLY\n")
    outFile.write("**\n")
    outFile.write("*Assembly, name=Assembly\n")
    outFile.write("**\n")
    outFile.write("*Instance, name=BEAM-1, part=BEAM\n")
    outFile.write("*End Instance\n")
    outFile.write("**\n")
    outFile.write("*End Assembly\n")
    outFile.write("**\n")
    outFile.write("** MATERIALS\n")
    outFile.write("**\n")
    outFile.write("*Material, name=DUMMY")

#---------------- Create Material input file ---------------------#
with io.FileIO(filenameMaterial,"w") as matFile:
    matFile.write('** E1, E2, E3, G23, G13, G12, NU23, NU13, NU12, Alpha1, Alpha2, Alpha3\n')
    # Write fiber materials
    for i in range(len(listNumb)-1):
        matFile.write('*Material, name=FIBERMATERIAL%s\n' %(i+1) )
        matFile.write('%8.3f, %8.3f, %8.3f, %8.3f, %8.3f, %8.3f, %8.3f, %8.3f, %8.3f, %8.7f, %8.7f, %8.7f\n' %(E1, E2, E3, G23, G13, G12, NU23, NU13, NU12, Alpha1, Alpha2, Alpha3) )
    # Write matrix material
    matFile.write('*Material, name=MATRIXMATERIAL\n')
    matFile.write('0.0, 0.0, 0.0\n')

#-------------------  PRINT PART INFORMATION ---------------------#
print ('*** Path and Material data have been written to ABAQUS input file ***')
print (' ')
print ('ABAQUS input file name:         %s' % filenameABAQUSinp )
print ('ABAQUS material file name:      %s' % filenameMaterial )
print (' ')
# Print number of Nodes, Tracks and Layers
nN = checkNodes(newCoorDict)
nF = checkFibres(newCoorDict)
print ('Total number of tracks: %s' % (countE))
layerNumb = layerList[-1]
print ('Total number of layers: %s' % (layerNumb - 1))
print (' ')
print ('Layer height: %s mm' % layerHeight)


