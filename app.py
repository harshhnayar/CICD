
def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    result = add_numbers(5, 7)
    output_text = f"Hello World! The calculation result is: {result}"
    print(output_text)
    with open("result.txt", "w") as f:
        f.write(output_text + "\n")