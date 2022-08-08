##**Lambda FUNCTIONS**
# How to use lambda expressions in your code
# First of all, lambda expressions mean as functions used in objects, is very similar a function using "def" but the difference is written only in one line.
import datetime 
import pandas as pd
 
# A lambda function is composed with a argument (value) and a expression (value). Lambda makes the code easier to understand and usable where is called just one time.
#       lambda argument(s): expression
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#Pattern functions
def somar(n, n1):
    s = n+n1
    return s

somar(1,1)

#**Same fucntion using the lambda expressions**
somar_l = lambda n, n1: n+n1
somar_l(1,2)

somaq = lambda a,b: a**2 + b**2
somaq(2,3)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#Return the numbers of divide by 2 in a range between 2 numbers
(lambda i, f : [i%2==0 for i in range(i,f)])(1,30)


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#**EXAMPLE** Using that in a Dataframe
# Create a DF and apply a lambda function in a columns.

df = pd.DataFrame({                             
    'Car': ['Golf','polo','fusca','Maseratti'],#create a df
    'Fabrication': [1976, 1984, 2013, 2016]})

df['time_use'] = df['Fabrication'].apply(lambda x: 2022 - x) # create a column and apply a lambda function
display(df) #will print the dataframe with the time of car's use.

#convert to upper-case
df['Car'] = df.apply(lambda x: x[['Car']].str.upper(), axis=1); df

#Other example
precos = [120,140,150] #create a list with values of a price of products.
impostos = list(map(lambda x: x * 0.3, precos)) # Lambda function with a map function. It means that each value from a list will be replaced with the function created.
print(impostos) #response of the function


tables = [lambda x=x: x*10 for x in range(1, 5)]
print([i for i in tables])

for table in tables:
    print(table())