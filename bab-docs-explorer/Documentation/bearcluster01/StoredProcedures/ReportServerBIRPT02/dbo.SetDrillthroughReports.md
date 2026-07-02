# dbo.SetDrillthroughReports

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SetDrillthroughReports"]
    dbo_ModelDrill(["dbo.ModelDrill"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ModelDrill |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[SetDrillthroughReports]
@ReportID uniqueidentifier,
@ModelID uniqueidentifier,
@ModelItemID nvarchar(425),
@Type tinyint
AS
 SET NOCOUNT OFF
 INSERT INTO ModelDrill (ModelDrillID, ModelID, ReportID, ModelItemID, [Type])
 VALUES (newid(), @ModelID, @ReportID, @ModelItemID, @Type)
```

