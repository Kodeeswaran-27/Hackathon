# Hackathon
For intel hackathon internal
    for loader in loaders:
        loader.load_text()  # loading text
        loader.load_and_split()  # Split the loaded text
        documents.extend(loader.lines)  # Add lines to the documents list
