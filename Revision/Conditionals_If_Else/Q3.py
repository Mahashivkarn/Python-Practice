insert_number_1=int(input("Two Numbers: "))
insert_number_2=int(input("Two Numbers: "))

operation=int(input("Choose a opertaion to perform:1 for +, 2 for -,3 for *,4 for /"))

match operation:
    case 1:
        print(insert_number_1 + insert_number_2)
    case 2:
        print(insert_number_1 - insert_number_2)
    case 3:
        print(insert_number_1 * insert_number_2)
    case 4:
        if(insert_number_2==0):
            print("invalid opertion")
        else:
            print(insert_number_1 / insert_number_2)
    case 5:
        print("Read the Instruction Carefully")