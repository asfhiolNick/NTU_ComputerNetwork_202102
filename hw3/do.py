import os
os.system("ls")
for i in range(0,100):
    cmd = f"python3 sp.py test_case/{i}.txt > nick/{i}.txt"
    print(i)
    os.popen(cmd)

