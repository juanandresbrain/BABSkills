# dbo.DeleteModelItemPolicy

**Database:** ReportServerWebIM  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DeleteModelItemPolicy"]
    ModelItemPolicy(["ModelItemPolicy"]) --> SP
    Policies(["Policies"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ModelItemPolicy |
| Policies |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[DeleteModelItemPolicy]
@CatalogItemID as uniqueidentifier,
@ModelItemID as nvarchar(425)
AS 
SET NOCOUNT OFF
DECLARE @PolicyID uniqueidentifier
SELECT @PolicyID = (SELECT PolicyID FROM ModelItemPolicy WHERE CatalogItemID = @CatalogItemID AND ModelItemID = @ModelItemID)
DELETE Policies FROM Policies WHERE Policies.PolicyID = @PolicyID
```

