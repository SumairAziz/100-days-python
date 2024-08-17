pairs = [
    "What is the feminine of male?", "Female",
    "What is the opposite of day?", "Night",
    "What is the plural of child?", "Children",
    "What is the synonym of happy?", "Joyful",
    "What is the capital of France?", "Paris"
]
count=0

for i in range(0,len(pairs),2):
    res=input(pairs[i])
    if(res.capitalize()==pairs[i]):
        count+=1

print("You got ",count," right answers")