import argparse

def demo() -> None: 	
    parser=argparse.ArgumentParser() 	
    parser.add_argument("--link",dest="input_path",help='Path to file',type=str)        	
    parser.add_argument("--num",dest="number",help='Enter a number',type=int)    
	
    args = parser.parse_args()  	

    filename=args.input_path 	
    numbers=args.number  	

    print("filename: ", filename) 	
    print("number is: ",numbers)

if __name__=='__main__': 	
    demo()
