
# python libraries
import fnmatch
import os
import re

WRITEABLE = 'w'
EOSection = ''

def regex_filter(file_list, expression):
    """
    Filters out file-names that don't match the expression

    :param:

     - `file_list`: list of strings to check
     - `expression`: regulare expression to match

    :yield: file-names that match the expression
    """
    for file_name in file_list:
        if re.match(expression, file_name):
            yield file_name
    return

def find(expression="*", start=None, regex=False):
    """
    Matches all below cwd or start-directory
    
    :param:

     - `expression`: A file-glob to match interesting files (or regex if flag is set)
     - `start`: The top path (finds files below the top)
     - `regex`: If true, assumes expression is regular

    :yield: Matching file name
    """
    if start is None:
        start = os.getcwd()
    if not regex:
        filterer = fnmatch.filter         
    else:
        filterer = regex_filter
    
    for path, dir_list, file_list in os.walk(start):
        for name in filterer(file_list, expression):
            yield os.path.join(path, name)
    return

class ShallowFind(object):
    """
    A finder of files that doesn't traverse directories
    """
    def __init__(self, glob, path=None):
        """
        :param:

         - `glob`: a file glob to match
         - `path`: an alternate to the current directory
        """
        self.glob = glob
        self._path = path
        self._filenames = None
        self._matching_names = None
        self._matching_count = None
        return

    @property
    def path(self):
        """
        :return: the path to the directory to search
        """
        if self._path is None:
            self._path = os.getcwd()
        return self._path

    @property
    def filenames(self):
        """
        :return: all files found in the path
        """
        if self._filenames is None:
            self._filenames = sorted(os.listdir(self.path))
        return self._filenames

    @property
    def matching_names(self):
        """
        Added so count could be given to hortator
        
        :return: list of matching names
        """
        if self._matching_names is None:
            self._matching_names = [name for name in fnmatch.filter(self.filenames, self.glob)]
        return self._matching_names

    @property
    def matching_count(self):
        """
        :return: count of matching names
        """
        if self._matching_count is None:
            self._matching_count = len(self.matching_names)
        return self._matching_count
    
    def reset(self):
        """
        Sets all properties to None
        """
        self._filenames = None
        self._path = None
        self._matching_names = None
        self._matching_count = None
        return

    def __iter__(self):
        """
        :yield: the matching filenames
        """
        for name in self.matching_names:
            yield name    
        return 
# end class ShallowFind

def shallow_find(expression='*', start = None, regex=False):
    """
    Matches only in one directory
    
    :param:

     - `expression`: A file-glob to match interesting files in this directory (or regex)
     - `start`: directory to start in
     - `regex`: if true, assume expression is regular
    """
    if not regex:
        filterer = fnmatch.filter
    else:
        filterer = regex_filter
    if start is None:
        start = os.getcwd()
    names = (name for name in os.listdir(start))
    for name in filterer(names, expression):
        yield os.path.join(start, name)
    return

def concatenate(glob, start=None):
    """
    :param:

     - `glob`: A file-glob to match interesting files.
     - `start`: The top path (finds files below the top)

    :yield: lines in matching files.
    """
    for name in find(glob, start):
        for line in open(name):
            yield line
    return