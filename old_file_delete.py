import os
import time
import logging
from logging.handlers import RotatingFileHandler

class DOF:
    """ A Class to delete images greater than x days old
        Delete Old Files"""
    pass

    def __init__(self):
        pass

    def file_logging(self):
        self.log_formatter = logging.Formatter("""%(asctime)s %(levelname)s"""
                                               """%(funcName)s (%(lineno)d) """
                                               """%(message)s""")
        self.logFile = '/root/old_file_delete/OFD_log.txt'
        self.my_handler = RotatingFileHandler(self.logFile, mode='a',
                                              maxBytes=50*1024, backupCount=2,
                                              encoding=None, delay=0)
        self.my_handler.setFormatter(self.log_formatter)
        self.my_handler.setLevel(logging.INFO)
        self.app_log = logging.getLogger('root')
        self.app_log.setLevel(logging.INFO)
        self.app_log.addHandler(self.my_handler)
        #self.app_log.info("Logging Facility Successfully initiated")
        

    def file_listing(self, filedir="/mnt/samba/garageCam"):
        """ Make a list of files in the directory and print the number """
        self.filedir = filedir
        self.filelist = os.listdir(filedir)
        ##print("There are %d files in this directory" %(len(self.filelist)))
        d.app_log.info("Files in Directory: " + str(len(self.filelist)))


    def del_older(self, age=3):
        """ Do the dirty work of deleting files older than x """
        self.shit_can = []
        os.chdir(self.filedir)
        self.age = age * 86400
        self.now = time.time()
        for file in self.filelist:
            self.modified = os.stat(file).st_mtime
            if self.now - self.modified > self.age:
                self.shit_can.append(file)
        ##print(len(self.shit_can))
        ##print(len(self.shit_can))
        for file in self.shit_can:
            os.remove(file)

## Instantiates the class
d = DOF()
## Starts logging facility
d.file_logging()
## prints the number of files headed for the shit can
d.file_listing()
## prints the file directory I'm working with
## print(d.filedir)
## creates the list and prints the files to be deleted
d.del_older(3)
## print(d.shit_can)

d.app_log.info("Files Deleted: " + str(len(d.shit_can)))
## for file in d.shit_can: d.app_log.info(file)
## app_log.info(d.filelist)

