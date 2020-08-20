#!/usr/bin/env python3
# coding: utf-8
from tkinter import *
from tkinter.messagebox import *

class Classpaht(Frame):

	"""Classe du tk.Entry Prix d'acht HT"""

	def __init__(self, fenetre):
		super(Classpaht, self).__init__()
		self.lab_paht = Label(fenetre, text = "Prix d'achat H.T.")
		self.lab_paht.place(x = 8, y = 10)
		self.var_paht = DoubleVar()
		self.paht = Entry(fenetre, textvariable = self.var_paht, width = 21)
		self.paht.place(x = 10, y = 30)
		
	def val_get(self):
		"""Méthode permettant de vérifier si l'entrée est numérique et de retourner
		un float"""
		
		try:
			float(self.paht.get())
		except ValueError:
			showerror("ERREUR", "Le PA H.T. n'est pas un nombre")

		if self.paht.get() == '':
			self.paht.insert(0, float(0))

		return float(self.paht.get())

	def lab_get(self):
		"""Méthode retournant le contenu du Label de la classe"""

		return self.lab_paht['text']

	def delete(self):
		"""Méthode effaçant le contenu de l'Entry de la classe"""

		return self.paht.delete(0,'end')

	def insert(self, arg1 ,arg2):
		"""Méthode permettant d'insérer un élément (arg2) dans l'Entry de la classe à partir d'une position (arg1)"""

		return self.paht.insert(arg1, arg2)

	def state(self, arg):
		"""Méthode permettant de définir l'état de l'Entry
		Normal -> saisie autorisée
		Disabled -> saisie bloquée"""
		
		try:
			assert arg == 'normal' or arg == 'disabled'
		except TypeError:
			pass
	
		self.paht['state'] = arg