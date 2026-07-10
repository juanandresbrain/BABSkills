# dbo.SPWebLimboOrdersByDateRange

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SPWebLimboOrdersByDateRange"]
    dbo_OrderGroup(["dbo.OrderGroup"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.OrderGroup |

## Stored Procedure Code

```sql
CREATE PROCEDURE SPWebLimboOrdersByDateRange
	@BeginDate datetime, 
	@EndDate datetime
AS 


SET @EndDate=dateadd(dd,1,@EndDate)

--Order Detail
SELECT    convert(varchar(12),d_DateCreated,101) PlacedDate,
          order_number,
          saved_cy_total_total Dollars,
          SiteCode,
	  CASE isnull(order_status_code,0)
		WHEN 4 THEN 'Pending'
		WHEN 8 THEN 'Processing'
		ELSE  'UNknown'
	  END as order_status
FROM       BearWebDB.WebCart_Commerce.dbo.OrderGroup 
WHERE     order_create_date>'10/19/2004' and
          order_create_date>=@BeginDate and 
          order_create_date<@EndDate and
          isnull(order_status_code,0) not in (16,32,64)
```

