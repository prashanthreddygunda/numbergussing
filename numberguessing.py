import random
print('hello! what is your name?')
name = input()
print('well '+ name + ' , i am thinking of a number can you guess it? its between 1 and 20')
secretnumber=random.randint(1,20)
for guesstaken in range (1,7):
      print('take a guess')
      guess=int(input())
      try:
      
          if secretnumber>guess:
              print('your number is too low')
          elif secretnumber<guess:
              print('your number is too high')
          else:
              break
      except ValueError:
            print('you have to enter a numerical')
     
if secretnumber==guess:
    print('great! you have got it right')
else:
    print("you have ran out of your chances by the way i was thinking abouit '+ secret number +' :)")
 
