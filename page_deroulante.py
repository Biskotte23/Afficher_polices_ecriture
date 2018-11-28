from tkinter import tix
from tkinter.constants import *
import sys
from tkinter import *
from tkinter.messagebox import *
import tkinter.font as tkFont

liste = ['System', 'Terminal', 'Fixedsys', 'Modern', 'Roman', 'Script', 'Courier', 'MS Serif', 'MS Sans Serif', 'Small Fonts','Marlett', 'Arial', 'Arabic Transparent', 'Arial Baltic', 'Arial CE', 'Arial CYR', 'Arial Greek', 'Arial TUR', 'Arial Black', 'Bahnschrift Light', 'Bahnschrift SemiLight', 'Bahnschrift', 'Bahnschrift SemiBold', 'Calibri', 'Calibri Light', 'Cambria', 'Cambria Math', 'Candara', 'Comic Sans MS', 'Consolas', 'Constantia', 'Corbel', 'Courier New', 'Courier New Baltic', 'Courier New CE', 'Courier New CYR', 'Courier New Greek', 'Courier New TUR', 'Ebrima', 'Franklin Gothic Medium', 'Gabriola', 'Gadugi', 'Georgia', 'Impact', 'Javanese Text', 'Leelawadee UI', 'Leelawadee UI Semilight', 'Lucida Console', 'Lucida Sans Unicode', 'Malgun Gothic', '@Malgun Gothic', 'Malgun Gothic Semilight', '@Malgun Gothic Semilight', 'Microsoft Himalaya', 'Microsoft JhengHei', '@Microsoft JhengHei', 'Microsoft JhengHei UI', '@Microsoft JhengHei UI', 'Microsoft JhengHei Light', '@Microsoft JhengHei Light', 'Microsoft JhengHei UI Light', '@Microsoft JhengHei UI Light', 'Microsoft New Tai Lue', 'Microsoft PhagsPa', 'Microsoft Sans Serif', 'Microsoft Tai Le', 'Microsoft YaHei', '@Microsoft YaHei', 'Microsoft YaHei UI', '@Microsoft YaHei UI', 'Microsoft YaHei Light', '@Microsoft YaHei Light', 'Microsoft YaHei UI Light', '@Microsoft YaHei UI Light', 'Microsoft Yi Baiti', 'MingLiU-ExtB', '@MingLiU-ExtB', 'PMingLiU-ExtB', '@PMingLiU-ExtB', 'MingLiU_HKSCS-ExtB', '@MingLiU_HKSCS-ExtB', 'Mongolian Baiti', 'MS Gothic', '@MS Gothic', 'MS UI Gothic', '@MS UI Gothic', 'MS PGothic', '@MS PGothic', 'MV Boli', 'Myanmar Text', 'Nirmala UI', 'Nirmala UI Semilight', 'Palatino Linotype', 'Segoe MDL2 Assets', 'Segoe Print', 'Segoe Script', 'Segoe UI', 'Segoe UI Black', 'Segoe UI Emoji', 'Segoe UI Historic', 'Segoe UI Light', 'Segoe UI Semibold', 'Segoe UI Semilight', 'Segoe UI Symbol', 'SimSun', '@SimSun', 'NSimSun', '@NSimSun', 'SimSun-ExtB', '@SimSun-ExtB', 'Sitka Small', 'Sitka Text', 'Sitka Subheading', 'Sitka Heading', 'Sitka Display', 'Sitka Banner', 'Sylfaen', 'Symbol', 'Tahoma', 'Times New Roman', 'Times New Roman Baltic', 'Times New Roman CE', 'Times New Roman CYR', 'Times New Roman Greek', 'Times New Roman TUR', 'Trebuchet MS', 'Verdana', 'Webdings', 'Wingdings', 'Yu Gothic', '@Yu Gothic', 'Yu Gothic UI', '@Yu Gothic UI', 'Yu Gothic UI Semibold', '@Yu Gothic UI Semibold', 'Yu Gothic Light', '@Yu Gothic Light', 'Yu Gothic UI Light', '@Yu Gothic UI Light', 'Yu Gothic Medium', '@Yu Gothic Medium', 'Yu Gothic UI Semilight', '@Yu Gothic UI Semilight', 'HoloLens MDL2 Assets', 'AR BERKLEY', 'AR BLANCA', 'AR BONNIE', 'AR CARTER', 'AR CENA', 'AR CHRISTY', 'AR DARLING', 'AR DECODE', 'AR DELANEY', 'AR DESTINE', 'AR ESSENCE', 'AR HERMANN', 'AR JULIAN', 'HP Simplified', 'HP Simplified Light', 'OpenSymbol', 'PT Serif', 'Source Sans Pro Black', 'Open Sans', 'DejaVu Math TeX Gyre', 'Gentium Basic', 'Liberation Mono', 'Liberation Sans Narrow', 'EmojiOne Color', 'Carlito', 'Linux Biolinum G', 'Source Code Pro Black', 'Caladea', 'DejaVu Sans', 'DejaVu Sans Light', 'DejaVu Sans Condensed', 'DejaVu Sans Mono', 'DejaVu Serif', 'DejaVu Serif Condensed', 'Gentium Book Basic', 'Liberation Sans', 'Liberation Serif', 'Linux Libertine Display G', 'Linux Libertine G', 'Source Code Pro', 'Source Code Pro ExtraLight', 'Source Code Pro Light', 'Source Code Pro Medium', 'Source Code Pro Semibold', 'Source Sans Pro', 'Source Sans Pro ExtraLight', 'Source Sans Pro Light', 'Source Sans Pro Semibold']

##def Affiche(evt):
##    print (varcombo.get()) # On affiche a l'ecran la valeur selectionnee



def police(emplacement):
    a = label.config(font = tkFont.Font(family = emplacement, size = 18))
    return a

def creation_polices():
    for i in range(192):
        emplacement = liste[i]
        combo.insert(i, liste[i]) # position dans la barre, nom affiché de la position
    combo.pack()

fenetre = tix.Tk()

contours = Label(fenetre, bg = "black")
contours.place(in_ = fenetre, x = 498, width = 604, y = 498, height = 204)


label = Label(fenetre, text = "Appercu de la police d'écriture", bg = "white", font = tkFont.Font(size = 18)) # Paramétrer le label (espace prévu pour écrire du texte) # bg (back ground) définit la couleur d'arrière plan
label.place(in_ = fenetre, x = 500, width = 600, y = 500, height = 200)

# creation fenetre deroulante
fenetre.tk.eval('package require Tix')
varcombo = tix.StringVar()
combo = tix.ComboBox(fenetre, editable = 1, dropdown = 1, variable = varcombo, command = police)
combo.entry.config(state='readonly')  # met la zone de texte en lecture seule

creation_polices()



fenetre.mainloop()
