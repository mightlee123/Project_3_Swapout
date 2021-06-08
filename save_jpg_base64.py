import base64
import pathlib as Path

#Path = "../Project_3_Swapout/jpg/Customer_A.jpg"
#python upload file
Path = ("../Project_3_Swapout/jpg/Customer_A.jpg")
#this function turns uploaded images into base64 bytes

def jpg_to_64base():
    with open(Path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        image_base64=encoded_string

#def save_64base_to_csv(email, df):