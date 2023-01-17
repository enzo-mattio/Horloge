import time

def votre_heure(heure, minutes, secondes):
  
  temps = True

  while temps == True:
    time.sleep(1)
    print("L'heure est :", heure, ":", minutes, ":", secondes, ".")
    secondes += 1
    if secondes > 59 :
      minutes += 1
      secondes = 0
    if minutes > 59 :
      heure += 1
      minutes = 0
    if heure > 23 :
      heure = 0
    

votre_heure(23, 59, 50)



  
  