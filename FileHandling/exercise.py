with open('file2.txt','r')as rf:
    with open('file1.txt','a')as af:
        for line in rf.readlines():
            name,salary = line.split(',')
            af.write(f"{name} 's  salary {salary}'")