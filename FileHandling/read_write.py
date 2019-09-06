with open("file4.txt","r")as read_file:
    with open('file1.txt','w')as write_file:
        write_file.write(read_file.read())