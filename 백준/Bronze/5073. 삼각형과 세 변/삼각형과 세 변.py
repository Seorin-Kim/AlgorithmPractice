while True:
    list_tri = [int(i) for i in input().split()]
    list_tri.sort(reverse=True)
    
    if list_tri[-1] == 0:
        break
    else:
        if list_tri[0] >= list_tri[1] + list_tri[2]:
            print("Invalid")
        elif list_tri[0] == list_tri[1]:
            if list_tri[1] == list_tri[2]:
                print("Equilateral")
            else:
                print("Isosceles")
        elif list_tri[1] == list_tri[2]:
            print("Isosceles")
        else:
            print("Scalene")
        