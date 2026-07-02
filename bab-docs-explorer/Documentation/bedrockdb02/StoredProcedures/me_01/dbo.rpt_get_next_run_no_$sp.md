# dbo.rpt_get_next_run_no_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.rpt_get_next_run_no_$sp"]
    dbo_wrk_rpt_run_no(["dbo.wrk_rpt_run_no"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.wrk_rpt_run_no |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[rpt_get_next_run_no_$sp] @table_id 	smallint

AS

/*
Proc name:		rpt_get_next_run_no_$sp
Description:	Gets the next run no. for a give table ID (currently only 1: wrk_rpt_po_temp_dtl)
*/

DECLARE	@next_run_no int

BEGIN TRANSACTION

UPDATE wrk_rpt_run_no
   SET last_run_no = CASE WHEN last_run_no < max_run_no THEN last_run_no + 1 ELSE 1 END
 WHERE table_id = @table_id

SELECT @next_run_no = last_run_no
  FROM wrk_rpt_run_no 
 WHERE table_id = @table_id

COMMIT TRANSACTION


RETURN @next_run_no
```

