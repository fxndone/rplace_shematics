from websocket import create_connection

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

x = int(input("X : "))
y = int(input("Y : "))

x -= 1
x_place = numberToBase(x, 255)
while len(x_place) < 4:
    x_place.append(0)
x_place.reverse()

y -= 1
y_place = numberToBase(y, 255)
while len(y_place) < 4:
    y_place.append(0)
y_place.reverse()

ws = create_connection("ws://place.minecraftbetter.com/ws")
ws.send_binary(x_place + y_place + [255, 255, 255])
ws.close()
