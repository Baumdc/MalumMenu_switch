import os
import requests
import zipfile
import shutil
import subprocess

# Function to get Among Us folder path
def get_among_us_folder():
    config_file = "among_us_path.txt"
    
    if os.path.exists(config_file):
        with open(config_file, "r") as file:
            among_us_path = file.read().strip()
    else:
        among_us_path = input("Please enter the Among Us folder path (e.g., D:\\SteamLibrary\\steamapps\\common\\Among Us): ").strip()
        with open(config_file, "w") as file:
            file.write(among_us_path)
    
    return among_us_path

# Function to move files and folders
def move_items(items, source, destination):
    for item in items:
        source_item = os.path.join(source, item)
        dest_item = os.path.join(destination, item)
        if os.path.exists(source_item):
            shutil.move(source_item, dest_item)

# Function to download and update the mod
def update_mod():
    among_us_path = get_among_us_folder()
    plugins_path = os.path.join(among_us_path, "BepInEx", "plugins")
    dll_destination_path = os.path.join(plugins_path, "MalumMenu.dll")

    # Download the ZIP file
    url = "https://github.com/scp222thj/MalumMenu/archive/refs/heads/main.zip"
    zip_path = "MalumMenu.zip"
    with requests.get(url, stream=True) as r:
        with open(zip_path, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    # Unzip the file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall("MalumMenu")

    # Build the project
    project_path = "MalumMenu/MalumMenu-main"
    subprocess.run(["dotnet", "build"], cwd=project_path, check=True)

    # Define DLL source path
    dll_source_path = os.path.join(project_path, "src", "bin", "Debug", "net6.0", "MalumMenu.dll")

    # Move the DLL file and overwrite the existing one
    shutil.copy(dll_source_path, dll_destination_path)

    # Clean up: remove the downloaded zip and the extracted folder
    os.remove(zip_path)
    shutil.rmtree("MalumMenu")

    print("Operation completed successfully.")

# Function to toggle mod on/off
def toggle_mod():
    among_us_folder = get_among_us_folder()
    backup_folder = os.path.join(among_us_folder, "mod_backup")
    
    mod_items = [
        "BepInEx",
        "dotnet",
        ".doorstop_version",
        "changelog.txt",
        "doorstop_config.ini",
        "steam_appid.txt",
        "winhttp.dll"
    ]
    
    if all(os.path.exists(os.path.join(among_us_folder, item)) for item in mod_items):
        # Mod is currently on, move items to backup folder
        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)
        move_items(mod_items, among_us_folder, backup_folder)
        print("Mod turned off and files moved to backup folder.")
    else:
        # Mod is currently off, move items back to Among Us folder
        if not os.path.exists(backup_folder):
            print("Backup folder does not exist. Nothing to restore.")
            return
        move_items(mod_items, backup_folder, among_us_folder)
        print("Mod turned on and files moved back to Among Us folder.")
        update_mod()

if __name__ == "__main__":
    toggle_mod()
