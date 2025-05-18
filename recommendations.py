def main():
  difficulty = input("Difficult or Casual? ")
  players = input("Multiplayer or Single-player? ")
  
  if difficulty == "Difficult":
    if players == "Multiplayer":
      recommend("PUBG")
      
    else:
      recommend("Elden Ring")
  elif difficulty == "Casual":
    if players == "Multiplayer":
      recommend("Free Fire")
    else:
      recommend("RDR2")
  else:
    print("Choose a valid option")
 
 
 
def recommend(game):
  print("You might like", game) 
  
  
  
  
main()