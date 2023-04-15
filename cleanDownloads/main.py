import os
from pathlib import Path 


def createDirectory(directory:Path)->None:
    if (not directory.exists()): # checks if directory does not exist
        os.mkdir(directory)
        print(f"Created directory: {directory}")
    


if __name__ == "__main__":
    downloads_directory = Path.home()/"Downloads"
    pictures_directory = downloads_directory/"Pictures"
    videos_directory = downloads_directory/"Movies"
    dmg_directory = downloads_directory/"DmgFiles"    
    directory_collection  = []
    directory_collection.extend([pictures_directory,videos_directory,dmg_directory])
    
    #creating directories if none exist
    for directory in directory_collection:
        createDirectory(directory)
    
    # creating extensions we want to find
    image_extensions = ('.jpg','.png')
    video_extensions = ('.mp4','.vid','.wmv')
    dmg_extensions = ['.dmg']

    for file in os.listdir(downloads_directory):
        file_suffix = Path(file).suffix
        if file_suffix in image_extensions:
            new_path = pictures_directory/file 
            print(new_path)
            (downloads_directory/file).rename(new_path)
        elif file_suffix in video_extensions:
            new_path = videos_directory/file 
            print(new_path)
            (downloads_directory/file).rename(new_path)
        elif file_suffix in dmg_extensions:
            new_path = dmg_directory/file 
            print(new_path)
            (downloads_directory/file).rename(new_path)
        else:
            continue
         