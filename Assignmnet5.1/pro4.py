# Function to calculate simple interest.
def simple_interest(principle,rate,time):
    return(principle*rate*time)/100
p=1000
r=5
t=2
interest=simple_interest(p,t,r)
print("simple_interest:",interest)