import os 

# Input/Output 

def rm(file_name):
    os.remove(file_name)
    return f"{file_name} has been deleted!"


if __name__ == '__main__':
    filename = input("What file would you like to delete? ")
    rm(filename)