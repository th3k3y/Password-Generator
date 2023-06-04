import random
import string
from PIL import ImageTk, Image
import customtkinter as ctk
import pyperclip 
from tkinter import messagebox 

lettres_majuscules = string.ascii_uppercase
lettres_minuscules = string.ascii_lowercase
chiffres = string.digits
symboles = string.punctuation

def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()

def generer_mot_de_passe():
    try:
        ensemble_caracteres = ""
        if majuscules_var.get() == "on":
            ensemble_caracteres += lettres_majuscules
        if minuscules_var.get() == "on":
            ensemble_caracteres += lettres_minuscules
        if chiffres_var.get() == "on":
            ensemble_caracteres += chiffres
        if symboles_var.get() == "on":
            ensemble_caracteres += symboles
        ensemble_caracteres += ensemble_caracteres_personnalise_var.get()

        if not ensemble_caracteres:
            raise ValueError("Aucun ensemble de caractères sélectionné. Veuillez cocher au moins une option ou fournir un ensemble de caractères personnalisé.")

        longueur = int(longueur_var.get())
        
        if longueur > 20:
            raise ValueError("La longueur maximale du mot de passe est de 20 caractères.")

        mot_de_passe = ''.join(random.choice(ensemble_caracteres) for _ in range(longueur))
        mot_de_passe_var.set(mot_de_passe)
        pyperclip.copy(mot_de_passe)  

        messagebox.showinfo("Succès", "Le mot de passe a été généré et copié sur le presse-papiers.")
    except ValueError as e:
        messagebox.showerror("Erreur", str(e))
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur inattendue est survenue: {str(e)}")

root = ctk.CTk()
root.geometry("550x550")
root.title("Générateur de mots de passe")

ctk.set_appearance_mode("dark")

image_logo = Image.open("logo.png")
image_logo = image_logo.resize((200, 200))

logo = ImageTk.PhotoImage(image_logo)

etiquette_logo = ctk.CTkLabel(root, image=logo, text="")
etiquette_logo.pack(pady=10)

cadre_cases_a_cocher = ctk.CTkFrame(root)
cadre_cases_a_cocher.pack(pady=10)

majuscules_var = ctk.StringVar()
case_a_cocher_majuscules = ctk.CTkCheckBox(cadre_cases_a_cocher, text="Lettres majuscules (A-Z)", variable=majuscules_var, onvalue="on", offvalue="off")
case_a_cocher_majuscules.grid(row=0, column=0, sticky="w")

minuscules_var = ctk.StringVar()
case_a_cocher_minuscules = ctk.CTkCheckBox(cadre_cases_a_cocher, text="Lettres minuscules (a-z)", variable=minuscules_var, onvalue="on", offvalue="off")
case_a_cocher_minuscules.grid(row=1, column=0, sticky="w")

chiffres_var = ctk.StringVar()
case_a_cocher_chiffres = ctk.CTkCheckBox(cadre_cases_a_cocher, text="Chiffres (0-9)", variable=chiffres_var, onvalue="on", offvalue="off")
case_a_cocher_chiffres.grid(row=2, column=0, sticky="w")

symboles_var = ctk.StringVar()
case_a_cocher_symboles = ctk.CTkCheckBox(cadre_cases_a_cocher, text="Symboles (!@#$%^&*)", variable=symboles_var, onvalue="on", offvalue="off")
case_a_cocher_symboles.grid(row=3, column=0, sticky="w")

longueur_var = ctk.StringVar()
etiquette_longueur = ctk.CTkLabel(root, text="Longueur minimale du mot de passe:")
etiquette_longueur.pack(pady=5, anchor="center")
entree_longueur = ctk.CTkEntry(root, textvariable=longueur_var)
entree_longueur.pack(pady=5, anchor="center")

ensemble_caracteres_personnalise_var = ctk.StringVar()
etiquette_ensemble_caracteres_personnalise = ctk.CTkLabel(root, text="Ensemble de caractères personnalisé:")
etiquette_ensemble_caracteres_personnalise.pack(pady=5, anchor="center")
entree_ensemble_caracteres_personnalise = ctk.CTkEntry(root, textvariable=ensemble_caracteres_personnalise_var)
entree_ensemble_caracteres_personnalise.pack(pady=5, anchor="center")

mot_de_passe_var = ctk.StringVar()
etiquette_mot_de_passe = ctk.CTkLabel(root, textvariable=mot_de_passe_var)
etiquette_mot_de_passe.pack(pady=10, anchor="center")

bouton_generer = ctk.CTkButton(root, text="Générer", command=generer_mot_de_passe)
bouton_generer.pack(pady=10, anchor="center")

root.mainloop()