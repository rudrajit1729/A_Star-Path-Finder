from tkinter import *
from tkinter import messagebox

def instruct():
	Tk().wm_withdraw()
	
	str = """
	Mouse Clicks:

	1st Left Click : Adds Start Node
	2nd Left Click : Adds End Node
	Remaining Left Clicks : Adds Barriers/Walls
	Right Clicks : Removes Nodes

	Note :
	If start/end erased 
	next left click(s) adds them back"""

	messagebox.showinfo('Instructions', (str))

	str = """
	Key Presses

	Space : Starts Algorithm
	(Start & End needed)

	c : Clears Map"""
	messagebox.showinfo('Instructions', (str))

