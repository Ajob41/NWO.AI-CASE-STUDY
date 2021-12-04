import gzip

path = "./Data/document.csv"

# check if file is compressed if not compress it print the file is compressed
if path.endswith(".gz"):
    print("File is already compressed")
else:
    with open(path, "rb") as f_in, gzip.open(path + ".gz", "wb") as f_out:
        f_out.writelines(f_in)
    print("File compressed")