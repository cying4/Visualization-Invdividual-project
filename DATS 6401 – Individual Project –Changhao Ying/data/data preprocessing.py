import numpy as np
import pandas as pd

#%%
military_gdp_raw=pd.read_excel('military.xls',header = 3,index_col = 0)
health_gdp_raw=pd.read_excel('health.xls',header = 3,index_col=0)
education_gdp_raw=pd.read_excel('education.xls',header = 3,index_col=0)
gdp_raw=pd.read_excel('gdp.xls',header=3,index_col = 0)
population_raw=pd.read_excel('population.xls',header=3,index_col = 0)
#%%
education_gdp_raw.head(5)

#%%
import warnings
warnings.filterwarnings('ignore')
military_gdp = military_gdp_raw.ix[['United Kingdom','Brazil','Germany','France', 'Italy','Mexico', 'Argentina','Switzerland', 'Australia','Indonesia'],['2011','2012','2013','2014','2015']]
health_gdp = health_gdp_raw.ix[['United Kingdom','Brazil','Germany','France', 'Italy','Mexico', 'Argentina','Switzerland', 'Australia','Indonesia'],['2011','2012','2013','2014','2015']]
education_gdp = education_gdp_raw.ix[['United Kingdom','Brazil','Germany','France', 'Italy','Mexico', 'Argentina','Switzerland', 'Australia','Indonesia'],['2011','2012','2013','2014','2015']]
gdp = gdp_raw.ix[['United Kingdom','Brazil','Germany','France', 'Italy','Mexico', 'Argentina','Switzerland', 'Australia','Indonesia'],['2011','2012','2013','2014','2015']]
population = population_raw.ix[['United Kingdom','Brazil','Germany','France', 'Italy','Mexico', 'Argentina','Switzerland', 'Australia','Indonesia'],['2011','2012','2013','2014','2015']]

#%%
population.head(5)

#%%
military_total_exp = military_gdp*gdp/100
health_total_exp = health_gdp*gdp/100
education_total_exp = education_gdp*gdp/100

#%%
military_total_exp1=military_total_exp.T
health_total_exp1=health_total_exp.T
education_total_exp1=education_total_exp.T
gdp1=gdp.T
#%%
mean_military = np.mean(military_total_exp, axis=1)
mean_health = np.mean(health_total_exp,axis=1)
mean_education = np.mean(education_total_exp,axis=1)
mean_gdp = np.mean(gdp,axis=1)

#%%
mean_education.describe()

#%%
military_mean= pd.DataFrame(mean_military)
health_mean= pd.DataFrame(mean_health)
education_mean= pd.DataFrame(mean_education)
gdp_mean= pd.DataFrame(mean_gdp)
military_mean.columns = ['military']
health_mean.columns = ['health']
education_mean.columns = ['education']
gdp_mean.columns = ['gdp']
#%%
education_mean.head(10)
#%%
overall = [military_mean,health_mean,education_mean,gdp_mean]
overall_mean = pd.concat(overall,axis=1)
overall_mean.head(10)
#%%
military_per = military_total_exp/population
health_per = health_total_exp/population
education_per = education_total_exp/population
gdp_per = gdp/population

#%%
military_per.head(5)

#%%
military_capita = np.mean(military_per, axis=1)
health_capita = np.mean(health_per,axis=1)
education_capita = np.mean(education_per,axis=1)
gdp_capita = np.mean(gdp_per,axis=1)
#%%
military_ca= pd.DataFrame(military_capita)
health_ca= pd.DataFrame(military_capita)
education_ca= pd.DataFrame(education_capita)
gdp_ca= pd.DataFrame(gdp_capita)
military_ca.columns = ['military']
health_ca.columns = ['health']
education_ca.columns = ['education']
gdp_ca.columns = ['gdp']
#%%
overall1 = [military_ca,health_ca,education_ca,gdp_ca]
overall_capita = pd.concat(overall1,axis=1)
overall_capita.head(10)

#%%
with pd.ExcelWriter('data.xlsx') as writer:
    military_total_exp1.to_excel(writer, sheet_name='military expenditure')
    health_total_exp1.to_excel(writer, sheet_name='health expenditure')
    education_total_exp1.to_excel(writer, sheet_name='education expenditure')
    overall_mean.to_excel(writer, sheet_name='mean expenditure')
    gdp1.to_excel(writer, sheet_name='gdp expenditure')
    military_per.to_excel(writer, sheet_name='military expenditure per person')
    health_per.to_excel(writer, sheet_name='health expenditure per person')
    education_per.to_excel(writer, sheet_name='edu expenditure per person')
    gdp_per.to_excel(writer, sheet_name='gdp expenditure per person')
    overall_capita.to_excel(writer,sheet_name='expcapita')
