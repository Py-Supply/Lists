# declare a list
fruit = ['oranges', 'apples', 'bananas', 'blueberries', 1.29, 2.30, 0.54, 3.99]
#print(fruit[2])

userInput = 0
while userInput != 5:
    print('Menu')
    print('1. oranges' + ' $' + str(fruit[4]))
    print('2. apples' + ' $' + str(fruit[5]))
    print('3. bananas' + ' $' + str(fruit[6]))
    print('4. blueberries' + ' $' + str(fruit[7]))
    print('5. exit')
    print('6. add a new item')
    userInput = int(input())
    if userInput >= 0 and userInput <= 4:
        print('You chose: ' + fruit[userInput - 1])
    if userInput == 6:
        print('enter the new fruit')
        fruitInput = input()
        fruit.append(fruitInput)

for i in range(len(fruit)):
    print(fruit[i])

