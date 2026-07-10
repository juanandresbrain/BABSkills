# dbo.IT_commworks_stage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | bigint | 8 | 1 |  |  |  |
| summary | nvarchar | -1 | 1 |  |  |  |
| recordType | bigint | 8 | 1 |  |  |  |
| boardName | nvarchar | 510 | 1 |  |  |  |
| statusName | nvarchar | 510 | 1 |  |  |  |
| companyName | nvarchar | 510 | 1 |  |  |  |
| siteName | nvarchar | 510 | 1 |  |  |  |
| addressLine1 | nvarchar | 510 | 1 |  |  |  |
| addressLine2 | nvarchar | 510 | 1 |  |  |  |
| city | nvarchar | 510 | 1 |  |  |  |
| stateIdentifier | nvarchar | 100 | 1 |  |  |  |
| zip | nvarchar | 100 | 1 |  |  |  |
| countryName | nvarchar | 510 | 1 |  |  |  |
| contactName | nvarchar | 510 | 1 |  |  |  |
| contactPhoneNumber | nvarchar | 100 | 1 |  |  |  |
| contactPhoneExtension | ntext | 16 | 1 |  |  |  |
| contactEmailAddress | nvarchar | 510 | 1 |  |  |  |
| typeName | nvarchar | 510 | 1 |  |  |  |
| itemName | nvarchar | 510 | 1 |  |  |  |
| priorityName | nvarchar | 510 | 1 |  |  |  |
| prioritySort | bigint | 8 | 1 |  |  |  |
| severity | bigint | 8 | 1 |  |  |  |
| impact | bigint | 8 | 1 |  |  |  |
| closedDate | ntext | 16 | 1 |  |  |  |
| closedBy | ntext | 16 | 1 |  |  |  |
| closedFlag | bit | 1 | 1 |  |  |  |
| actualHours | ntext | 16 | 1 |  |  |  |
| approved | bit | 1 | 1 |  |  |  |
| dateResolved | ntext | 16 | 1 |  |  |  |
| dateResplan | ntext | 16 | 1 |  |  |  |
| dateResponded | datetime | 8 | 1 |  |  |  |
| resolveMinutes | bigint | 8 | 1 |  |  |  |
| resPlanMinutes | bigint | 8 | 1 |  |  |  |
| respondMinutes | bigint | 8 | 1 |  |  |  |
| isInSla | bit | 1 | 1 |  |  |  |
| resources | ntext | 16 | 1 |  |  |  |
| parentTicketId | ntext | 16 | 1 |  |  |  |
| hasChildTicket | bit | 1 | 1 |  |  |  |
| lastUpdated | datetime | 8 | 1 |  |  |  |
| updatedBy | nvarchar | 100 | 1 |  |  |  |
| dateEntered1 | datetime | 8 | 1 |  |  |  |
| enteredBy1 | nvarchar | 100 | 1 |  |  |  |
| subTypeName | nvarchar | 510 | 1 |  |  |  |
| carrierTicket | ntext | 16 | 1 |  |  |  |
