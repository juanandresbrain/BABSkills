# dbo.DeleteDrillthroughReports

**Database:** ReportServerWebIM  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DeleteDrillthroughReports"]
    ModelDrill(["ModelDrill"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ModelDrill |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[DeleteDrillthroughReports]
@ModelID uniqueidentifier,
@ModelItemID nvarchar(425)
AS
 DELETE ModelDrill WHERE ModelID = @ModelID and ModelItemID = @ModelItemID
```

