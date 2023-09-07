#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hidden
    arg_list = dir(hidden)
    for n in arg_list:
        if n[:2] != "__":
            print(f"{n}")
