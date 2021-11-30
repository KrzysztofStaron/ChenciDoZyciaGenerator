import time

x = input("Wpisz ile chcesz chęci do życia:")
print ("Dodawanie...")

for y in range(100):
	print(str(y)+"%")
	if y == 98:
		time.sleep(3)
	time.sleep(0.05)

print("coś poszło nie tak")
