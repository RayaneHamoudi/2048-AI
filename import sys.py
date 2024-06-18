import sys


line = int(sys.stdin.readline().rstrip('\n'))
for i in range(1):
    match line:
        case 0:
            print("Start song")
        case 1:
            print("Restart song")
        case 2:
            print("Tempo up")
        case 3:
            print("Tempo down")
        case 4:
            print("Pause someone tripped")
        case 5:
            print("Drop the bass")
        case 6:
            print("Drop it lower!")
        case 7:
            print("Pitch higher")
        case 8:
            print("Pitch too high, shattering glass!")
        case 9:
            print("Get my agent on the phone")
        
