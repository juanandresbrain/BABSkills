# dbo.vwCustomerCubeTimeDim

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwCustomerCubeTimeDim"]
    time_dim(["time_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| time_dim |

## View Code

```sql
CREATE view [dbo].[vwCustomerCubeTimeDim]

as 

SELECT     
	time_key as TimeKey, 
	hour as TimeHour, 
	minute as TimeMinute, 
	concat(RIGHT('0' + CAST(hour AS varchar), 2), ':', RIGHT('0' + CAST(minute AS varchar), 2)) as Time,
	dense_rank() over(order by hour) as HourID,
	dense_rank() over(order by hour, minute) as MinuteID
FROM         time_dim with (nolock)
--where time_key > 0
```

