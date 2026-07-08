# dbo.DeleteModelPerspectives

**Database:** ReportServerWebIM  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DeleteModelPerspectives"]
    ModelPerspective(["ModelPerspective"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ModelPerspective |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[DeleteModelPerspectives]
@ModelID as uniqueidentifier
AS

DELETE
FROM [ModelPerspective]
WHERE [ModelID] = @ModelID
```

