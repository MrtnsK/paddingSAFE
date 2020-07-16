from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

if __name__ == "__main__":
	
	Tk().withdraw()
	filename = askopenfilename()
	with open(filename) as file:
		f = open("./rendu.txt", 'w+')
		tmp = file.readline()
		while (tmp):
			array = tmp.split()
			if (len(array) == 5):
				tmpline = array[0] + "        " + array[1] + "                      " + array[2] + "      " + array[3]
				nbr = array[4].rjust(21, ' ')
				f.writelines(tmpline + nbr + '\n')
			if (len(array) == 4):
				tmpline = array[0] + "                                  " + array[1] + "      " + array[2]
				nbr = array[3].rjust(21, ' ')
				f.writelines(tmpline + nbr + '\n')
			tmp = file.readline()
	f.close
	file.close
	if os.name == 'nt':
		os.system("pause")
