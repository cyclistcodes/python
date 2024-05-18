def main():

    my_list=[1,2,3,4,5]

    print(f"The list is: {my_list}")

    while True:
        try:
            index=int(input("Write index: "))

            if index < 0 or index >= len(my_list):
                print("Error: Index should be smaller")
            else: 
                print(f"Elemnt at index {index} is: {my_list[index]}")
                break

        except ValueError:
            print("Error: Please enter a valid integer. ")

if __name__ == "__main__":
    main()