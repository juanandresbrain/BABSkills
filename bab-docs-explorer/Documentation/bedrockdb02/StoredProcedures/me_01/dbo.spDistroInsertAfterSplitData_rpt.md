# dbo.spDistroInsertAfterSplitData_rpt

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spDistroInsertAfterSplitData_rpt"]
    dbo_distribution_data_after_split_rpt(["dbo.distribution_data_after_split_rpt"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.distribution_data_after_split_rpt |

## Stored Procedure Code

```sql
CREATE procEDURE [dbo].[spDistroInsertAfterSplitData_rpt]
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
	INSERT INTO   distribution_data_after_split_rpt( Id, SourceID, DestID, style_code, quantity, rec_Type, sequencenbr, distribution_number, ref_field_1, release_date, active_pick_flag)
VALUES (@id, @iSourceID, @iDestID, @style, @quantity, @recType, @sequencenbr, @distribution_number, @ref_field_1, getdate(), @activePickFlag)
```

