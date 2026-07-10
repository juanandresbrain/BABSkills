# dbo.DailyDefrag

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DailyDefrag"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE DailyDefrag
AS
DECLARE @Counter INT

SET @Counter = 1

WHILE @Counter <= 7
    BEGIN
       DBCC IndexDefrag(DW, METRIC_FACTS, @Counter)
    SET @COUNTER = (@COUNTER + 1)
   
    END
```

