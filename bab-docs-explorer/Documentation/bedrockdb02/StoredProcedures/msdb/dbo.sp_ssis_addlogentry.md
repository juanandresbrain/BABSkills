# dbo.sp_ssis_addlogentry

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_ssis_addlogentry"]
    dbo_sysssislog(["dbo.sysssislog"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sysssislog |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[sp_ssis_addlogentry]
  @event sysname,
  @computer nvarchar(128),
  @operator nvarchar(128),
  @source nvarchar(1024),
  @sourceid uniqueidentifier,
  @executionid uniqueidentifier,
  @starttime datetime,
  @endtime datetime,
  @datacode int,
  @databytes image,
  @message nvarchar(2048)
AS
  INSERT INTO sysssislog (
      event,
      computer,
      operator,
      source,
      sourceid,
      executionid,
      starttime,
      endtime,
      datacode,
      databytes,
      message )
  VALUES (
      @event,
      @computer,
      @operator,
      @source,
      @sourceid,
      @executionid,
      @starttime,
      @endtime,
      @datacode,
      @databytes,
      @message )
  RETURN 0
```

