def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100
p=int(input())
r=int(input())
t=int(input())
print("Simple Interest:", simple_interest(p,r,t))