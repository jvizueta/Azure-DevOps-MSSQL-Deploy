import os
import logging
from CommonUtils import CommonUtils

class DBmWorkspace:
    def __init__(self, folder_name = "DBmWork"):
        self.folder_name = folder_name

    def create_folder(self):
        path = os.path.join(".", self.folder_name)
        os.mkdir(path)
        logging.info(f"Workspace Folder created at {path}")
    
