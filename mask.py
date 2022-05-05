import os
print("I AM NOT RESPONSIBLE FOR ANY ILLEGAL USE!")
def Power():
    terminal = str(input("root@m0d10:~#"))
    if terminal == "boody":
        org_link = str(input("Enter Your Link Without The Protocol:\n  "))
        mask = str(input("Mask This:\n  "))
        mskd_link = mask + "@" + org_link
        print(mskd_link)
    elif terminal == "exit":
        exit()
    elif terminal == "clear":
        os.system("clear")
while True:
    Power()
