import json
import logging
from DBmAgent import DBmAgent
from CommonUtils import CommonUtils

class DBmEnvironment:
    def __init__(self, name, dbm_project, dbm_agent):
        self.name = name
        self.package_file_path = self.name + "_env_packages.json"
        self.dbm_project = dbm_project
        self.dbm_agent = dbm_agent

    def get_packages(self):
        self.dbm_agent.get_env_packages(self.dbm_project.name, self.name, self.package_file_path)

    def upgrade(self, dbm_package_name):
        self.dbm_agent.upgrade(self.dbm_project.name, self.name, dbm_package_name)

    def get_latest_deployed_package(self):
        self.get_packages()
        with open(self.package_file_path) as f:
            versions = json.load(f)
        for keyval in versions:
            if(keyval['EnvDeployed'] != None):
                return keyval['VersionName']
        return None

    def increment_latest_deployed_version(self):
        return CommonUtils.increment_version(self.get_latest_deployed_version())

    def get_latest_deployed_version(self):
        package_name = self.get_latest_deployed_package()
        logging.info(f"Latest Deployed Package in {self.dbm_project.name}/{self.name} is {package_name}")
        found_version = None
        if package_name is not None:
            found_version = CommonUtils.find_version(package_name)
        logging.info(f"Latest Deployed Version in {self.dbm_project.name}/{self.name} is {found_version}")
        return found_version
    
    def upgrade_to_latest_available_package(self):
        latest_deployed_package_in_rs_env = self.dbm_project.rs_env.get_latest_deployed_package()
        self.upgrade(latest_deployed_package_in_rs_env)


    
        
