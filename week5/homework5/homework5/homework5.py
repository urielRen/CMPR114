# Uriel Renteria
# 3/13/23
# Homework for week 5

# Project 1 - Property Tax
#def main():
#    actual_value = float(input('Enter property value: $'))
#    assessment = assessment_value(actual_value)
#    property_tax(assessment)

#def assessment_value(actual_value):
#    land = actual_value * .6
#    return land

#def property_tax(assessment):
#    tax = assessment / 100 * .72 
#    print(f'Assessment value of the property: ${assessment: ,.2f}')
#    print(f'Property tax of the property: ${tax: ,.2f}')

#main()

# Project 2
#CLASSA = 20
#CLASSB = 15
#CLASSC = 10

#def main():
#    ticketsA = int(input('Enter the number of class A tickets sold: '))
#    ticketsB = int(input('Enter the number of class B tickets sold: '))
#    ticketsC = int(input('Enter the number of class C tickets sold: '))
#    classA = classA_sold(ticketsA)
#    classB = classB_sold(ticketsB)
#    classC = classC_sold(ticketsC)
#    total_sold(classA, classB, classC)

#def classA_sold(ticketsA):
#    tickets = ticketsA * CLASSA
#    return tickets

#def classB_sold(ticketsB):
#    tickets = ticketsB * CLASSB
#    return tickets

#def classC_sold(ticketsC):
#    tickets = ticketsC * CLASSC
#    return tickets

#def total_sold(classA, classB, classC):
#    total = classA + classB + classC
#    print(f'Class A tickets total sold: ${classA: ,.2f}')
#    print(f'Class B tickets total sold: ${classB: ,.2f}')
#    print(f'Class C tickets total sold: ${classC: ,.2f}')
#    print(f'Total tickets sold: ${total: ,.2f}')

#if __name__ == '__main__':
#    main()

# Project 3
#STATE_RATE = .05
#COUNTY_RATE = .025

#def main():
#    sales = float(input('Enter total sales for the month: $'))
#    state_sales = state_tax(sales)
#    county_sales = county_tax(sales)
#    total_taxes(state_sales, county_sales)

#def state_tax(sales):
#    stateTax = sales * STATE_RATE
#    return stateTax

#def county_tax(sales):
#    countyTax = sales * COUNTY_RATE
#    return countyTax

#def total_taxes(state_sales, county_sales):
#    total = state_sales + county_sales
#    print(f'County sales tax: ${county_sales: ,.2f}')
#    print(f'State sales tax: ${state_sales: ,.2f}')
#    print(f'Total sales tax: ${total: ,.2f}')

#if __name__ == '__main__':
#    main()
