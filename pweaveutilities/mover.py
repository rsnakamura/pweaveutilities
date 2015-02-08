
# python standard library
import os
import shutil

# this package
from pweaveutilities.generators import find

def move(source_glob, source_path, target_path):
    """
    Moves files matching the source-glob in the source_path to the target_path
    """
    try:
        os.makedirs(target_path)
    except OSError:
        pass
    for path in find(source_glob, source_path):
        #base, filename = os.path.split(path)
        target = path.replace(source_path, target_path)
        os.renames(path, target)
    return