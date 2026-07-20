# dbo.TestView

**Database:** BABLakehouse_Test_Test  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.TestView"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
-- Test creating a simple view first to check permissions
CREATE VIEW [dbo].[TestView] AS 
SELECT TOP 1 'Test' as test_column;
```

