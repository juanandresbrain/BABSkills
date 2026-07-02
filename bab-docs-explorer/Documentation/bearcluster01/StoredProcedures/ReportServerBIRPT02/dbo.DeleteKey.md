# dbo.DeleteKey

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DeleteKey"]
    dbo_keys(["dbo.keys"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.keys |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[DeleteKey]
@InstallationID uniqueidentifier
AS

if (@InstallationID = '00000000-0000-0000-0000-000000000000')
RAISERROR('Cannot delete reserved key', 16, 1)

-- Remove the encryption keys
delete from keys where InstallationID = @InstallationID and Client = 1
```

