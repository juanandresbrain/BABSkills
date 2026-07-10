# dbo.spDropLinkedStoreServer

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spDropLinkedStoreServer"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE proc [dbo].[spDropLinkedStoreServer]
@ServerName varchar(15)

as

EXEC master.dbo.sp_dropserver @server= @ServerName, @droplogins='droplogins'
--EXEC master.dbo.sp_dropserver @server=N'STORESERVER', @droplogins='droplogins'
```

