#!/usr/bin/env python3
# coding: utf-8
from tkinter import *
from tkinter.messagebox import showerror


class Classtxtva(Frame):
	"""Classe du tk.Entry Taux de la TVA"""

	def __init__(self, fenetre):
		super(Classtxtva, self).__init__()
		self.lab_txtva = Label(fenetre, text="Taux de T.V.A.")
		self.lab_txtva.place(x=200, y=10)
		self.listTaux = ["20 %", "10 %", "5,50 %", "2,10 %", "0 %", "Inconnu"]
		self.var_txtva = StringVar()
		self.var_txtva.set(self.listTaux[0])
		self.txtva = OptionMenu(fenetre, self.var_txtva, *self.listTaux)
		self.txtva.place(x=200, y=30)

	def val_get(self):
		"""Méthode permettant de vérifier si l'entrée est numérique et de retourner un float"""

		if self.var_txtva.get() == self.listTaux[5]:
			txselec = self.listTaux[5]
		else:
			txselec = self.var_txtva.get()
			txselec = txselec[:-2]
			if txselec == '5,50':
				txselec = 5.5
			elif txselec == '2,10':
				txselec = 2.1
			txselec = float(txselec)

		return txselec

	def lab_get(self):
		"""Méthode retournant le contenu du Label de la classe"""

		return self.lab_txtva['text']

	def delete(self):
		"""Méthode effaçant le contenu de l'Entry de la classe"""

		return self.var_txtva.set(self.listTaux[0])

	def insert(self, arg):
		"""Méthode permettant de définir le taux de TVA dans l'OptionMenu"""

		val_arg = {float(20): '0', float(10): '1', 5.5: '2', 2.1: '3', float(0): '4', "Inconnu": 5}
		if arg in val_arg.keys():
			arg = val_arg[arg]
			return self.var_txtva.set(self.listTaux[int(arg)])
		else:
			showerror("ERREUR", f"Vous avez du faire une erreur de saisie \n Le Taux de TVA {arg:.2f}% n'existe pas.")
			return self.var_txtva.set(arg)

	def state(self, arg):
		"""Méthode permettant de définir l'état de l'Entry
		Normal -> saisie autorisée
		Disabled -> saisie bloquée"""

		try:
			assert arg == 'normal' or arg == 'disabled'
		except ValueError:
			pass

		self.txtva['state'] = arg
