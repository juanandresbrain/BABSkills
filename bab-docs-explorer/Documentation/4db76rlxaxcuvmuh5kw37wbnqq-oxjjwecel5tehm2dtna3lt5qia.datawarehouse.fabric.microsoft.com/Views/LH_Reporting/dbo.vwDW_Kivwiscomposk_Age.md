# dbo.vwDW_Kivwiscomposk_Age

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_Kivwiscomposk_Age"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIEW [dbo].[vwDW_Kivwiscomposk_Age]
AS 
SELECT        1 AS isComp, 'Comp' AS Description
UNION ALL
SELECT        0 AS isComp, 'Not Comp' AS Description
```

