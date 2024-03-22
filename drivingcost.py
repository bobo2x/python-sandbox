# Define your function here.
def driving_cost(mpg, dpg, miles):
    return miles / mpg * dpg

if __name__ == '__main__':
    # Type your code here.
    miles_per_gallon = float(20)
    dollars_per_gallon = float(3.1599)

    
    cost = driving_cost(miles_per_gallon, dollars_per_gallon, 10)
    print(f'{cost:.2f}')
    assert f'{cost:.2f}' == "1.58"
    
   
    cost = driving_cost(miles_per_gallon, dollars_per_gallon, 50)
    print(f'{cost:.2f}')
    assert f'{cost:.2f}' == "7.90"

    cost = driving_cost(miles_per_gallon, dollars_per_gallon, 400)
    print(f'{cost:.2f}')
    assert f'{cost:.2f}' == "63.20"
