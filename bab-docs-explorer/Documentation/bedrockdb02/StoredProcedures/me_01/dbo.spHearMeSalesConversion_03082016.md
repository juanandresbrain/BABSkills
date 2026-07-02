# dbo.spHearMeSalesConversion_03082016

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spHearMeSalesConversion_03082016"]
    dbo_attribute(["dbo.attribute"]) --> SP
    dbo_attribute_set(["dbo.attribute_set"]) --> SP
    dbo_entity_attribute_set(["dbo.entity_attribute_set"]) --> SP
    dbo_ib_inventory(["dbo.ib_inventory"]) --> SP
    dbo_ib_inventory_id_hearme(["dbo.ib_inventory_id_hearme"]) --> SP
    dbo_inventory_update2__sp(["dbo.inventory_update2_$sp"]) --> SP
    dbo_location(["dbo.location"]) --> SP
    dbo_sku(["dbo.sku"]) --> SP
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
    dbo_style(["dbo.style"]) --> SP
    dbo_tblHearMeSalesConversionArchive(["dbo.tblHearMeSalesConversionArchive"]) --> SP
    dbo_tblHearMeSalesConversionArchive_original(["dbo.tblHearMeSalesConversionArchive_original"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.attribute |
| dbo.attribute_set |
| dbo.entity_attribute_set |
| dbo.ib_inventory |
| dbo.ib_inventory_id_hearme |
| dbo.inventory_update2_$sp |
| dbo.location |
| dbo.sku |
| dbo.sp_send_dbmail |
| dbo.style |
| dbo.tblHearMeSalesConversionArchive |
| dbo.tblHearMeSalesConversionArchive_original |

## Stored Procedure Code

```sql
CREATE procedure [dbo].[spHearMeSalesConversion_03082016]

as

-- =====================================================================================================
-- Name: spHearMeSalesConversion
--
-- Description:	Captures record of Sound sales transactions, negates the transactions in Merch, 
--				inserts new transactions for the physical universal sound sku.
--				Send email to report number of original, negated and universal transactions processed.
--
-- Input:	NA
--			
--
-- Output: 
--			
--
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		04/25/2012		Created proc.	--based on spHearMeSalesConversion_bak20120425
--		Dan Tweedie		05/04/2012		Added parameter to show max(ib_inventory_id) at beginning of process, for comparison at the end of the process
--		Dan Tweedie		06/08/2012		max(ib_inventory_id) no longer needed, but I'm leaving it there anyway, it's just being captured and not used at this point.
--		Dan Tweedie		06/08/2012		Added input of new data into temp table before prod table, this is used to query from at the end.
--		Dan Tweedie		01/29/2013		Set value to 0 for insert of transaction_valuation_retail and transaction_selling_retail when inserting record for universal sound sku
--		Dan Tweedie		06/24/2013		Removed hard code 0 transaction_valuation_retail and transaction_selling_retail, reversing the change made on 1/29/2013
--      Keith Lee		07/19/2015		Added new columns for ib_inventory Merch 5.0 system.
--		Dan Tweedie		08/18/2015		Added code to stage data for insert into ib_inventory_total, and call Aptos proc. 
--		Keith Lee		02/24/2016		Added these fields to be recorded in the negatation transaction_no,batch_no,register_no
-- =====================================================================================================


-- Find Sales for new HearMe Sounds, insert into archive table
--- this table can now be our point of reference for historical reference of the original sound transaction
------only good from 04/12/2012 and forward
declare @trans_id int
select @trans_id = max(ib_inventory_id) from ib_inventory (nolock)

truncate table tblHearMeSalesConversionArchive_original



insert tblHearMeSalesConversionArchive_original
select  ii.ib_inventory_id,
		getdate() proc_date,
		ii.sku_id, 
		ii.location_id, 
		ii.price_status_id, 
		ii.transaction_date, 
		ii.transaction_type_code, 
		ii.inventory_status_id, 
		ii.other_location_id, 
		ii.transaction_reason_id, 
		ii.document_number, 
		ii.transaction_units, 
		ii.transaction_cost, 
		ii.transaction_valuation_retail, 
		ii.transaction_selling_retail, 
		ii.price_change_type, 
		ii.units_affected,
		s.style_code,
		s.short_desc,
		l.location_code, 
		ii.transaction_cost_local,
		ii.updated_flag,
		ii.transaction_no,
		ii.batch_no,
		ii.register_no
from	ib_inventory ii
inner join sku sk (nolock) on ii.sku_id = sk.sku_id
inner join style s (nolock) on sk.style_id = s.style_id
inner join location l (nolock) on ii.location_id = l.location_id
inner join entity_attribute_set eas_m (nolock) on s.style_id = eas_m.parent_id
inner join attribute_set ats_m (nolock) on eas_m.attribute_set_id = ats_m.attribute_set_id
inner join attribute a_m (nolock) on eas_m.attribute_id = a_m.attribute_id
where   a_m.attribute_code = 'MSOUND'
and		ii.transaction_type_code in (600,601,603,605,610,615)
and		ii.ib_inventory_id > (select ib_inventory_id from ib_inventory_id_hearme)
order by ii.transaction_date

if (select count(*) from tblHearMeSalesConversionArchive_original) > 0

begin

	---archive data permanently -- -I left this a separate step to make it easier to manually run the process if necessary
	--if we need to investigate later, this table will be helpful.
	insert tblHearMeSalesConversionArchive
	select * 
	from tblHearMeSalesConversionArchive_original
    ------------------------------------------------------------------------------------
    --take snapshot so we can capture the totals at the end
    IF (Object_ID('tempdb..#negated') IS NOT NULL) DROP TABLE #negated
    select  
			t.sku_id, 
			t.location_id, 
			t.price_status_id, 
			t.transaction_date, 
			t.transaction_type_code, 
			t.inventory_status_id, 
			t.other_location_id, 
			t.transaction_reason_id, --tr.transaction_reason_code,
			t.document_number, 
			t.transaction_units * -1 as transaction_units, 
			t.transaction_cost * -1 as transaction_cost, 
			t.transaction_valuation_retail * -1 as transaction_valuation_retail, 
			t.transaction_selling_retail * -1 as transaction_selling_retail, 
			t.price_change_type, 
			t.units_affected *-1 as units_affected,
			t.transaction_cost_local * -1 as transaction_cost_local,
			t.updated_flag,
			t.transaction_no,
			t.batch_no,
			t.register_no
	into #negated
	from	tblHearMeSalesConversionArchive_original t
    
    
	IF (Object_ID('tempdb..#sound') IS NOT NULL) DROP TABLE #sound
	select  sk_m.sku_id, 
			t.location_id, 
			t.price_status_id, 
			t.transaction_date, 
			t.transaction_type_code, 
			t.inventory_status_id, 
			t.other_location_id, 
			t.transaction_reason_id, --tr.transaction_reason_code,
			s.style_code as document_number, 
			t.transaction_units , 
			t.transaction_cost, 
			t.transaction_valuation_retail, --removed hard coded '0' 06/24/2013 Dan T
			t.transaction_selling_retail, --removed hard coded '0' 06/24/2013 Dan T
			t.price_change_type, 
			t.units_affected  as units_affected,
			t.transaction_cost_local,
			t.updated_flag,
			t.transaction_no,
			t.batch_no,
			t.register_no
	into #sound
	from	tblHearMeSalesConversionArchive_original t
	inner join sku sk (nolock) on t.sku_id = sk.sku_id
	inner join style s (nolock) on sk.style_id = s.style_id
	inner join location l (nolock) on t.location_id = l.location_id
	inner join entity_attribute_set eas_m (nolock) on s.style_id = eas_m.parent_id
	inner join attribute_set ats_m (nolock) on eas_m.attribute_set_id = ats_m.attribute_set_id
	inner join attribute a_m (nolock) on eas_m.attribute_id = a_m.attribute_id
	inner join style s_m (nolock) on ats_m.attribute_set_label = s_m.style_code
	inner join sku sk_m (nolock) on s_m.style_id = sk_m.style_id
	where a_m.attribute_code = 'MSOUND'
	order by t.transaction_date

	------------------------------------------------------------------------------------
	-------STAGE DATA FOR INSERT INTO IB_INVENTORY_TOTAL
	
	IF (Object_ID('me_01..tmpStageIb_Inventory_Total') IS NOT NULL) DROP TABLE tmpStageIb_Inventory_Total
	SELECT sku_id, 
		   location_id, 
		   price_status_id,
		   transaction_date,
		   transaction_type_code,
		   inventory_status_id,
		   other_location_id,
		   transaction_reason_id,
		   document_number,
		   transaction_units,
		   transaction_cost,
		   transaction_cost_local,
		   transaction_valuation_retail, 
		   transaction_selling_retail,
		   price_change_type,
		   units_affected,
		   transaction_no,
		   batch_no,
		   register_no
	INTO tmpStageIb_Inventory_Total
	from #negated
	union all
	SELECT sku_id, 
		   location_id, 
		   price_status_id,
		   transaction_date,
		   transaction_type_code,
		   inventory_status_id,
		   other_location_id,
		   transaction_reason_id,
		   document_number,
		   transaction_units,
		   transaction_cost,
		   transaction_cost_local,
		   transaction_valuation_retail, 
		   transaction_selling_retail,
		   price_change_type,
		   units_affected,
		   transaction_no,
		   batch_no,
		   register_no
	from #sound

	--CALL EPICOR PROC TO INSERT STAGED DATA
	EXEC inventory_update2_$sp 'SELECT sku_id, location_id, price_status_id,transaction_date,transaction_type_code,
              inventory_status_id,other_location_id,transaction_reason_id,document_number,transaction_units,transaction_cost,transaction_cost_local,
              transaction_valuation_retail, transaction_selling_retail,price_change_type,units_affected FROM tmpStageIb_Inventory_Total'

-- Update ib_inventory_id so we capture any new transctions next time the code runs.
	update  ib_inventory_id_hearme
	set ib_inventory_id = (select max(ib_inventory_id) as ib_inventory_id from ib_inventory with (nolock))
	--------------------------------------------------------------------------------------------------

	--send email summary
	declare @original int,
			@negate int,
			@sound int
			
	select @original = count(*) from tblHearMeSalesConversionArchive_original
	
	select @negate = count(*) from #negated
			
	select @sound = count(*) from #sound
			

	declare @text nvarchar(max)
	
	 
	set @text = '<font face =arial size = 2></font>' + 
				'<font face =arial size = 2>' + 
				'The HearMe Sales Conversion Process has completed.' +
				'<br>'+
				'Total Sound Transactions: ' + convert(varchar,@original) +
				'<br>' +
				'Total Negated Transactions: ' + convert(varchar,@negate) +
				'<br>' +
				'Total Universal Sound Transactions: ' + convert(varchar,@sound) +
					'</font></p></p> <br><br><br>'
		


	exec msdb.dbo.sp_send_dbmail
	@profile_name = 'merchadmin',
	@recipients = 'merchadmin@buildabear.com', 
	@body = @text,
	@subject = 'HearMe Sales Conversion Process Complete',
	@body_format = 'HTML'


end
```

