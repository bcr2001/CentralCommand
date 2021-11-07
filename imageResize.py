from PIL import Image



def Image_resize(image,w,h):
    fileImage = Image.open(f"C:\\Users\\Hx101X\\Desktop\\Stock Images\\{image}.png")
    resizeFileImage = fileImage.resize((w,h))
    resizeFileImage.save(
        f"C:\\Users\\Hx101X\\Desktop\\centralcommand\\Images\\{image}Resized.png")


Image_resize("play2", 50, 50)
