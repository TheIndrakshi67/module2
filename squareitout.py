def square_and_split(start, end):

    squares = [i**2 for i in range(start, end + 1)]
    
   
    evens = [s for s in squares if s % 2 == 0]
    odds = [s for s in squares if s % 2 != 0]
    

    print(f"All Squares: {squares}")
    print(f"Even Squares: {evens}")
    print(f"Odd Squares: {odds}")


begin = int(input("Enter beginning range: "))
finish = int(input("Enter end range: "))
square_and_split(begin, finish)
