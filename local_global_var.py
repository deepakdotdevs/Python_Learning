n=1 # Global variable, access outside and inside the function too
def fn():
    global n # for assigning local var to global var
    n=5 # known as local variable, we access this inside the function
    print('in', n) # if we delete 'n=5' from function then global n value print inside the function
fn()
print('out', n)

# Note - if we want local variable value to be assigned to global variable then, assigned it to global variable inside that function
# the local variable has been preferred in a higher position than the global variable