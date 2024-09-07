# Discovering Medical Codexes within Synthetic Medicare Fee-for-Service Claims Data

The data was loaded from Data.CMS.gov
It was difficult to understand when loading the data initially at it had all the columns and values. 

I first began with analyzing the columns only. I listed out the columns.
Next, I removed columns with null or missing data

I then identified 8 unique columns from the list. 

Within each column, I extracted unique values and their counts

### Additional analysis

Next, I went through the initial list of columns and looked into the most interesting ones. I looked at the claim charge amount, the principal diagnosis codes and the hcpcs code. 

The most frequently occuring value in the claim charge amount column was $950.31

The most frequently occuring value in the principal diagnosis codes column was Z733. Upon a simple google search, I was able to find that Z73 relates to Problems related to life-management difficulty. Behavorial health has taken a big leap in the current healthcare landscape and it was evident in this data. 

The most frequently occuring HCPCS code was 99221. Another google search showed that the code is used when a patient is admitted to the hospital for a condition of low complexity. This seemed straightforward and rational 
