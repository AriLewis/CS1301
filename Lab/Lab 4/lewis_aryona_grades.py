d1 = {"Mary", "Jake", "Sam", "Alex", "Percy", "Jessica" , "Trent" , "Mahmoud"}
d2 = {"Jake", "Sam", "Alex", "Percy", "Mahmoud", "Trent", "Caleb", "Zayne"}
grades = [83, 85, 72, 65, 76, 90, 79, 88, 93, 70, 67, 80]

print(len(grades),"Students took the exam.")
print("The highest grade was", max(grades))
print("The lowest grade was", min(grades))
print("The average grade for the exam was", sum(grades)/len(grades))
two = d1.intersection(d2)
one = d1.symmetric_difference(d2)

total = d1.union(d2)
print(len(total), "students attended the class.")
print(two, "attended both class days.")
print(one, "attended one class day.")