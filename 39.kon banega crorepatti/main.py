questions = [
    ["Which language was used to create Facebook?", "Python", "JavaScript", "C++", "PHP", 4],
    ["What is the capital of Japan?", "Beijing", "Seoul", "Tokyo", "Bangkok", 3],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 2],
    ["Who wrote 'Hamlet'?", "Charles Dickens", "J.K. Rowling", "William Shakespeare", "George Orwell", 3],
    ["Which element has the chemical symbol 'O'?", "Oxygen", "Gold", "Silver", "Iron", 1]
]
questions.extend([
    ["What is the largest ocean on Earth?", "Indian", "Pacific", "Atlantic", "Arctic", 2],
    ["Who is known as the father of computers?", "Alan Turing", "Charles Babbage", "John von Neumann", "Steve Jobs", 2],
    ["What is the boiling point of water in Celsius?", "90°C", "100°C", "110°C", "120°C", 2],
    ["Which animal is known as the 'King of the Jungle'?", "Tiger", "Elephant", "Lion", "Leopard", 3],
    ["In which year did World War II end?", "1942", "1943", "1945", "1946", 3]
])



levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0

for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(question[0])
  print(f"1. {question[1]}          2. {question[2]} ")
  print(f"3. {question[3]}          4. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    # print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
#   else:
    # print("Wrong answer!")
    # break 

print(f"Your take home money is {money}")