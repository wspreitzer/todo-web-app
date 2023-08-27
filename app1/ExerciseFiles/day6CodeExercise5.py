file = open(r"C:\Users\JPawl\Downloads\members.txt", "r")
members = file.readlines()
file.close()

member = input("Add a new Member: ") + "\n"
members.append(member)
file = open(r"C:\Users\JPawl\Downloads\members.txt", "w")
file.writelines(members)
file.close()
