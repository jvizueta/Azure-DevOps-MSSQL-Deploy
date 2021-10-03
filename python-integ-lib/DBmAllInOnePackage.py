from DBmPackage import DBmPackage
class DBmAllInOnePackage(DBmPackage):
    def __init__(self, dbm_project, dbm_agent, workspace, version_package_names):
        version = dbm_project.rs_env.increment_latest_deployed_version()
        name = f"V{version}__precheckall"
        super().init__(dbm_project, dbm_agent, name, workspace.folder_name, version)
        self.version_package_names = version_package_names
