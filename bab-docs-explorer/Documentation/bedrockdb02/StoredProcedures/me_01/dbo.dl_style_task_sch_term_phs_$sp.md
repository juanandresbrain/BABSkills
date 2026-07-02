# dbo.dl_style_task_sch_term_phs_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.dl_style_task_sch_term_phs_$sp"]
    dbo_dl_style_task(["dbo.dl_style_task"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dl_style_task |

## Stored Procedure Code

```sql
create proc dbo.dl_style_task_sch_term_phs_$sp (
   @dl_style_task_id bigint,
   @total_schema_rejects bigint
)

AS

BEGIN
   SET XACT_ABORT ON
   SET IMPLICIT_TRANSACTIONS OFF

   BEGIN TRAN  
      UPDATE dl_style_task
      SET current_phase = 2, total_schema_rejects = @total_schema_rejects
      WHERE dl_style_task_id = @dl_style_task_id
   COMMIT  
END
```

