
def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

if __name__ == "__main__":
    calc_sum = add_numbers(5, 7)
    calc_prod = multiply_numbers(4, 5)
    
    output_text = f"Calculation Results -> Added: {calc_sum} | Multiplied: {calc_prod}"
    print(output_text)
    
    with open("result.txt", "w") as f:
        f.write(output_text + "\n")