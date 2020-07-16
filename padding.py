from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
import datetime

if __name__ == "__main__":
	x = datetime.datetime.now()
	date = x.strftime("%d%m%y_%H%M_")
	desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
	outpt = desktop + '\\' + date + 'Journalisation.txt'
	Tk().withdraw()
	filename = askopenfilename()
	print("le résultat de l'opération sera dans le fichier : " + outpt)
	with open(filename) as file:
		f = open(outpt, 'w+')
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
	print("[Opération terminée]")
	f.close
	file.close
	if os.name == 'nt':
		os.system("pause")
