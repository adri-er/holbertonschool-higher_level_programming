#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4).sort()
    for name in names:
        if (name[:2] == "__"):
            continue
        else:
            print("{}".format(name))
