# Get input for the check amount.
check = input("Enter check amount:")
# Convert to float.
int(check)

# Get input for the tip percent. Convert to int.
tip = input("Tip percent:")
int(tip)

# Calculate the tip amount.  Don't forget to divide by 100 to a *real* percent.
total = check/tip
amount = total/100
# Print the tip results in the format `A PCT% tip on $CHECK is $AMOUNT`. Except
# for the tip PCT (which should be an int), just let the number of decimal
# places run long or short. We'll learn how to round and format these numbers
# later. You may want to construct an output string a step at a time to avoice a
# really long concatenation.
print(f"A {tip}% tip on ${check} is ${amount}")
