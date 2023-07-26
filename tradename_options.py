with open("tradename.txt", "r") as file: 
    lines = file.read().split("\n")

    f = open("tradename_options.txt", "w")

    for line in lines:
        id_ = "\t" + "id: " + '"' + line + '",'
        label_ = "\t" + "label: " + '"' + line + '"'

        f.write("{" + "\n")
        f.write(id_ + "\n")
        f.write(label_ + "\n")
        f.write("}," + "\n")

    f.close()