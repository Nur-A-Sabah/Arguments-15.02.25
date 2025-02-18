import os 

shutdown = input("Do you want to shutdown your computer? (Yes/No): ")

if shutdown=="No":
    exit( )
    
else:
    os.system("shutdown /s /t 1")