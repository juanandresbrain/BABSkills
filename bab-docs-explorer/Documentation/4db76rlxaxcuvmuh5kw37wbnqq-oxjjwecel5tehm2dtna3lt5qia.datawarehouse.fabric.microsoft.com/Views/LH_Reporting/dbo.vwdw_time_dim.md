# dbo.vwdw_time_dim

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_time_dim"]
    dbo_time_dim(["dbo.time_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.time_dim |

## View Code

```sql
CREATE VIEW vwdw_time_dim 
AS
SELECT time_key
	,ISNULL([hour], - 1) AS [hour]
	,ISNULL([minute], - 1) AS [minute]
	,ISNULL(daypart, 'N/A') AS daypart
	,ISNULL(half_hour_id, - 1) AS half_hour_id
	,ISNULL(qtr_hour_id, - 1) AS qtr_hour_id
	,ISNULL(RIGHT('0' + CAST([hour] AS VARCHAR), 2) + RIGHT('0' + CAST([minute] AS VARCHAR), 2), 'N/A') AS HourMinuteKey
	,ISNULL(RIGHT('0' + CAST([hour] AS VARCHAR), 2) + ':' + RIGHT('0' + CAST([minute] AS VARCHAR), 2), 'N/A') AS HourMinuteDisplay
	,CASE 
		WHEN time_key = 0
			THEN 'N/A'
		ELSE CASE 
				WHEN [hour] = 0
					THEN '12'
				WHEN [hour] >= 13
					THEN CAST(([hour] - 12) AS VARCHAR)
				ELSE CAST([hour] AS VARCHAR)
				END + ' ' + CASE 
				WHEN [hour] < 12
					THEN 'AM'
				ELSE 'PM'
				END
		END AS HourDescription
	,CASE 
		WHEN time_key = 0
			THEN 'N/A'
		ELSE CASE 
				WHEN [hour] = 0
					THEN '12'
				WHEN [hour] >= 13
					THEN CAST(([hour] - 12) AS VARCHAR)
				ELSE CAST([hour] AS VARCHAR)
				END + ':' + CASE 
				WHEN half_hour_id = 1
					THEN '00'
				ELSE '30'
				END + ' ' + CASE 
				WHEN [hour] < 12
					THEN 'AM'
				ELSE 'PM'
				END
		END AS HalfHourDescription
	,ISNULL([hour] * 10 + half_hour_id, - 1) AS HalfHourKey
	,CASE 
		WHEN time_key = 0
			THEN 'N/A'
		ELSE CASE 
				WHEN [hour] = 0
					THEN '12'
				WHEN [hour] >= 13
					THEN CAST(([hour] - 12) AS VARCHAR)
				ELSE CAST([hour] AS VARCHAR)
				END + ':' + CASE 
				WHEN qtr_hour_id = 1
					THEN '00'
				WHEN qtr_hour_id = 2
					THEN '15'
				WHEN qtr_hour_id = 3
					THEN '30'
				ELSE '45'
				END + ' ' + CASE 
				WHEN [hour] < 12
					THEN 'AM'
				ELSE 'PM'
				END
		END AS QuarterHourDescription
	,ISNULL([hour] * 10 + qtr_hour_id, - 1) AS QuarterHourKey
	,CASE daypart
		WHEN 'Morning'
			THEN 1
		WHEN 'Mid'
			THEN 2
		ELSE 3
		END AS dayPartKey
FROM LH_Mart.dbo.time_dim
WHERE (time_key >= 0)
```

