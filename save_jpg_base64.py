import base64
import pathlib as Path

#Path = "../Project_3_Swapout/jpg/Customer_A.jpg"
#python upload file
with open(XXX.jpg, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
