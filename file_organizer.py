from pathlib import Path

class FileOrganizer:
    """ Organizes files in a folder into subfolders based on their extension."""
    
    def __init__(self, folder_path):
        self.folder_path = Path(folder_path)
        self.mapping = {
            "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
            "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
            "Videos": [".mp4", ".mov", ".avi"],
            "Music": [".mp3", ".wav", ".flac"]
        }

    def get_category(self, suffix):
        """ Return the category for a file extension or 'Other' if extension is unknown."""
        for category, extensions in self.mapping.items():
            if suffix.lower() in extensions:
                return category
            
        return 'Other'


    def organize(self):
        if not self.folder_path.exists():
            print("Path does not exist.")
            return
        
        for file in self.folder_path.iterdir():
            if file.is_file():
                
                # Skip the organizer script itself
                if file.name == Path(__file__).name:
                    continue

                # Skip hidden files
                if file.name.startswith("."):
                    continue

                category = self.get_category(file.suffix)
                full_path = self.folder_path / category
                full_path.mkdir(parents=False, exist_ok=True) # Create subfolder if it doesn't exist

                # Handle duplicate filenames
                destination = full_path / file.name
                if destination.exists():
                    destination = full_path / f"{file.stem}_1{file.suffix}"
                
                file.rename(destination)
                print(f"Moved {file.name} to {category}")

        return


folder_path = input("Enter folder path: ")
organizer = FileOrganizer(folder_path)
organizer.organize()
