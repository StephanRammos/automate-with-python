# backupToZip.py
# Backs up the entire 'automate-the-boring-stuff-with-python' folder into a zip file.
# Each backup is saved in D:\ with an incremented filename:
# e.g., 'automate-the-boring-stuff-with-python_1.zip', '..._2.zip', etc.

import zipfile, os

def backupToZip(folder, destDir):
    folder = os.path.abspath(folder)  # Absolute path to source folder
    destDir = os.path.abspath(destDir)  # Absolute path to destination directory

    # append date to end of filename
    baseName = os.path.basename(folder)
    while True:
        from datetime import datetime
        date_str = datetime.now().strftime('%Y-%m-%d')
        zipFilename = zipFilename = os.path.join(destDir, baseName + '_' + date_str + '.zip')
        if not os.path.exists(zipFilename):
            break
        

    # Create the zip file
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress files
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding folder: {foldername}')
        backupZip.write(foldername, os.path.relpath(foldername, folder))

        for filename in filenames:
            # Skip previously created backup zip files in source folder
            if filename.startswith(baseName + '_') and filename.endswith('.zip'):
                continue
            filePath = os.path.join(foldername, filename)
            arcname = os.path.relpath(filePath, folder)  # store relative path
            backupZip.write(filePath, arcname)
    backupZip.close()
    print('Backup complete.')

# Define source and destination
sourceFolder = 'C:\\Users\\user\\Desktop\\automate-the-boring-stuff-with-python'
destinationFolder = 'D:\\'

backupToZip(sourceFolder, destinationFolder)
