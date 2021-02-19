from PIL import Image, ImageFilter

img_path = '../images'

img = Image.open(f'{img_path}/bulbasaur.jpg')
filtered_img = img.filter(ImageFilter.GaussianBlur)
filtered_img.save(f"{img_path}/blur.png", "png")

img2 = Image.open(img_path + '/pikachu.jpg')
filter2 = img2.filter(ImageFilter.SHARPEN)
filter2.save(img_path + '/sharppika.png', "png")

img3 = Image.open(img_path + '/squirtle.jpg')
filter3 = img3.convert('L')
crooked = filter3.rotate(90)
crooked.show()
filter3.save(img_path + "/graysquirt.png", "png")
