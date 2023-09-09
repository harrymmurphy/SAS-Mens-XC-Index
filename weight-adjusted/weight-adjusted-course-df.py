"""
Load and inspect each individual race dataset. Must donwload into individual data sets because these are used as sample dataframes for the ranking method
"""
import pandas as pd
import numpy as np
# State Brandywine 11/8/2014
States_Brandy_2014 = 'https://raw.githubusercontent.com/harrymmurphy/SAS-Mens-XC-Index/main/milesplit-data/Brandywine%20States%2011_8_2014%20-%20Sheet1%20(1).csv'
States_Brandy_2014 = pd.read_csv(States_Brandy_2014)
print(States_Brandy_2014.head(5))

# State Brandywine 11/12/2016

States_Brandy_2016 = 'https://raw.githubusercontent.com/harrymmurphy/SAS-Mens-XC-Index/main/milesplit-data/Brandywine%20States%2011_12_2016%20-%20Sheet1.csv'
States_Brandy_2016 = pd.read_csv(States_Brandy_2016)
print(States_Brandy_2016.head(5))

# State Brandywine 11/10/2018
States_Brandy_2016 = 'https://raw.githubusercontent.com/harrymmurphy/SAS-Mens-XC-Index/main/milesplit-data/Brandywine%20States%2011_10_2018%20-%20Sheet1.csv'
States_Brandy_2016 = pd.read_csv(States_Brandy_2016)
print(States_Brandy_2016.head(5))

# State Brandywine 11/13/2021
States_Brandy_2021 = 'https://raw.githubusercontent.com/harrymmurphy/SAS-Mens-XC-Index/main/milesplit-data/Brandywine%20States%2011_13_2021%20-%20Sheet1.csv'
States_Brandy_2021 = pd.read_csv(States_Brandy_2021)
print(States_Brandy_2021.head(5))

# Oneill 10/19/2018
Oniell_2018 = 'https://raw.githubusercontent.com/harrymmurphy/SAS-Mens-XC-Index/main/milesplit-data/Oniell%2010_19_2018%20-%20Sheet1.csv'
Oniell_2018 = pd.read_csv(Oniell_2018)
print(Oniell_2018.head(5))

# Oneill 10/19/2019
Oniell_2019 = 'https://raw.githubusercontent.com/harrymmurphy/SAS-Mens-XC-Index/main/milesplit-data/Oniell%2010_19_2019%20-%20Sheet1.csv'
Oniell_2019 = pd.read_csv(Oniell_2019)
print(Oniell_2019.head(5))

# Oniell 10/15/2021
Oniell_2021 = 'https://raw.githubusercontent.com/harrymmurphy/SAS-Mens-XC-Index/main/milesplit-data/Oniell%2010_15_2021%20-%20Sheet1%20(1).csv'
Oniell_2021 = pd.read_csv(Oniell_2021)
print(Oniell_2021.head(5))

#Oniell 10/14/2022
Oniell_2022 = 'https://raw.githubusercontent.com/harrymmurphy/SAS-Mens-XC-Index/main/milesplit-data/Oniell%2010_14_2022%20-%20Sheet1.csv'
Oniell_2022 = pd.read_csv(Oniell_2022)
print(Oniell_2022.head(5))

# DISC 10/29/2015

DISC_2015 = 'https://raw.githubusercontent.com/harrymmurphy/SAS-Mens-XC-Index/main/milesplit-data/DISC%2010_29_2015%20-%20Sheet1.csv'
DISC_2015 = pd.read_csv(DISC_2015)
print(DISC_2015.head(5))

# DISC 10/25/2017
DISC_2017 = 'https://raw.githubusercontent.com/harrymmurphy/SAS-Mens-XC-Index/main/milesplit-data/DISC%2010_25_2017%20(Tatnall)%20-%20Sheet1.csv'
DISC_2017 = pd.read_csv(DISC_2017)
print(DISC_2017.head(5))

# DISC 10/26/2018
DISC_2018 = 'https://raw.githubusercontent.com/harrymmurphy/SAS-Mens-XC-Index/main/milesplit-data/DISC%2010_26_2018%20-%20Sheet1.csv'
DISC_2018 = pd.read_csv(DISC_2018)
print(DISC_2018.head(5))

#DISC 10/27/2022
DISC_2022 = 'https://raw.githubusercontent.com/harrymmurphy/SAS-Mens-XC-Index/main/milesplit-data/DISC%2010_27_2022%20-%20Sheet1.csv'
DISC_2022 = pd.read_csv(DISC_2022)
print(DISC_2022.head(5))

# Counties 11/04/2017
Counties_2017 = 'https://raw.githubusercontent.com/harrymmurphy/SAS-Mens-XC-Index/main/milesplit-data/Counties%2011_04_2017%20-%20Sheet1.csv'
Counties_2017 = pd.read_csv(Counties_2017)
print(Counties_2017.head(5))

# Counties 11/03/2018

Counties_2018 = 'https://raw.githubusercontent.com/harrymmurphy/SAS-Mens-XC-Index/main/milesplit-data/Counties%2011_03_2018%20-%20Sheet1.csv'
Counties_2018 = pd.read_csv(Counties_2018)
print(Counties_2018.head(5))

# Counties 11/2/2019

Counties_2019 = 'https://raw.githubusercontent.com/harrymmurphy/SAS-Mens-XC-Index/main/milesplit-data/Counties%2011_2_2019%20-%20Sheet1.csv'
Counties_2019 = pd.read_csv(Counties_2019)
print(Counties_2019.head(5))

# Counties 11/06/2021

Counties_2021 = 'https://raw.githubusercontent.com/harrymmurphy/SAS-Mens-XC-Index/main/milesplit-data/Counties%2011_26_2021%20-%20Sheet1.csv'
Counties_2021 = pd.read_csv(Counties_2021)
print(Counties_2021.head(5))

# Killens States 11/12/2011
States_Killens_2011 = 'https://raw.githubusercontent.com/harrymmurphy/SAS-Mens-XC-Index/main/milesplit-data/Killens%20States%2011_12_2011%20-%20Sheet1.csv'
States_Killens_2011 = pd.read_csv(States_Killens_2011)
print(States_Killens_2011.head(5))

# Killen States 11/11/2017

States_Killens_2017 = 'https://raw.githubusercontent.com/harrymmurphy/SAS-Mens-XC-Index/main/milesplit-data/Killens%20States%2011_11_2017%20-%20Sheet1.csv'
States_Killens_2017 = pd.read_csv(States_Killens_2017)
print(States_Killens_2017.head(5))

# Killen States 11/9/2019

States_Killens_2019 = 'https://raw.githubusercontent.com/harrymmurphy/SAS-Mens-XC-Index/main/milesplit-data/Killens%20States%2011_9_2019%20-%20Sheet1.csv'
States_Killens_2019 = pd.read_csv(States_Killens_2019)
print(States_Killens_2019.head(5))

# Killens States 11/12/2022

States_Killens_2022 ='https://raw.githubusercontent.com/harrymmurphy/SAS-Mens-XC-Index/main/milesplit-data/Killens%20States%2011_12_2022%20-%20Sheet1.csv'
States_Killens_2022 = pd.read_csv(States_Killens_2022)
print(States_Killens_2022.head(5))

def fivenum(v):
    from scipy.stats import scoreatpercentile
    try:
        np.sum(v)
    except TypeError:
        print('Error: you must provide a list or array of only numbers')
    q1 = scoreatpercentile(v,25)
    q3 = scoreatpercentile(v,75)
    iqd = q3-q1
    md = np.median(v)
    whisker = 1.5*iqd
    return np.min(v), md-whisker, md, md+whisker, np.max(v),
  

fivenum(State_Brandy_2014['Time'])

