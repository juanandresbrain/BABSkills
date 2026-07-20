# dbo.it_commworks_stage

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | bigint | 8 | 1 |  |  |  |
| summary | varchar | 8000 | 1 |  |  |  |
| recordType | bigint | 8 | 1 |  |  |  |
| boardName | varchar | 8000 | 1 |  |  |  |
| statusName | varchar | 8000 | 1 |  |  |  |
| companyName | varchar | 8000 | 1 |  |  |  |
| siteName | varchar | 8000 | 1 |  |  |  |
| addressLine1 | varchar | 8000 | 1 |  |  |  |
| addressLine2 | varchar | 8000 | 1 |  |  |  |
| city | varchar | 8000 | 1 |  |  |  |
| stateIdentifier | varchar | 8000 | 1 |  |  |  |
| zip | varchar | 8000 | 1 |  |  |  |
| countryName | varchar | 8000 | 1 |  |  |  |
| contactName | varchar | 8000 | 1 |  |  |  |
| contactPhoneNumber | varchar | 8000 | 1 |  |  |  |
| contactPhoneExtension | varchar | 8000 | 1 |  |  |  |
| contactEmailAddress | varchar | 8000 | 1 |  |  |  |
| typeName | varchar | 8000 | 1 |  |  |  |
| itemName | varchar | 8000 | 1 |  |  |  |
| priorityName | varchar | 8000 | 1 |  |  |  |
| prioritySort | bigint | 8 | 1 |  |  |  |
| severity | bigint | 8 | 1 |  |  |  |
| impact | bigint | 8 | 1 |  |  |  |
| closedDate | varchar | 8000 | 1 |  |  |  |
| closedBy | varchar | 8000 | 1 |  |  |  |
| closedFlag | bit | 1 | 1 |  |  |  |
| actualHours | varchar | 8000 | 1 |  |  |  |
| approved | bit | 1 | 1 |  |  |  |
| dateResolved | varchar | 8000 | 1 |  |  |  |
| dateResplan | varchar | 8000 | 1 |  |  |  |
| dateResponded | datetime2 | 8 | 1 |  |  |  |
| resolveMinutes | bigint | 8 | 1 |  |  |  |
| resPlanMinutes | bigint | 8 | 1 |  |  |  |
| respondMinutes | bigint | 8 | 1 |  |  |  |
| isInSla | bit | 1 | 1 |  |  |  |
| resources | varchar | 8000 | 1 |  |  |  |
| parentTicketId | varchar | 8000 | 1 |  |  |  |
| hasChildTicket | bit | 1 | 1 |  |  |  |
| lastUpdated | datetime2 | 8 | 1 |  |  |  |
| updatedBy | varchar | 8000 | 1 |  |  |  |
| dateEntered1 | datetime2 | 8 | 1 |  |  |  |
| enteredBy1 | varchar | 8000 | 1 |  |  |  |
| subTypeName | varchar | 8000 | 1 |  |  |  |
| carrierTicket | varchar | 8000 | 1 |  |  |  |
