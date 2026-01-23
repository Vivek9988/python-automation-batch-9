def exception_demo():
    try:
        print("----- Exception Handling Demo Start -----")

        # 1. ZeroDivisionError
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        result = a / b   # may cause ZeroDivisionError

        # 2. ValueError (if user enters string)
        num = int("abc")  # intentional error

        # 3. IndexError
        arr = [10, 20, 30]
        print(arr[10])    # out of range

        # 4. Custom exception using raise
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative!")

        print("All operations successful!")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

    except ValueError as e:
        print("Value Error:", e)

    except IndexError:
        print("Error: Index out of range")

    except Exception as e:
        print(" Unknown Error:", e)

    else:
        print("No exception occurred")

    finally:
        print("This block always runs")
        print("----- Program End -----")


# Run the function
exception_demo()
exception_demo()
exception_demo()
exception_demo

