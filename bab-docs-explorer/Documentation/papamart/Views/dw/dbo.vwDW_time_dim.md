# dbo.vwDW_time_dim

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_time_dim"]
    time_dim(["time_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| time_dim |

## View Code

```sql
CREATE view vwDW_time_dim
as

SELECT     time_key, hour, minute, daypart, half_hour_id, qtr_hour_id, RIGHT('0' + CAST(hour AS varchar), 2) + RIGHT('0' + CAST(minute AS varchar), 2) 
                      AS HourMinuteKey, RIGHT('0' + CAST(hour AS varchar), 2) + ':' + RIGHT('0' + CAST(minute AS varchar), 2) AS HourMinuteDisplay, 
                      CASE WHEN hour = 0 THEN '12' WHEN hour >= 13 THEN CAST((hour - 12) AS varchar) ELSE CAST(hour AS varchar) 
                      END + ' ' + CASE WHEN hour < 13 THEN 'AM' ELSE 'PM' END AS HourDescription, 
                      CASE daypart WHEN 'Morning' THEN 1 WHEN 'Mid' THEN 2 ELSE 3 END AS dayPartKey
FROM         time_dim
WHERE     (time_key > 0)
```

