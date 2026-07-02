# dbo.aspnet_WebEvent_Events

**Database:** ApplicationResources  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EventId | char | 32 | 0 | YES |  |  |
| EventTimeUtc | datetime | 8 | 0 |  |  |  |
| EventTime | datetime | 8 | 0 |  |  |  |
| EventType | nvarchar | 512 | 0 |  |  |  |
| EventSequence | decimal | 9 | 0 |  |  |  |
| EventOccurrence | decimal | 9 | 0 |  |  |  |
| EventCode | int | 4 | 0 |  |  |  |
| EventDetailCode | int | 4 | 0 |  |  |  |
| Message | nvarchar | 2048 | 1 |  |  |  |
| ApplicationPath | nvarchar | 512 | 1 |  |  |  |
| ApplicationVirtualPath | nvarchar | 512 | 1 |  |  |  |
| MachineName | nvarchar | 512 | 0 |  |  |  |
| RequestUrl | nvarchar | 2048 | 1 |  |  |  |
| ExceptionType | nvarchar | 512 | 1 |  |  |  |
| Details | ntext | 16 | 1 |  |  |  |

