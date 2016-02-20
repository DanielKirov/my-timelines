from PIL import Image, ImageOps, ImageDraw, ImageFilter

size = (128, 128)

# take a name like pat.jpg.zip removes everything after first .
# then generates a string pat
def createName(imageName):
    return imageName.split('.', 1)[0]


# take a Image.open(X) type of a parameter as an image and a name
# generates a thumbnail 128x128 based on global var
# named name_thumbnail.png
def thumblyFy(im, imageName):
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)
    output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)
    output = output.filter(ImageFilter.SHARPEN)
    output.save(createName(imageName) + '_thumbnail.png')
