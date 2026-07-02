# esell.csaUserReportCriteria

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RETAILER_ID | int | 4 | 0 | YES |  |  |
| USER_ID | nvarchar | 200 | 0 | YES |  |  |
| ReportIdentifier | nvarchar | 240 | 0 | YES |  |  |
| UserReportName | nvarchar | 240 | 0 | YES |  |  |
| LocationAttributeTypeID | nvarchar | 160 | 1 |  |  |  |
| AttributeList | nvarchar | 510 | 1 |  |  |  |
| AttributeExpandCollapseList | nvarchar | 510 | 1 |  |  |  |
| ExpandCollapseHierarchyTypeID | int | 4 | 1 |  |  |  |
| LocationFilterTypeID | int | 4 | 1 |  |  |  |
| LocationList | nvarchar | 510 | 1 |  |  |  |
| DateTypeID | int | 4 | 1 |  |  |  |
| StartDate | datetime | 8 | 1 |  |  |  |
| EndDate | datetime | 8 | 1 |  |  |  |
| NumberOfDays | int | 4 | 1 |  |  |  |
| SRT | int | 4 | 1 |  |  |  |
| SRTORDER | nvarchar | 20 | 1 |  |  |  |
| GRP | int | 4 | 1 |  |  |  |
| UsePageBreak | nvarchar | 40 | 1 |  |  |  |
| TopNSelection | int | 4 | 1 |  |  |  |
| TopNRows | int | 4 | 1 |  |  |  |
| NoOfOrdersOverValue | int | 4 | 1 |  |  |  |
| NoStockReasonCodes | nvarchar | 510 | 1 |  |  |  |
| OrderStatuses | nvarchar | 1000 | 1 |  |  |  |
| SaveAsTypeID | int | 4 | 1 |  |  |  |

