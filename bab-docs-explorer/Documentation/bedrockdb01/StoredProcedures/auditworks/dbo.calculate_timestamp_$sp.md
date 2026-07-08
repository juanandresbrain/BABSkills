# dbo.calculate_timestamp_$sp

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.calculate_timestamp_$sp"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
create procedure dbo.calculate_timestamp_$sp
@process_timestamp float OUTPUT
AS

/* Version:1.00 Date:1996/05/09 */
/* Desc: calaculate process timestamp.
   Called by edit, move and transaction_header_$trD */

DECLARE @current_date datetime

/*{ calculate process_timestamp as
 month-day-hour-min-sec-millisec */

SELECT @current_date = getdate()

SELECT @process_timestamp = DATEPART ( mm, @current_date ) * 100000000000.0
		+ DATEPART ( dd, @current_date )* 1000000000.0
		+ DATEPART ( hh, @current_date ) * 10000000.0
		+ DATEPART ( mi, @current_date ) * 100000.0
		+ DATEPART ( ss, @current_date ) * 1000.0
		+ DATEPART ( ms, @current_date )

/*} calculate process_timestamp */

RETURN 0
```

