# dbo.Sr_ActivateJob

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sr_ActivateJob"]
    Sr_Job(["Sr_Job"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Sr_Job |

## Stored Procedure Code

```sql
create proc dbo.Sr_ActivateJob    (@job_id int,  @data varchar(50), @data_ext varchar(50))

/*******************************************************/
/*	                                                 */
/*	    Author 		Andrea Nagy              */
/*	    Creation Date       07/25/00                 */
/*	    Comments                                     */
/*	                                                 */
/*******************************************************/

AS 


begin

IF (ISNULL(@data,'0') ='0' OR ISNULL(ltrim(rtrim(@data)),'0') = '0')
      AND (ISNULL(@data_ext,'0') ='0' OR ISNULL(ltrim(rtrim(@data_ext)),'0') = '0')
	UPDATE Sr_Job
	SET scheduled_executions = scheduled_executions + 1
	WHERE job_id = @job_id
  
IF (ISNULL(@data,'0') <> '0' OR ISNULL(ltrim(rtrim(@data)),'0') <> '0') 
      AND (ISNULL(@data_ext,'0') ='0' OR ISNULL(ltrim(rtrim(@data_ext)),'0') = '0')
   UPDATE Sr_Job
      SET scheduled_executions = scheduled_executions + 1,
          data = @data
    WHERE job_id = @job_id
    
  
IF (ISNULL(@data,'0') = '0' OR ISNULL(ltrim(rtrim(@data)),'0') = '0') 
      AND (ISNULL(@data_ext,'0') <>'0' OR ISNULL(ltrim(rtrim(@data_ext)),'0') <> '0')
   
   UPDATE Sr_Job
      SET scheduled_executions = scheduled_executions + 1,
          data_ext = @data_ext
    WHERE job_id = @job_id
  
IF (ISNULL(@data,'0') <>'0' OR ISNULL(ltrim(rtrim(@data)),'0') <> '0')
      AND (ISNULL(@data_ext,'0') <>'0' OR ISNULL(ltrim(rtrim(@data_ext)),'0') <> '0')
   UPDATE Sr_Job
      SET scheduled_executions = scheduled_executions + 1,
          data_ext = @data_ext,
          data = @data
    WHERE job_id = @job_id
      


end
```

