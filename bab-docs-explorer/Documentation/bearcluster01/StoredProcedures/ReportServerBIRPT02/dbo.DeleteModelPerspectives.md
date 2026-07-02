# dbo.DeleteModelPerspectives

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DeleteModelPerspectives"]
    dbo_ModelPerspective(["dbo.ModelPerspective"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ModelPerspective |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[DeleteModelPerspectives]
@ModelID as uniqueidentifier
AS

DELETE
FROM [ModelPerspective]
WHERE [ModelID] = @ModelID
```

