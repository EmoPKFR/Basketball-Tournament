wins = 0
losses = 0
matches_with_one_oponent = 0
total_matches = 0

while True:
    oponent_name = input()
    
    if oponent_name == "End of tournaments":
        break
    
    n_matches = int(input())
    
    for i in range(n_matches):
        desi_total = 0
        oponent_total = 0
        
        desi_score = int(input())
        oponent_score = int(input())
        
        desi_total += desi_score
        oponent_total += oponent_score
        
        total_matches += 1
        matches_with_one_oponent += 1
        
        if desi_total > oponent_total:
            print(f"Game {matches_with_one_oponent} of tournament {oponent_name}: win with {desi_total - oponent_total} points.")
            wins += 1
        else:
            print(f"Game {matches_with_one_oponent} of tournament {oponent_name}: lost with {oponent_total - desi_total} points.")
            losses += 1
            
    matches_with_one_oponent = 0    
    
formatted_wins = "{:.2f}".format(wins / total_matches * 100)
formatted_losses = "{:.2f}".format(losses / total_matches * 100)
    
print(f"{formatted_wins}% matches win")
print(f"{formatted_losses}% matches lost")