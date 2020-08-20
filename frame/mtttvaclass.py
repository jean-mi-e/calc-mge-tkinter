#!/usr/bin/env python3
# coding: utf-8
from tkinter import *
from tkinter.messagebox import *

class Classmtttva(Frame):

	"""Classe du tk.Entry Montant de la TVA"""

	def __init__(self, fenetre):
		super(Classmtttva, self).__init__()
		self.lab_mtttva = Label(fenetre, text = "Montant T.V.A. sur achats")
		self.lab_mtttva.place(x = 8, y = 60)
		self.var_mtttva = DoubleVar()
		self.mtttva = Entry(fenetre, textvariable = self.var_mtttva, width = 21)
		self.mtttva.place(x = 10, y = 80)
		
	def val_get(self):
		"""Méthode permettant de vérifier si l'entrée est numérique et de retourner
		un float"""
		
		try:
			float(self.mtttva.get())
		except ValueError:
			showerror("ERREUR", "Le Montant de la T.V.A n'est pas un nombre")
		
		if self.mtttva.get() == '':
			self.mtttva.insert(0, float(0))
			
		return float(self.mtttva.get())

	def lab_get(self):
		"""Méthode retournant le contenu du Label de la classe"""

		return self.lab_mtttva['text']

	def delete(self):
		"""Méthode effaçant le contenu de l'Entry de la classe"""

		return self.mtttva.delete(0,'end')

	def insert(self, arg1 ,arg2):
		"""Méthode permettant d'insérer un élément (arg2) dans l'Entry de la classe à partir d'une position (arg1)"""

		return self.mtttva.insert(arg1, arg2)

	def state(self, arg):
		"""Méthode permettant de définir l'état de l'Entry
		Normal -> saisie autorisée
		Disabled -> saisie bloquée"""
		
		try:
			assert arg == 'normal' or arg == 'disabled'
		except ValueError:
			pass
	
		self.mtttva['state'] = arg