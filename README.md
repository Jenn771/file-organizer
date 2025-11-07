# File Organizer

## Goal
Automatically sort files in a folder into subfolders based on their extensions.

## How it Works
1. Ask for a folder path (like `/Users/name/Downloads`)
2. List all files in the folder (`.iterdir()`)
3. Get each file's extension (`.suffix`)
4. Decide which folder it should go in
    - Create subfolders if they don't exist (`.mkdir()`)
5. Move the file to the correct folder (`.rename()`)
6. Unknown extensions are moved to the `Other` folder

## Features
- Handles Images, Documents, Videos, Music
- Moves unknown file types to `Other`
- Prevents overwriting by renaming duplicates
- Skips hidden files and the organizer script itself
