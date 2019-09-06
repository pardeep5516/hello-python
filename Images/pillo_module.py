from PIL import Image,ImageEnhance,ImageFilter
import os


# img1 = Image.open("Bindesh.jpg")
# img1.save('bin.pdf')
# img1.show('bin.png')

#!image size

# MAX_SIZE  = (500,500)
# img1.thumbnail(MAX_SIZE)
# img1.save('bin2.jpg')

# for item in os.listdir():
#     if item.endswith('.jpg'):
#         img1 = Image.open(item)
#         file_name,extension = os.path.splitext(item)
#         img1.save(f"{file_name}.png")



#!ImageEnhance
# img1 = Image.open("Bindesh.jpg")
# enhance  = ImageEnhance.Sharpness(img1)
# enhance.enhance(5).save('bin1.jpg') 
#0 blurry
# 1: original image,
# 2 image with increase sharpness
# 3 : increase sharpness  

#!........color......
# img1 = Image.open("Bindesh.jpg")
# enhance  = ImageEnhance.Color(img1)
# enhance.enhance(3).save('bin1.jpg') 


#!.......brightness.......!
# img1 = Image.open("Bindesh.jpg")
# enhance  = ImageEnhance.Brightness(img1)
# enhance.enhance(2).save('bin1.jpg') 

# !.........contrast....
# img1 = Image.open("Bindesh.jpg")
# enhance  = ImageEnhance.Contrast(img1)
# enhance.enhance(2).save('bin1.jpg') 

# !.......image_blur>>>>
img1 = Image.open("Bindesh.jpg")
img1.filter(ImageFilter.GaussianBlur(radius = 4)).save('bin2.jpg') 
