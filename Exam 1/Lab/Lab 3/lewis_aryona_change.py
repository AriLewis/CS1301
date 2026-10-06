cents = int(input('Please enter the number of cents:'))
mod_cents = cents
quarter = mod_cents // 25
mod_cents = mod_cents % 25

dime = mod_cents // 10
mod_cents = mod_cents % 10
nickle = mod_cents // 5
mod_cents = mod_cents % 5

penny = mod_cents
print(f'Coins: {quarter} quarters, {dime} dimes, {nickle} nickles, {mod_cents} pennies')
