#!/usr/bin/env python3
# coding: utf-8
from tkinter import *
from tkinter.messagebox import showerror

class Classmttmge(Frame):

	"""Classe du tk.Entry Montant de la marge"""

	def __init__(self, fenetre):
		super(Classmttmge, self).__init__()
		self.lab_mttmge = Label(fenetre, text = "Montant de la marge")
		self.lab_mttmge.place(x = 98, y = 150)
		self.var_mttmge = DoubleVar()
		self.mttmge = Entry(fenetre, textvariable = self.var_mttmge, width = 21)
		self.mttmge.place(x = 100, y = 170)
		
	def val_get(self):
		"""Méthode permettant de vérifier si l'entrée est numérique et de retourner
		un float"""

		try:
			float(self.mttmge.get())
		except ValueError:
			showerror("ERREUR", "Le Montant de la marge n'est pas un nombre")
		
		if self.mttmge.get() == '':
			self.mttmge.insert(0, float(0))
			
		return float(self.mttmge.get())

	def lab_get(self):
		"""Méthode retournant le contenu du Label de la classe"""

		return self.lab_mttmge['text']

	def delete(self):
		"""Méthode effaçant le contenu de l'Entry de la classe"""

		return self.mttmge.delete(0,'end')

	def insert(self, arg1 ,arg2):
		"""Méthode permettant d'insérer un élément (arg2) dans l'Entry de la classe à partir d'une position (arg1)"""

		return self.mttmge.insert(arg1, arg2)

	def state(self, arg):
		"""Méthode permettant de définir l'état de l'Entry
		Normal -> saisie autorisée
		Disabled -> saisie bloquée"""
		
		try:
			assert arg == 'normal' or arg == 'disabled'
		except ValueError:
			pass
	
		self.mttmge['state'] = arg