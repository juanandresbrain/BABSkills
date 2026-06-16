# POS.POS_SalesAudit_APILog

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| IntegrationName | nvarchar | 200 | 1 |  |  |  |
| MergedJson | nvarchar | -1 | 1 |  |  |  |
| ContentType | nvarchar | 510 | 1 |  |  |  |
| ContentLength | numeric | 13 | 1 |  |  |  |
| HttpStatusCode | smallint | 2 | 1 |  |  |  |
| HttpResponseUrl | nvarchar | 4168 | 1 |  |  |  |
| HttpStatusCodeName | nvarchar | 510 | 1 |  |  |  |
| ResponseBody | nvarchar | -1 | 1 |  |  |  |
| ExceptionError | nvarchar | -1 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| HttpRequestHeaders | nvarchar | -1 | 1 |  |  |  |
| HttpRequestMethod | nvarchar | 510 | 1 |  |  |  |
| HttpRequestBody | nvarchar | 510 | 1 |  |  |  |
| HttpResponseHeaders | nvarchar | -1 | 1 |  |  |  |
| MessageID | nvarchar | 510 | 1 |  |  |  |
| Sequence | bigint | 8 | 1 |  |  |  |

