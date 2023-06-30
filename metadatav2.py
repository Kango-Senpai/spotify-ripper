from metadatav2_utils import repair_files, get_metadata, write_metadata
import os
from os.path import exists

def process(file_list):
    count = 0
    succeeded = 0
    for mp3 in file_list:
        if mp3.name.endswith(".mp3"):
            #print(f"Overwriting metadata for \"{mp3.name}\".")
            metadata = get_metadata(mp3.name)
            succeeded += write_metadata(mp3.name,metadata[0],metadata[1])
            count += 1
        
    return [succeeded,count]

def main():
    target_dir = input("Directory: ")
    # target_dir = "C:\\Users\\Henry\\Desktop\\Convert\\Henry\\"
    #target_dir = "./convert/"
    try:
        os.chdir(target_dir)
    except Exception as ex:
        print("\033[31mInvalid directory. Defaulting to cwd.\033[37m")
        try:
            os.mkdir("convert/")
        except:
            print("Directory exists")
        os.chdir("convert/")
    print(f"Target directory: {target_dir}")
    input("\n\nREADY")
    metrics = [1,1]
    os.system("clear")
    for i in range(1,3):
        print(f"PASS {i}")
        dir_scan = os.scandir('./')
        metrics = process(dir_scan)
        print(f"Processed {metrics[0]} of {metrics[1]} files.")
        if metrics[0] != metrics[1]:
            repair_files()
        else:
            break

main()