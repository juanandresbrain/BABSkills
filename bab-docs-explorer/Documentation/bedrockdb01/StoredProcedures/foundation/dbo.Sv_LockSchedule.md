# dbo.Sv_LockSchedule

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sv_LockSchedule"]
    Sv_Schedule(["Sv_Schedule"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Sv_Schedule |

## Stored Procedure Code

```sql
create proc Sv_LockSchedule @object_id 	int,
@db_group_id 	int
as
/* Proc to lock the schedule record and return 1 if OK 0 if not  */
/* By Ashraf Zaid				Date June 20 1997 */
UPDATE Sv_Schedule
	SET server_lock = 1
	WHERE object_id = @object_id
	  AND db_group_id = @db_group_id
	  AND server_lock = 0
	IF @@ROWCOUNT = 0
		RETURN 0
	ELSE
		RETURN 1
```

