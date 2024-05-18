
my_list=[1,2,3,4,5]

while True:
        try:
            # Skapa en variabel 
            index = int(input("Write index: "))
            if index < 0 or index >= len(my_list):
                print("Error: write a smaller index: ")
            else:
                print(f"The index is {index} and the value is {my_list[index]}")
                break

        except ValueError:
            print("Error: write a valid integer")