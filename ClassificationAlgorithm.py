import math
#================= Runs K Mean =================================
def findNum(image,images,numImages,numRows,numCol,skip,minCutoff):
    minIndex = 0
    minValue = distance(image,images[0],numRows,numCol)
    for i in range(1,numImages):
        if i % (numImages/10) == 0:
            print(".")
        if minValue > distance(image,images[i],numRows,numCol):
            minIndex = i
            minValue = distance(image,images[i],numRows,numCol)
            if(minValue < minCutoff):
                return [images[minIndex],minValue]
    results = [images[minIndex],minValue]
   
    return results

#=========== Determines euclidian distance between images ============
def distance(image1, image2, numRows,numCol):
    dist = 0
    for i in range(0,numRows):
        for j in range(0,numCol):
            dist += (image1.pixels[i*numRows+j] - image2.pixels[i*numRows+j])**2
    return math.sqrt(dist)

#============ Prints Image ============================
def printImage(image,numRows,numCol):
    for i in range(0,numRows):
        print()
        for j in range(0,numCol):
            if image.pixels[i*numRows+j] == 0:
                print(" ",end="")
            else:
                print("0",end=" ")
    print()

# Gets user image
def getUserImage():
    userFile = open("Images/output.txt","r");
    pixels = []
    for i in range(0,28*28):
        byte = userFile.read(1)
        if int(byte) == 0:
            pixels.append(0)
        elif int(byte) == 1:
            pixels.append(255)
        elif int(byte) == 2:
           pixels.append(200)
        else:
            pixels.append(0)
    return Image(-1,pixels)

# Loads images               
def loadImages(trainingImageFile,trainingLabelFile,numImages,numRows,numCol):
    print("Loading " + str(numImages) + " images")
    images = []
    for i in range(0,numImages):
        if i % (numImages/10) == 0:
            print(".")
        pixelsTemp = []
        label = int.from_bytes(trainingLabelFile.read(1),'big')
        for i in range(0,numRows*numCol):
            pixelsTemp.append(int.from_bytes(trainingImageFile.read(1),'big'))

        images.append(Image(label,pixelsTemp))
    return images
def testImages(testnumImages,testImages,trainingImages,numImages,numRows,numCol):
    print("Testing Images")
    correctCount = 0
    for i in range(0,testnumImages):
        if i % (testnumImages/100) == 0:
            print(".")
        value = findNum(testImages[i],trainingImages,numImages,numRows,numCol,-1,00)[0].number
        if(value == testImages[i].number):
            correctCount += 1
        print(str(i) + ". Count: " + str(correctCount/(i+1)))
    print(correctCount/testnumImages)
    
def main():
    
    print("Starting Program")

    # Open image files
    trainingImageFile = open("TrainingData/train-images.idx3-ubyte","rb")
    trainingLabelFile = open("TrainingData/train-labels.idx1-ubyte","rb")
    testImageFile = open("TestData/t10k-images.idx3-ubyte","rb")
    testLabelFile = open("TestData/t10k-labels.idx1-ubyte","rb")

   

    
    
    


    
   




    # Load header information
    magicNumber = int.from_bytes(trainingImageFile.read(4),'big')
    numImages = int.from_bytes(trainingImageFile.read(4),'big')
    numRows = int.from_bytes(trainingImageFile.read(4),'big')
    numCol = int.from_bytes(trainingImageFile.read(4),'big')
    magicLabelNumber = int.from_bytes(trainingLabelFile.read(4),'big')
    numLabels = int.from_bytes(trainingLabelFile.read(4),'big')

    testmagicNumber = int.from_bytes(testImageFile.read(4),'big')
    testnumImages = int.from_bytes(testImageFile.read(4),'big')
    testnumRows = int.from_bytes(testImageFile.read(4),'big')
    testnumCol = int.from_bytes(testImageFile.read(4),'big')
    testmagicLabelNumber = int.from_bytes(testLabelFile.read(4),'big')
    testnumLabels = int.from_bytes(testLabelFile.read(4),'big')
    print("Header information loaded")

    # Load images
    trainingImages = loadImages(trainingImageFile,trainingLabelFile,numImages,numCol,numRows)
    #testImages = loadImages(testImageFile,testLabelFile,testnumImages,numCol,numRows)
    print("Training Images Loaded")

    # Test Images
    #testImages(testnumImages,testImages,trainingImages,numImages,numRows,numCol)
    
    while(True):
        choice = input("Load image (y/n):")
        if(choice == "y"):
            userImage = getUserImage()
            print("Analyzing")
            result = findNum(userImage,trainingImages,numImages,numRows,numCol,-1,0)
            #printImage(userImage,numRows,numCol)
            print("The image is a " + str(result[0].number))
            #print("Matched Image")
            #printImage(result[0],numRows,numCol)
            #print("Match Percentage: ",end = " ")
            #print(result[1])
        

    

    

    
       
class Image:
    def __init__(self,_number,_pixels):
        self.pixels = _pixels
        self.number = _number
main()