# dbo.UpdatePolicy

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.UpdatePolicy"]
    dbo_SecData(["dbo.SecData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.SecData |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[UpdatePolicy]
    @PolicyID as uniqueidentifier,
    @PrimarySecDesc as image,
    @SecondarySecDesc as ntext = NULL,
    @AuthType int
AS
    UPDATE SecData
    SET
        NtSecDescPrimary = @PrimarySecDesc,
        NtSecDescSecondary = @SecondarySecDesc,
        NtSecDescState = 0 -- Setting State back to Valid
    WHERE
        SecData.PolicyID = @PolicyID AND
        SecData.AuthType = @AuthType
```

