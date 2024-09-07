
import pandas as pd

### Loading the Data

ip_data = pd.read_csv("https://data.cms.gov/sites/default/files/2023-04/67157de9-d962-4af0-bf0e-3578b3afec58/inpatient.csv", sep='|')
print(ip_data)

#access and print columns

col_names= ip_data.columns
print(col_names)

### Analyzing Medical Codex Data

#excluding codex-columns with null/missing data
emp_codex = ip_data.dropna(how= "all", axis=1)
print("\n Listed below are non empty columns: - \n")

#print non-empty columns
for column in emp_codex.columns:
    print(column)

#identifying unique medical codexes
uniq_col = emp_codex.columns.unique() [:8]

#print 8 unique non-empty columns
print("\n The 8 unique columns are: \n")

#loops through the uniq_col
for column in uniq_col:
  print(column)

#list of the 8 columns
eight_col = ['BENE_ID',
'CLM_ID', 'NCH_NEAR_LINE_REC_IDENT_CD', 'NCH_CLM_TYPE_CD', 'CLM_FROM_DT',
'CLM_THRU_DT',
'NCH_WKLY_PROC_DT',
'CLAIM_QUERY_CODE']

#get the count of unique values for each column
unique_val = {col: ip_data[col].nunique() for col in eight_col}

#print the counts
for col, count in unique_val.items():
  print (f"\nFrequency count of unique values in column {col}: {count}\n")


#print the first 5 unique values in the columns
for col in eight_col:
    unique_vals = ip_data[col].unique()
    print(f"\nFirst 5 unique values in column '{col}':")
    print(unique_vals[:5])

#analyzing the most frequent values in certain columns
# lists out 20 claim total charge amounts and the most frequent amount
# lists out 20 principal diagnosis codes and the most frequent dx code
# lists out 20 hcpcs codes and the most frequent hcpcs code

test_col=['CLM_TOT_CHRG_AMT', 'PRNCPAL_DGNS_CD', 'HCPCS_CD']

for col in test_col:
    unique_vals = ip_data[col].unique()
    print(f"\nFirst 20 values in column '{col}':")
    print(ip_data[col].head(20))
    freq_val = ip_data[col].mode()[0]
    print(f"\n The most frequently occuring values in column {col} is: {freq_val}")
    print(freq_val)



