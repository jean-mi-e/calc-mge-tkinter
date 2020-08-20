#!/usr/bin/env python3
# coding: utf-8
from tkinter import *
from tkinter.messagebox import *

class Classtxmge(Frame):

	"""Classe du tk.Entry Taux de marge"""

	def __init__(self, fenetre):
		super(Classtxmge, self).__init__()
		self.lab_txmge = Label(fenetre, text = "Taux de marge")
		self.lab_txmge.place(x = 198, y = 110)
		self.var_txmge = DoubleVar()
		self.txmge = Entry(fenetre, textvariable = self.var_txmge, width = 21)
		self.txmge.place(x = 200, y = 130)
		
	def val_get(self):
		"""Méthode permettant de vérifier si l'entrée est numérique et de retourner
		un float"""
		
		try:
			float(self.txmge.get())
		except ValueError:
			showerror("ERREUR", "Le Taux de Marge n'est pas un nombre")

		if self.txmge.get() == '':
			self.txmge.insert(0, float(0))
			
		return float(self.txmge.get())

	def lab_get(self):
		"""Méthode retournant le contenu du Label de la classe"""

		return self.lab_txmge['text']

	def delete(self):
		"""Méthode effaçant le contenu de l'Entry de la classe"""

		return self.txmge.delete(0,'end')

	def insert(self, arg1 ,arg2):
		"""Méthode permettant d'insérer un élément (arg2) dans l'Entry de la classe à partir d'une position (arg1)"""

		return self.txmge.insert(arg1, arg2)

	def state(self, arg):
		"""Méthode permettant de définir l'état de l'Entry
		Normal -> saisie autorisée
		Disabled -> saisie bloquée"""
		
		try:
			assert arg == 'normal' or arg == 'disabled'
		except ValueError:
			pass
	
		self.txmge['state'] = arg