# dbo.syssessions

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| session_id | int | 4 | 0 | YES |  |  |
| agent_start_date | datetime | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [DBAUtility: dbo.spSqlAgentJobStatus](../../StoredProcedures/DBAUtility/dbo.spSqlAgentJobStatus.md)

