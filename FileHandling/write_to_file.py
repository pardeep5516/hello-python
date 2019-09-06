

with open('file4.txt','r+') as f:
    f.seek(len(f.read()))
    f.write("hello alice")