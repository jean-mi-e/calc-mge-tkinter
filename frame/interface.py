#!/usr/bin/env python3
# coding: utf-8
import tkinter
from tkinter import *
from tkinter.messagebox import showerror, showwarning
import frame.fonctionscalculs as fc
import frame.mttmgeclass as seven
import frame.mtttvaclass as three
import frame.pahtclass as one
import frame.pattcclass as four
import frame.pvttcclass as five
import frame.txmgeclass as six
import frame.txtvaclass as two


# from operator import itemgetter => a servi pendant le développement, conservé au cas où besoin dans future mise à jour

class Interface(Frame):
    """Notre fenêtre principale qui hérite de Frame

    Les éléments principaux sont stockés comme attributs de cette fenêtre

    Les widgets sont créés par une méthode de classe lors de l'initialisation"""

    def __init__(self, fenetre):
        Frame.__init__(self, fenetre)
        self.fenetre = fenetre
        self.fenetre.title('Calculatrice de marge')
        self.fenetre.geometry("350x310")
        self.fenetre.resizable(width=False, height=False)
        self._centrefenetre(self.fenetre)
        self.pack()
        self._create_widgets()

    def _geoliste(self, g):
        """Méthode qui prend la chaine LxH+X+Y de la fenêtre en paramètre
        et qui renvoie la liste des 4 valeurs converties en entier"""

        r = [i for i in range(0, len(g)) if not g[i].isdigit()]
        return [int(g[0:r[0]]), int(g[r[0] + 1:r[1]]), int(g[r[1] + 1:r[2]]), int(g[r[2] + 1:])]

    def _centrefenetre(self, fen):
        """Méthode permettant de centrer la fenêtre à l'écran"""

        fen.update_idletasks()
        l, h, x, y = self._geoliste(fen.geometry())
        fen.geometry("%dx%d%+d%+d" % (l, h, (fen.winfo_screenwidth() - l) // 2, (fen.winfo_screenheight() - h) // 2))

    def _create_widgets(self):
        # Méthode de mise en place des widgets

        # Instanciation des widgets à partir des différentes classes
        self.list_inst_wid = [one.Classpaht(self.fenetre), two.Classtxtva(self.fenetre),
                              three.Classmtttva(self.fenetre), four.Classpattc(self.fenetre),
                              five.Classpvttc(self.fenetre), six.Classtxmge(self.fenetre),
                              seven.Classmttmge(self.fenetre)]
        self.listwidgets = []

        for wid in self.list_inst_wid:
            self.listwidgets.append(wid)

        # Création de listes des libellés et entry instanciés
        self.list_labels = [self.listwidgets[0].lab_get(), self.listwidgets[1].lab_get(),
                            self.listwidgets[2].lab_get(), self.listwidgets[3].lab_get(),
                            self.listwidgets[4].lab_get(), self.listwidgets[5].lab_get(),
                            self.listwidgets[6].lab_get()]
        self.list_entry = [self.listwidgets[0], self.listwidgets[2], self.listwidgets[3],
                           self.listwidgets[4], self.listwidgets[5], self.listwidgets[6]]

        # Les boutons ne sont pas des classes -> choix personnel, changera peut-être en cas de développement futur
        self.bouton_raz = Button(self.fenetre, text="Remise à zéro", command=self._raz, width=19, height=2,
                                 activebackground='White')
        self.bouton_raz.place(x=175, y=250)

        self.bouton_quitter = Button(self.fenetre, text="Quitter", command=self.fenetre.destroy, width=19, height=2,
                                     activebackground='White')
        self.bouton_quitter.place(x=25, y=250)

        self.bouton_calcul = Button(self.fenetre, text="Calcul", fg="red", command=self._cliquer, width=19, height=2,
                                    activebackground='White')
        self.bouton_calcul.place(x=100, y=200)

        # Gestion des évènements en passant par des lambda pour éviter de créer plusieurs méthodes d'une seule ligne
        self.fenetre.bind('<Return>', lambda e: self._cliquer())
        self.fenetre.bind('<KP_Enter>', lambda e: self._cliquer())  # pour la touche entrée du pavé numérique sous linux
        self.fenetre.bind('<Escape>', lambda e: self.fenetre.destroy())

    def _cliquer(self):
        """Il y a eu un clic sur le bouton Calcul.
        
        On lance les contrôles et calculs pour trouver les résultats souhaités."""

        if self._ctrl_nb_data():
            showwarning("ERREUR", "Vous devez renseigner au minimum 3 données \n pour avoir un maximum de résultats",
                        parent=self.fenetre)

        # On récupère dans une liste les clés du dictionnaire dont les entry ne sont ni vides ni à 0 val_entered =
        # itemgetter(*[idx for idx,e in enumerate(list(self.mondico.values())) if e != '0.0' and e != ''])(list(
        # self.mondico.keys())) inutile ici, je l'ai gardé pour référence future

        self.list_var = self._recup_val()

        # On crée une liste des calculs à réaliser
        self.list_calculs = [fc.calc_paht(*self.list_var), fc.calc_txtva(*self.list_var),
                             fc.calc_mtttva(*self.list_var), fc.calc_pattc(*self.list_var),
                             fc.calc_pvttc(*self.list_var), fc.calc_txmge(*self.list_var),
                             fc.calc_mttmge(*self.list_var)]

        # On crée une liste vide pour insérer les résultats
        self.list_resultats = []

        # On effectue les calculs et on les places dans la liste de résultats
        for calc in self.list_calculs:
            self.list_resultats.append(calc)

        # Contrôles de cohérence
        if self.list_resultats[1] == 'Inconnu' or self.list_resultats[1] == float(0):
            control = round(self.list_resultats[4] - self.list_resultats[0], 2)
        else:
            control = round(self.list_resultats[4] / (1 + (self.list_resultats[1] / 100)) - self.list_resultats[0], 2)

        if control != self.list_resultats[6]:
            showerror("ERREUR",
                      "Les données saisies contiennent une anomalie et/ou ne suffisent pas à calculer un résultat "
                      "juste.")

        # mise à jour des Entry
        idx = 0
        for elt in self.list_entry:
            elt.delete()
            if idx == 1:  # On saute le résultat txtva car il fonctionne différement des autres (OptionMenu pas Entry)
                idx = 2
            elt.insert(0, self.list_resultats[idx])
            idx += 1

        self.listwidgets[1].insert(self.list_resultats[1])

        # Mise en state='disabled' les widgets pour figer les résultats
        for elt in self.listwidgets:
            elt.state('disabled')

    def _recup_val(self):
        """Affectation des valeurs saisies dans les entry à une liste."""

        list_val = []
        for elt in self.listwidgets:
            list_val.append(elt.val_get())

        return list_val

    def _ctrl_nb_data(self):
        """Méthode vérifiant qu'au moins 3 données ont été renseignées pour les calculs"""

        idx = 0
        list_control = list(self._recup_val())
        del list_control[1]
        for elt in list_control:
            if str(elt) != '0.0' and str(elt) != '':
                idx += 1

        if self.listwidgets[1].val_get() != 'Inconnu':
            idx += 1

        if idx < 3:
            return True
        else:
            return False

    def _modifier(self):
        """Méthode débloquant les widgets pour pouvoir modifier les données"""

        for elt in self.listwidgets:
            elt.state('normal')

    def _raz(self):
        """Méthode remettant tous les Widgets de saisie en mode initial"""

        for elt in self.listwidgets:
            elt.state('normal')
            elt.delete()

        for elt in self.list_entry:
            elt.insert(0, 0.0)


if __name__ == "__main__":
    root = tkinter.Tk()
    app = Interface(root)
    app.mainloop()
