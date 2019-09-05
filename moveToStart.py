import os
import shutil
import sys

def moveFile(filePath):
	filename = filePath.split('\\')[-1]
	startPath = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp'
	file = startPath + "\\" + filename
	if os.path.isfile(filename):#判断要移动的是否是文件
		if os.path.exists(file):#判断目标路径内文件是否存在
			print(file)
			print('file is exists')
			while True:
				print('input "y" to remove  %s  move it, input "n" to exit program.' %filename)
				answer = input()
				if answer == 'y':
					os.remove(file)
					shutil.move(filePath,startPath)
					print('move sussessful')
					break
				elif answer =='n':
					print('exit successful')
					exit()
				else:
					print('input error')
					continue
		else:
			shutil.move(filePath,startPath)
	elif not os.path.exists(filename):
		print('file not exists')
	else:
		print('can not remove dir,please input bat file.')

def main():
	file = sys.argv[1]
	moveFile(file)

						
				
