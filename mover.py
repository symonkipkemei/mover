import pathlib


# path to my desktop
path = pathlib.Path("/home/symon_kipkemei")


# create new folder
new_path = pathlib.Path("/home/symon_kipkemei/shots")
new_path.mkdir(exist_ok=True )



# create an object that points to where the images are 

for images in path.iterdir():
    print(images.name)
    if images.suffix == ".png":
         # create a new path for the images 
        new_filepath = new_path.joinpath(images.name)
    
        #move files
        images.replace(new_filepath)

    elif images.suffix == ".PNG":
         # create a new path for the images 
        new_filepath = new_path.joinpath(images.name)
    
        #move files
        images.replace(new_filepath)


print("completed succesfully")