#!/usr/bin/env python3
# coding: utf-8
from tkinter import *
from tkinter.messagebox import *

class Classpvttc(Frame):

	"""Classe du tk.Entry Prix de Vente TTC"""

	def __init__(self, fenetre):
		super(Classpvttc, self).__init__()
		self.lab_pvttc = Label(fenetre, text = "Prix de vente T.T.C.")
		self.lab_pvttc.place(x = 8, y = 110)
		self.var_pvttc = DoubleVar()
		self.pvttc = Entry(fenetre, textvariable = self.var_pvttc, width = 21)
		self.pvttc.place(x = 10, y = 130)
		
	def val_get(self):
		"""Méthode permettant de vérifier si l'entrée est numérique et de retourner
		un float"""
		
		try:
			float(self.pvttc.get())
		except ValueError:
			showerror("ERREUR", "Le Prix de Vente T.T.C n'est pas un nombre")

		if self.pvttc.get() == '':
			self.pvttc.insert(0, float(0))

		return float(self.pvttc.get())

	def lab_get(self):
		"""Méthode retournant le contenu du Label de la classe"""

		return self.lab_pvttc['text']

	def delete(self):
		"""Méthode effaçant le contenu de l'Entry de la classe"""

		return self.pvttc.delete(0,'end')

	def insert(self, arg1 ,arg2):
		"""Méthode permettant d'insérer un élément (arg2) dans l'Entry de la classe à partir d'une position (arg1)"""

		return self.pvttc.insert(arg1, arg2)

	def state(self, arg):
		"""Méthode permettant de définir l'état de l'Entry
		Normal -> saisie autorisée
		Disabled -> saisie bloquée"""
		
		try:
			assert arg == 'normal' or arg == 'disabled'
		except ValueError:
			pass
	
		self.pvttc['state'] = arg