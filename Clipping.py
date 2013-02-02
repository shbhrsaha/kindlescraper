class Clipping:
    
    type = ""
    title = ""
    page = 0
    location = 0
    dateTimeAdded = ""
    content = ""
    
    def __init__(self, chunk):
        chunkLines = chunk.split('\n')
        secondLine = chunkLines[2].strip()
        secondLineSplit = secondLine.split(" ")
        
        #title
        self.title = chunkLines[1].strip()
        
        #type
        self.type = secondLineSplit[1]
        
        #page
        self.page = secondLineSplit[4]
        
        #location
        self.location = secondLineSplit[7]
        
        # date & time
        self.dateTimeAdded = secondLine.split("Added on ")[-1]
        
        if (self.type != "Bookmark"):
            self.content = chunkLines[-2]
            