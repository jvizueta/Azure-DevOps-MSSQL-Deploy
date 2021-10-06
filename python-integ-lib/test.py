import sys
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

'''
print(len(sys.argv))

if(len(sys.argv) > 1):
    print(sys.argv[1])
else:
    print("no args")
'''

#####################################
# PARAMETER START
#####################################

dbm_server_name = "t21-jc"
dbm_server_port = "8017"
dbm_server_use_ssl = "n"

dbm_user_auth_type = "DBmaestro Account"
dbm_user_username = "poc@dbmaestro.com"
dbm_user_password = "VmzU9NIDff1BALGXgsh58XXIg89FH7U5"

dbm_agent_path = "C:\\Program Files (x86)\\DBmaestro\\DOP Server\\Agent\\DBmaestroAgent.jar"

dbm_package_root_folder = "versions"

dbm_project_name = "MSSQL_P2"
dbm_project_rs_env_name = "RS"
# dbm_project_action = sys.argv[11]

#####################################
# PARAMETER END
#####################################

logging.basicConfig(encoding="utf-8", format='DBmLibs> %(asctime)s - %(levelname)s: %(message)s', level=logging.INFO)
logging.info("Parameters set")

dbm_server = DBmServer(dbm_server_name, dbm_server_port, dbm_server_use_ssl)
dbm_user = DBmUser(dbm_user_auth_type, dbm_user_username, dbm_user_password)
dbm_agent = DBmAgent(dbm_agent_path, dbm_server, dbm_user)

dbm_project = DBmProject(dbm_project_name, dbm_project_rs_env_name, dbm_agent, dbm_package_root_folder)

dbm_package = DBmPackage(dbm_project, dbm_agent, "V1.1__person", dbm_package_root_folder, "1.1", "adhoc")
dbm_package.create_manifest_file()