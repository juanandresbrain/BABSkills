# dbo.DeleteDrillthroughReports

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DeleteDrillthroughReports"]
    dbo_ModelDrill(["dbo.ModelDrill"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ModelDrill |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[DeleteDrillthroughReports]
@ModelID uniqueidentifier,
@ModelItemID nvarchar(425)
AS
 DELETE ModelDrill WHERE ModelID = @ModelID and ModelItemID = @ModelItemID
```

