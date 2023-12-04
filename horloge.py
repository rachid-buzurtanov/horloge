import time

temps = True
pause = False


def votre_heure(heure, minutes, secondes):
  
  alarme_secondes = ""
  alarme_heure = ""
  alarme_minutes = ""

 
  print("Souhaitez-vous mettre en place un réveil ? (O/N)" )

  alarme = input()

  if alarme == "O":
    print("Veuillez notez l'heure :")
    alarme_heure = int(input())
    print("Les minutes :")
    alarme_minutes = int(input())
    print("Les secondes :")
    alarme_secondes = int(input())
  
  print("Quelle type d'affichage voulez-vous ? (24H/AMPM)")
  
  affichage = input()
  
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
    
    if affichage == "24H":
      print("L'heure est :", heure, ":", minutes, ":", secondes, ".")
      
    elif affichage == "AMPM":
      if heure > 12 :
        print("L'heure est :", heure - 12 , ":", minutes, ":", secondes, "AM.") 
      else:
        print("L'heure est :", heure, ":", minutes, ":", secondes, "PM.") 
    
    if alarme_heure == heure and alarme_minutes == minutes and alarme_secondes == secondes:
      print("C'est l'heure !!!!")
      break
    
    time.sleep(1)
    
votre_heure(12, 59, 50)