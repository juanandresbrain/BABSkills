# dbo.UpdatePolicyStatus

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.UpdatePolicyStatus"]
    dbo_SecData(["dbo.SecData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.SecData |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[UpdatePolicyStatus]
    @PolicyID as uniqueidentifier,
    @AuthType int,
    @Status int
AS
    UPDATE SecData
    SET
        NtSecDescState = @Status
    WHERE
        SecData.PolicyID = @PolicyID AND SecData.AuthType = @AuthType
```

