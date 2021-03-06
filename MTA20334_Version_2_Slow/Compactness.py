from BoundingBox import *


class Compactness:
    debug = True
    allPixelsInBoundary = 0

    def __init__(self, image):
        self.image = image

    def calculateCompactness(self):
        height = self.image.shape[0]
        width = self.image.shape[1]
        # Calculating the area by multiplying the height with the width
        area = (height * width)

        allWhitePixels = len(self.image[self.image == 255])
        # Compactness is calculated by taking 100 and dividing it with the area multiplied with all the white pixels
        compactness = round((100 / area) * allWhitePixels)
        return compactness

    def printResults(self):
        print("| Compactness:", self.calculateCompactness(), "%")
        print("|------------------------------------------------")
        print("| Hand Gesture Detected as:", self.compactnessComparison())
        print("+-----------------------------------------------+")

