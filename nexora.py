from PySide6.QtWidgets import *
import smtplib
from email.message  import EmailMessage
import random
import os


from dotenv import load_dotenv
load_dotenv()

mon_mot_de_passe = os.getenv("MOT_DE_PASSE_NEXORA")
email = os.getenv("EMAIL_NEXORA")
app = QApplication([])
fenetre = QWidget()
layout = QVBoxLayout()
fenetre.resize(600,600)
fenetre.setWindowTitle("Page De Connexion")
titre = QLabel(" 🔐 CONNEXION ")
bienvenue = QLabel("Bienvenue !    ")
email = QLabel("📧 Email")
champ_email = QLineEdit()
champ_email.setPlaceholderText("Veuillez Entrez Votre Email")
mot_de_passe = QLabel("🔑 Mot de passe  ")
champ_mot_de_passe = QLineEdit()
champ_mot_de_passe.setPlaceholderText("Veuillez Entrez Votre Mot De Passe")
champ_mot_de_passe.setEchoMode(QLineEdit.Password)
se_connecter = QPushButton("Se Connecter")
bouton_verifier = QPushButton("Verifier")
bouton_verifier.hide()
label_code = QLabel("Veuillez Entrez Le Code ")
entry_code = QLineEdit()
label_code.hide()
entry_code.hide()
nombre = None
def connexion():
    global nombre
    nombre = random.randint(100000,999999)
    email_message = EmailMessage()
    email_message["From"] = email
    email_message["To"] = champ_email.text()
    email_message["Subject"] = "Code de vérification – Connexion à votre compte"
    email_message.set_content(f"""Bonjour,

Une tentative de connexion à votre compte a été effectuée.

Votre code de vérification est :

{nombre}

Ce code est valable pendant quelques minutes.

Si vous n'êtes pas à l'origine de cette tentative de connexion, vous pouvez ignorer cet e-mail.

Cordialement,

L'équipe de Nexora""")
    serveur = smtplib.SMTP("smtp.gmail.com",587)
    serveur.starttls()
    serveur.login(email,mon_mot_de_passe)
    serveur.send_message(email_message)
    serveur.quit()
    label_code.show()
    entry_code.show()
    bouton_verifier.show()

def cacher_widget():
    titre.hide()
    bienvenue.hide()
    email.hide()
    champ_email.hide()
    mot_de_passe.hide()
    champ_mot_de_passe.hide()
    se_connecter.hide()
    bouton_verifier.hide()
    label_code.hide()
    entry_code.hide()

def afficher_widget():
    titre.show()
    bienvenue.show()
    email.show()
    champ_email.show()
    mot_de_passe.show()
    champ_mot_de_passe.show()
    se_connecter.show()
    bouton_verifier.show()
    label_code.show()
    entry_code.show()

def afficher_widget_2():
    titre.show()
    bienvenue.show()
    email.show()
    champ_email.show()
    mot_de_passe.show()
    champ_mot_de_passe.show()
    se_connecter.show()
    
def connexion_reussi():
    cacher_widget()
    nexora = QLabel("  🏠 NEXORA   ")
    bienvenue_2 = QLabel(" Bienvenue sur Nexora !  ")
    reussi_connexion = QLabel(" Connexion réussie ✅    ")
    layout.addWidget(nexora)
    layout.addWidget(bienvenue_2)
    layout.addWidget(reussi_connexion)

def retour():
    afficher_widget_2()


def verifier():
    global nombre

    try:
        resultat_code = int(entry_code.text())

    except ValueError:
        cacher_widget()
        error_type = QLabel("❌ Veuillez entrer des chiffres")
        layout.addWidget(error_type)

        reessayer = QPushButton("❌ Réessayer")
        reessayer.clicked.connect(retour)
        layout.addWidget(reessayer)
        return

    if nombre == resultat_code:
        cacher_widget()
        code_valider = QLabel("Code valide ✅")
        layout.addWidget(code_valider)

        continuer = QPushButton("Continuer ✅")
        continuer.clicked.connect(connexion_reussi)
        layout.addWidget(continuer)

    else:
        cacher_widget()
        code_invalide = QLabel("❌ Code invalide")
        layout.addWidget(code_invalide)

        reessayer_2 = QPushButton("❌ Réessayer")
        reessayer_2.clicked.connect(retour)
        layout.addWidget(reessayer_2)        
bouton_verifier.clicked.connect(verifier)
se_connecter.clicked.connect(connexion)
layout_2 = QHBoxLayout()
layout.addWidget(titre)
layout.addWidget(bienvenue)
layout.addWidget(email)
layout.addWidget(champ_email)
layout.addWidget(mot_de_passe)
layout.addWidget(champ_mot_de_passe)
layout.addWidget(se_connecter)
layout.addLayout(layout_2)
layout_2.addWidget(label_code)
layout_2.addWidget(entry_code)
layout.addWidget(bouton_verifier)
fenetre.setLayout(layout)
fenetre.show()
app.exec()
