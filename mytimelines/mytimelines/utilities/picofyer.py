from PIL import Image, ImageOps, ImageDraw, ImageFilter



size = (128, 128)


def thumblyFy(im, name):
	mask = Image.new('L', size, 0)
	draw = ImageDraw.Draw(mask) 
	draw.ellipse((0, 0) + size, fill=255)
	output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
	output.putalpha(mask)
	output = output.filter(ImageFilter.SHARPEN)
	output.save(name+'_thumbnail.png')
