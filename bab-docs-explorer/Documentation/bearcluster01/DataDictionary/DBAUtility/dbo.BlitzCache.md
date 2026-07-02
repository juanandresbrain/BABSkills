# dbo.BlitzCache

**Database:** DBAUtility  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | bigint | 8 | 0 | YES |  |  |
| ServerName | nvarchar | 516 | 1 |  |  |  |
| CheckDate | datetimeoffset | 10 | 1 |  |  |  |
| Version | nvarchar | 516 | 1 |  |  |  |
| QueryType | nvarchar | 516 | 1 |  |  |  |
| Warnings | varchar | -1 | 1 |  |  |  |
| DatabaseName | sysname | 256 | 0 |  |  |  |
| SerialDesiredMemory | float | 8 | 1 |  |  |  |
| SerialRequiredMemory | float | 8 | 1 |  |  |  |
| AverageCPU | bigint | 8 | 1 |  |  |  |
| TotalCPU | bigint | 8 | 1 |  |  |  |
| PercentCPUByType | money | 8 | 1 |  |  |  |
| CPUWeight | money | 8 | 1 |  |  |  |
| AverageDuration | bigint | 8 | 1 |  |  |  |
| TotalDuration | bigint | 8 | 1 |  |  |  |
| DurationWeight | money | 8 | 1 |  |  |  |
| PercentDurationByType | money | 8 | 1 |  |  |  |
| AverageReads | bigint | 8 | 1 |  |  |  |
| TotalReads | bigint | 8 | 1 |  |  |  |
| ReadWeight | money | 8 | 1 |  |  |  |
| PercentReadsByType | money | 8 | 1 |  |  |  |
| AverageWrites | bigint | 8 | 1 |  |  |  |
| TotalWrites | bigint | 8 | 1 |  |  |  |
| WriteWeight | money | 8 | 1 |  |  |  |
| PercentWritesByType | money | 8 | 1 |  |  |  |
| ExecutionCount | bigint | 8 | 1 |  |  |  |
| ExecutionWeight | money | 8 | 1 |  |  |  |
| PercentExecutionsByType | money | 8 | 1 |  |  |  |
| ExecutionsPerMinute | money | 8 | 1 |  |  |  |
| PlanCreationTime | datetime | 8 | 1 |  |  |  |
| PlanCreationTimeHours | int | 4 | 1 |  |  |  |
| LastExecutionTime | datetime | 8 | 1 |  |  |  |
| PlanHandle | varbinary | 64 | 1 |  |  |  |
| Remove Plan Handle From Cache | varchar | 150 | 1 |  |  |  |
| SqlHandle | varbinary | 64 | 1 |  |  |  |
| Remove SQL Handle From Cache | varchar | 150 | 1 |  |  |  |
| SQL Handle More Info | varchar | 169 | 1 |  |  |  |
| QueryHash | binary | 8 | 1 |  |  |  |
| Query Hash More Info | varchar | 74 | 1 |  |  |  |
| QueryPlanHash | binary | 8 | 1 |  |  |  |
| StatementStartOffset | int | 4 | 1 |  |  |  |
| StatementEndOffset | int | 4 | 1 |  |  |  |
| MinReturnedRows | bigint | 8 | 1 |  |  |  |
| MaxReturnedRows | bigint | 8 | 1 |  |  |  |
| AverageReturnedRows | money | 8 | 1 |  |  |  |
| TotalReturnedRows | bigint | 8 | 1 |  |  |  |
| QueryText | nvarchar | -1 | 1 |  |  |  |
| QueryPlan | xml | -1 | 1 |  |  |  |
| NumberOfPlans | int | 4 | 1 |  |  |  |
| NumberOfDistinctPlans | int | 4 | 1 |  |  |  |
| MinGrantKB | bigint | 8 | 1 |  |  |  |
| MaxGrantKB | bigint | 8 | 1 |  |  |  |
| MinUsedGrantKB | bigint | 8 | 1 |  |  |  |
| MaxUsedGrantKB | bigint | 8 | 1 |  |  |  |
| PercentMemoryGrantUsed | money | 8 | 1 |  |  |  |
| AvgMaxMemoryGrant | money | 8 | 1 |  |  |  |
| MinSpills | bigint | 8 | 1 |  |  |  |
| MaxSpills | bigint | 8 | 1 |  |  |  |
| TotalSpills | bigint | 8 | 1 |  |  |  |
| AvgSpills | money | 8 | 1 |  |  |  |
| QueryPlanCost | float | 8 | 1 |  |  |  |

