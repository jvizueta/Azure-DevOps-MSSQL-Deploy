from CommonUtils import CommonUtils
from DBmAgent import DBmAgent
from DBmUser import DBmUser

class DBmPackage:

    def __init__(self, dbm_project, dbm_agent, name, root_folder, version):
        self.dbm_project = dbm_project
        self.dbm_agent = dbm_agent
        self.name = name
        self.root_folder = root_folder
        self.version = version
        if(self.version is None):
            self.version = CommonUtils.find_version(self.name)

    def create_manifest_file(self, operation = "CreateOrUpdate"):
        path_to_scripts_folder = self.root_folder + "\\" + self.name
        self.dbm_agent.create_manifest_file(path_to_scripts_folder, operation)

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