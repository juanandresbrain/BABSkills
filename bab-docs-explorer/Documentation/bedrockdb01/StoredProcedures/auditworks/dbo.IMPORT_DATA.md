# dbo.IMPORT_DATA

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.IMPORT_DATA"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[IMPORT_DATA] AS
BEGIN
exec master..xp_cmdshell 'bcp auditworks.dbo.user_subclass in \\buildabear.com\us\shared\IT\SAProdExport\user_subclass.txt -T -c -S BedrockTESTdb01'
exec master..xp_cmdshell 'bcp auditworks.dbo.user_class in \\buildabear.com\us\shared\IT\SAProdExport\user_class.txt -T -c -S BedrockTESTdb01'
exec master..xp_cmdshell 'bcp auditworks.dbo.user_department in \\buildabear.com\us\shared\IT\SAProdExport\user_department.txt -T -c -S BedrockTESTdb01'
exec master..xp_cmdshell 'bcp auditworks.dbo.user_district in \\buildabear.com\us\shared\IT\SAProdExport\user_district.txt -T -c -S BedrockTESTdb01'
exec master..xp_cmdshell 'bcp auditworks.dbo.user_division in \\buildabear.com\us\shared\IT\SAProdExport\user_division.txt -T -c -S BedrockTESTdb01'
exec master..xp_cmdshell 'bcp auditworks.dbo.user_region in \\buildabear.com\us\shared\IT\SAProdExport\user_region.txt -T -c -S BedrockTESTdb01'
exec master..xp_cmdshell 'bcp auditworks.dbo.user_style in \\buildabear.com\us\shared\IT\SAProdExport\user_style.txt -T -c -S BedrockTESTdb01'
exec master..xp_cmdshell 'bcp auditworks.dbo.user_upc in \\buildabear.com\us\shared\IT\SAProdExport\user_upc.txt -T -c -S BedrockTESTdb01'
END;
```

