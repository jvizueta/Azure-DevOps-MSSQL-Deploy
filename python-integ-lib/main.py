import logging
import sys
from DBmServer import DBmServer
from DBmUser import DBmUser
from DBmAgent import DBmAgent
from DBmProject import DBmProject
from DBmPackage import DBmPackage
from DBmWorkspace import DBmWorkspace
from DBmEnvironment import DBmEnvironment
from CommonUtils import CommonUtils

#####################################
# PARAMETER START
#####################################

dbm_server_name = sys.argv[1] #"t21-jc"
dbm_server_port = sys.argv[2] #"8017"
dbm_server_use_ssl = sys.argv[3] #"n"

dbm_user_auth_type = sys.argv[4] #"DBmaestro Account"
dbm_user_username = sys.argv[5] #"poc@dbmaestro.com"
dbm_user_password = sys.argv[6] #"VmzU9NIDff1BALGXgsh58XXIg89FH7U5"

dbm_agent_path = sys.argv[7] #"C:\\Program Files (x86)\\DBmaestro\\DOP Server\\Agent\\DBmaestroAgent.jar"

dbm_package_root_folder = sys.argv[8] #"versions"
# dbm_package_version = "4"

dbm_project_name = sys.argv[9] #"MSSQL_P2"
dbm_project_rs_env_name = sys.argv[10] #"RS"
dbm_project_action = sys.argv[11]

#####################################
# PARAMETER END
#####################################

logging.basicConfig(encoding="utf-8", format='DBmLibs> %(asctime)s - %(levelname)s: %(message)s', level=logging.INFO)
logging.info("Parameters set")

dbm_server = DBmServer(dbm_server_name, dbm_server_port, dbm_server_use_ssl)
dbm_user = DBmUser(dbm_user_auth_type, dbm_user_username, dbm_user_password)
dbm_agent = DBmAgent(dbm_agent_path, dbm_server, dbm_user)

dbm_project = DBmProject(dbm_project_name, dbm_project_rs_env_name, dbm_agent, dbm_package_root_folder)

dbm_workspace = DBmWorkspace()

logging.info("Basic objects created")
# dbm_package = DBmPackage(dbm_package_root_folder, dbm_package_version, dbm_project, dbm_agent)

#dbm_package.create_manifest_file()
#dbm_package.create_or_update()
#dbm_project.upgrade_release_source(dbm_package.name)

#dbm_project.rs_env.get_packages()
#print(dbm_project.rs_env.get_latest_deployed_package())

# latest_deployed_version = dbm_project.rs_env.get_latest_deployed_version()
# print(CommonUtils.get_version_folders(dbm_package_root_folder, latest_deployed_version))
#print(CommonUtils.get_version_folders(dbm_package_root_folder, "1.1"))

# print(dbm_project.get_available_packages())

# dbm_project.upgrade_release_source_with_all_available_packages()

# print(dbm_project.rs_env.increment_latest_deployed_version())

#dbm_project.upgrade_release_source_with_all_available_packages()


if (dbm_project_action == "precheckAllOneByOne"):
    up_to_version = None
    if(len(sys.argv) > 12):
        up_to_version = sys.argv[12]
    dbm_project.precheck_all_available_package_folders_one_by_one(up_to_version)
elif (dbm_project_action == "releaseSourceAll"):
    up_to_version = None
    if(len(sys.argv) > 12):
        up_to_version = sys.argv[12]
    dbm_project.upgrade_release_source_with_all_available_package_folders(up_to_version)
elif (dbm_project_action == "upgradeEnvToVersion"):
    env_name = sys.argv[12]
    dbm_environment = DBmEnvironment(env_name, dbm_project, dbm_agent)
    if(len(sys.argv) > 13):
        up_to_version = sys.argv[13]
        package_name = dbm_environment.get_version_package_name(up_to_version)
        if(package_name is not None):
            dbm_environment.upgrade(package_name)
        else:
            logging.error(f"No package found for version {up_to_version}")
    else:
        dbm_environment.upgrade_to_latest_available_package()
elif (dbm_project_action == "moveEnvToVersion"):
    env_name = sys.argv[12]
    dbm_environment = DBmEnvironment(env_name, dbm_project, dbm_agent)
    if(len(sys.argv) > 13):
        up_to_version = sys.argv[13]
        package_name = dbm_environment.get_version_package_name(up_to_version)
        if(package_name is not None):
            dbm_environment.move_to_package(package_name)
        else:
            logging.error(f"No package found for version {up_to_version}")
    else:
        dbm_environment.upgrade_to_latest_available_package()

"""
from DBmUtils import DBmUtils


root_folder = "versions"
package_folder = "V1.1__person"
path_to_scripts_folder = f"{root_folder}\\{package_folder}"

dbmaestro_agent_path = "C:\\Program Files (x86)\\DBmaestro\\DOP Server\\Agent\\DBmaestroAgent.jar"

x = DBmUtils(dbmaestro_agent_path)

"""
"""
x.createManifestFile(path_to_scripts_folder)

path = f"{root_folder}\\{package_folder}\\*"
CommonUtils.powershell("echo hola")
CommonUtils.zip(path,f"{package_folder}.zip")

from CommonUtils import CommonUtils
print(CommonUtils.find_version_folder("versions","1.1"))
"""