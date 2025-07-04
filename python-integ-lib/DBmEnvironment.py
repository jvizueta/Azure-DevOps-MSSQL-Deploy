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

    def upgrade(self, package_name):
        self.dbm_agent.upgrade(self.dbm_project.name, self.name, package_name)

    def rollback(self, package_name):
        self.dbm_agent.rollback(self.dbm_project.name, self.name, package_name)

    def get_latest_deployed_package(self):
        self.get_packages()
        with open(self.package_file_path) as f:
            versions = json.load(f)
        for keyval in versions:
            if(keyval['EnvDeployed'] != None):
                return keyval['VersionName']
        return None

    def get_version_package_name(self, version_searched):
        self.get_packages()
        with open(self.package_file_path) as f:
            versions = json.load(f)
        for keyval in versions:
            package_name = keyval['VersionName']
            version_found = CommonUtils.find_specific_version(package_name, version_searched)
            if(version_found):
                return package_name
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

    def move_to_package(self, package_name):
        package_version = CommonUtils.find_version(package_name)
        latest_deployed_version = self.get_latest_deployed_version()
        if(CommonUtils.is_version_greater_than(package_version, latest_deployed_version)):
            self.upgrade(package_name)
        else:
            self.rollback(package_name)


    
        
