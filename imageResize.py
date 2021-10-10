from PIL import Image



def Image_resize(image,w,h):
    fileImage = Image.open(f"C:\\Users\\Hx101X\\Desktop\\Stock Images\\{image}.png")
    resizeFileImage = fileImage.resize((w,h))
    resizeFileImage.save(f"C:\\Users\\Hx101X\\Desktop\\passwordManager\\Images\\{image}Resized.png")


Image_resize("admin", 50, 50)
