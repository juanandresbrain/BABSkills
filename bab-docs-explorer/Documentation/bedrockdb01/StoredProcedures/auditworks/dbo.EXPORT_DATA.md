# dbo.EXPORT_DATA

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.EXPORT_DATA"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
--Stored Procedure to EXPORT table data from PRODUCTION server (BEDROCKDB01)
CREATE PROCEDURE EXPORT_DATA AS
BEGIN
exec master..xp_cmdshell 'bcp auditworks.dbo.user_subclass out \\buildabear.com\us\shared\IT\SAProdExport\user_subclass.txt -T -c -S Bedrockdb01'
exec master..xp_cmdshell 'bcp auditworks.dbo.user_class out \\buildabear.com\us\shared\IT\SAProdExport\user_class.txt -T -c -S Bedrockdb01'
exec master..xp_cmdshell 'bcp auditworks.dbo.user_department out \\buildabear.com\us\shared\IT\SAProdExport\user_department.txt -T -c -S Bedrockdb01'
exec master..xp_cmdshell 'bcp auditworks.dbo.user_district out \\buildabear.com\us\shared\IT\SAProdExport\user_district.txt -T -c -S Bedrockdb01'
exec master..xp_cmdshell 'bcp auditworks.dbo.user_division out \\buildabear.com\us\shared\IT\SAProdExport\user_division.txt -T -c -S Bedrockdb01'
exec master..xp_cmdshell 'bcp auditworks.dbo.user_region out \\buildabear.com\us\shared\IT\SAProdExport\user_region.txt -T -c -S Bedrockdb01'
exec master..xp_cmdshell 'bcp auditworks.dbo.user_style out \\buildabear.com\us\shared\IT\SAProdExport\user_style.txt -T -c -S Bedrockdb01'
exec master..xp_cmdshell 'bcp auditworks.dbo.user_upc out \\buildabear.com\us\shared\IT\SAProdExport\user_upc.txt -T -c -S Bedrockdb01'
END;
```

