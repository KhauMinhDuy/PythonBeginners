

temperature = int(input("temperature today: "))

message = "Stay Inside"

if temperature > 80:
    print("It's too hot!")
    print(message)
elif temperature < 60:
    print("It's too cold")
    print(message)
else:
    print("Have a good day")
    print("Enjoy the outdoors")


if temperature > 80 or temperature < 60:
    print(message)
else:
    print("Enjoy the outdoors")