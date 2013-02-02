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
            
# print welcome message

print "Kindle Scraper 1.0. Copyright 2011 Shubhro Saha"

# load the file, and if not found, keep waiting.

foundKindle = False

try:
    f = open("/Volumes/Kindle/documents/My Clippings.txt", 'r')
    foundKindle = True
except:
    print "Kindle not detected. Please plug it in now."
    foundKindle = False

while (foundKindle == False):
    try:
        f = open("/Volumes/Kindle/documents/My Clippings.txt", 'r')
        foundKindle = True
    except:
        foundKindle = False
        
print "Kindle detected."

# split file into list of clippings' content and show how many found

clippingListChunks = f.read().split("==========")

print str(len(clippingListChunks)) + " clippings found."

# convert clipping chunks of content into list of Clipping objects

clippingList = []

del clippingListChunks[0]
del clippingListChunks[-1]

for c in clippingListChunks:
    clippingList.append(Clipping(c))
    
# identify all unique titles and give option to print their note contents by key

uniqueTitles = []

for c in clippingList:
    if c.title not in uniqueTitles:
        uniqueTitles.append(c.title)

i = 0
print "Please indicate the title you wish to retrieve highlights for."
for title in uniqueTitles:
    print "[" + str(i) + "] " + title
    i = i + 1
    
titleIndex = int(raw_input("Title Index #: "))
title = uniqueTitles[titleIndex]

# bring together all highlights for that title

output = ""

for c in clippingList:
    if (c.title == title):
        if (c.type == "Highlight"):
            #output = output + c.content + "\n\n"
            print c.content + "\n"
            
            
## write output to file
#
#f = open("output.txt", "w")
#f.write(output)
#
#print "All highlights have been written to file."
