def main():
  difficulty = input("Difficult or Casual? ")
  players = input("Multiplayer or Single-player? ")
  
  if difficulty == "Difficult":
    if players == "Multiplayer":
      recommend("PUBG")
      
    elif players == "Single-player":
      recommend("Elden Ring")
      
    else:
      print("Enter valid number of player")
  elif difficulty == "Casual":
    if players == "Multiplayer":
      recommend("Free Fire")
    elif players == "Single-player":
      recommend("RDR2")
    else:
      print("Choose a valid number of player")
      
  else:
    print("Enter a valid difficulty")
 
 
 
def recommend(game):
  print("You might like", game) 
  
  
  
  
main()