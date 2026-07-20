# dbo.vwInventSum

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwInventSum"]
    dbo_inventsum(["dbo.inventsum"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.inventsum |

## View Code

```sql
CREATE   VIEW [dbo].[vwInventSum] AS (     SELECT         [rows].[dataareaid] AS [dataareaid],         [rows].[inventsiteid] AS [inventsiteid],         [rows].[inventlocationid] AS [inventlocationid],         [rows].[itemid] AS [itemid],         [rows].[inventstatusid] AS [inventstatusid],         SUM([rows].[closed]) AS [Closed],         SUM([rows].[closedqty]) AS [ClosedQty],         SUM([rows].[arrived]) AS [Arrived],         SUM([rows].[availordered]) AS [AvailOrdered],         SUM([rows].[deducted]) AS [Deducted],         SUM([rows].[onorder]) AS [OnOrder],         SUM([rows].[ordered]) AS [Ordered],         SUM([rows].[physicalinvent]) AS [PhysicalInvent],         SUM([rows].[physicalvalue]) AS [PhysicalValue],         SUM([rows].[picked]) AS [Picked],         SUM([rows].[postedqty]) AS [PostedQty],         SUM([rows].[postedvalue]) AS [PostedValue],         SUM([rows].[received]) AS [Received],         SUM([rows].[registered]) AS [Registered],         SUM([rows].[reservordered]) AS [ReservOrdered],         SUM([rows].[reservphysical]) AS [ReservPhysical]     FROM     (         SELECT             [closed],             [closedqty],             [arrived],             [availordered],             [deducted],             [itemid],             [onorder],             [ordered],             [physicalinvent],             [physicalvalue],             [picked],             [postedqty],             [postedvalue],             [received],             [registered],             [reservordered],             [reservphysical],             [inventlocationid],             [inventsiteid],             [inventstatusid],             [dataareaid]         FROM             [LH_D365].[dbo].[inventsum] AS [$Table]     ) AS [rows]     GROUP BY         [dataareaid],         [inventsiteid],         [inventlocationid],         [itemid],         [inventstatusid] );
```

