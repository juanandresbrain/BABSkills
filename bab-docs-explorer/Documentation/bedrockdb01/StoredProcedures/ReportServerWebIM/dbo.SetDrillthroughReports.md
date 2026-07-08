# dbo.SetDrillthroughReports

**Database:** ReportServerWebIM  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SetDrillthroughReports"]
    ModelDrill(["ModelDrill"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ModelDrill |

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

