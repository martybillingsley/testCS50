from PIL import Image

# returns a new RGB image of width w, height h, and color c
# color can be a three-tuple or a color name
# Ex: img = makeEmptyPicture(100,200, (255,0,0))
# Ex: img = makeEmptyPicture(100,200, 'red')
def makeEmptyPicture(w, h, c):
    im = Image.new("RGB", (w, h), c)
    return (im)

# opens and returns an Image, given a (local) filename
def makePicture(fName):
    im = Image.open(fName)
    return (im)

# shows an image in it's own window within the GUI window
def show(img):
    img.show()
 
