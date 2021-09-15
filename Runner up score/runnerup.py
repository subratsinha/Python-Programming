

n = int(input("enter the total number of scores you want to enter"))
score=list()
for i in range(0,n):
    num=int(input("enter the scores"))
    score.append(num)
score.sort()
print("scores you have entered",score)
m1 = max(score)
m2 = -99999
for i in range(n):
    if score[i] != m1 and score[i] > m2:
        m2 = score[i]
print ("runner up scores is",m2)
