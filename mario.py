def main():
    print_square(3)
    
def print_square(size):
    # for each row of bricks
    for i in range(size):
            
        # for each brick in a row
        for j in range(size):
            print("#", end="")
            
        print()

main()