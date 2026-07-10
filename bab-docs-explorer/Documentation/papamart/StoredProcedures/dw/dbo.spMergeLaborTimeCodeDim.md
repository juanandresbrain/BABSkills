# dbo.spMergeLaborTimeCodeDim

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMergeLaborTimeCodeDim"]
    Labor_Timecode_Dim(["Labor_Timecode_Dim"]) --> SP
    UTATimeCode(["UTATimeCode"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Labor_Timecode_Dim |
| UTATimeCode |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMergeLaborTimeCodeDim] 

as 

------------------------------------------------------------------------
--	2019-01-21	Dan Tweedie	Created proc
------------------------------------------------------------------------

set nocount on

declare 
	@LogID int

select @LogID = max(etl_log_id)+1 from Labor_Timecode_Dim;

merge into Labor_Timecode_Dim as target
using UTATimeCode as source
on 
	(
		target.wb_cd=source.TCode_Name
	)
when matched 
	and 
		(
			isnull(target.descr,'x')<>isnull(source.TCode_Desc,'x')
			OR
			isnull(target.abrv,'x')<>isnull(source.TCode_Name,'x')
		)
	then Update
		set
			target.descr=source.TCode_Desc,
			target.abrv=source.TCode_Name,
			target.Upd_Dt=getdate()
when not matched by target
	then Insert
		(
			wb_cd,
			descr,
			abrv,
			etl_log_id,
			etl_evnt_id,
			Ins_Dt
		)
	values
		(
			source.TCode_Name,
			source.TCode_Desc,
			source.TCode_Name,
			@LogID,
			@LogID,
			getdate()
		)
;
```

