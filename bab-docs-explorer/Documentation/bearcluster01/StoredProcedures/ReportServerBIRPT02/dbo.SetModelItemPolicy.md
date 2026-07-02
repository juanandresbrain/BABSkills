# dbo.SetModelItemPolicy

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SetModelItemPolicy"]
    dbo_ModelItemPolicy(["dbo.ModelItemPolicy"]) --> SP
    dbo_Policies(["dbo.Policies"]) --> SP
    dbo_PolicyUserRole(["dbo.PolicyUserRole"]) --> SP
    dbo_SecData(["dbo.SecData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ModelItemPolicy |
| dbo.Policies |
| dbo.PolicyUserRole |
| dbo.SecData |

## Stored Procedure Code

```sql
-- update the system policy
CREATE PROCEDURE [dbo].[SetModelItemPolicy]
@CatalogItemID as uniqueidentifier,
@ModelItemID as nvarchar(425),
@PrimarySecDesc as image,
@SecondarySecDesc as ntext = NULL,
@XmlPolicy as ntext,
@AuthType as int,
@PolicyID uniqueidentifier OUTPUT
AS
SELECT @PolicyID = (SELECT PolicyID FROM ModelItemPolicy WHERE CatalogItemID = @CatalogItemID AND ModelItemID = @ModelItemID )
IF (@PolicyID IS NULL)
   BEGIN
     SET @PolicyID = newid()
     INSERT INTO Policies (PolicyID, PolicyFlag)
     VALUES (@PolicyID, 2)
     INSERT INTO SecData (SecDataID, PolicyID, AuthType, XmlDescription, NTSecDescPrimary, NtSecDescSecondary)
     VALUES (newid(), @PolicyID, @AuthType, @XmlPolicy, @PrimarySecDesc, @SecondarySecDesc)
     INSERT INTO ModelItemPolicy (ID, CatalogItemID, ModelItemID, PolicyID)
     VALUES (newid(), @CatalogItemID, @ModelItemID, @PolicyID)
   END
ELSE
   BEGIN
      DECLARE @SecDataID as uniqueidentifier
      SELECT @SecDataID = (SELECT SecDataID FROM SecData WHERE PolicyID = @PolicyID and AuthType = @AuthType)
      IF (@SecDataID IS NULL)
      BEGIN -- insert new sec desc's
        INSERT INTO SecData (SecDataID, PolicyID, AuthType, XmlDescription, NTSecDescPrimary, NtSecDescSecondary)
        VALUES (newid(), @PolicyID, @AuthType, @XmlPolicy, @PrimarySecDesc, @SecondarySecDesc)
      END
      ELSE
      BEGIN -- update existing sec desc's
        UPDATE SecData SET
        XmlDescription = @XmlPolicy,
        NtSecDescPrimary = @PrimarySecDesc,
        NtSecDescSecondary = @SecondarySecDesc
        WHERE SecData.PolicyID = @PolicyID
        AND AuthType = @AuthType

      END
   END
DELETE FROM PolicyUserRole WHERE PolicyID = @PolicyID
```

