# while loops repeatedly execute a block of code as long as a specified condition remains True

#example 1
count = 1
while count <= 5:
    print(count)
    count += 1
    if count == 4:
       print('the excecution is done')
       break


level = 0
while(level < 10):
  print(level)
  level += 1