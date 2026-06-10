# Open source file in read mode
source = open("source.txt", "r")

# Read entire content
data = source.read()

# Open destination file in write mode
destination = open("destination.txt", "w")

# Write content to destination file
destination.write(data)

# Close both files
source.close()
destination.close()

print("File copied successfully!")