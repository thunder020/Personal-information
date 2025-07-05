customer = input('write coustomer name:')
buying_cost = float(input('write the costs:'))
membership = input('are you memmbership of here?(yes/no)') == 'yes'
highcosts= buying_cost>10000
if highcosts and membership:
    discount= buying_cost*0.10
elif highcosts or membership:
   discount = buying_cost*0.5
else:
    discount = 0.0
final_cost = buying_cost - discount
print(f'hello {customer}.\n your buying cost is {buying_cost}\n and your membership statuse is: {membership} :\n your discount is:{discount}dollars.\n your final cost is:{final_cost} dollars.')
