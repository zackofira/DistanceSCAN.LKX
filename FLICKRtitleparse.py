
# Import the libraries
import time
import xml.etree.ElementTree as ET
# Save time
start = time.time()

#Set this to wherever the file is located on your machine
tree = ET.parse('D:\\flickrXml\\photosPASCAL.xml')
root = tree.getroot()

#allparsed.txt can be replaced with whatever you want the name of the file to be
File_object = open(r"titles.txt", "w+", encoding="utf-8")
tempString = ""

# 10188 total things in the photosPASCAL file
for x in range(10188):
    #change the number after root[x][ to get different information
    #0 for image owners, 1 for image titles, 2 for descriptions, 3 for visibility, 4 for dates
    #5 for editability, 6 for publiceditability, 7 for usage, 8 for comments, 9 for notes, 10 for tags
    #11 for urls, 12 for groups, 13 for galleries, 14 for labels, 15 for comments again?
    tempString = (f"{root[x][1].text}\n")
    (File_object.write(tempString))

#end file writing
File_object.close()

#Calculate and display run time
end = time.time()
length = end - start
print(length, "seconds",sep=" ")