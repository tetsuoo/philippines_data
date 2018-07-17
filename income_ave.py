import pandas as pd

df = pd.read_csv("pwt90_w_country_names.csv")

##make income average column
df['income_ave'] = df['rgdpo'] / df['pop']

##generalize income ave by phili(2011)
income_criteria = df[(df['countrycode']=='PHL') & (df['year']==2011)]['income_ave'].values
#print(income_criteria)
df['ge_income_ave'] = df['income_ave'] / income_criteria * 100
#print(df[(df['countrycode']=='PHL')])

##generalize rgdp by phili(2011)
rgdp_criteria = df[(df['countrycode']=='PHL') & (df['year']==2011)]['rgdpo'].values
#print(income_criteria)
df['ge_gdp'] = df['rgdpo'] / rgdp_criteria * 100
#print(df[(df['countrycode']=='PHL')])

#make total trade
df['trade'] = df['csh_x'] -  df['csh_m']

##generalize TFP level by phili(2011)
ctfp_criteria = df[(df['countrycode']=='PHL') & (df['year']==2011)]['ctfp'].values
#print(income_criteria)
df['ge_ctfp'] = df['ctfp'] / ctfp_criteria * 100
#print(df[(df['countrycode']=='PHL')])


##select countries
countries = []
max_income = 150
min_income = 50
for country in df['country'].unique():
    x = df[(df['country']==country) & (df['year']==2011)]['ge_income_ave'].values
    p = df[(df['country']==country) & (df['year']==2011)]['pop'].values
    #print(country, x, '\n')
    if (x < max_income) and (x > min_income) and p >50:
        countries.append(country)


#print(df['country'].unique(), '\n')
countries.append('Japan')
countries.append('United States')
print(countries)

df = df[(df['country'].isin(countries))]


##
def str_join(df, sep, *cols):
    from functools import reduce
    return reduce(lambda x, y: x.astype(str).str.cat(y.astype(str), sep=sep),
                    [df[col] for col in cols])

#print(str_join(df, '-', 'countrycode' ,'year'))

print(df[df['country']=='United States']['ctfp'])
#df.to_csv('comparison_data_set')