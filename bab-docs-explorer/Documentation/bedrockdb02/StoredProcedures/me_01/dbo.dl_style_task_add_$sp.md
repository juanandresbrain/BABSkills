# dbo.dl_style_task_add_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.dl_style_task_add_$sp"]
    dbo_dl_style_task(["dbo.dl_style_task"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dl_style_task |

## Stored Procedure Code

```sql
create proc [dbo].[dl_style_task_add_$sp] 
(
   @action_type tinyint,
   @file_name nvarchar(255),
   @encoding tinyint,
   @max_rejects bigint,
   @temp_folder nvarchar(255),
   @threads int,
   @max_rows_per_batch int,  
   @pct_rows_per_batch float,
   @dl_style_task_id bigint OUTPUT, 
   @start_date smalldatetime OUTPUT 
)

AS

DECLARE
   
   @failure int,
   @in_progress_flag bit

BEGIN
   SET XACT_ABORT ON
   SET IMPLICIT_TRANSACTIONS OFF

   SET @failure = 1  
   SET @in_progress_flag = 0
      
   BEGIN TRAN  
      SELECT TOP 1 dl_style_task_id FROM dl_style_task WITH (TABLOCKX)
      
      SELECT @dl_style_task_id = ISNULL(MAX(dl_style_task_id), -1)
      FROM dl_style_task
      
      IF @dl_style_task_id <> -1
         BEGIN    
            SELECT @in_progress_flag = in_progress_flag, @start_date = start_date
            FROM dl_style_task 
            WHERE dl_style_task_id = @dl_style_task_id
         END

      IF @in_progress_flag = 0
         BEGIN
            SET  @start_date = getdate()
            
            INSERT INTO dl_style_task (start_date, action_type, file_name, encoding, max_rejects, temp_folder, threads, 
               max_rows_per_batch, pct_rows_per_batch)
            VALUES (@start_date, @action_type, @file_name, @encoding, @max_rejects, @temp_folder, @threads, 
               @max_rows_per_batch, @pct_rows_per_batch) 
            
            SET @dl_style_task_id = IDENT_CURRENT(N'dl_style_task')
            
            SET @failure = 0
         END  
  COMMIT
  
  RETURN @failure
END
```

