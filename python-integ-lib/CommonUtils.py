import os
import logging
import subprocess
import re
import glob
from packaging import version

class CommonUtils:
    def print(msg):
        print(f"DBmLibs > {msg}")

    def headline(msg):
        print("###########################################################################")
        print(f"  DBmLibs > {msg}")
        print("###########################################################################")
    
    def run(cmd):
        return subprocess.run(cmd, shell=True, check=True)

    def powershell(ps_cmd):
        return CommonUtils.run(f"powershell.exe -NonInteractive -ExecutionPolicy Bypass -Command \"$ErrorActionPreference='Stop';[Console]::OutputEncoding=[System.Text.Encoding]::UTF8;{ps_cmd};EXIT $global:LastExitCode\"")

    def zip(path, destination_path):
        # CommonUtils.print(f"Zipping package folder content ({path})")
        CommonUtils.powershell(f"Compress-Archive -Path {path} -DestinationPath {destination_path} -Force")

    def find_version(txt):
        # CommonUtils.print(f"Looking for a version in {txt}")
        x = re.search("(\d+\.)?(\d+\.)?(\d+\.)?(\d+)", txt)
        if x:
            return x.group()
        else:
            return None

    def find_specific_version(txt, version_searched):
        found_version = CommonUtils.find_version(txt)
        if found_version is not None and version_searched == found_version:
            # CommonUtils.print(f"Found specific version {version_searched}")
            return True
        return False

    def find_version_folder(root_folder, version_searched):
        version_folders = glob.glob(f"{root_folder}\\V{version_searched}*")
        for version_folder_path in version_folders:
            version_folder_name = os.path.basename(os.path.normpath(version_folder_path))
            version_found = CommonUtils.find_specific_version(version_folder_name, version_searched)
            if version_found:
                return version_folder_name
        return None

    def is_version_folder(folder_name):
        x = re.search("V(\d+\.)?(\d+\.)?(\d+\.)?(\d+)", folder_name)
        if x:
            return True
        else:
            return False

    def increment_version(version):
        incremented_version = None
        if version is not None:
            version_parts = version.split('.')
            number_of_parts = len(version_parts)
            if number_of_parts < 2:
                version_parts.append("0")
            if number_of_parts < 3:
                version_parts.append("0")
            if number_of_parts < 4:
                version_parts.append("1")
            else:
                version_parts[3] = str(int(version_parts[3]) + 1)
            incremented_version = '.'.join(version_parts)
        return incremented_version

    def get_version_folders(root_folder, greater_than = None):
        version_folders = list()
        for file in os.scandir(root_folder):
            if file.is_dir() and CommonUtils.is_version_folder(file.name):
                append = True
                if(greater_than is not None):
                    version_found = CommonUtils.find_version(file.name)
                    append = CommonUtils.is_version_greater_than(version_found, greater_than) 
                if(append):
                    version_folders.append(file.name)
        version_folders = sorted(version_folders, key=lambda version_folder_name: version.parse(CommonUtils.find_version(version_folder_name)))
        logging.info(f"Version Folders in '{root_folder}' folder greater than {greater_than}: {version_folders}")
        return version_folders

    def is_version_greater_than(my_version, greater_than):
        return version.parse(my_version) > version.parse(greater_than)

