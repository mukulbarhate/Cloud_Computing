#find the highest salary for recent 7 days
import pandas as pd

data = pd.read_csv('data.csv')
print(data)
df = pd.DataFrame(data)
print(df)
d = df.sort_values(by='JoiningDate',ascending=False)
print(d)
grouped = d.groupby(by='JoiningDate',sort=False).apply(lambda x: x.loc[x['Salary'].idxmax()]).head(7)
print("First 7 emp : ",grouped)

df=pd.DataFrame(data)

##for age 21-30
age_21_30=df[(df['Age']>=21) & (df['Age']<=30)]['Salary'].sum()
count_21_30=df[(df['Age']>=21) & (df['Age']<=30)]['Age'].count()
print("Total emp between Age 21-30 :--",count_21_30)
print("Sum of age 21-30",age_21_30)
print()

##for age 31-40
count_31_40=df[(df['Age']>=31) & (df['Age']<=40)]["Age"].count()
age_31_40=df[(df['Age']>=31) & (df['Age']<=40)]['Salary'].sum()
print("Total emp between Age 31-40 :--",count_31_40)
print("Sum of age 21-30",age_31_40)
print()

##for age 41-50
count_41_50=df[(df['Age']>=41) & (df['Age']<=50)]["Age"].count()
age_41_50=df[(df['Age']>=41) & (df['Age']<=50)]['Salary'].sum()
print("Total emp between Age 41-50 :--",count_41_50)
print("Sum of age 41-50",age_41_50)
print()

#avg group wise
grp1=age_21_30/count_21_30
grp2=age_31_40/count_31_40
grp3=age_41_50/count_41_50

data={"Age_wise":["age_21_30","age_31_40","age_41_50"],"Sum_agewise":[age_21_30,age_31_40,age_41_50],"Avg_salaray":[grp1,grp2,grp3]}
new_df=pd.DataFrame(data)
print(new_df)

with pd.ExcelWriter('Sorted_emplyoee.xlsx') as mywriter:
    grouped.to_excel(mywriter, sheet_name='Sheet1',index=False)
    new_df.to_excel(mywriter, sheet_name='Sheet2',index=False)