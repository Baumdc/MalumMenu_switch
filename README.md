# Among Us Mod Toggle Script

This Python script allows you to easily toggle a mod on and off for the game Among Us by moving mod-related files and folders to and from a backup directory.

## Features

- Automatically detects the Among Us installation folder.
- Moves mod-related files to a backup folder to turn the mod off.
- Restores mod-related files from the backup folder to turn the mod on.
- Optionally downloads and updates the mod code from GitHub.

## Requirements

- [Python 3](https://www.python.org/downloads/)
- [NET SDK](dotnet.microsoft.com/download) (required only for the script that updates the mod)

## Usage

### Option 1: Script Without Auto Update

1. Clone the repository or download the script `toggle_among_us_mod.py`.
2. Ensure you have Python installed on your system.
3. Run the script using the following command or run `run.bat`:

    ```bash
    python toggle_among_us_mod.py
    ```

4. When running the script for the first time, you will be prompted to enter the path to your Among Us installation folder (e.g., `D:\\SteamLibrary\\steamapps\\common\\Among Us`). This path will be saved in a configuration file (`among_us_path.txt`) for future use.

### Option 2: Script With Auto Update

1. Clone the repository or download the script `toggle_among_us_mod_with_update.py`.
2. Ensure you have Python and .NET SDK installed on your system.
3. Run the script using the following command or run `run+update.bat`:

    ```bash
    python toggle_among_us_mod_with_update.py
    ```

4. When running the script for the first time, you will be prompted to enter the path to your Among Us installation folder (e.g., `D:\\SteamLibrary\\steamapps\\common\\Among Us`). This path will be saved in a configuration file (`among_us_path.txt`) for future use.

## How It Works

- The script checks if the following mod-related items are present in the Among Us folder:
  - `BepInEx` (folder)
  - `dotnet` (folder)
  - `.doorstop_version`
  - `changelog.txt`
  - `doorstop_config.ini`
  - `steam_appid.txt`
  - `winhttp.dll`

- If these items are found, the script moves them to a backup folder (`mod_backup`) within the Among Us folder and prints a message indicating the mod has been turned off.

- If these items are not found, the script attempts to move them back from the backup folder to the Among Us folder and prints a message indicating the mod has been turned on. If the backup folder does not exist, an error message is printed.

### Script With Auto Update (`toggle_among_us_mod_with_update.py`)

- The script performs the same steps as the script without auto update to toggle the mod on or off.
- After restoring the mod files, the script downloads the latest version of the mod from GitHub, builds it using .NET SDK, and moves the updated DLL file to the `BepInEx/plugins` folder.


## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This script is provided as-is and is not affiliated with or endorsed by the developers of Among Us.

