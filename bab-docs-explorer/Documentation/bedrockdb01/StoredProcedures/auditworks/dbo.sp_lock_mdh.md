# dbo.sp_lock_mdh

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_lock_mdh"]
    dbo_spt_values(["dbo.spt_values"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.spt_values |

## Stored Procedure Code

```sql
CREATE proc  [dbo].[sp_lock_mdh] --- 1996/04/08 00:00
@spid1 int = NULL,		/* server process id to check for locks */
@spid2 int = NULL		/* other process id to check for locks */
as
-- =====================================================================================================
-- Name: sp_lock_mdh
--
-- Description:	
--
-- Input:	
--			
--
-- Output: Resultset with the following columns:
--			
--
-- Dependencies: None
--
-- Revision History
--		Name:			Date:			Comments:
--		Garyd			08/30/2010		Initial version in source control
-- =====================================================================================================
set nocount on
/*
**  Show the locks for both parameters.
*/
if @spid1 is not NULL
begin
	select 	convert (smallint, req_spid) As spid, 
--		rsc_dbid As dbid, 
--		rsc_objid As ObjId,
--		rsc_indid As IndId,
		rsc_dbid As dbid, 
		o.name As Objectname,
		rsc_indid As Indexname,
		substring (v.name, 1, 4) As Type,
		substring (rsc_text, 1, 16) as Resource,
		substring (u.name, 1, 8) As Mode,
		substring (x.name, 1, 5) As Status

	from 	master.dbo.syslockinfo,
		master.dbo.spt_values v,
		master.dbo.spt_values x,
		master.dbo.spt_values u,
		auditworks.dbo.sysobjects o

	where   master.dbo.syslockinfo.rsc_type = v.number
			and v.type = 'LR'
			and master.dbo.syslockinfo.req_status = x.number
			and x.type = 'LS'
			and master.dbo.syslockinfo.req_mode + 1 = u.number
			and u.type = 'L'
			and o.id = rsc_objid
			and req_spid in (@spid1, @spid2)
end

/*
**  No parameters, so show all the locks.
*/
else
begin
	select 	convert (smallint, req_spid) As spid, 
		rsc_dbid As dbid, 
		o.name As Objectname,
		rsc_indid As Indexname,
		substring (v.name, 1, 4) As Type,
		substring (rsc_text, 1, 16) as Resource,
		substring (u.name, 1, 8) As Mode,
		substring (x.name, 1, 5) As Status

	from 	master.dbo.syslockinfo,
		master.dbo.spt_values v,
		master.dbo.spt_values x,
		master.dbo.spt_values u,
		auditworks.dbo.sysobjects o

	where   master.dbo.syslockinfo.rsc_type = v.number
			and v.type = 'LR'
			and master.dbo.syslockinfo.req_status = x.number
			and x.type = 'LS'
			and master.dbo.syslockinfo.req_mode + 1 = u.number
			and u.type = 'L'
			and o.id = rsc_objid
	order by spid 
end

return (0) -- sp_lock
```

