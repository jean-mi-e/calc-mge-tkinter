#!/usr/bin/env python3
# coding: utf-8
from tkinter import *
from tkinter.messagebox import *

class Classpattc(Frame):

	"""Classe du tk.Entry Prix d'achat TTC"""

	def __init__(self, fenetre):
		super(Classpattc, self).__init__()
		self.lab_pattc = Label(fenetre, text = "Prix d'achat T.T.C.")
		self.lab_pattc.place(x = 198, y = 60)
		self.var_pattc = DoubleVar()
		self.pattc = Entry(fenetre, textvariable = self.var_pattc, width = 21)
		self.pattc.place(x = 200, y = 80)
		
	def val_get(self):
		"""Méthode permettant de vérifier si l'entrée est numérique et de retourner
		un float"""
		
		try:
			float(self.pattc.get())
		except ValueError:
			showerror("ERREUR", "Le Prix d'Achat T.T.C n'est pas un nombre")

		if self.pattc.get() == '':
			self.pattc.insert(0, float(0))

		return float(self.pattc.get())

	def lab_get(self):
		"""Méthode retournant le contenu du Label de la classe"""

		return self.lab_pattc['text']

	def delete(self):
		"""Méthode effaçant le contenu de l'Entry de la classe"""

		return self.pattc.delete(0,'end')

	def insert(self, arg1 ,arg2):
		"""Méthode permettant d'insérer un élément (arg2) dans l'Entry de la classe à partir d'une position (arg1)"""

		return self.pattc.insert(arg1, arg2)

	def state(self, arg):
		"""Méthode permettant de définir l'état de l'Entry
		Normal -> saisie autorisée
		Disabled -> saisie bloquée"""
		
		try:
			assert arg == 'normal' or arg == 'disabled'
		except ValueError:
			pass
	
		self.pattc['state'] = arg