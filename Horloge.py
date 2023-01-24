import time
import keyboard

temps = True
pause = False


def votre_heure(heure, minutes, secondes):
  
  alarme_secondes = ""
  alarme_heure = ""
  alarme_minutes = ""
  
  # Demande pour la mise en place d'une alarme 
 
  print("Voulez-vous programmez un reveil ? (y/n)" )

  alarme = input()
  

  # Mise en place de l'alarme
  if alarme == "y":
    print("Veuillez notez l'heure :")
    alarme_heure = int(input())
    print("Les minutes :")
    alarme_minutes = int(input())
    print("Les secondes :")
    alarme_secondes = int(input())
  
  # Demande pour l'affichage 
  print("Quelle type d'affichage voulez-vous ? (EU/UK)")
  
  affichage = input()
  
  # Boucle qui calcule le temps et affiche l'heure selon le type d'affichage demandé
  while temps == True:
    # Test d'ajout d'une pause
    # key = keyboard.read_key() 
    # if key == 'space':
      # input("Appuyez sur <Entrer> pour continuer")   

    secondes += 1
    if secondes > 59 :
      minutes += 1
      secondes = 0
    if minutes > 59 :
      heure += 1
      minutes = 0
    if heure > 23 :
      heure = 0
    
    if affichage == "EU":
      print("L'heure est :", heure, ":", minutes, ":", secondes, ".")
      
    elif affichage == "UK":
      if heure > 12 :
        print("L'heure est :", heure - 12 , ":", minutes, ":", secondes, "AM.") 
      else:
        print("L'heure est :", heure, ":", minutes, ":", secondes, "PM.") 
    
    if alarme_heure == heure and alarme_minutes == minutes and alarme_secondes == secondes:
      print("C'est l'heure !!!!")
      break
    
    time.sleep(1)
    
  # Test d'ajout d'une pause
  # 

# def pause_key():
  
  # key = keyboard.read_key() 
  # if key == 'space':
    # input("Appuyez sur <Entrer> pour continuer")
    


  

# Notez l'heure (Heure, Minutes, Secondes)
votre_heure(23, 59, 50)
