from CommonUtils import CommonUtils
import logging

class DBmAgent:

    def __init__(self, agent_path):
        self.agent_path = agent_path

    def __init__(self, agent_path, dbm_server, dbm_user):
        self.agent_path = agent_path
        self.dbm_server = dbm_server
        self.dbm_user = dbm_user

    ######################################
    # AUTOMATION COMMANDS START
    ######################################

    def create_manifest_file(self, path_to_scripts_folder, operation = "CreateOrUpdate"):
        logging.info(f"\n")
        logging.info(f"CREATING package.json MANIFEST FILE FOR PACKAGE FOLDER '{path_to_scripts_folder}'")
        logging.info(f"CREATEMANIFESTFILE START")
        cmd = f"java -jar \"{self.agent_path}\" -CreateManifestFile -PathToScriptsFolder \"{path_to_scripts_folder}\" -Operation {operation}"
        logging.info(f"Cmd: {cmd}")
        CommonUtils.run(cmd)
        logging.info(f"CREATEMANIFESTFILE END\n")

    def get_env_packages(self, project_name, env_name, file_path):
        logging.info(f"\n")
        logging.info(f"GET PACKAGES OF '{project_name}/{env_name}' ENVIRONMENT AND PUT THEM IN FILE NAMED '{file_path}'")
        logging.info(f"GETENVPACKAGES START")
        cmd = f"java -jar \"{self.agent_path}\" -GetEnvPackages -ProjectName \"{project_name}\" -EnvName \"{env_name}\" -FilePath {file_path} -Server {self.dbm_server} -AuthType \"{self.dbm_user.auth_type}\" -UserName {self.dbm_user.username} -Password {self.dbm_user.password} -UseSSL {self.dbm_server.use_ssl}"
        logging.info(f"Cmd: {cmd}")
        CommonUtils.run(cmd)
        logging.info(f"GETENVPACKAGES END\n")

    def package(self, project_name, file_path):
        logging.info(f"\n")
        logging.info(f"PACKAGING FILE '{file_path}' INTO PROJECT '{project_name}'")
        logging.info(f"PACKAGE START")
        cmd = f"java -jar \"{self.agent_path}\" -Package -ProjectName \"{project_name}\" -FilePath {file_path} -Server {self.dbm_server} -AuthType \"{self.dbm_user.auth_type}\" -UserName {self.dbm_user.username} -Password {self.dbm_user.password} -UseSSL {self.dbm_server.use_ssl}"
        logging.info(f"Cmd: {cmd}")
        CommonUtils.run(cmd)
        logging.info(f"PACKAGE END\n")

    def precheck(self, project_name, package_name):
        logging.info(f"\n")
        logging.info(f"PRECHECK PACKAGE '{package_name}' IN '{project_name}' PROJECT")
        logging.info(f"PRECHECK START")
        cmd = f"java -jar \"{self.agent_path}\" -PreCheck -ProjectName \"{project_name}\" -PackageName {package_name} -Server {self.dbm_server} -AuthType \"{self.dbm_user.auth_type}\" -UserName {self.dbm_user.username} -Password {self.dbm_user.password} -UseSSL {self.dbm_server.use_ssl}"
        logging.info(f"Cmd: {cmd}")
        CommonUtils.run(cmd)
        logging.info(f"PRECHECK END\n")

    def upgrade(self, project_name, env_name, package_name):
        logging.info(f"\n")
        logging.info(f"UPGRADING '{project_name}/{env_name}' ENVIRONMENT TO PACKAGE '{package_name}'")
        logging.info(f"UPGRADE START")
        cmd = f"java -jar \"{self.agent_path}\" -Upgrade -ProjectName \"{project_name}\" -EnvName \"{env_name}\" -PackageName {package_name} -Server {self.dbm_server} -AuthType \"{self.dbm_user.auth_type}\" -UserName {self.dbm_user.username} -Password {self.dbm_user.password} -UseSSL {self.dbm_server.use_ssl}"
        logging.info(f"Cmd: {cmd}")
        CommonUtils.run(cmd)
        logging.info(f"UPGRADE END\n")

    def rollback(self, project_name, env_name, package_name):
        logging.info(f"\n")
        logging.info(f"ROLLING BACK '{project_name}/{env_name}' ENVIRONMENT TO PACKAGE '{package_name}'")
        logging.info(f"ROLLBACK START")
        cmd = f"java -jar \"{self.agent_path}\" -Rollback -ProjectName \"{project_name}\" -EnvName \"{env_name}\" -PackageName {package_name} -Server {self.dbm_server} -AuthType \"{self.dbm_user.auth_type}\" -UserName {self.dbm_user.username} -Password {self.dbm_user.password} -UseSSL {self.dbm_server.use_ssl}"
        logging.info(f"Cmd: {cmd}")
        CommonUtils.run(cmd)
        logging.info(f"ROLLBACK END\n")

    ######################################
    # AUTOMATION COMMANDS END
    ######################################
