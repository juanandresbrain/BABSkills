# dbo.sp_dts_addlogentry

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_dts_addlogentry"]
    sysdtslog90(["sysdtslog90"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| sysdtslog90 |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[sp_dts_addlogentry]  @event sysname,  @computer nvarchar(128),  @operator nvarchar(128),  @source nvarchar(1024),  @sourceid uniqueidentifier,  @executionid uniqueidentifier,  @starttime datetime,  @endtime datetime,  @datacode int,  @databytes image,  @message nvarchar(2048)AS  INSERT INTO sysdtslog90 (      event,      computer,      operator,      source,      sourceid,      executionid,      starttime,      endtime,      datacode,      databytes,      message )  VALUES (      @event,      @computer,      @operator,      @source,      @sourceid,      @executionid,      @starttime,      @endtime,      @datacode,      @databytes,      @message )  RETURN 0
```

