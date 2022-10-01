score_of_the_player = int(input("Enter a score of the test -1 to stop: "))   
total_score= 0
scorecount= 0                       

while score_of_the_player != -1:                     
    total_score = total_score + score_of_the_player
    scorecount= scorecount + 1
    score_of_the_player = int(input("Enter a score of the test -1 to stop: "))  
print ("The average for the test is ",total_score/scorecount)
