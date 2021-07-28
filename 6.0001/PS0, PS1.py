##PS0 

#1. Asks the user to enter a number “x”
#2. Asks the user to enter a number “y”
#3. Prints out number “x”, raised to the power “y”.
#4. Prints out the log (base 2) of “x”.
import math 
x=int(input('enter a number “x” : '))
y=int(input('enter a number “y” : '))
print('x ^y = ' , x**y)
print('log 2 x = ' ,round(math.log2(x), 4))

#===============================
##PS1a

#You have graduated from MIT and now have a great job! You move to the San Francisco Bay Area and decide that you want to start saving to buy a house. 
#As housing prices are very high in the Bay Area, you realize you are going to have to save for several years before you can afford to make the down payment on a house. 
#In Part A, we are going to determine how long it will take you to save enough money to make the down payment given the following assumptions:
#Call the cost of your dream home total_cost.
#Call the portion of the cost needed for a down payment portion_down_payment. For simplicity, assume that portion_down_payment = 0.25 (25%).
#Call the amount that you have saved thus far current_savings. You start with a current savings of $0.
#Assume that you invest your current savings wisely, with an annual return of r (in other words, at the end of each month, you receive an additional current_savings*r/12 funds to put into your savings – the 12 is because r is an annual rate). Assume that your investments earn a return of r = 0.04 (4%).
#Assume your annual salary is annual_salary.
#Assume you are going to dedicate a certain amount of your salary each month to saving for the down payment. Call that portion_saved. This variable should be in decimal form (i.e. 0.1 for 10%).
#At the end of each month, your savings will be increased by the return on your investment, plus a percentage of your monthly salary (annual salary / 12). Write a program to calculate how many months it will take you to save up enough money for a down payment. You will want your main variables to be floats, so you should cast user inputs to floats.
#1 Your program should ask the user to enter the following variables:
#The starting annual salary (annual_salary)
#The portion of salary to be saved (portion_saved)
#The cost of your dream home (total_cost

def calculate_house_time(annual_salary = 10000,portion_saved = 0.1, total_cost = 10000):
    time = 0 #months
    current_saving = 0 
    portion_down_payment = 0.25 
    
    monthly_salary = annual_salary / 12
    invest_annual_r = 0.04 
    invest_monthly_r = (1+invest_annual_r) ** (1/12) -1 
    while current_saving >=0: 
        if current_saving >= total_cost * portion_down_payment:
            return 'the time that takes to gain down payment portion is ' + str(time) + ' months' 
            break 
        else:     
            current_saving =current_saving*(1+invest_monthly_r)  #전월의 효과
            current_saving += monthly_salary*portion_saved #save 10 percent 
            time+=1
            
calculate_house_time() #try it!
        
##PS1b

#In ps1b.py, copy your solution to Part A (as we are going to reuse much of that machinery).  Modify your program to include the following
#1. Have the user input a semi-annual salary raise semi_annual_raise (as a decimal percentage)
#2. After the 6th month, increase your salary by that percentage.  Do the same after the 12th month, the 18  month, and so on. 

def calculate_house_time_semiannualraise(annual_salary = 10000,portion_saved = 0.1, total_cost = 10000, semiannualraise = 0.03):
    time = 0 #months
    current_saving = 0 
    portion_down_payment = 0.25 
    monthly_salary = annual_salary / 12
    #print('time ', 'current_saving ', 'monthly_salary ')
    #print(time , current_saving , monthly_salary )
    
    invest_annual_r = 0.04 
    invest_monthly_r = (1+invest_annual_r) ** (1/12) -1 
    while current_saving >=0: 
        if current_saving >= total_cost * portion_down_payment:
            return 'the time that takes to gain down payment portion is ' + str(time) + ' months' 
            break 
        else:     
            current_saving =current_saving*(1+invest_monthly_r)  #전월의 효과
            if time%6 == 0 and time > 0 : 
                monthly_salary += monthly_salary*semiannualraise
            current_saving += monthly_salary*portion_saved #save 10 percent 
            time+=1
            #print(time, round(current_saving,3), round(monthly_salary,2))
            
 ################################################################################################################           
##PS1c
def calculate_house_time_semiannualraise(annual_salary,portion_saved, \
                                         total_cost, semiannualraise):
    time=0 
    current_saving = 0 
    portion_down_payment = 0.25 
    monthly_salary = annual_salary / 12
    #print('time ', 'current_saving ', 'monthly_salary ')
    #print(time , current_saving , monthly_salary )
    
    invest_annual_r = 0.04 
    invest_monthly_r = (1+invest_annual_r) ** (1/12) -1 
    while current_saving >=0: 
        if current_saving >= total_cost * portion_down_payment:
            return time #time took in months 
            break 
        else:     
            current_saving =current_saving*(1+invest_monthly_r)  #전월의 효과
            if time%6 == 0 and time > 0 : 
                monthly_salary += monthly_salary*semiannualraise
            current_saving += monthly_salary*portion_saved #save by numX percent 
            time+=1
            
def calculate_house_portionsave_36 (annual_salary): 
    iterate = 0
    psave1, psave2 = 0, 1 # portion saved, in fraction: 
    
    #conditional settings
    semiannual = 0.07
    annualreturn = 0.04
    downpay_portion= 0.25# this is already implanted in calculate semiannualraise function
    total_cost=1000000 #of house
    
    timestandard=36 #mo 
    
def calculate_house_portionsave_36 (annual_salary): 
    iterate = 0
    psave1, psave2 = 0, 1 # portion saved, in fraction: 
    
    #conditional settings
    semiannual = 0.07
    annualreturn = 0.04
    downpay_portion= 0.25# this is already implanted in calculate semiannualraise function
    total_cost=1000000 #of house
    
    timestandard=36 #mo 
    
def calculate_house_portionsave_36 (annual_salary): 
    iterate = 0
    psave1, psave2 = 0.001, 0.5 # portion saved, in fraction: 
    
    time=0 #for the calculate_house_semiannualraise
    
    #conditional settings
    semiannual = 0.07
    annualreturn = 0.04
    downpay_portion= 0.25# this is already implanted in calculate semiannualraise function
    total_cost=1000000 #of house
    
    timestandard=36 #mo 
    
    while iterate <20:
        psaveweek1 = calculate_house_time_semiannualraise(annual_salary, psave1, total_cost, semiannual, time)
        if bool(psaveweek1) == False: 
            psaveweek1 = 99999
        psaveweek2 = calculate_house_time_semiannualraise(annual_salary, psave2, total_cost, semiannual, time)
        psavemid = (psave1 + psave2)/2
        psaveweekmid = calculate_house_time_semiannualraise(annual_salary, psavemid, total_cost, semiannual, time)
        if psaveweekmid == 36:
            return 'The wanted portion save for $' + str(annual_salary) + ' initial annual salary'\
                    ' is: ' + str(psavemid)
            break
        elif abs(psaveweek1-timestandard) <= abs(psave2-timestandard): 
            psave1, psave2 = psave1, psavemid
            iterate+=1
            time +=1
            print('case#1: iterate:', iterate, ',   portion saved frame:', psaveweek1,'',psaveweek2, ' psave:', psave1, psave2, ' framesize:', abs(psave1-psave2)) 
        elif abs(psaveweek1-timestandard) > abs(psave2-timestandard): 
            psave1, psave2= psavemid, psave2
            iterate+=1
            time +=1
            print('case#2: iterate:', iterate, ',   portion saved frame:', psaveweek1,'',psaveweek2, ' psave:', psave1, psave2, ' framesize:', abs(psave1-psave2)) 


        
        
#
annualsalary=150000
calculate_house_portionsave_36(annualsalary)
#expected portion save: 0.4411  
#expected Steps in bisection search: 12 
