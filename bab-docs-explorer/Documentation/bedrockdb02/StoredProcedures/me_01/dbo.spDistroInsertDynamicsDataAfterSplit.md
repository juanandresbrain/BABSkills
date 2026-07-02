# dbo.spDistroInsertDynamicsDataAfterSplit

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spDistroInsertDynamicsDataAfterSplit"]
    dbo_DynamicsDataAfterSplit(["dbo.DynamicsDataAfterSplit"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DynamicsDataAfterSplit |

## Stored Procedure Code

```sql
--======================================================================================================================================
--	Dan Tweedie	2020-09-01	Created Proc - Copied from spDistroInsertAfterSplitData, but inserts into new table DynamicsDataAfterSplit
--======================================================================================================================================

create procEDURE [dbo].[spDistroInsertDynamicsDataAfterSplit]
	(
		@id bigint, 
		@iSourceID varchar(20), 
		@iDestID varchar(21), 
		@style varchar(20), 
		@quantity int, 
		@recType varchar(6), 
		@sequencenbr bigint, 
		@distribution_number varchar(20), 
		@ref_field_1 int, 
		@date smalldatetime, 
		@activePickFlag varchar(1)
	)
	
AS
	INSERT INTO   DynamicsDataAfterSplit( Id, SourceID, DestID, style_code, quantity, rec_Type, sequencenbr, distribution_number, ref_field_1, release_date, active_pick_flag)
VALUES (@id, @iSourceID, @iDestID, @style, @quantity, @recType, @sequencenbr, @distribution_number, @ref_field_1, getdate(), @activePickFlag)
```

