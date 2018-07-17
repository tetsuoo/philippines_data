import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('comparison_data_set')
#countries = df['country'].unique()
#code = df['countrycode'].unique()
code = ['PHL', 'VNM', 'MMR', 'PAK', 'IND','NGA', 'USA', 'JPN']
#print(code)
countries = ['Philippines',  'Viet Nam', 'Myanmar','Pakistan', 'India', 'Nigeria', 'United States', 'Japan']
#print(countries)

##GDP AND GDP per Capita
def gdp():
    fig1 = plt.figure()
    fig1.suptitle('GDP and GDP Per Capita(Philippines in 2011 = 100)', size=18)
    i=1
    for country in countries:
        X = df.loc[df['country']==country].year
        Y = df.loc[df['country']==country].ge_gdp
        Z = df.loc[df['country']==country].ge_income_ave
        ax1 = fig1.add_subplot(3,3,i)
        ax2 = ax1.twinx()
        ax1.tick_params(axis='y')
        ax2.tick_params(axis='y',  colors ='blue')
        ax1.plot(X, Y, label = 'GDP', color ='grey')
        ax2.plot(X, Z, label = 'GDP Per Capita',  color ='blue')
        plt.title(country)
        i += 1

    ax = fig1.add_subplot(3, 3, 9)
    ax.plot([], [], label='RGDP(of Phi in 2011 =100)', color='grey')
    ax.plot([], [], label='GDP Per Capita(of Phi in 2011 =100)', color='blue')
    ax.patch.set_visible(False)
    ax.axis('off')
    ax.legend(loc='center', frameon=False)
    fig1.subplots_adjust(wspace=0.3, hspace=0.4)
    plt.show()

#gdp()


##GDP AND GDP per Capita
#trade: csh_x + csh_m
#import: csh_x
#export: csh_m
def trade():
    fig1 = plt.figure()
    fig1.suptitle('Share of Import and Export(% of RGDP)', size=18)
    i=1
    for country in countries:
        X = df.loc[df['country']==country].year
        TR = df.loc[df['country']==country].trade
        IM = -1 * df.loc[df['country']==country].csh_m
        EX = df.loc[df['country']==country].csh_x
        ax = fig1.add_subplot(3,3,i)
        ax.plot(X, TR, label = 'GDP', color ='grey')
        ax.plot(X, IM, label = 'GDP Per Capita',  color='r')
        ax.plot(X, EX, label = 'GDP Per Capita',  color='b')
        plt.title(country)
        i += 1

    ax = fig1.add_subplot(3, 3, 9)
    ax.plot([], [], label='Import + Export(% of RGDP)', color='grey')
    ax.plot([], [], label='Import(% of RGDP)', color='r')
    ax.plot([], [], label='Export(% of RGDP)', color='b')
    ax.patch.set_visible(False)
    ax.axis('off')
    ax.legend(loc='center', frameon=False)
    fig1.subplots_adjust(wspace=0.3, hspace=0.4)
    plt.show()

#trade()


##TFP LVEL
def tfp():
    fig1 = plt.figure()
    fig1.suptitle('TFP Level Against to America(Philippines in 2011 = 100)', size=18)
    i=1
    for country in countries:
        X = df.loc[df['country']==country].year
        Y = df.loc[df['country']==country].ge_gdp
        Z = df.loc[df['country']==country].ge_ctfp
        ax1 = fig1.add_subplot(3,3,i)
        ax2 = ax1.twinx()
        ax1.tick_params(axis='y')
        ax2.tick_params(axis='y',  colors ='blue')
        ax1.plot(X, Y, color ='grey')
        ax2.plot(X, Z, color ='blue')
        plt.title(country)
        i += 1

    ax = fig1.add_subplot(3, 3, 9)
    ax.plot([], [], label='RGDP(of Phi in 2011 =100)', color='grey')
    ax.plot([], [], label='TFP Level(of Phi in 2011 =100)', color='blue')
    ax.patch.set_visible(False)
    ax.axis('off')
    ax.legend(loc='center', frameon=False)
    fig1.subplots_adjust(wspace=0.3, hspace=0.4)
    plt.show()

#tfp()





ysh = pd.read_csv('BL2013_MF2599_v2.2.csv')
BLcode = ['PHL', 'VNM', 'MMR', 'PAK', 'IND', 'USA', 'JPN']
BLcountries = ['Philippines',  'Viet Nam', 'Myanmar','Pakistan', 'India', 'USA', 'Japan']
ysh = ysh[(ysh['WBcode'].isin(BLcode))]
#print(ysh['country'].unique())

def schooling():
    fig1 = plt.figure()
    fig1.suptitle('Ave Years of Schooling', size=18)
    i=1
    for country in BLcountries:
        X = ysh.loc[ysh['country']==country].year
        Ave = ysh.loc[ysh['country']==country]['yr_sch']
        Pri = ysh.loc[ysh['country']==country]['yr_sch_pri']
        Sec = ysh.loc[ysh['country']==country]['yr_sch_sec']
        Ter = ysh.loc[ysh['country']==country]['yr_sch_sec']
        ax = fig1.add_subplot(3,3,i)
        ax.set_ylim(0,15)
        ax.plot(X, Ave, color ='r')
        ax.plot(X, Pri, color ='g')
        ax.plot(X, Sec, color ='c')
        ax.plot(X, Ter, color ='m')
        plt.title(country)
        if i == 5:
            i += 2
        else:
            i +=1
    ax = fig1.add_subplot(3, 3, 9)
    ax.plot([], [], label='Average Years of Schooling Attained', color='r')
    ax.plot([], [], label='Average Years of Primary Schooling Attained', color='g')
    ax.plot([], [], label='Average Years of Secondary Schooling Attained', color='c')
    ax.plot([], [], label='Average Years of Tertirary Attained', color='m')
    ax.patch.set_visible(False)
    ax.axis('off')
    ax.legend(loc='center', frameon=False)
    fig1.subplots_adjust(wspace=0.3, hspace=0.4)
    plt.show()

#schooling()
#  yr_sch  Average Years of Schooling Attained
#  yr_sch_pri  Average Years of Primary Schooling Attained
#  yr_sch_sec  Average Years of Secondary Schooling Attained
#  yr_sch_ter  Average Years of Tertirary Schooling Attained


def pct_schooling_completed():
    fig1 = plt.figure()
    fig1.suptitle('Percentage of Schooling', size=18)
    i=1
    for country in BLcountries:
        X = ysh.loc[ysh['country']==country].year
        Ave = ysh.loc[ysh['country']==country]['lu']
        Pri = ysh.loc[ysh['country']==country]['lpc']
        Sec = ysh.loc[ysh['country']==country]['lsc']
        Ter = ysh.loc[ysh['country']==country]['lhc']
        ax = fig1.add_subplot(3,3,i)
        ax.set_ylim(0,100)
        ax.fill_between(X, 0, Pri, facecolor="#CC6666", alpha=.7)
        ax.fill_between(X, Pri, Sec, facecolor="#1DACD6", alpha=.7)
        ax.fill_between(X, Sec, Ter, facecolor="#6E5160")
        #ax.plot(X, Ave, color ='r')
        #ax.plot(X, Pri, color ='g')
        #ax.plot(X, Sec, color ='c')
        #ax.plot(X, Ter, color ='m')
        plt.title(country)
        if i == 5:
            i += 2
        else:
            i +=1
    ax = fig1.add_subplot(3, 3, 9)
    ax.plot([], [], label='Percentage of No Schooling  Attained in Pop', color='r')
    ax.plot([], [], label='Percentage of Complete Primary Schooling Attained in Pop', color='g')
    ax.plot([], [], label='Percentage of Complete Secondary Schooling Attained in Pop', color='c')
    ax.plot([], [], label='Percentage of Complete Tertiary Schooling Attained in Pop', color='m')
    ax.patch.set_visible(False)
    ax.axis('off')
    ax.legend(loc='center', frameon=False)
    fig1.subplots_adjust(wspace=0.3, hspace=0.4)
    plt.show()

#pct_schooling_completed

def pct_schooling():
    fig1 = plt.figure()
    fig1.suptitle('Percentage of Schooling in Population', size=18)
    i=1
    label = ['Primary Attained','Secondary Attained', 'Tertiary Attained','No Schooling']
    pal = ['lightblue', 'lemonchiffon', 'lightgreen', 'mistyrose']
    for country in BLcountries:
        year_of_schooling = pd.DataFrame({'year':ysh.loc[ysh['country'] == country]['year'],
                                        'Primary Attained': ysh.loc[ysh['country'] == country]['lp'],
                                          'Secondary Attained': ysh.loc[ysh['country'] == country]['ls'],
                                          'Tertiary Attained': ysh.loc[ysh['country'] == country]['lh'],
                                          'No Schooling': ysh.loc[ysh['country'] == country]['lu']})
        ax = fig1.add_subplot(3,3,i)
        X = ysh.loc[ysh['country']==country]['year']
        Pri = ysh.loc[ysh['country']==country]['lpc']
        Sec = ysh.loc[ysh['country']==country]['lsc']
        Ter = ysh.loc[ysh['country']==country]['lhc']
        ax.plot(X, Pri, color ='g', ls='--')
        ax.plot(X, Sec, color ='c', ls='--')
        ax.plot(X, Ter, color ='m', ls='--')
        ax.stackplot(year_of_schooling['year'].values, year_of_schooling.drop('year',axis=1).T, labels =label, colors=pal)
        plt.ylabel("%")
        plt.title(country)

        if i == 5:
            i += 2
        else:
            i +=1

    # legend for lone plot
    ax = fig1.add_subplot(3, 3, 9)
    ax.plot([], [], label='Percentage of Complete Primary Schooling', color='g', ls='--')
    ax.plot([], [], label='Percentage of Complete Secondary Schooling', color='c', ls='--')
    ax.plot([], [], label='Percentage of Complete Tertiary Schooling', color='m', ls='--')
    ax.patch.set_visible(False)
    ax.axis('off')
    #ax.legend(loc='center', frameon=False)

    #legend for area plot
    ax = fig1.add_subplot(3, 3, 9)
    ax.stackplot([], [[], [], [], []], labels=label, colors=pal)
    ax.patch.set_visible(False)
    ax.axis('off')
    ax.legend(loc='center', frameon=False)


    fig1.subplots_adjust(wspace=0.3, hspace=0.4)
    plt.show()


pct_schooling()