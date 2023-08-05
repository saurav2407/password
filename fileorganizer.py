from tkinter import *
from tkinter import filedialog
import os
import shutil


class GUI(Tk):
	def __init__(self):
		super().__init__()
		self.geometry('500x500')

	def gettingPath(self):
		self.path = filedialog.askdirectory()
		return self.path

	def startButton(self, path_value):
		self.button_Frame = Frame(self)
		self.button_Frame.pack()
		self.start_Button = Button(self.button_Frame, text='Start', command=lambda: self.startOperation(
			path_value)).grid(row=0, column=0)

	def startOperation(self, path_value):
		count = 0
		os.chdir(path_value)
		self.file_list = os.listdir()
		no_of_files = len(self.file_list)
		if len(self.file_list) == 0:
			self.error_label = Label(text="Error empty folder").pack()
			exit()
		for file in self.file_list:
			if file.endswith(".png"):
				self.dir_name = "PngFiles"
				self.new_path = os.path.join(path_value, self.dir_name)
				self.file_list = os.listdir()
				if self.dir_name not in self.file_list:
					os.mkdir(self.new_path)
				shutil.move(file, self.new_path)

			elif file.endswith(".txt"):
				self.dir_name = "TextFiles"
				self.new_path = os.path.join(path_value, self.dir_name)
				self.file_list = os.listdir()
				if self.dir_name not in self.file_list:
					os.mkdir(self.new_path)
				shutil.move(file, self.new_path)
			count = count+1

		if(count == no_of_files):
			success = Label(text="Operation Successful!").pack()
		else:
			error = Label(text="Failed").pack()


if __name__ == '__main__':
	object = GUI()
	path = object.gettingPath()
	object.startButton(path)
	object.mainloop()
