# dbo.vwReturnRand

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwReturnRand"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIEW dbo.vwReturnRand
WITH SCHEMABINDING
AS
SELECT     RAND() AS r
```

