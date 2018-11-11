try:
	int(input("Enter a number: "))
except ValueError:
	print("input is not a number")
else:
	print("its a number and you are in ELSE block")
finally:
	print("Runs no matter what!")
