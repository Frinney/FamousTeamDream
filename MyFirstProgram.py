import time
mainsIsOn = True
targetValue = -1

while mainsIsOn:
    print("Select category\n"
          "0 - Close App\n"
          "1 - Lists\n"
          )
    if targetValue == -1:
        try:
            targetValue = int(input())
        except ValueError as e:
            print("wrong statement try again")
            targetValue = -1
    if targetValue  == 1:
        print("List = []\n"
        "Initialize empty lsit\n"
        "List = [a, b, c]\n"
        "Initialize string list\n"
        "List = [1, 2, 3]\n"
        "Initialize string list\n"
        )
        time.sleep(5)
        targetValue = -1
    if targetValue == 0:
        print("showdown the app")
        time.sleep(1)
        print("5")
        time.sleep(1)
        print("4")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        mainsIsOn = False
        print("good night rofl")
