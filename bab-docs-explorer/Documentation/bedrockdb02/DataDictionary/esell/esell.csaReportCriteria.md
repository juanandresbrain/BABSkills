# esell.csaReportCriteria

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RETAILER_ID | int | 4 | 0 | YES |  |  |
| RequestIdentifier | nvarchar | 200 | 0 | YES |  |  |
| ReportIdentifier | nvarchar | 240 | 0 | YES |  |  |
| LocationAttributeTypeID | nvarchar | 160 | 1 |  |  |  |
| LocationAttributeTypeDesc | nvarchar | 510 | 1 |  |  |  |
| ExpandCollapseHierarchyTypeID | int | 4 | 1 |  |  |  |
| AttributeLvl | int | 4 | 1 |  |  |  |
| AttributeList | nvarchar | 510 | 1 |  |  |  |
| AttributeListDesc | nvarchar | 510 | 1 |  |  |  |
| LocationList | nvarchar | 510 | 1 |  |  |  |
| LenLocationList | int | 4 | 1 |  |  |  |
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
| NoStockReasonCodesDesc | nvarchar | 510 | 1 |  |  |  |
| LenNoStockReasonCodes | int | 4 | 1 |  |  |  |
| OrderStatuses | nvarchar | 1000 | 1 |  |  |  |
| OrderStatusesDesc | nvarchar | 1000 | 1 |  |  |  |
| LenOrderStatuses | int | 4 | 1 |  |  |  |
| DivisionIdLen | int | 4 | 1 |  |  |  |

