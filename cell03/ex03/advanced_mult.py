def display_multiplication_tables():
    for i in range(11):
        print(f"Table of {i}: ", end="")
        
        for j in range(1, 11):
            if j == 1:
                print(f"{i * j:02d}", end="")
            else:
                print(f"{i * j:02d}", end=" ")
        
        print()

if __name__ == "__main__":
    display_multiplication_tables()
