import time
import keyboard

# Choisir l'heure de l'horloge
heure_actuelle = (16, 30, 0)
# Choisir l'heure de l'alarme
alarme = (16, 30, 10)
# Choisir si on active le mode 12h ou 24h (True = mode 12h | False = mode 24h)
mode_12_heures = True


# Fonction de l'heure
def reglage_heure(heure):
    global heure_actuelle
    heure_actuelle = heure


# Fonction de l'alarme
def reglage_alarme(alarm):
    global alarme
    alarme = alarm


# Fonction mode 12h ou 24h
def changer_mode(mode):
    global mode_12_heures
    mode_12_heures = mode


# Affichage de l'heure
def afficher_heure():
    global heure_actuelle
    if heure_actuelle == (25, 0, 0):
        heure_actuelle = (1, 0, 0)
    if mode_12_heures:
        heures = heure_actuelle[0] % 12
        if heures == 0:
            heures = 12
        am_pm = "AM" if heure_actuelle[0] < 12 else "PM"
        print("\r{:02d}:{:02d}:{:02d} {}".format(heures, heure_actuelle[1], heure_actuelle[2], am_pm), end="")
    else:
        print("\r{:02d}:{:02d}:{:02d}".format(*heure_actuelle), end="")


# Fonction qui permet de passer les heures ,les minutes et les secondes
def actualisation_heure():
    global heure_actuelle
    heure_actuelle = (heure_actuelle[0], heure_actuelle[1], heure_actuelle[2] + 1)
    if heure_actuelle[2] == 60:
        heure_actuelle = (heure_actuelle[0], heure_actuelle[1] + 1, 0)
    if heure_actuelle[1] == 60:
        heure_actuelle = (heure_actuelle[0] + 1, 0, 0)
    if heure_actuelle == (24, 0, 0):
        heure_actuelle = (0, 0, 0)
    afficher_heure()
    if heure_actuelle == alarme:
        print("\nDRING! L'alarme a sonnée")

    pause()


# Fonction pour mettre en pause l'horloge
def pause():
    running = True
    display = True
    block = False

    while running:
        time.sleep(1)
        # Rester appuyer quelque seconde pour mettre en pause l'horloge
        if keyboard.is_pressed("down") and display == True:
            print("\nPause")
            if not block:
                display = not display
                block = True
                print("Rester appuyer sur la touche flèche du bas pour relancer l'horloge.")
        elif keyboard.is_pressed("down") and display == False:
            print("Le temps reprend son cours...")
            if not block:
                display = not display
                block = True
        else:
            block = False
        if display:
            return


while True:
    actualisation_heure()
