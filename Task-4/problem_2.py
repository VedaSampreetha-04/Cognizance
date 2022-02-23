# Method-1

input_text=input ("Enter the input_text : ")
print("even_index characters : ")
for i in range(len(input_text)):
    if i%2 == 0:
        print(input_text[i])
print()

# Method 2 - using string slice

input_text=input("Enter the string : ")
evenindex=slice(0, len(input_text), 2)
print("even_index characters: ",input_text[evenindex])
