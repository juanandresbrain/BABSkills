# dbo.z_Redemption_Validate

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RefType | char | 1 | 0 |  |  |  |
| RefNo | varchar | 20 | 0 |  |  |  |
| IssuDate | char | 10 | 0 |  |  |  |
| Amount | decimal | 9 | 0 |  |  |  |
| CustNum | char | 20 | 1 |  |  |  |
| FirstName | char | 20 | 1 |  |  |  |
| LastName | char | 20 | 1 |  |  |  |
| Address | char | 40 | 1 |  |  |  |
| Address2 | char | 40 | 1 |  |  |  |
| City | char | 40 | 1 |  |  |  |
| State | char | 40 | 1 |  |  |  |
| ZipCode | char | 20 | 1 |  |  |  |
| ZipCode2 | char | 20 | 1 |  |  |  |
| Country | char | 40 | 1 |  |  |  |
| Email | char | 50 | 1 |  |  |  |
