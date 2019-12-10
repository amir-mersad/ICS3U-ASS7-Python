#!/usr/bin/env python3

# Created by: Amir Mersad
# Created on: December 2019
# This program is for assignment 7 ics3u


def printing(input_list):
    # Process
    line = ""
    result = ""
    for word in input_list:
        line = f"* {word} *"
        if word == input_list[-1]:
            result += line
        else:
            result += line + "\n"
    return result


def main():
    # This function gets the input and passes it to another function
    input_list = []

    # Input and part of Process
    while True:
        word = input('Enter the word:\t (type "stop!" when done)')
        if word == "stop!":
            break
        elif word == "":
            pass
        else:
            input_list.append(word)

    # Passing to another function
    result = printing(input_list)

    # Output
    print("*********")
    print(result)
    print("*********")


if __name__ == "__main__":
    main()
