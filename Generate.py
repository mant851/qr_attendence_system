from MyQR import myqr
import os

f = open(r'C:\Users\manth\Downloads\DE II-B\QR_Attendance-main\QR_Attendance\students.txt','r')
lines = f.read().split("\n")
print(lines)

for _ in range (0,len(lines)):
    data = lines[_]
    version,level,qr = myqr.run(
        words=str(data),
        level='H',
        version=1,
        contrast=1.0,
        brightness=1.0,
        save_name = str(lines[_]+'.png'),
        picture='C:\\Users\manth\Downloads\DE II-B\QR_Attendance-main\QR_Attendance\pic.jpg',
        save_dir=os.getcwd()
    )