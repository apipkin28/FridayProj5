import sqlite3

conn = sqlite3.connect('Fridayproj5.db')
cursor = conn.cursor()

# Used GAI to help extract table name -- "QuestAns"
#cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#tables = cursor.fetchall()
#print("Tables in the database:")
#for table in tables:
    #print(table[0])

# Now will use GAI to help extract table column names -- "id" "question" "answer"
#tableName = 'QuestAns'
#cursor.execute("PRAGMA table_info({})".format(tableName))
#columns = cursor.fetchall()
#print("Columns in the table '{}'".format(tableName))
#for column in columns:
    #print(column[1])

cursor.execute("SELECT question, answer from QuestAns")
questionsList = cursor.fetchall()

print("Welcome to The QuizBowl! Your questions start now.")

score = 0
for question, answer in questionsList:
    print(question)
    response = input("Your answer: ")
    if response.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The answer is "+answer+".")

print("Quiz ended. Your score is "+str(score)+" out of "+ str(len(questionsList)) + ".")

# GAI showed how to close the db connection - good habit to get into
conn.close()