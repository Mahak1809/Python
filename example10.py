fruits = ["apple","banana","mango"]
print(fruits[0]);

fruits = ["apple","banana","mango"]
print(fruits[-2]);

fruits = ["apple","banana","mango","grapes","kiwi"]
print(fruits[1:4]);

fruits = ["apple","banana","mango","grapes","kiwi"]
print(fruits[:3]);

fruits = ["apple","banana","mango","grapes","kiwi"]
print(fruits[3:]);

fruits = ["apple","banana","mango","grapes","kiwi"]
fruits[1]="watermelon"
print(fruits);

fruits = ["apple","banana"]
fruits.append("mango")
print(fruits);
# append adds an element at the end of the list

fruits = ["apple","banana"]
fruits.insert(1, "mango")
print(fruits);
# it adds an element at specific index

fruits=["apple","banana","mango","banana"]
fruits.remove("banana")
print(fruits);

fruits=["apple","banana","mango","banana"]
fruits.pop()
print(fruits);