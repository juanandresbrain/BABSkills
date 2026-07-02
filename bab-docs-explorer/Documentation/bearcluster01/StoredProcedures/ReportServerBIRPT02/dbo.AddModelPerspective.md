# dbo.AddModelPerspective

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.AddModelPerspective"]
    dbo_ModelPerspective(["dbo.ModelPerspective"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ModelPerspective |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[AddModelPerspective]
@ModelID as uniqueidentifier,
@PerspectiveID as ntext,
@PerspectiveName as ntext = null,
@PerspectiveDescription as ntext = null
AS

INSERT
INTO [ModelPerspective]
    ([ID], [ModelID], [PerspectiveID], [PerspectiveName], [PerspectiveDescription])
VALUES
    (newid(), @ModelID, @PerspectiveID, @PerspectiveName, @PerspectiveDescription)
```

