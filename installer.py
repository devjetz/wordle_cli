agreement_text = """
Hello, there!

THIS INSTALLER IS FOR WINDOWS ONLY. DO NOT TYPE 'y' IF YOU'RE ON ANYTHING ELSE THAN WINDOWS.

This is the installer of some of my projects. You do not need to accept this, or run this.
What this installer will do:
    - Create a folder called 'scripts_dev_signature_'
    - Create a folder inside the past one called 'pathers'
    - Add 'pathers' to PATH, which will allow you to run any exe in that file in CMD, just by typing the name
    - Move the downloaded .EXE or .PY to this folder

You do not need to agree to this, but it's highly recommended to get a true CLI feeling.

Thanks!



Do you allow this code to do as mentioned above?
"""
choice = input(f"{agreement_text}\n(y/n)\n~> ").lower()

if "y" in choice:
    choice = input(f"Double checking that you agree?\n (y/n)\n~> ").lower()
    if "y" in choice:
        print("Alright, installing now!\nDo not exit this program before it's finished.")
        import os, winreg, shutil

        # Folder to hold the exe
        folder = r"C:\scripts_dev_signature_\pathers"
        folder = os.path.expandvars(folder)

        # Create folder if it doesn't exist
        os.makedirs(folder, exist_ok=True)
        print(f"Creates {folder}...")

        # Current folder (where installer is)
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        # Move exe to the new folder
        shutil.copy(os.path.join(BASE_DIR, "wordle.exe"), folder)
        print(f"Moving wordle.exe to {folder}")


        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment", 0, winreg.KEY_READ) as k:
                try:
                    current_path = winreg.QueryValueEx(k, "Path")[0]
                except FileNotFoundError:
                    current_path = ""
        except PermissionError:
            print("Warning: Cannot read registry PATH. You may need to run this installer as Administrator.")
            current_path = ""

        # Now open for writing
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment", 0, winreg.KEY_WRITE) as k:
                if folder not in current_path.split(";"):
                    print("Folder not already in PATH.\nAdding folder to PATH..")
                    new_path = folder + ";" + current_path if current_path else folder
                    winreg.SetValueEx(k, "Path", 0, winreg.REG_EXPAND_SZ, new_path)
                    print("Added folder to path.")
                else:
                    print("Folder already in PATH.")
        except PermissionError:
            print("Warning: Cannot write to registry PATH. You may need to run this installer as Administrator.")

        print("Folder is now in PATH, and you can open any terminal and run 'wordle' to play wordle in your terminal!.")

choice = input(f"Thanks for installing!\n\nClick enter to exit this menu.")
