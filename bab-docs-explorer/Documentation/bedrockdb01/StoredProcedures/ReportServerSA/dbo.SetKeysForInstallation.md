# dbo.SetKeysForInstallation

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SetKeysForInstallation"]
    dbo_Keys(["dbo.Keys"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Keys |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[SetKeysForInstallation]
@InstallationID uniqueidentifier,
@SymmetricKey image = NULL,
@PublicKey image
AS

update [dbo].[Keys]
set [SymmetricKey] = @SymmetricKey, [PublicKey] = @PublicKey
where [InstallationID] = @InstallationID and [Client] = 1
```

