# dbo.sp_keith_ib_audit_trailBAK20220801

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_keith_ib_audit_trailBAK20220801"]
    dbo_ib_audit_trail(["dbo.ib_audit_trail"]) --> SP
    dbo_keith_ib_audit_trail(["dbo.keith_ib_audit_trail"]) --> SP
    dbo_location(["dbo.location"]) --> SP
    dbo_po(["dbo.po"]) --> SP
    dbo_po_location(["dbo.po_location"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ib_audit_trail |
| dbo.keith_ib_audit_trail |
| dbo.location |
| dbo.po |
| dbo.po_location |

## Stored Procedure Code

```sql
CREATE procedure [dbo].[sp_keith_ib_audit_trailBAK20220801]

as
-- =====================================================================================================
-- Name: sp_keith_ib_audit_trail
--
-- Description:	
--
-- Input: 
--
-- Output: 
--
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Keith Lee		xx/xx/xxx		Created proc.	
--		Tim Callahan	01/22/2016		Added China Warehouses 3970, 3980 to be included		
--		Tim Callahan	01/25/2018		Added China Warehouses 8502 to be included		
--		Tim Callahan	03/03/2018		Added China Warehouses 8505 to be included		
--		
-- =====================================================================================================


--drop table keith_ib_audit_trail

insert into keith_ib_audit_trail(
[po_no],[entry_date],[employee_first_name], [employee_last_name] 
)

select 	distinct iat.application_identifier as po_no, 
	iat.entry_date,
	iat.employee_first_name, 
	iat.employee_last_name 
from ib_audit_trail iat with (nolock)
JOIN po po with (nolock) on iat.application_identifier = po.po_no
JOIN po_location ploc with (nolock) on po.po_id = ploc.po_id
JOIN location l with (nolock) ON ploc.location_id = l.location_id
where iat.application = 'POM' 
and iat.activity = 'Create'
and	iat.application_identifier not in (select po_no from keith_ib_audit_trail)
and	l.location_code in ('0980','0470','2970','0975','0960','3970','3980','8502','8505','0013') -- Added China Warehouses 3970, 3980 , 8502, 8505
```

