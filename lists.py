# declare a list
fruit = ['oranges', 'apples', 'bananas', 'blueberries']
#print(fruit[2])

userInput = 0
while userInput != 5:
    print('Menu')
    print('1. oranges')
    print('2. apples')
    print('3. bananas')
    print('4. blueberries')
    print('5. exit')
    userInput = int(input())
    if userInput >= 0 and userInput <= 4:
        print('You chose: ' + fruit[userInput - 1])