import pandas as pd 
data = pd.read_csv("C:\HAP672\dr_min_data(4).csv")
data 

snomed = pd.read_csv("C:\HAP672\snomed1.csv", encoding='iso-8859-1')
snomed

data['patient_id'].nunique()

for i in data['diagnosis1']:
    if "." in i:
        print("dot:", i)
    else:
        print(i)

snomed['SNOMED_CID'].nunique()

snomed['ICD_CODE'].nunique()

snomed.sort_values(by=['SNOMED_CID','ICD_CODE'])

df_1 = data.merge(snomed, left_on='diagnosis1',right_on= 'ICD_CODE' , how='left')
df_2 = data.merge(snomed, left_on='diagnosis2',right_on= 'ICD_CODE' , how='left')
df_3 = data.merge(snomed, left_on='diagnosis3',right_on= 'ICD_CODE' , how='left')
df_4 = data.merge(snomed, left_on='diagnosis4',right_on= 'ICD_CODE' , how='left')
df_5 = data.merge(snomed, left_on='diagnosis5',right_on= 'ICD_CODE' , how='left')

df_1.drop_duplicates()

cols_1 = ['patient_id' , 'diagnosis1','ICD_CODE''SNOMED_CID']
cols_2 = ['patient_id' , 'diagnosis2','ICD_CODE''SNOMED_CID']
cols_3 = ['patient_id' , 'diagnosis3','ICD_CODE''SNOMED_CID']
cols_4 = ['patient_id' , 'diagnosis4','ICD_CODE''SNOMED_CID']
cols_5 = ['patient_id' , 'diagnosis5','ICD_CODE''SNOMED_CID']

# Rename columns
df_1.rename(columns={"ICD_CODE": "ICD_CODE1", "SNOMED_CID": "SNOMED_CID1"}, inplace=True)
df_2.rename(columns={"ICD_CODE": "ICD_CODE2", "SNOMED_CID": "SNOMED_CID2"}, inplace=True)
df_3.rename(columns={"ICD_CODE": "ICD_CODE3", "SNOMED_CID": "SNOMED_CID3"}, inplace=True)
df_4.rename(columns={"ICD_CODE": "ICD_CODE4", "SNOMED_CID": "SNOMED_CID4"}, inplace=True)
df_5.rename(columns={"ICD_CODE": "ICD_CODE5", "SNOMED_CID": "SNOMED_CID5"}, inplace=True)

df_1=df_1[['patient_id','diagnosis1','SNOMED_CID1']]
df_2=df_2[['patient_id','diagnosis2','SNOMED_CID2']]
df_3=df_3[['patient_id','diagnosis3','SNOMED_CID3']]
df_4=df_4[['patient_id','diagnosis4','SNOMED_CID4']]
df_5=df_5[['patient_id','diagnosis5','SNOMED_CID5']]

dfm = pd.merge(df_1,df_2, on='patient_id', how='left')
dfm2 = pd.merge(dfm,df_3, on='patient_id', how='left')
dfm3 = pd.merge(dfm2,df_4, on='patient_id', how='left')
dfm4 = pd.merge(dfm3,df_5, on='patient_id', how='left')

dfm4_unique = dfm4.drop


dfm4_unique = dfm4.drop_duplicates(subset='patient_id')


dfm4_unique = dfm4.drop_duplicates(subset='patient_id', keep='last')


dfm4.drop_duplicates()

dfm4.to_csv("C:/HAP672/SNOMEDfinal.csv")