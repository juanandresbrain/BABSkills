# HR.UKPanToSageNewHireStaging

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CreatedDate | datetime | 8 | 1 |  |  |  |
| fHCM2__First_Name__c | varchar | 80 | 0 |  |  |  |
| fHCM2__Surname__c | varchar | 80 | 0 |  |  |  |
| fHCM2__Manager__c | varchar | 64 | 0 |  |  |  |
| fHCM2__Employment__c.fHCM2__Start_Date__c | date | 3 | 1 |  |  |  |
| fHCM2__Personal_Mobile__c | varchar | 40 | 1 |  |  |  |
| fHCM2__Birth_Date__c | date | 3 | 0 |  |  |  |
| National_Insurance_Number__c | varchar | 9 | 0 |  |  |  |
| fHCM2__Gender__c | varchar | 50 | 1 |  |  |  |
| Activ_Payroll_Email_Address__c | varchar | 80 | 0 |  |  |  |
| fHCM2__Employment__c.Is_a_rehire__c | varchar | 10 | 0 |  |  |  |
| fHCM2__Home_Address_1__c | varchar | 255 | 0 |  |  |  |
| asfHCM2__Home_Address_2__c | varchar | 255 | 1 |  |  |  |
| fHCM2__Home_Address_City__c | varchar | 128 | 0 |  |  |  |
| fHCM2__Home_Address_Postal_Code__c | varchar | 16 | 0 |  |  |  |
| Title__c | int | 4 | 1 |  |  |  |
| fHCM2__Department__c | varchar | 80 | 1 |  |  |  |
| fHCM2__Policy__c | varchar | 80 | 1 |  |  |  |
| Payroll_Group__c | varchar | 80 | 1 |  |  |  |
| StoreForce_User__c | varchar | 4 | 1 |  |  |  |
| fHCM2__Employment_Status__c | int | 4 | 1 |  |  |  |
| fHCM2__Employment__c.Job_Title1__c | varchar | 50 | 1 |  |  |  |
| fHCM2__Employment__c.Minimum_Weekly_Contract_Hours__c | int | 4 | 1 |  |  |  |
| fHCM2__Employment__c.Maximum_Weekly_Contract_Hours__c | int | 4 | 1 |  |  |  |
| fHCM2__Employment__c.fHCM2__Hours_Worked__c | numeric | 5 | 0 |  |  |  |
| fHCM2__Employment__c.Division__c | varchar | 255 | 1 |  |  |  |
| fHCM2__Employment__c.Business__c | int | 4 | 1 |  |  |  |
| fHCM2__Employment__c.Team__c | varchar | 50 | 1 |  |  |  |
| fHCM2__Employment__c.Function__c | int | 4 | 1 |  |  |  |
| fHCM2__Employment__c.fHCM2__Continuous_Service_Date__c | int | 4 | 1 |  |  |  |
| fHCM2__Employment__c.fHCM2__Work_Location__c | varchar | 255 | 1 |  |  |  |
| fHCM2__Employment__c.fHCM2__Basis__c | varchar | 9 | 1 |  |  |  |
| fHCM2__Employment__c.Contract_Type__c | varchar | 50 | 1 |  |  |  |
| fHCM2__Employment__c.fHCM2__Contract_End_Date__c | date | 3 | 1 |  |  |  |
| PPS_Number__c | varchar | 10 | 1 |  |  |  |
| fHCM2__Employment__c.fHCM2__Bank_Name__c | varchar | 255 | 1 |  |  |  |
| fHCM2__Employment__c.fHCM2__Account_Name__c | varchar | 255 | 1 |  |  |  |
| fHCM2__Employment__c.fHCM2__Account_No__c | varchar | 8 | 1 |  |  |  |
| fHCM2__Employment__c.fHCM2__Sort_Code__c | varchar | 6 | 1 |  |  |  |
| fHCM2__Employment__c.IBAN__c  | varchar | 30 | 1 |  |  |  |
| fHCM2__Employment__c.SWIFT__c | varchar | 30 | 1 |  |  |  |
| fHCM2__Salary__c.fHCM2__Start_Date__c | datetime | 8 | 1 |  |  |  |
| fHCM2__Salary__c.fHCM2__Period__c | varchar | 50 | 1 |  |  |  |
| fHCM2__Salary__c.fHCM2__Amount__c | numeric | 9 | 1 |  |  |  |
| fHCM2__Salary__c.fHCM2__Currency__c | varchar | 3 | 1 |  |  |  |
| fHCM2__Salary__c.fHCM2__Change_Reason__c | int | 4 | 1 |  |  |  |
| fHCM2__Salary__c.fHCM2__Annual_Multiplier__c | numeric | 9 | 1 |  |  |  |
| fHCM2__Unique_Id__c | int | 4 | 0 | YES |  |  |
| udf_Bulk_Import_Flag__c | bit | 1 | 1 |  |  |  |

