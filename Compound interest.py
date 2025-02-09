def compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time) - principal
p=int(input())
r=int(input())
t=int(input())
print("Compound Interest:", compound_interest(p,r,t))