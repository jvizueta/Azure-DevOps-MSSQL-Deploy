import logging
from DBmEnvironment import DBmEnvironment
from CommonUtils import CommonUtils
from DBmPackage import DBmPackage
from DBmAllInOnePackage import DBmAllInOnePackage

class DBmProject:

    def __init__(self, name, rs_env_name, dbm_agent, root_folder):
        self.name = name
        self.dbm_agent = dbm_agent
        self.root_folder = root_folder
        self.rs_env = DBmEnvironment(rs_env_name, self, self.dbm_agent)

    def upgrade_release_source(self, package_name):
        self.rs_env.upgrade(package_name)

    def get_available_package_names(self):
        latest_deployed_version = self.rs_env.get_latest_deployed_version()
        return CommonUtils.get_version_folders(self.root_folder, latest_deployed_version)

    def upgrade_release_source_with_all_available_packages(self, up_to_version = None):
        available_package_names = self.get_available_package_names()
        for package_name in available_package_names:
            package_version = CommonUtils.find_version(package_name)
            if(up_to_version is None or not CommonUtils.is_version_greater_than(package_version, up_to_version)):
                package = DBmPackage(self, self.dbm_agent, package_name, self.root_folder, None)
                package.create_or_update()
                self.rs_env.upgrade(package.name)

    def precheck_all_available_packages_one_by_one(self, up_to_version = None):
        available_package_names = self.get_available_package_names()
        latest_package = None
        for package_name in available_package_names:
            package_version = CommonUtils.find_version(package_name)
            if(up_to_version is None or not CommonUtils.is_version_greater_than(package_version, up_to_version)):
                package = DBmPackage(self, self.dbm_agent, package_name, self.root_folder, None)
                package.create_or_update()
                latest_package = package
        if latest_package is not None:
            latest_package.precheck()
    
    def precheck_all_available_packages_all_in_one(self, dbm_workspace):
        # TO BE IMPLEMENTED
        return None
