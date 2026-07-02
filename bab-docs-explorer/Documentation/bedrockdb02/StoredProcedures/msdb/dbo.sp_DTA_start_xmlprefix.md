# dbo.sp_DTA_start_xmlprefix

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_DTA_start_xmlprefix"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
create procedure sp_DTA_start_xmlprefix
as
begin
	declare @startTags nvarchar(128)
	set @startTags = N'<DTAXML><DTAOutput><AnalysisReport>'
	select @startTags
end
```

