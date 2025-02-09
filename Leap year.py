x=int(input())
if x%4==0:
  if x%100==0:
    if x%400==0:
      print("is a leap year")
    else:
      print("it is not a leap year")
  else:
    print("is a leap year")
else:
  print("is not a leap year")


