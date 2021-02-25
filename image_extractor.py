import os
import pathlib
from PIL import Image

fileDir= r"C:\Users\pyada\.spyder-py3\60ft_multi"  #Modify this to directory path where your images of different extensions are located.
fileExt= r"*.jpg"       #You can modify this depending on what type of images you would like to extract from the directory.
saveDir= r"C:\Users\pyada\.spyder-py3\60ft_multi_img"   #This is the path of directory where you want to save your extracted images of desired extension.

def image_extractor(fileDir, fileExt,saveDir):
    a=list(pathlib.Path(fileDir).glob(fileExt))
    img_num=1
    for fp in a:
        b=str(fp)
        savedir=saveDir
        name, ext = os.path.splitext(b)
        name=os.path.basename(b)
        name=os.path.splitext(name)[0]
        img=Image.open(os.path.join(fileDir,b))
        save_to= os.path.join(savedir, name+"_{:03}.tif")
        img.save(save_to.format(img_num))
        img_num += 1
    print("Image Extraction Completed!")

image_extractor(fileDir,fileExt,saveDir)
