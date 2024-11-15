#Devloppeurs :
#HAKKACHE Haytam
#AIT ALLA Anass
#BENSIALI Mohammed
#TOURIRI Abdellatif

import io #fournit des fonctions pour travailler avec les flux d'entrée et de sortie
from tkinter import * # module tkinter, qui est une boîte à outils graphique standard en Python.
from tkinter import ttk,messagebox,colorchooser,filedialog,font
from PIL import ImageTk,Image #Python Imaging Library : converti format qui peut être utilisé par les widgets Tkinter,pour instancie classe Image
import tkinter as tk 

class Croquis:
    def __init__(self, root):
        #les parametres de fenetre
        self.fenetre = root 
        self.fenetre.title("DISSINATEUR")
        self.fenetre.geometry("1280x680+20+20")
        self.fenetre.resizable(width=False, height=False)
       
        # creer de canvas
        self.creer_canvas = Canvas(self.fenetre, width=1072, height=510, bg="white", relief=RIDGE, bd=0)
        self.creer_canvas.place(x=62, y=102) #placeer canvas dans la fenetre

        #Declarations des varaibles
        self.take = None                # v.i des objets
        self.option_menu = None         #vi menu option
        self.coord = None               #vi de label affiche pos de curseur
        self.status = None              #vi label  affiche titre des operation
        self.Ensemble_control = None    #vi label frame boite a outil
        # variable instance img
        self.line_img = None            # vi image l.continu
        self.das_img = None             #vi image l.descontinue
        self.pencil_img = None          
        self.circle_img = None          
        self.rectangle_img = None       
        self.eraser_img = None          #vi img gomme
        self.text_img = None            #vi img texte
        self.parallelogram_img = None   
        self.traingle_img = None        
        self.pentagon_img = None        
        self.hexagon_img = None         
        self.arrow_img = None           #vi img fleche verticale
        self.right_angled_traingle_img = None   #vi img triangle rectangle
        self.rounded_rec_img = None             #vi img rectangle arrondi
        self.arrow_left_img = None              #vi img fleche horiwontql
        
        self.eraser = None                  #vi btn supp
        self.top = None                     #vi forme pour creer le text
        self.eraser_controller = None       #vi scale taille de la gomme
        self.color_box = None               #vi coleur de bordure des forme a dessiner
        self.color_box_img = None           #vi img ''
        self.notation_box = None            #vi ou on met id des instance creer

        #Declarations des listes
        self.img_container = []         #vi stocker img a ouvrir
        self.undo_container = []        #liste des id objet dessiner
 
        self.menu_img_container = []    #liste img pour menu

        #Declaration des couleur d'objet
        self.fill_color = ""               #v pour couleur de remplissage des objei a dessiner
        self.outline_color_line = "black"       #v pour '' bordure des forme et ligne objet a dessiner
        self.color_container_box = "black"      #v pour stocker couleur recuperer de palette de couleur
        self.font_color="black"                 #couleur de police du texte

        #Initailisations des varaibles
        self.img_counter = -1                   #liste des image a ouvrir prevue liste des canvas
        self.width_controller_scale = 0         #vi scale  pour epaisseur de crayon
        self.width_maintainer = 1               #v stocker epaisseur crayon et autre objet a dessiner
        self.erase_width_maintainer = 1         # v epaisseur de la gome
        self.forme_obj="Crayon"                 #v stocker nom d objet a dessiner

        self.control(1)                         #initialiser control(1) cad crayon
        self.controller()                       #charger des graphique au demarrage
        self.make_menu()                        #creer mnu ''
        self.make_status_bar()                  #creer statrut ''
        self.width_controller()                 #definir epaisseur de la gomme
        self.color_set()                        #charger graphique de choix couleur bordure et le fond des objets a dessinés
        
        self.creer_canvas.bind('<Motion>', self.movement_cursor)
        
    #les bouton de controle
    def control(self, notation):
        self.creer_canvas.config(cursor="TCROSS")
    # supprimer la liaison du gestionnaire d'événements pour les événements sur un canevas
    # (certain evennemt seront toujour declancher donc les methode activer)
        self.creer_canvas.unbind("<B1-Motion>")
        self.creer_canvas.unbind("<ButtonRelease-1>")
        self.creer_canvas.unbind("<Button-1>")
# dessiner avec crayon
        if notation == 1:
            self.creer_canvas.bind("<Button-1>", self.position_depart)
            self.creer_canvas.bind("<B1-Motion>", self.crayon)
            self.creer_canvas.bind('<ButtonRelease-1>', lambda event: self.Calque_liste("Crayon"))
#circle
        elif notation == 2:
            self.creer_canvas.bind("<Button-1>", self.position_depart)
            self.creer_canvas.bind("<B1-Motion>", self.Tcircle)
            self.creer_canvas.bind('<ButtonRelease-1>', lambda event: self.Calque_liste("Circle"))
#rectangle
        elif notation == 3:
            self.creer_canvas.bind("<Button-1>", self.position_depart)
            self.creer_canvas.bind("<B1-Motion>", self.rectangle)
            self.creer_canvas.bind('<ButtonRelease-1>', lambda event: self.Calque_liste("Rectangle"))
#ligne continue
        elif notation == 4:
            self.creer_canvas.bind("<Button-1>", self.position_depart)
            self.creer_canvas.bind("<B1-Motion>", self.ligne_continue)
            self.creer_canvas.bind("<ButtonRelease-1>", lambda event: self.Calque_liste("L.Continue"))
#gomme
        elif notation == 5:
            self.creer_canvas.bind("<Button-1>", self.position_depart)
            self.creer_canvas.config(cursor="dotbox")
            self.creer_canvas.bind("<B1-Motion>", self.gomme_effacer)
#boite de texte
        elif notation == 6:
            self.Boite_dialogue_txt()
#triangle
        elif notation == 7:
            self.creer_canvas.bind("<Button-1>", self.position_depart)
            self.creer_canvas.bind('<B1-Motion>', self.traingle)
            self.creer_canvas.bind('<ButtonRelease-1>', lambda event: self.Calque_liste("Triangle"))
#//gramme
        elif notation == 8:
            self.creer_canvas.bind("<Button-1>", self.position_depart)
            self.creer_canvas.bind('<B1-Motion>', self.parallelogramme)
            self.creer_canvas.bind('<ButtonRelease-1>', lambda event: self.Calque_liste("//gramme"))
#pentagone
        elif notation == 9:
            self.creer_canvas.bind("<Button-1>", self.position_depart)
            self.creer_canvas.bind('<B1-Motion>', self.pentagon)
            self.creer_canvas.bind('<ButtonRelease-1>', lambda event: self.Calque_liste("Pentagone"))
#hexagon
        elif notation == 10:
            self.creer_canvas.bind("<Button-1>", self.position_depart)
            self.creer_canvas.bind('<B1-Motion>', self.hexagon)
            self.creer_canvas.bind('<ButtonRelease-1>', lambda event: self.Calque_liste("Hexagone"))
#fleche verticale
        elif notation == 11:
            self.creer_canvas.bind("<Button-1>", self.position_depart)
            self.creer_canvas.bind('<B1-Motion>', self.fleche_haut)
            self.creer_canvas.bind('<ButtonRelease-1>', lambda event: self.Calque_liste("F.Vertical"))
# ligne descontinue
        elif notation == 12:
            self.creer_canvas.bind("<Button-1>", self.position_depart)
            self.creer_canvas.bind('<B1-Motion>', self.ligne_discontinue)
            self.creer_canvas.bind("<ButtonRelease-1>", lambda event: self.Calque_liste("L.descontinue"))
#couleur de boudure des objet a dessiner
        elif notation == 14:
            
            self.status['text'] = "Choisir la couleur de Bordure a"
            self.color_container_box = colorchooser.askcolor()[1]
            self.outline_color_line = self.color_container_box
#fleche horizontal
        elif notation == 15:
            self.creer_canvas.bind("<Button-1>", self.position_depart)
            self.creer_canvas.bind('<B1-Motion>', self.fleche_horizontal)
            self.creer_canvas.bind("<ButtonRelease-1>", lambda event: self.Calque_liste("F.Horizontal"))
#rectangle avec arrondi des coin
        elif notation == 16:
            self.creer_canvas.bind("<Button-1>", self.position_depart)
            self.creer_canvas.bind('<B1-Motion>', self.rectangle_arrondi)
            self.creer_canvas.bind("<ButtonRelease-1>", lambda event: self.Calque_liste("Rect.Arr"))
#triangle rectangle
        elif notation == 17:
            self.creer_canvas.bind("<Button-1>", self.position_depart)
            self.creer_canvas.bind('<B1-Motion>', self.triagle_rectangle)
            self.creer_canvas.bind("<ButtonRelease-1>", lambda event: self.Calque_liste("Triangle.R"))
#menu ficheier ==>nouveau
        elif notation == 19:
            self.status["text"]="Nouveau Ficihier"
            self.creer_canvas.delete("all")
            # Videz la liste des calques
            self.notation_box.delete(0, tk.END)
            self.undo_container = []
#menu fichier ==> quitter
        elif notation == 20:
            take = messagebox.askyesno("Confirmation de quitter", "Étes vous sûr de quitter?")
            if take is True:
                self.fenetre.destroy()
#menu couleur (arriere plan)
        elif notation == 21:
            take = colorchooser.askcolor()[1]
            if take:
                self.creer_canvas['bg'] = take
                self.creer_canvas.update()

    # Boite des controles graphique +++++++++++++++++++++++++++++++++++++++++++++++++++
    def controller(self):
        #label de frame de boite a outil en haut ++++++++++++++++++++++++++++++++++++++
        self.Ensemble_control = LabelFrame(self.fenetre,text="Boite a outils",bg="#F5F6F7",fg="black",width=1100,height=100,relief=RAISED,bd=1, font=("Arial", 10, "bold"))
        self.Ensemble_control.place(x=60,y=0)
        
        #label de frame de bouton de dessin de forme geometrique++++++++++++++++++++++
        self.Forme_geometrique = LabelFrame(self.fenetre,text="Forme",bg="#F5F6F7",fg="black",width=60,height=625,relief=RAISED,bd=1, font=("Arial", 10, "bold"))
        self.Forme_geometrique.place(x=0,y=0)
        
        #label de frame controle liste pour index des objet ++++++++++++++++++++++++++
        self.list = LabelFrame(self.fenetre, text="Calques", bg="#F5F6F7", fg="black", width=145, height=625,
                               relief=RAISED, bd=2, font=("Arial", 10, "bold"))
        self.list.place(x=1140, y=0)
        
        #label de frame pour le bouton boite de dialogue texte++++++++++++++++++++++++
        self.text = LabelFrame(self.fenetre, text="Texte", bg="#F5F6F7", fg="black", width=50, height=60,
                                     relief=RAISED, bd=2, font=("Arial", 10, "bold"))
        self.text.place(x=580, y=20)
        # label de frame pour supprimer les objets++++++++++++++++++++++++
        self.supprimer = LabelFrame(self.fenetre, text="Supprimer", bg="#F5F6F7", fg="black", width=80, height=60,
                                    relief=RAISED, bd=2, font=("Arial", 10, "bold"))
        self.supprimer.place(x=940, y=20)
        # label de frame pour le zoom
        self.zoom = LabelFrame(self.fenetre, text="Zoom", bg="#F5F6F7", fg="black", width=100, height=60,
                                    relief=RAISED, bd=2, font=("Arial", 10, "bold"))
        self.zoom.place(x=810, y=20)
        # label de frame pour modifier
        self.modifier = LabelFrame(self.fenetre, text="Modifier", bg="#F5F6F7", fg="black", width=130, height=60,
                                    relief=RAISED, bd=2, font=("Arial", 10, "bold"))
        self.modifier.place(x=650, y=20)
        #controle liste box pour afficher les index des controle dessiner+++++++++++++
        self.notation_box = Listbox(self.list, selectmode=tk.EXTENDED , exportselection=False,width=16, height=600, font=("Arial", 10, "bold"), fg="blue",
                                    bg="#F5F6F7", relief=SUNKEN, bd=2)
        self.notation_box.place(x=8, y=5)
        
        #boutton de ligne continue lamda 4 +++++++++++++++++++++++++++++++++++++++++++
        self.line_img = ImageTk.PhotoImage(Image.open("Images/ligne.png").resize((20, 20), Image.BICUBIC))
        self.C_ligne = Button(self.Forme_geometrique, image=self.line_img, bg="#F5F6F7",
                                    font=("Arial", 10, "bold"), relief=RIDGE, bd=1, command=lambda: self.control(4))
        self.C_ligne.place(x=15, y=22)
        
        #boutton de ligne descontinue lambda 12 +++++++++++++++++++++++++++++++++++++++
        self.das_img = ImageTk.PhotoImage(Image.open("Images/dashed_line.png").resize((20, 20), Image.BICUBIC))
        self.D_ligne = Button(self.Forme_geometrique, image=self.das_img, bg="#F5F6F7",
                                      font=("Arial", 10, "bold"), relief=RAISED, bd=1, command=lambda: self.control(12))
        self.D_ligne.place(x=15, y=62)
        
        #bouton rectangle lambda 3 ++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.rectangle_img = ImageTk.PhotoImage(Image.open("Images/rectangle.png").resize((20, 20), Image.BICUBIC))
        self.Rectan = Button(self.Forme_geometrique, image=self.rectangle_img, bg="#F5F6F7", font=("Arial", 10, "bold"),relief=RAISED, bd=1, command=lambda: self.control(3))
        self.Rectan.place(x=15,y=107)
        
        #bouton // grame lambda 8 +++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.parallelogram_img = ImageTk.PhotoImage(Image.open("Images/parallelogram.png").resize((20, 20), Image.BICUBIC))
        self.parallelogram_btn = Button(self.Forme_geometrique, image=self.parallelogram_img, bg="#F5F6F7",
                                        font=("Arial", 10, "bold"), relief=RAISED, bd=1,
                                        command=lambda: self.control(8))
        self.parallelogram_btn.place(x=15, y=152)
        
        #bouton triangle lambda 7 +++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.traingle_img = ImageTk.PhotoImage(Image.open("Images/traingle.png").resize((20, 20), Image.BICUBIC))
        self.traingle_btn = Button(self.Forme_geometrique, image=self.traingle_img, bg="#F5F6F7",
                                   font=("Arial", 10, "bold"), relief=RAISED, bd=1, command=lambda: self.control(7))
        self.traingle_btn.place(x=15, y=202)
        
        #bouton pentagon lambda 9 +++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.pentagon_img = ImageTk.PhotoImage(Image.open("Images/pentagon.png").resize((20, 20), Image.BICUBIC))
        self.pentagon_btn = Button(self.Forme_geometrique, image=self.pentagon_img, bg="#F5F6F7",
                                   font=("Arial", 10, "bold"), relief=RAISED, bd=1, command=lambda: self.control(9))
        self.pentagon_btn.place(x=15, y=252)
        
        #bouton hexagon lambda 10 +++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.hexagon_img = ImageTk.PhotoImage(Image.open("Images/hexagon.png").resize((20, 20), Image.BICUBIC))
        self.hexagon_btn = Button(self.Forme_geometrique, image=self.hexagon_img, bg="#F5F6F7",
                                   font=("Arial", 10, "bold"), relief=RAISED, bd=1, command=lambda: self.control(10))
        self.hexagon_btn.place(x=15, y=302)
        
        #bouton fleche vertical lamda 11 ++++++++++++++++++++++++++++++++++++++++++++++
        self.arrow_img = ImageTk.PhotoImage(Image.open("Images/UParrow.png").resize((20, 20), Image.BICUBIC))
        self.f_vertical_btn = Button(self.Forme_geometrique, image=self.arrow_img,bg="#F5F6F7",
                                  font=("Arial", 10, "bold"), relief=RAISED, bd=1, command=lambda: self.control(11))
        self.f_vertical_btn.place(x=15, y=352)
        
        #bouton circle lambda 2 +++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.circle_img = ImageTk.PhotoImage(Image.open("Images/cercle.png").resize((20, 20), Image.BICUBIC))
        self.circle = Button(self.Forme_geometrique, image=self.circle_img, bg="#F5F6F7",
                             font=("Arial", 10, "bold"), relief=RAISED, bd=1, command=lambda: self.control(2))
        self.circle.place(x=15, y=402)
        
        #bouton triangle rectangle lambda 17 ++++++++++++++++++++++++++++++++++++++++++
        self.right_angled_traingle_img = ImageTk.PhotoImage(Image.open("Images/right_angled_traingle.png").resize((20, 20), Image.BICUBIC))
        self.triangle_rectan_btn = Button(self.Forme_geometrique, image=self.right_angled_traingle_img, bg="#F5F6F7",
                                      font=("Arial", 10, "bold"), relief=RAISED, bd=1, command=lambda: self.control(17))
        self.triangle_rectan_btn.place(x=15, y=452)
        
        #bouton rectangle arrondi lambda 16 +++++++++++++++++++++++++++++++++++++++++++
        self.rounded_rec_img = ImageTk.PhotoImage(Image.open("Images/rounded_rectangle.png").resize((20, 20), Image.BICUBIC))
        self.rounded_rectan_btn = Button(self.Forme_geometrique, image=self.rounded_rec_img, bg="#F5F6F7",
                                  font=("Arial", 10, "bold"), relief=RAISED, bd=1, command=lambda: self.control(16))
        self.rounded_rectan_btn.place(x=15, y=502)
        
        #bouton fleche horizontal lambda 15 +++++++++++++++++++++++++++++++++++++++++++
        self.arrow_left_img = ImageTk.PhotoImage(Image.open("Images/left-arrow.png").resize((20, 20), Image.BICUBIC))
        self.arr_left_btn = Button(self.Forme_geometrique, image=self.arrow_left_img, bg="#F5F6F7",
                              font=("Arial", 10, "bold"), relief=RAISED, bd=1, command=lambda: self.control(15))
        self.arr_left_btn.place(x=15, y=552)
        
        #bouton boite de dialogue pour creation de toexte lambda 6 ++++++++++++++++++++
        self.text_img = ImageTk.PhotoImage(Image.open("Images/text.png").resize((17, 17), Image.BICUBIC))
        self.text_btn = Button(self.text, image=self.text_img, bg="#F5F6F7",
                             font=("Arial", 10, "bold"), relief=RAISED, bd=1, command=lambda: self.control(6))
        self.text_btn.place(x=10, y=10)

        #label deframe de bouton crayon +++++++++++++++++++++++++++++++++++++++++++++++
        self.controller = LabelFrame(self.fenetre,text="Crayon",bg="#F5F6F7",fg="black",width=160,height=60,relief=RAISED,bd=2, font=("Arial", 10, "bold"))
        self.controller.place(x=90,y=20)
        #frame de bouton crayon +++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.frame = Frame(self.controller, relief=GROOVE, bd=0, width=10, height=10)
        self.frame.place(x=45, y=8)
        # frame de bouton supprimer +++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.sup_img = ImageTk.PhotoImage(Image.open("Images/supprimer.png").resize((17, 17), Image.BICUBIC))
        self.text_btn = Button(self.supprimer, image=self.sup_img, bg="#F5F6F7",
                               font=("Arial", 10, "bold"), relief=RAISED, bd=1,command=self.supprimer_forme_selectionnee)
        self.text_btn.place(x=10, y=10)
        #button zoom in
        self.zoom_in = ImageTk.PhotoImage(Image.open("Images/zoom_in_img.png").resize((20, 20), Image.BICUBIC))
        self.text_btn = Button(self.zoom, image=self.zoom_in, bg="#F5F6F7",
                               font=("Arial", 10, "bold"), relief=RAISED, bd=1,
                               command=lambda: self.zoom_controller(1))
        self.text_btn.place(x=10, y=10)
        #button zoom out
        self.zoom_out = ImageTk.PhotoImage(Image.open("Images/zoom_out_img.png").resize((20, 20), Image.BICUBIC))
        self.text_btn = Button(self.zoom, image=self.zoom_out, bg="#F5F6F7",
                               font=("Arial", 10, "bold"), relief=RAISED, bd=1,
                               command=lambda: self.zoom_controller(0))
        self.text_btn.place(x=50, y=10)
        # button pour modifier le fond
        self.modifier_fond = ImageTk.PhotoImage(Image.open("Images/mod_fond.png").resize((20, 20), Image.BICUBIC))
        self.text_btn = Button(self.modifier, image=self.modifier_fond, bg="#F5F6F7",
                               font=("Arial", 10, "bold"), relief=RAISED, bd=1,
                               command=self.changer_couleur_fond)
        self.text_btn.place(x=10, y=10)
        # button pour modifier la barre
        self.modifier_barre = ImageTk.PhotoImage(Image.open("Images/mod_barre.png").resize((20, 20), Image.BICUBIC))
        self.text_btn = Button(self.modifier, image=self.modifier_barre, bg="#F5F6F7",
                               font=("Arial", 10, "bold"), relief=RAISED, bd=1,
                               command=self.changer_couleur_barre)
        self.text_btn.place(x=50, y=10)

        #pour reinitialiser les couleur
        self.supprimer_couleur = ImageTk.PhotoImage(Image.open("Images/supb.png").resize((20, 20), Image.BICUBIC))
        self.fond_vid_btn = Button(self.modifier, image=self.supprimer_couleur, fg="red", bg="#F5F6F7",
                               font=("Arial", 10, "bold"), relief=RAISED, bd=1,command=self.renitialiser_couleur)
        self.fond_vid_btn.place(x=90, y=10)

        #Evenement de deplacement des objets par les fleches clavier
        self.fenetre.bind('<Left>', self.movement)
        self.fenetre.bind('<Right>', self.movement)
        self.fenetre.bind('<Up>', self.movement)
        self.fenetre.bind('<Down>', self.movement)
#epaisseur de crayon et gomme
    def width_controller(self):
        #Bouton pour crayon lambda 1 ----------------------------------------------------------
        self.pencil_img = ImageTk.PhotoImage(Image.open("Images/pencil.png").resize((17, 17), Image.BICUBIC))
        self.pencil = Button(self.controller, image=self.pencil_img, bg="#F5F6F7", fg="red",
                             font=("Arial", 10, "bold"), relief=RAISED, bd=1, command=lambda: self.control(1))
        self.pencil.place(x=10, y=10)
        #Epaisseur des foremes geometrique
        def Epaiss_Controle(valeur):
            
            self.width_maintainer = valeur
        # Epaisseur de gomme
        def Epaisseur_gomme(e):
            self.erase_width_maintainer = e
        #le controle scale du crayon -------------------------------------------------------------
        self.width_controller_scale = ttk.Scale(self.frame, orient=HORIZONTAL, from_=1, to=100,
                                                command=Epaiss_Controle)
        self.width_controller_scale.pack(pady=0)
        #label de frame de la gomme ---------------------------------------------------------------------------------
        self.controller1 = LabelFrame(self.fenetre, text="Gomme", bg="#F5F6F7", fg="black", width=160, height=60,
                                     relief=RAISED, bd=2, font=("Arial", 10, "bold"))
        self.controller1.place(x=280, y=20)
        #frame de la gomme -----------------------------------------------------------------------------------
        self.frame1 = Frame(self.controller1, relief=GROOVE, bd=0, width=10, height=10)
        self.frame1.place(x=45, y=8)
        #bouton de la gomme lambda 5 -------------------------------------------------------------------------
        self.eraser_img = ImageTk.PhotoImage(Image.open("Images/eraser.png").resize((17, 17), Image.BICUBIC))
        self.eraser = Button(self.controller1, image=self.eraser_img, fg="red", bg="#F5F6F7", font=("Arial", 10, "bold"),relief=RAISED, bd=1, command=lambda: self.control(5))
        self.eraser.place(x=10,y=10)
        #controle scale de la gomme--------------------------------------------------------------------------
        self.eraser_controller = ttk.Scale(self.frame1, orient=HORIZONTAL, from_=1, to=100,
                                           command=Epaisseur_gomme)
        self.eraser_controller.pack(pady=0)
    #couleur de la bordure et le fond des objets a dessinés
    def color_set(self):
        
        self.remplissage = LabelFrame(self.fenetre, text="Couleurs", bg="#F5F6F7", fg="black", width=90, height=60,
                                      relief=RAISED, bd=2, font=("Arial", 10, "bold"))
        self.remplissage.place(x=470, y=20)

        self.color_box_img = ImageTk.PhotoImage(Image.open("Images/palette.png").resize((20, 20), Image.BICUBIC))
        self.color_box = Button(self.remplissage,image=self.color_box_img, bg="#F5F6F7",
                                     font=("Arial", 10, "bold"), relief=RAISED, bd=1,
                                     command=lambda: self.control(14))
        self.color_box.place(x=50, y=10)

        self.ver_img = ImageTk.PhotoImage(Image.open("Images/verso.png").resize((20, 20), Image.BICUBIC))
        self.verso_text_btn = Button(self.remplissage, image=self.ver_img, fg="red", bg="#F5F6F7",
                                     font=("Arial", 10, "bold"), relief=RAISED, bd=1, command=lambda: self.activate_coloring(2))
        self.verso_text_btn.place(x=10, y=10)
#les menu
    def make_menu(self):
        self.my_menu = Menu(self.fenetre)
        self.fenetre.config(menu=self.my_menu)
        menu_img = ["new_img.png", "open_img.png", "save_img.png", "exit_img.png", "undo_img.png","clear_img.png", "cut_img.png", "copy_img.jpg", "paste_img.jpg","screenshot_img.jpg", "bgcolor_img.png", "fill_outline_img.png", "zoom_in_img.png", "zoom_out_img.png", "colorpen_img.png", "movement_img.png","about_img.jpg"]
        for i in range(17):
            self.menu_img_container.append(i)
            self.menu_img_container[i] = ImageTk.PhotoImage(
                Image.open("Images/" + menu_img[i]).resize((30, 30), Image.BICUBIC))
        #Menu Fichier
        self.file_menu = Menu(self.my_menu,tearoff=False)
        self.my_menu.add_cascade(label="Fichier",menu=self.file_menu)
        self.file_menu.add_command(label="Nouveau",accelerator="(Ctrl+N)",command=lambda: self.control(19),image=self.menu_img_container[0],compound=LEFT,background="#F5F6F7",foreground="blue",font=("Arial",10,"bold"))
        self.file_menu.add_command(label="Ouvrir",accelerator="(Ctrl+O)",command=lambda: self.open_file(False),image=self.menu_img_container[1],compound=LEFT,background="#F5F6F7",foreground="blue",font=("Arial",10,"bold"))
        self.file_menu.add_command(label="Enregistrer",accelerator="(Ctrl+S)",command=lambda: self.save_file(False) ,image=self.menu_img_container[2],compound=LEFT,background="#F5F6F7",foreground="blue",font=("Arial",10,"bold"))
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quitter",command=lambda: self.control(20),image=self.menu_img_container[3],compound=LEFT,background="#F5F6F7",foreground="blue",font=("Arial",10,"bold"))

        self.fenetre.bind('<Control-Key-n>', lambda e:self.control(19))
        self.fenetre.bind('<Control-Key-o>', self.open_file)
        self.fenetre.bind('<Control-Key-s>', self.save_file)

        #Menu couleur
        self.color_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Couleur", menu=self.color_menu)
        self.color_menu.add_command(label="Changer Couleur de l'arriere Plan",command=lambda: self.control(21),image=self.menu_img_container[10],compound=LEFT,background="#F5F6F7",foreground="blue",font=("Arial",10,"bold"),activebackground="blue",activeforeground="#F5F6F7")

        #Menu Option
        self.option_menu = Menu(self.my_menu,tearoff=False)
        self.my_menu.add_cascade(label="Option", menu=self.option_menu)
        self.option_menu.add_command(label="Zoom Arriere",accelerator="(Ctrl+Scroll up)",command=lambda: self.zoom_controller(0),image=self.menu_img_container[13],compound=LEFT,background="#F5F6F7",foreground="blue",font=("Arial",10,"bold"),activebackground="blue",activeforeground="#F5F6F7")
        self.option_menu.add_command(label="Zoom Avant", accelerator="(Ctrl+Scroll down)",command=lambda: self.zoom_controller(1),image=self.menu_img_container[12],compound=LEFT,background="#F5F6F7",foreground="blue",font=("Arial",10,"bold"),activebackground="blue",activeforeground="#F5F6F7")

       #Menu help
        self.help_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Aide", menu=self.help_menu)
        self.help_menu.add_command(label="A propos",command=self.about,image=self.menu_img_container[16],compound=LEFT,background="#F5F6F7",foreground="blue",font=("Arial",10,"bold"),activebackground="blue",activeforeground="#F5F6F7")
        self.help_menu.add_separator()
        self.help_menu.add_command(label="Astuce", command=self.tips, image=self.menu_img_container[16], compound=LEFT, background="#F5F6F7", foreground="blue", font=("Arial", 10, "bold"), activebackground="blue", activeforeground="#F5F6F7")
#position curseur en cour de mouvement
    def movement_cursor(self, e):
        self.coord.config(text=str(e.x) + "," + str(e.y) + "px")

#methode de creation de barre de statut pour afficher les nominations des operations et les cordonnees de crseur
    def make_status_bar(self):
        self.status_bar = LabelFrame(self.fenetre,bg="#C5CFDF",fg="black",width=1300,height=50,relief=RAISED, font=("Arial", 10, "bold"))
        self.status_bar.place(x=0,y=620)

        self.status = Label(self.status_bar, text="Dessiner ....",bg="#C5CFDF", fg="blue", font=("Arial", 12, "bold"))
        self.status.place(x=900, y=5)

        self.coord = Label(self.status_bar, text="",bg="#C5CFDF", fg="blue", font=("Arial", 9, "bold"))
        self.coord.place(x=20, y=5)

    # Ouvrire le fichier png existant
    def open_file(self,e):
        self.status["text"] = "Ouvrire Fichier"
        if self.notation_box['state'] == DISABLED:
            self.notation_box['state'] = NORMAL

        image_mine = filedialog.askopenfilename(initialdir="Saved_file", title="Selectioner une image",filetypes=(("PNG Images", "*.PNG"), ("JPG images", "*JPG")))

        if image_mine:
            self.img_container.append(ImageTk.PhotoImage(Image.open(image_mine)))
            self.img_counter+=1
            self.creer_canvas.create_image(540, 260, image=self.img_container[self.img_counter])
        self.notation_box.delete(0, tk.END)
        self.undo_container = []

#Enregister
    def save_file(self,e):
        try:
            self.status["text"] = "Enregistrer Fichier"
            file = filedialog.asksaveasfilename(initialdir="Saved_file",filetypes=[("PNG Images", "*.png")])
            if file:
                # Générer une représentation PostScript du canvas spécifique
                ps_data = self.creer_canvas.postscript(colormode="color", pagewidth=self.creer_canvas.winfo_reqwidth(), pageheight=self.creer_canvas.winfo_reqheight())
                # Convertir la représentation PostScript en image
                image = Image.open(io.BytesIO(ps_data.encode("utf-8")))
                # Enregistrer l'image en format PNG
                image.save(file + ".png")
        except:
            messagebox.showinfo('Dissinateur','Veuillez installer Ghostscript: https://ghostscript.com/releases/gsdnld.html')
#Zoom avant et arrier
    def zoom_controller(self,e):
        self.status['text'] = "Zoom Controller"
        if e == 1:
                self.creer_canvas.scale("all", 550, 350, 1.1, 1.1)
        else:
                self.creer_canvas.scale("all", 550, 350, 0.9, 0.9)

#=======================================================================
#Effacer aver la gomme
    def gomme_effacer(self,e):
        self.status['text'] = "Effacer avec la gomme"
        self.creer_canvas.create_rectangle(self.Start_X,self.Start_Y,e.x,e.y,width=self.erase_width_maintainer,fill="white",outline="white")
#=======================================================================
#Forme de dessin du texte a inserer
    def Boite_dialogue_txt(self):
        self.status['text'] = "Taper votre texte"
        self.top = Toplevel()
        self.top.grab_set()
        self.top.title("Taper le Texte")
        self.top.geometry("400x500")
        self.top.wm_iconbitmap("images/main_logo.ico")
        
        canvas_frame = ttk.Frame(self.top)
        canvas_frame.pack(pady=10)

        self.canvas = tk.Canvas(canvas_frame, width=400, height=200, bg="white")
        self.canvas.pack()

        # creer Label par défaut sur le canvas
        self.text_aff = self.canvas.create_text(200, 50, text="Votre Texte Ici!", font=("Arial", 12), tags="draggable")
                
        # Ajouter une zone de Text sur le canvas
        self.entry = tk.Entry(self.canvas, font=("Arial", 12))
        self.entry_window = self.canvas.create_window(200, 150, window=self.entry, anchor="center")
               
        # Frame pour les options de texte
        options_frame = ttk.Frame(self.top)
        options_frame.pack(pady=10)

        # Bouton pour choisir la couleur du texte
        color_button = ttk.Button(options_frame, text="Couleur du Texte", command=self.Choisir_couleur_texte)
        color_button.grid(row=0, column=1, padx=5)

        # Combobox pour choisir la police
        font_label = ttk.Label(options_frame, text="Police:")
        font_label.grid(row=1, column=1, padx=5, pady=5, sticky="W")
        self.font_var = tk.StringVar()
        font_combobox = ttk.Combobox(options_frame, textvariable=self.font_var, values=font.families())
        font_combobox.grid(row=2, column=1, padx=5, pady=5, sticky="W")
        font_combobox.bind("<<ComboboxSelected>>", self.update_police_taille)
       
        # Scale pour choisir la taille de la police
        size_label = ttk.Label(options_frame, text="Taille:")
        size_label.grid(row=3, column=1, padx=5, pady=5, sticky="W")
        self.size_var = tk.StringVar(value="12")
        size_scale = ttk.Scale(options_frame, from_=8, to=72, variable=self.size_var, orient="horizontal")
        size_scale.grid(row=4, column=1, padx=5, pady=5, sticky="W")
        size_scale.bind("<B1-Motion>", self.update_police_taille)

        # Bouton pour mettre à jour le texte depuis la zone de saisie
        update_text_button = ttk.Button(options_frame, text="Acceptée", command=self.Ajouter_Texte)
        update_text_button.grid(row=5, column=1, columnspan=2, pady=5)
        self.entry.bind("<KeyRelease>", self.on_saisie_clavier) 
    
    def on_saisie_clavier(self,e):
        self.canvas.itemconfig(self.text_aff, text=self.entry.get())
    
    def Choisir_couleur_texte(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.canvas.itemconfig(self.text_aff, fill=color)
            self.font_color=color


    def renitialiser_couleur(self):
        try:
            self.fill_color=""
            index_selectionne = self.notation_box.curselection()[0]
            self.creer_canvas.itemconfig(self.undo_container[index_selectionne], fill=self.fill_color)
            self.status['text'] = "Couleur de fond changée"
        except:
            messagebox.showinfo("Attention", "Veuillez selectioner un element de la liste")
    def update_police_taille(self, event=None):
        selected_font = self.font_var.get()
        selected_size = int(float(self.size_var.get()))
        
        self.canvas.itemconfig(self.text_aff, font=(selected_font, selected_size))

    def Ajouter_Texte(self):
        police =self.font_var.get()
        taille =int(float(self.size_var.get()))
        self.take=self.creer_canvas.create_text(300, 300, text=self.entry.get(), font=(police , taille), fill=self.font_color, tags="draggable") 
        self.Calque_liste('Texte')
        self.top.destroy()
        
#======================================================================
#definir position de depart
    def position_depart(self,e):
        self.Start_X = e.x
        self.Start_Y = e.y  
        
#======================================================================
#Ajouter a la liste des calque    
    def Calque_liste(self,forme_obj):
       
        self.undo_container.append(self.take)
        self.notation_box.insert(END,(len(self.undo_container) - 1,":",forme_obj))
        self.take = None  

#======================================================================        
#tracer avec crayon
    def crayon(self,e):
        self.status['text'] = "Dessiner avec crayon"
        self.take =self.creer_canvas.create_line(self.Start_X,self.Start_Y,e.x,e.y,fill=self.outline_color_line,
                                            width=self.width_maintainer,smooth=True,capstyle=ROUND)
        self.Start_X = e.x
        self.Start_Y = e.y
        
#======================================================================
# Tracer Circle
    def Tcircle(self,e):
        self.status['text'] = "Tracer circle"
        if self.take:
            self.creer_canvas.delete(self.take)
        self.take = self.creer_canvas.create_oval(self.Start_X, self.Start_Y, e.x, e.y, width=self.width_maintainer,outline=self.outline_color_line,fill=self.fill_color)
        
#======================================================================
#tracer le rectangle
    def rectangle(self,e):
        self.status['text'] = "Tracer rectangle"
        if self.take:
            self.creer_canvas.delete(self.take)
        self.take = self.creer_canvas.create_rectangle(self.Start_X, self.Start_Y, e.x, e.y, width=self.width_maintainer,fill=self.fill_color,outline=self.outline_color_line)

#======================================================================
# Tracer la ligne continue
    def ligne_continue(self,e):
        self.status['text'] = "Tracer ligne Continue"
        if self.take:
            self.creer_canvas.delete(self.take)
        self.take = self.creer_canvas.create_line(self.Start_X, self.Start_Y, e.x, e.y, width=self.width_maintainer, fill=self.outline_color_line)

#=======================================================================
    def ligne_discontinue(self,e):
        self.status['text'] = "Tracer ligne discontinue"
        if self.take:
            self.creer_canvas.delete(self.take)
        self.take = self.creer_canvas.create_line(self.Start_X, self.Start_Y, e.x, e.y, width=self.width_maintainer, fill=self.outline_color_line, dash=(10,1))
       
#=======================================================================
    def traingle(self, e):
        self.status['text'] = "Tracer triangle"
        if self.take:
            self.creer_canvas.delete(self.take)        
        self.take = self.creer_canvas.create_polygon(self.Start_X, self.Start_Y, self.Start_X-(e.x-self.Start_X), e.y, e.x, e.y,width=self.width_maintainer,fill=self.fill_color,outline=self.outline_color_line)

#=======================================================================
#creer parallelogramme      
    def parallelogramme(self, e):
        self.status['text'] = "Tracer Parallélogramme"
        if self.take:
            self.creer_canvas.delete(self.take)
        points = [self.Start_X,self.Start_Y,int(self.Start_X)+30,e.y,e.x,e.y,int(e.x)-30,self.Start_Y]
        self.take = self.creer_canvas.create_polygon(points,width=self.width_maintainer, fill=self.fill_color,outline=self.outline_color_line)

#=======================================================================
# tracer le pentagon 
    def pentagon(self, e):
        
        self.status['text'] = "Dessiner pentagon"
        if self.take:
            self.creer_canvas.delete(self.take)
        points = [self.Start_X, self.Start_Y, self.Start_X, e.y, e.x, e.y, int(e.x), self.Start_Y,
                          (self.Start_X + e.x) / 2, self.Start_Y - 20]
        self.take = self.creer_canvas.create_polygon(points, width=self.width_maintainer, fill=self.fill_color,
                                                       outline=self.outline_color_line)

#=======================================================================
#tracer hexagon
    def hexagon(self, e):
        self.status['text'] = "Dessiner Hexagone"
        if self.take:
            self.creer_canvas.delete(self.take)
        points = [self.Start_X, self.Start_Y, int(self.Start_X), e.y, (int(self.Start_X)+int(e.x))/2, int(e.y)+50, e.x, e.y, int(e.x), self.Start_Y, (self.Start_X+e.x)/2,self.Start_Y-50]
        self.take = self.creer_canvas.create_polygon(points,width=self.width_maintainer, fill=self.fill_color,outline=self.outline_color_line)

#=======================================================================
#Dessiner fleche verticale 
    def fleche_haut(self, e):
        self.status['text'] = "Dessiner fleche vers le haut"
        if self.take:
            self.creer_canvas.delete(self.take)
        points = [self.Start_X, self.Start_Y, (int(self.Start_X)+int(self.Start_X+e.x)/2)/2, self.Start_Y, (int(self.Start_X)+int(self.Start_X+e.x)/2)/2, int(e.y), ((int(self.Start_X+e.x)/2)+int(e.x))/2, e.y, ((int(self.Start_X+e.x)/2)+int(e.x))/2,self.Start_Y,  int(e.x),self.Start_Y,  int(self.Start_X+e.x)/2, self.Start_Y+(int((self.Start_Y-e.y))/2)]
        self.take = self.creer_canvas.create_polygon(points,width=self.width_maintainer, fill=self.fill_color,outline=self.outline_color_line)

#=======================================================================
#Dessiner fleche horizontale
    def fleche_horizontal(self,e):
        self.status['text'] = "Dessiner fleche horizontal"
        if self.take:
            self.creer_canvas.delete(self.take)
        m = (self.Start_X + e.x)/2
        points = [self.Start_X, self.Start_Y, int(m), self.Start_Y+20, int(m), self.Start_Y+10, e.x, int(self.Start_Y)+10, e.x, int(self.Start_Y)-10, int(m), int(self.Start_Y)-10, int(m), int(self.Start_Y)-20]
        self.take = self.creer_canvas.create_polygon(points,width=self.width_maintainer, fill=self.fill_color,outline=self.outline_color_line)

#trace triangle rectangle
    def triagle_rectangle(self,e):
        self.status['text'] = "Dessiner triangle rectangle"
        if self.take:
           self.creer_canvas.delete(self.take) 
        points = [self.Start_X,self.Start_Y, self.Start_X,e.y, e.x,e.y]
        self.take = self.creer_canvas.create_polygon(points,width=self.width_maintainer, fill=self.fill_color,outline=self.outline_color_line)

#======================================================================
#Tracer rectangle avec les coins arrondi
    def rectangle_arrondi(self,e):
        self.status['text'] = "Dessiner rectangle avec coin arrondi"
        if self.take:
            self.creer_canvas.delete(self.take)
        points = [self.Start_X,self.Start_Y, int(self.Start_X)+3,int(self.Start_Y)-5, int(self.Start_X)+7,int(self.Start_Y)-7, int(self.Start_X)+11,int(self.Start_Y)-9, int(self.Start_X)+13,int(self.Start_Y)-9, e.x,int(self.Start_Y)-9, int(e.x)+5,int(self.Start_Y)-7, int(e.x)+8,int(self.Start_Y)-5, int(e.x)+11,self.Start_Y, int(e.x)+11,e.y, int(e.x)+8,int(e.y)+5, int(e.x)+5,int(e.y)+7, e.x,int(e.y)+8, int(self.Start_X)+13,int(e.y)+8, int(self.Start_X)+11,int(e.y)+7, int(self.Start_X)+7,int(e.y)+5, int(self.Start_X)+3,int(e.y)+3, int(self.Start_X),int(e.y)-2]
        self.take = self.creer_canvas.create_polygon(points,width=self.width_maintainer, fill=self.fill_color,outline=self.outline_color_line)

#=======================================================================
#Mouvement des objets par fleches de clavier
    def movement(self,e):
        self.creer_canvas.focus_set()
        try:
            self.status['text'] = "Movement"
            take = self.notation_box.get(ACTIVE)
            take = self.undo_container[take[0]]

            if e.keycode == 37:

                if type(take) == list:
                    for x in take:
                        self.creer_canvas.move(x, -8, 0)
                else:
                    self.creer_canvas.move(take, -8, 0)
            if e.keycode == 38:

                if type(take) == list:
                    for x in take:
                        self.creer_canvas.move(x, 0, -8)
                else:
                    self.creer_canvas.move(take, 0, -8)
            if e.keycode == 39:

                if type(take) == list:
                    for x in take:
                        self.creer_canvas.move(x, 8, 0)
                else:
                    self.creer_canvas.move(take, 8, 0)
            if e.keycode == 40:

                if type(take) == list:
                    for x in take:
                        self.creer_canvas.move(x, 0, 8)
                else:
                    self.creer_canvas.move(take, 0, 8)

        except:
            messagebox.showinfo("Attention", "Veuillez selectioner un element de la liste")

#couleur de remplissage des objets
    def activate_coloring(self,notation):
        if notation != 1 :
            self.fill_color = colorchooser.askcolor()[1]

    def about(self):
        top = Toplevel()
        top.title("A propos")
        top.geometry("800x620")
        top.wm_iconbitmap("images/main_logo.ico")
        top.config(bg="white")
        self.image = ImageTk.PhotoImage(Image.open("Images/propos.jpeg").resize((800,600), Image.BICUBIC))
        tip_label = Label(top, image=self.image, relief=RAISED, bd=0)
        tip_label.place(x=0, y=0)

#Modifier la couleur des objets deja dessiner
    def changer_couleur_fond(self, event=None):
        try:
            # Obtenez l'index de la forme sélectionnée dans le calque
            index_selectionne = self.notation_box.curselection()[0]

            # Appelez la méthode activate_coloring pour obtenir la nouvelle couleur de fond
            self.activate_coloring(2)

            # Changez la couleur de fond de la forme sélectionnée dans le canevas
            self.creer_canvas.itemconfig(self.undo_container[index_selectionne], fill=self.fill_color)

            self.status['text'] = "Couleur de fond changée"
            #self.status.place(x=1180, y=685)
        except IndexError:
            messagebox.showwarning("Sélection requise",
                                   "Veuillez sélectionner une forme dans le calque pour changer la couleur de fond.")

# Modifier la couleur des barres d'objets deja dessiner
    def changer_couleur_barre(self, event=None):
        try:
            # Obtenez l'index de la barre sélectionnée dans le calque
            index_selectionne = self.notation_box.curselection()[0]

            # Appelez la méthode activate_coloring pour obtenir la nouvelle couleur de la barre
            self.activate_coloring(2)

            # Changez la couleur de la barre sélectionnée dans le canevas (utilisez la propriété outline)
            self.creer_canvas.itemconfig(self.undo_container[index_selectionne], outline=self.fill_color)

            self.status['text'] = "Couleur de la barre changée"
            self.status.place(x=1180, y=685)
        except IndexError:
            messagebox.showwarning("Sélection requise",
                                   "Veuillez sélectionner une barre dans le calque pour changer la couleur.")

    def supprimer_forme_selectionnee(self, event=None):
        selection = self.notation_box.curselection()
        if selection:
            index_a_supprimer = selection[0]
            self.notation_box.delete(index_a_supprimer)  # Supprime l'élément de la Listbox
            # Supprimer la forme correspondante dans le canevas
            if index_a_supprimer < len(self.undo_container):
                forme_a_supprimer = self.undo_container[index_a_supprimer]
                self.creer_canvas.delete(forme_a_supprimer)  # Supprime la forme du canevas
                del self.undo_container[index_a_supprimer]  # Supprime l'élément de la liste
        else:
            messagebox.showwarning('Dessinateur', 'Selectionner un element de la liste')
    def tips(self):
        top = Toplevel()
        top.title("Astuce")
        top.geometry("800x620")
        top.wm_iconbitmap("images/main_logo.ico")
        top.config(bg="white")
        self.image = ImageTk.PhotoImage(Image.open("Images/astuce.png").resize((800,600), Image.BICUBIC))
        tip_label = Label(top, image=self.image, relief=RAISED, bd=0)
        tip_label.place(x=0, y=0)

if __name__ == '__main__':
    fenetre = Tk()
    fenetre.wm_iconbitmap("images/main_logo.ico")
    fenetre.config(bg="#C5CFDF")
    Croquis(fenetre)
    fenetre.mainloop()
