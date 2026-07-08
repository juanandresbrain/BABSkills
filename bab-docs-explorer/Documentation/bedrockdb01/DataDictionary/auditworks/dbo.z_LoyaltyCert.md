# dbo.z_LoyaltyCert

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ProcRule | char | 1 | 0 |  |  |  |
| RefNo | varchar | 20 | 0 |  |  |  |
| IssuDate | char | 10 | 0 |  |  |  |
| Amount | decimal | 9 | 0 |  |  |  |
| IssuStore | int | 4 | 1 |  |  |  |
| UPC | varchar | 14 | 1 |  |  |  |
| PosId | char | 20 | 1 |  |  |  |
| Units | char | 11 | 1 |  |  |  |
| CustNum | char | 20 | 1 |  |  |  |
| EmpNum | char | 10 | 1 |  |  |  |
| Title | char | 10 | 1 |  |  |  |
| FirstName | char | 20 | 1 |  |  |  |
| LastName | char | 20 | 1 |  |  |  |
| Address | char | 40 | 1 |  |  |  |
| Address2 | char | 40 | 1 |  |  |  |
| City | char | 40 | 1 |  |  |  |
| County | char | 40 | 1 |  |  |  |
| State | char | 40 | 1 |  |  |  |
| Country | char | 40 | 1 |  |  |  |
| ZipCode | char | 20 | 1 |  |  |  |
| Tax | char | 20 | 1 |  |  |  |
| Phone | char | 16 | 1 |  |  |  |
| Phone2 | char | 16 | 1 |  |  |  |
| Fax | char | 16 | 1 |  |  |  |
| Email | char | 50 | 1 |  |  |  |
| ReplaceNum | char | 20 | 1 |  |  |  |
| DestStore | char | 10 | 1 |  |  |  |
| ExpireDate | char | 10 | 1 |  |  |  |
