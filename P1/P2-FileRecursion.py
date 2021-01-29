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
    list_of_paths = []

    list = os.listdir(path)
    #print(list)
    for val in list:
        full_path = os.path.join(path,val)
        if os.path.isfile(full_path) and val.endswith(suffix):
            #print("file found : ", full_path)
            list_of_paths.append(full_path)
        elif os.path.isdir(os.path.join(path,val)):
            #print("dir found : ", val)
            list_of_paths.append(find_files(suffix,full_path))
    return list_of_paths

# test1
list_of_paths = find_files(".c","D:\\nd256\P1\\testdir")
print(list_of_paths)  # [['D:\\nd256\\P1\\testdir\\subdir1\\a.c'], [], [['D:\\nd256\\P1\\testdir\\subdir3\\subsubdir1\\b.c']], [], ['D:\\nd256\\P1\\testdir\\subdir5\\a.c'], 'D:\\nd256\\P1\\testdir\\t1.c']

# test2 : testing on parent foler for testdir
list_of_paths = find_files(".c","D:\\nd256\P1")
print(list_of_paths)
#[[['D:\\nd256\\P1\\testdir\\subdir1\\a.c'], [], [['D:\\nd256\\P1\\testdir\\subdir3\\subsubdir1\\b.c']], [], ['D:\\nd256\\P1\\testdir\\subdir5\\a.c'], 'D:\\nd256\\P1\\testdir\\t1.c']]

# test 3
list_of_paths = find_files(".c","D:\\nd256\P0")
print(list_of_paths)
# []
