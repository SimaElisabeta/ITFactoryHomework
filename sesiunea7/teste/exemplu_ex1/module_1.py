# def hello():
#     print('Hello!')
#
# if __name__=="__main__":
#     pass


def my_function(a):
    print(f"my_function got {a}")


if __name__ == "__main__":
    print("This is module_1")
    my_function(23)


    def my_function_private(a):
        print(f"my_function_private got {a}")


    my_function_private(24)
