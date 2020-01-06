import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    
    if suffix == "":
        return "Please enter a valid suffix"
    
    if path == "":
        return "Please enter a valid path"
    
    output = check_folder(suffix, path)
    
    return output

def check_folder(suffix, path):
    output = []
    
    for x in os.listdir(path):
        if os.path.isfile(x):
            if x.endswith(suffix):
                output.append(x)
        else:
            output = output + check_folder(suffix, x)
    
    return output

# test case 1
    
print(find_files("py", "C:\\Users\\E058325\Desktop\P1")) # should return 5 files

# test case 2

print(find_files("", "C:\\Users\\E058325\\Desktop\\P1")) # should return 5 files

# test case 3

print(find_files("py", "")) # should return 5 files
