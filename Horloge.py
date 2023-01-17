import time

def votre_heure(heure, minutes, secondes, affichage):
  
  temps = True

  while temps == True:

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

    time.sleep(1)
    

votre_heure(23, 59, 50, "EU")