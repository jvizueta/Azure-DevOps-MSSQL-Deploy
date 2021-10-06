import logging
from CommonUtils import CommonUtils
from DBmAgent import DBmAgent
from DBmUser import DBmUser

class DBmPackage:

    def __init__(self, dbm_project, dbm_agent, name, root_folder, version, type="regular"):
        self.dbm_project = dbm_project
        self.dbm_agent = dbm_agent
        self.name = name
        self.root_folder = root_folder
        self.version = version
        if(self.version is None):
            self.version = CommonUtils.find_version(self.name)
        self.type = type

    def create_manifest_file(self, operation = "CreateOrUpdate"):
        path_to_scripts_folder = self.root_folder + "\\" + self.name
        self.dbm_agent.create_manifest_file(path_to_scripts_folder, operation)
        if(self.type == "adhoc"):
            manifest_file_path = path_to_scripts_folder + "\\package.json"
            CommonUtils.ps_replace(manifest_file_path, "regular", "adhoc")
            logging.info(f"Package Type in Manifest (package.json file) set to 'adhoc'")

    def zip(self):
        path = self.root_folder + "\\" + self.name + "\\*"
        self.zip_path = self.name + ".zip"
        CommonUtils.zip(path, self.zip_path)

    def package(self):
        self.dbm_agent.package(self.dbm_project.name, self.zip_path)

    def create_or_update(self, operation = "CreateOrUpdate"):
        self.create_manifest_file(operation)
        self.zip()
        self.package()

    def precheck(self):
        self.dbm_agent.precheck(self.dbm_project.name, self.name)