import argparse

parser= argparse.ArgumentParser(description ="Simple Calculator")

parser.add_argument("num1",type =float,help="First Number")
parser.add_argument("num2",type =float,help="Second Number")
parser.add_argument("opertion", choices=["add","subtract","Div","Mul"] ,help="Opertion to perform")

args=parser.parse_args()

print(args) 

if(args.opertion == "add"):
    print(f"The result is {args.num1 + args.num2}")
elif(args.opertion == "subtract"):
    print(f"The result is{args.num1 - args.num2}")
elif(args.opertion =="Mul"):
    print(f"The result is {args.num1 * args.num2}")
elif(args.opertion =="Div"):
    print(f"The result is {args.num1 / args.num2} ")
else:
    print("Some Error Occured")