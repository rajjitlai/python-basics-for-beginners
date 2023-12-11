# Finding the resolution of an Image

def fRes(file_name):
    with open(file_name, 'rb') as image:
        # image.seek(22) # for png
        image.seek(163) # for jpg

        h_var = image.read(2)
        resHeight = (h_var[0] << 8) + h_var[1]
        w_var = image.read(2)
        resWidth = (w_var[0] << 8) + w_var[1]
    print("The resolution of the image is: ", resWidth, "X", resHeight)

# fRes("file.png")
fRes("file.jpg")