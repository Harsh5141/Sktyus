# Simulate a traffic light: Red = Stop, Yellow = Wait, Green = Go.
signal=input("enter a signal light: ")
if signal == "Red":
    print("stop")
elif signal == "Yellow":
    print("Wait")
elif signal == "Green":
    print("Go")
else:
    print("Invalid color")