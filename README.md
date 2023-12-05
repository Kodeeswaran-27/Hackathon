# Hackathon
For intel hackathon internal


        #For case File
    folder_path='./cases'
    loaders = [TextFileLoader(os.path.join(folder_path, fn)) for fn in os.listdir(folder_path) if fn.endswith('.txt')]
    documents = []  # Initialize an empty list to store all lines from all loaders

    for loader in loaders:
        loader.load_text()  # loading text
        loader.load_and_split()  # Split the loaded text
        documents.extend(loader.lines)  # Add lines to the documents list
