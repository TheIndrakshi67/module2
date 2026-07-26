gradebook= {
    "Alice":88,
    "Bob":95,
    "Charlie":72,
    "Yuka":91,
    "Ren":84
}

total_score=0
for score in gradebook.values():
    total_score+=score

average_score=total_score/len(gradebook)
print("Class Average: ", average_score)

highest=max(gradebook,key=gradebook.get)
lowest=min(gradebook,key=gradebook.get)

print("Highest Scorer: ", highest)
print("Lowest Scorer: ", lowest)
search_name=input("Enter Student name: ")
studentscore=gradebook.get(search_name)

if studentscore is not None:
    print(search_name,"grade is", studentscore)
else:
    print("Student not found.")