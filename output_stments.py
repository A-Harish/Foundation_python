# output statements

# a = int(input('enter a value :'))
# b = int(input('enter b value :'))

# print(a,b)


# sep
# print(a,b,sep='&')#seperate the values with any character upto you

# end 
# print(a,b,a,sep=' $ ',end='ends here')








# Q-1 ::input = 'john'----- output = 'hello,john!'

# name = input('enter name :')
# print('hello',name,sep=',',end='!')

# Q-2 ::input = 5 ---- output = 'your entered : 5'
# number = int(input('num :'))
# print('your entered',number,sep=':')


# Q-3 :: input: 3.14 ---- output: "Value of pi:3.14"
# pi = 3.14
# print('Value of pi:',pi)

# Q-4 :: taking multiple inputs in single line 
# input : 10 20 30    output : "sum of inputs:60"
# a = input('enter 3 digits :')
# x,y,z = a.split(' ')#seperation of 3 digits 
# sum = int(x)+int(y)+int(z)# convert string data to integer
# print(sum)



# Q-5 : specifing seperator in output
# input : "john",25 --- output : "Name:john,Age:25"
 
# data = input('enter data:john,25:')
# name,age = data.split(",")
# print('Name:',name,'Age',age)



# Q-6 : End parameter in output -- i/p: 5 ---- o/p: Countdown:54321Blastoff
    
# print('Countdown:5 4 3 2 1','Blastoff')



# Q-7: Arthamatic operators : i/p=10,5  ----

# a,b = input('enter a and b values: ').split(' ')
# a,b = int(a),int(b)
# print('Addition:',a+b,'Substration: ',a-b,'Multiplication: ',a*b,'Division: ',a/b)


# Q---   find area of circle {PI*r**2}
# radius = int(input('radius value: '))
# pi = 3.14
# area = pi*(radius**2)
# print('Area: ',area)



# Q---  Quadratic equation      i/p: a=1,b=-3,c=2   roots:(2.0,1.0)
# 

# a = int(input('enter a:'))
# b = int(input('enter b:'))
# c = int(input('enter b:'))

# # formula = ((-b(b**2-4*a*c))**0.5)/2*a 

# d = b**2-4*a*c
# root1 = (-b + (d**(0.5)))/2*a
# root2 = (-b - (d**(0.5)))/2*a
# print('Roots : ',root1,root2)


# Q ---- swap the values of two variables without using a temparary variable
# i/p : a = 10 , b = 20       o/p : a = 20 ,b = 10


# with out using temp
# approch-1
# a = int(input('value of a: '))
# b = int(input('value of b: '))
# print('before swaping : ',a,b)
# a,b = b,a
# print('after swaping :',a,b)

# approch-2
# a = int(input('value of a: '))
# b = int(input('value of b: '))
# print('before swaping : ',a,b)
# b = b+a
# a = b-a
# b = b-a
# print('after swaping :',a,b)

# with temp
# a = int(input('value of a: '))
# b = int(input('value of b: '))
# print('before swaping : ',a,b)
# temp = a
# a,b = b,temp
# print('after swaping :',a,b)


#Q --- converting tempechere units 
# i/p: temp_c = 30  o/p: temp_in_forinheight = 86.0 temp_in_kelvin: 303.15

# c = int(input('enter c value : '))
# formula1 = c*(9/5)+32
# formula2 = float(273+c)
# print('temp in forignheat : ',formula1)
# print('temp in kelvins : ',formula2)




# Q --- Basic currency converter
# i/p: amount_in_usd = 100,exchange_rate_usd_to_eur = 0.85  o/p: Equalent_amount_to_eur = 85.0 

exchange_rate_usd_to_eur = 100
amount_in_usd = 0.85
formula = exchange_rate_usd_to_eur*amount_in_usd

print(f'Equalent_amount_to_eur {formula}')
