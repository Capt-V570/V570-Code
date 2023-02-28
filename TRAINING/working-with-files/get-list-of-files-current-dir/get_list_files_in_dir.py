import os


total_bytes = 0

# Get a list of all files in the current directory
dir_list = os.listdir()
for entry in dir_list:
    # Make sure is a file!
    if os.path.isfile(entry):
        # Add file size to the total:
        file_size = os.path.getsize(entry)
        total_bytes += file_size

# Create a subdirectory called 'results':
os.mkdir("results")

# Create the output file:
results_file = open("results/results.txt", "w+")
if results_file.mode == "w+":
    results_file.write("Total bytecount:" + str(total_bytes) + "\n")
    results_file.write("Files list:\n")
    results_file.write("-------------\n")
    # Write the results into the 'results' file
    for entry in dir_list:
        if os.path.isfile(entry):
            # write the file name to the results ledger:
            results_file.write(entry + "\n")

    # Close the file when done:
    results_file.close()
