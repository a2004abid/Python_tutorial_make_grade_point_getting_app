

#write a program which help us to get grade point for our institure result

marks_ = int(input("Enter a Number: "))

if marks_ >= 80 and marks_ <= 99:
	print("You Got : A+")

elif marks_ >= 70 and marks_ <= 79:
	print("You Got: A") 

elif marks_ >= 60 and marks_ <= 69:
	print("You Got: A-")

elif marks_ >= 50 and marks_ <= 59:
	print("You Got: B")

elif marks_ >= 40 and marks_ <= 49:
	print("You Got: C")

elif marks_ >= 33 and marks_ <= 39:
	print("You Got: D")

else:
	print("You Are Fail In The Exam")


input()