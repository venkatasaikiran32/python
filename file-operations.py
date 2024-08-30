# file_operations.py

def read_file(file_path):
    """
    it is used to read the contents of a file.
    """
    f=open(file_path,'r')
    content=f.read()
    f.close()
    return content

def write_file(file_path, data):
    """
    it is used to Write data to a file. 
    it Overwrites the file if it already exists.
    
    """
    f=open(file_path,'w')
    f.write(data)
    f.close()
    

def append_file(file_path, data):
    """
    it is used to appends data to a file. 
    Creates the file if it does not exist.
    and it not overides the contents of the file if already present
    """
    f=open(file_path,'a')
    f.write(data)
    f.close()
    

def read_file_lines(file_path):
    """
    it is used to read the contents of a file and returns it as a list of lines.
    
   
    """
    f=open(file_path,'r')
    content=f.readlines(data)
    f.close()
    return content


def write_file_lines(file_path, lines):
    """
    it is used to Writes a list of lines to a file.
    it Overwrites the file if it already exists.
    .
    """
    f=open(file_path,'w')
    f.writelines(data)
    f.close()
    
def append_file_lines(file_path, lines):
    """
     it is used to appends a list of lines to a file. 
     it Creates the file if it does not exist.
    
    """
    f=open(file_path,'a')
    f.writelines(data)
    f.close()
    