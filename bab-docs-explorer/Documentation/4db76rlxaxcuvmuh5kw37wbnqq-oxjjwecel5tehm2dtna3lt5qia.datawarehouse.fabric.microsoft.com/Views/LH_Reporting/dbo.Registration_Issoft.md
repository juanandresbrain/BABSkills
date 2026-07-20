# dbo.Registration_Issoft

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.Registration_Issoft"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIEW dbo.Registration_Issoft
AS
SELECT        CAST(1 AS smallint) AS isSOTF, CAST('Yes' AS varchar) AS Descr
UNION ALL
SELECT        CAST(0 AS smallint) AS isSOTF, CAST('No' AS varchar) AS Descr
```

