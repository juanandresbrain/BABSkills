# dbo.spAddLinkedStoreServer

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spAddLinkedStoreServer"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE proc [dbo].[spAddLinkedStoreServer] 
@IP varchar(15),
@Pword varchar(52),
@ServerName varchar(15)

as

set nocount on

EXEC master.dbo.sp_addlinkedserver @server= @ServerName, @srvproduct=N'sql_server', @provider=N'SQLNCLI11', @datasrc= @IP, @catalog=N'USICOAL'
EXEC master.dbo.sp_addlinkedsrvlogin @rmtsrvname= @ServerName,@useself=N'False',@locallogin=NULL,@rmtuser=N'sa',@rmtpassword= @Pword
EXEC master.dbo.sp_serveroption @server= @ServerName, @optname=N'data access', @optvalue=N'true'
EXEC master.dbo.sp_serveroption @server= @ServerName, @optname=N'rpc', @optvalue=N'true'
EXEC master.dbo.sp_serveroption @server= @ServerName, @optname=N'rpc out', @optvalue=N'true'
	
--EXEC master.dbo.sp_addlinkedserver @server = N'STORESERVER', @srvproduct=N'sql_server', @provider=N'SQLNCLI11', @datasrc= @IP, @catalog=N'USICOAL'
--EXEC master.dbo.sp_addlinkedsrvlogin @rmtsrvname=N'STORESERVER',@useself=N'False',@locallogin=NULL,@rmtuser=N'sa',@rmtpassword= @Pword
--EXEC master.dbo.sp_serveroption @server=N'STORESERVER', @optname=N'data access', @optvalue=N'true'
--EXEC master.dbo.sp_serveroption @server=N'STORESERVER', @optname=N'rpc', @optvalue=N'true'
--EXEC master.dbo.sp_serveroption @server=N'STORESERVER', @optname=N'rpc out', @optvalue=N'true'
```

