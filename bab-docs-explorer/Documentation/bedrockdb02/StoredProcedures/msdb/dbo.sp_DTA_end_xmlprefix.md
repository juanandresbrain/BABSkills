# dbo.sp_DTA_end_xmlprefix

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_DTA_end_xmlprefix"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
create procedure sp_DTA_end_xmlprefix
as
begin
	declare @endTags nvarchar(128)
	set @endTags = N'</AnalysisReport></DTAOutput></DTAXML>'
	select @endTags
end
```

