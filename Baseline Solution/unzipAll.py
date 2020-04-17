import os, zipfile

####
# Copy script to folder and then run it
####

def unzipAll(dir_name, extension):     

    os.chdir(dir_name) # change directory from working dir to dir with files

    for item in os.listdir(dir_name): # loop through items in dir
        if item.endswith(extension): # check for ".zip" extension
            file_name = os.path.abspath(item) # get full path of files
            zip_ref = zipfile.ZipFile(file_name) # create zipfile object
            fname = item.split('.')[0]
            dir = os.path.join(dir_name,fname)
            #print("Directory name now is: ",dir)
            zip_ref.extractall(dir) # extract file to dir
            
            print(dir) # extract file to dir
            zip_ref.close() # close file
            os.remove(file_name) # delete zipped file

if __name__ == "__main__":
    # print("Unzipping started")
    # for item in os.listdir(os.getcwd()): # loop through items in dir
    #     print ("Item found: "+ item)
    #     try:
    #         print("Unzipping: " + item)
    #         unzipAll(os.getcwd() + "\\\\" + item, ".zip")
    #     except Exception e:
    #         print("Unzip failed: " + item)
    print("Unzipping started")
    unzipAll(os.getcwd(), ".zip")
