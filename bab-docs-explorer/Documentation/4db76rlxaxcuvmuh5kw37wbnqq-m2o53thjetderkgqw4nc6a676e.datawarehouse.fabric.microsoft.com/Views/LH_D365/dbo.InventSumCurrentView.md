# dbo.InventSumCurrentView

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.InventSumCurrentView"]
    dbo_d365LocationMapping_View(["dbo.d365LocationMapping_View"]) --> VIEW
    dbo_inventsum(["dbo.inventsum"]) --> VIEW
    dbo_product_dim_le(["dbo.product_dim_le"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.d365LocationMapping_View |
| dbo.inventsum |
| dbo.product_dim_le |

## View Code

```sql
CREATE   VIEW [dbo].[InventSumCurrentView]
AS
(
    SELECT
        [rows].[dataareaid] AS [dataareaid],
        [rows].[inventsiteid] AS [inventsiteid],
        [rows].[inventlocationid] AS [inventlocationid],
        [rows].[itemid] AS [itemid],
        [rows].[inventstatusid] AS [inventstatusid],
        pd.product_key AS [product_key],
        [rows].[inventlocationid] + '-' + [rows].[dataareaid] AS [LocationKey],
        SUM([rows].[closed]) AS [Closed],
        SUM([rows].[closedqty]) AS [ClosedQty],
        SUM([rows].[arrived]) AS [Arrived],
        SUM([rows].[availordered]) AS [AvailOrdered],
        SUM([rows].[deducted]) AS [Deducted],
        SUM([rows].[onorder]) AS [OnOrder],
        SUM([rows].[ordered]) AS [Ordered],
        SUM([rows].[physicalinvent]) AS [PhysicalInvent],
        SUM([rows].[physicalvalue]) AS [PhysicalValue],
        SUM([rows].[picked]) AS [Picked],
        SUM([rows].[postedqty]) AS [PostedQty],
        SUM([rows].[postedvalue]) AS [PostedValue],
        SUM([rows].[received]) AS [Received],
        SUM([rows].[registered]) AS [Registered],
        SUM([rows].[reservordered]) AS [ReservOrdered],
        SUM([rows].[reservphysical]) AS [ReservPhysical],
        SUM([rows].postedqty + [rows].received + [rows].registered - [rows].deducted - [rows].picked - [rows].reservphysical) AS Availablephysical,
        SUM([rows].ordered + [rows].arrived) AS AllocationUnit
    FROM
    (
        SELECT
            [closed],
            [closedqty],
            [arrived],
            [availordered],
            [deducted],
            [itemid],
            [onorder],
            [ordered],
            [physicalinvent],
            [physicalvalue],
            [picked],
            [postedqty],
            [postedvalue],
            [received],
            [registered],
            [reservordered],
            CASE WHEN wmslocationid IS NULL AND licenseplateid IS NULL THEN [reservphysical] ELSE 0 END [reservphysical],
            [inventlocationid],
            [inventsiteid],
            [inventstatusid],
            [dataareaid]
        FROM
            [LH_D365].[dbo].[inventsum] AS [$Table]
    ) AS [rows]
    JOIN dbo.d365LocationMapping_View locationMapping
        ON [rows].inventlocationid = locationMapping.inventlocationid AND locationMapping.legalentity = [rows].dataareaid
    JOIN LH_D365.dbo.product_dim_le pd
        ON pd.style_code = [rows].itemid AND pd.jurisdiction_code = locationMapping.JurisidictionCode AND [rows].dataareaid = pd.LegalEntity
    GROUP BY
        [dataareaid],
        [rows].[inventsiteid],
        [rows].[inventlocationid],
        [itemid],
        [inventstatusid],
        pd.product_key
);
```

