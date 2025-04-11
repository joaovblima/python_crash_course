requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for resquested_topping in requested_toppings:
    if resquested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now")
    else:
        print(f"Adding {resquested_topping}")
print("\nFinished making your pizza")