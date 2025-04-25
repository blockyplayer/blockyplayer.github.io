from pathlib import Path

# Specify the directory path
directory = "default_directory"

# Create the directory if it doesn't exist
path = Path(directory)
if not path.exists():
    path.mkdir(parents=True)
    print("")
    print("Directory created successfully!")
else:
    print("Directory already exists!")
    exit()

print("")
print("New root folder created! Available action key-words:")
print("")
print("         create <name>")
print("         open <path>")
print("         delete <path>")
print("         find <searchterm>")
print("")

action = input("Enter key-word action: ")
action = action.lower()
action = action.split()    