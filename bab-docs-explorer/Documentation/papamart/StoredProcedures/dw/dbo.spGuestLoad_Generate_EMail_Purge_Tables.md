# dbo.spGuestLoad_Generate_EMail_Purge_Tables

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spGuestLoad_Generate_EMail_Purge_Tables"]
    dbo_GuestLoad_CRM_Update_Batch_EMail(["dbo.GuestLoad_CRM_Update_Batch_EMail"]) --> SP
    dbo_GuestLoad_CRM_Update_Email(["dbo.GuestLoad_CRM_Update_Email"]) --> SP
    dbo_GuestLoad_CRM_Update_EMail_Trans(["dbo.GuestLoad_CRM_Update_EMail_Trans"]) --> SP
    dbo_GuestLoad_CRM_Update_EMail_Trans_Customers(["dbo.GuestLoad_CRM_Update_EMail_Trans_Customers"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.GuestLoad_CRM_Update_Batch_EMail |
| dbo.GuestLoad_CRM_Update_Email |
| dbo.GuestLoad_CRM_Update_EMail_Trans |
| dbo.GuestLoad_CRM_Update_EMail_Trans_Customers |

## Stored Procedure Code

```sql
-- =============================================================================================================
-- Name: spGuestLoad_Generate_EMail_Purge_Tables
--
-- Description:	
--		This procedure will purge all of the work data from the datawarehouse to CRM upload
--		process. We will retain the information for 2 weeks
--
-- Input:
--		None
--
-- Output: 
--		None
--
-- Dependencies: 
--
-- EXAMPLE:
--		exec dw.dbo.spGuestLoad_Generate_EMail_Purge_Tables
--
-- Revision History
--		Name:				Date:			Comments:
--		Gary Murrish		5/13/2011		created
-- =============================================================================================================	
CREATE PROCEDURE [dbo].[spGuestLoad_Generate_EMail_Purge_Tables] 

AS
BEGIN


DECLARE @maxDate AS datetime
DECLARE @maxBatch AS int
SET @maxDate = DATEADD(d, -14, GETDATE())

SET @maxbatch = (SELECT
                     MAX(batch_id)
                 FROM
                     dbo.GuestLoad_CRM_Update_Batch_EMail WITH (NOLOCK)
                 WHERE
                 INS_DT < @maxDate)

-- Purge from Dave's trigger of the process.
DELETE  FROM
        dbo.GuestLoad_CRM_Update_Email
WHERE
batch_id BETWEEN-1 * @maxBatch
AND @maxBatch


-- Purge the file which contains the trigger records in CRM
DELETE  FROM
        crmdb02.crm.dbo.GuestLoad_CRM_Update_EMail_Trans
WHERE
BATCH_ID <= @maxBatch

-- Purge the file which contains the records to update in CRM
DELETE  FROM
        crmdb02.crm.dbo.GuestLoad_CRM_Update_EMail_Trans_Customers
WHERE
BATCH_ID <= @maxBatch

-- Purge the records from the batch table
DELETE  FROM
        dbo.GuestLoad_CRM_Update_Batch_EMail
WHERE
batch_id <= @maxBatch


END
```

