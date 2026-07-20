# dbo.vwdw_store_newhearme

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_store_newhearme"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIEW dbo.vwdw_store_newhearme (
  store_key,
  startingDate)
AS SELECT 105 AS store_key, CAST('2011-05-10' AS DATETIME2(6)) AS startingDate
UNION ALL SELECT 48 AS store_key, CAST('2011-08-10' AS DATETIME2(6)) AS startingDate
UNION ALL SELECT 210 AS store_key, CAST('2011-07-09' AS DATETIME2(6)) AS startingDate -- Store 200 MOA
UNION ALL SELECT 324 AS store_key, CAST('2011-09-14' AS DATETIME2(6)) AS startingDate -- Store 248 La Plaza
UNION ALL SELECT 55 AS store_key, CAST('2011-09-15' AS DATETIME2(6)) AS startingDate -- Store 055 Baybrook
UNION ALL SELECT 100 AS store_key, CAST('2011-09-20' AS DATETIME2(6)) AS startingDate -- Roosevelt Field
UNION ALL SELECT 3 AS store_key, CAST('2011-04-10' AS DATETIME2(6)) AS startingDate -- Woodfield Mall
UNION ALL SELECT 4 AS store_key, CAST('2011-07-10' AS DATETIME2(6)) AS startingDate -- Oakbrook Center
UNION ALL SELECT 16 AS store_key, CAST('2011-12-10' AS DATETIME2(6)) AS startingDate -- Easton
UNION ALL SELECT 1 AS store_key, CAST('2011-10-19' AS DATETIME2(6)) AS startingDate -- Galleria (REAL IMPLEMENTATION)
UNION ALL SELECT 46 AS store_key, CAST('2012-01-01' AS DATETIME2(6)) AS startingDate -- Washington Square
UNION ALL SELECT 19 AS store_key, CAST('2012-01-04' AS DATETIME2(6)) AS startingDate -- Opry Mills
UNION ALL SELECT 56 AS store_key, CAST('2012-04-30' AS DATETIME2(6)) AS startingDate -- Ross Park
UNION ALL SELECT 38 AS store_key, CAST('2012-12-05' AS DATETIME2(6)) AS startingDate -- Rivertown
UNION ALL SELECT 281 AS store_key, CAST('2012-01-06' AS DATETIME2(6)) AS startingDate -- 2019 (Hamley's)
UNION ALL SELECT 615 AS store_key, CAST('2012-06-22' AS DATETIME2(6)) AS startingDate -- 603 Gurnee Mills POP
UNION ALL SELECT 64 AS store_key, CAST('2012-12-07' AS DATETIME2(6)) AS startingDate -- 64 Palisades
UNION ALL SELECT 79 AS store_key, CAST('2012-06-22' AS DATETIME2(6)) AS startingDate -- 80 Paramus
UNION ALL SELECT 686 AS store_key, CAST('2012-01-10' AS DATETIME2(6)) AS startingDate -- 307 Stonebridge
UNION ALL SELECT 78 AS store_key, CAST('2012-10-15' AS DATETIME2(6)) AS startingDate -- 079 Westfield Anapolis
UNION ALL SELECT 20 AS store_key, CAST('2012-10-22' AS DATETIME2(6)) AS startingDate -- 020 Somerset Collection
UNION ALL SELECT 107 AS store_key, CAST('2012-05-11' AS DATETIME2(6)) AS startingDate -- 107 Fair Oaks
UNION ALL SELECT 12 AS store_key, CAST('2012-12-11' AS DATETIME2(6)) AS startingDate -- 012 Castleton Square
UNION ALL SELECT 30 AS store_key, CAST('2012-05-10' AS DATETIME2(6)) AS startingDate -- 030 King of Prussia
UNION ALL SELECT 10 AS store_key, CAST('2013-04-22' AS DATETIME2(6)) AS startingDate -- 010 Mall of Georgia
UNION ALL SELECT 21 AS store_key, CAST('2013-04-29' AS DATETIME2(6)) AS startingDate -- 021 Orland Square
UNION ALL SELECT 96 AS store_key, CAST('2013-06-05' AS DATETIME2(6)) AS startingDate -- 096 Northshore Mall
UNION ALL SELECT 9 AS store_key, CAST('2013-06-05' AS DATETIME2(6)) AS startingDate -- 9 The Gardens of Palm Beaches
UNION ALL SELECT 15 AS store_key, CAST('2013-06-05' AS DATETIME2(6)) AS startingDate -- 15 The Florida Mall
UNION ALL SELECT 40 AS store_key, CAST('2013-06-05' AS DATETIME2(6)) AS startingDate -- 40 Crabtree Valley Mall
UNION ALL SELECT 41 AS store_key, CAST('2013-06-05' AS DATETIME2(6)) AS startingDate -- 41 Westfield Valley Fair
UNION ALL SELECT 47 AS store_key, CAST('2013-06-05' AS DATETIME2(6)) AS startingDate -- 47 Smith Haven Mall
UNION ALL SELECT 63 AS store_key, CAST('2013-06-05' AS DATETIME2(6)) AS startingDate -- 63 Great Lakes Mall
UNION ALL SELECT 72 AS store_key, CAST('2013-06-05' AS DATETIME2(6)) AS startingDate -- 72 The Oaks
UNION ALL SELECT 88 AS store_key, CAST('2013-06-05' AS DATETIME2(6)) AS startingDate -- 88 Westfield Montgomery
UNION ALL SELECT 89 AS store_key, CAST('2013-06-05' AS DATETIME2(6)) AS startingDate -- 89 Memorial City Mall
UNION ALL SELECT 139 AS store_key, CAST('2013-06-05' AS DATETIME2(6)) AS startingDate -- 137 Cherry Hill Mall
UNI
```

