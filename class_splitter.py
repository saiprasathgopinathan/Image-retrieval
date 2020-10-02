import cv2
import os
import shutil

main = "/home/saiprasad/Downloads/avantari_image_splitted/cheetah/"
for files in os.listdir(main):
    
    img = cv2.imread(os.path.join(main,files))
    cv2.imshow('image',img)
    chooser = cv2.waitKey(0)
    #print(chooser)
    file1 = os.path.join(main,files)
    if chooser == 99:
        shutil.move(file1,"/home/saiprasad/Downloads/avantari_image_splitted/cheetah/")
        print("Cheetah")

    if chooser == 102:
        shutil.move(file1,"/home/saiprasad/Downloads/avantari_image_splitted/fox/")
        print("fox")
        #pass

    if chooser == 116:
        shutil.move(file1,"/home/saiprasad/Downloads/avantari_image_splitted/tiger/")
        print("tiger")
        #pass

    if chooser == 108:
        shutil.move(file1,"/home/saiprasad/Downloads/avantari_image_splitted/lion/")
        print("lion")
        #pass

    cv2.destroyAllWindows()