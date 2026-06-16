# WMS.spSelectWMSPurchaseOrderReceipts

**Database:** IntegrationStaging  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WMS.spSelectWMSPurchaseOrderReceipts"]
    WMS_PurchaseOrderReceipt(["WMS.PurchaseOrderReceipt"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WMS.PurchaseOrderReceipt |

## Stored Procedure Code

```sql
CREATE proc [WMS].[spSelectWMSPurchaseOrderReceipts] 

as 

-----------------------------------------------------------------------------------------------------------------------------------------------------
--	Dan Tweedie	2019-07-02	Created proc to push PO Receipts from Dynamics WMS to Aptos / Merchandising. Proc will be called so it goes into a file
----						PROC ASSUMES THAT INTEGRATION WILL HAVE ASN NUMBER THAT WE CAN PUT INTO REF_NBR FIELD - 
-----------------------------------------------------------------------------------------------------------------------------------------------------



set nocount on


IF (Object_ID('tempdb..#stage') IS NOT NULL) DROP TABLE #stage
select *
into #stage
from WMS.PurchaseOrderReceipt 
where PostedToAptosDate is NULL
and Warehouse in ('9980','0980', '1013','0013', '2991', '8010') 



set nocount on 

--capture po receipt data into work table
if (object_id('tempdb..#wms_po_receipts') is not null) drop table #wms_po_receipts
create table #wms_po_receipts
(
	Warehouse varchar(4),
	receipt_date varchar(10),
	po varchar(20),
	ASN varchar(20),
	UPC varchar(12),
	Units int,
	BOL varchar(52),
	id int identity(100, 1)
)

insert #wms_po_receipts
select	
		Warehouse,
		convert(varchar, cast(MessageQueueDateUTC as smalldatetime), 101) as receipt_date,
		AptosPONumber as PO, 
		ASN,
		'000000' + right(ItemID,6) as UPC, 
		sum(ReceivedQty) as rcvd_units,
		'' as BOL
from #stage
group by convert(varchar, cast(MessageQueueDateUTC as smalldatetime), 101), AptosPONumber, ASN, ItemID, Warehouse

---prepare data for printing
	declare @date varchar(12),
			@counterH int,
			@counterD int,
			@totalH int,
			@totalD int,
			@docnbr varchar(20),
			@po varchar(20),
			@ASN varchar(20),
			@UPC varchar(12),
			@Units int, 
			@bol varchar(52),
			@warehouse varchar(4)

	set @date = convert(varchar, getdate(), 101)
	select @totalH = count(distinct po+asn) from #wms_po_receipts
	set @counterH = 1

	declare header cursor for
		select distinct convert(varchar, getdate(), 112) + convert(varchar, datepart(hh, getdate())) + convert(varchar, datepart(mi, getdate())) + convert(varchar, datepart(ss, getdate())) + convert(varchar, max(id)) doc_nbr, isnull(bol, 'NO_BOL') bol, po, asn, case when Warehouse='9980' then '0980' when Warehouse='1013' then '0013' else Warehouse end as Warehouse
		from #wms_po_receipts
		group by po, asn, bol, case when Warehouse='9980' then '0980' when Warehouse='1013' then '0013' else Warehouse end
		order by po, asn, bol

	open header
	while @counterH <= @totalH
		begin
			fetch next from header into @docnbr, @bol, @po, @asn, @Warehouse
			print 'H' + '	' + 'A' + '	' + @docnbr + '	' + @bol + '	' + @date + '	' + @Warehouse + '	' + @po + '	' + 'Administrator' + '	' + '	' + '	' + '	' + '	' + @asn + '	' + '	' + '	' + '	' + '	' + '	' + '	' + '	' + '	' + '	' + '	' + 'N' + '	'
				--detail cursor
					set @counterD = 1
					select @totalD = count(upc) from #wms_po_receipts where po = @po and asn = @asn and isnull(bol, 'NO_BOL') = @bol
													
					declare detail cursor for
						select upc, units 
						from #wms_po_receipts
						where po = @po 
						and asn = @asn
						and isnull(bol, 'NO_BOL') = @bol
						and case when Warehouse='9980' then '0980' when Warehouse='1013' then '0013' else Warehouse end=@Warehouse
						order by upc
					
					open detail
					while @counterD <= @totalD
						begin
							fetch next from detail into @upc, @units
							print 'D' + '	' + 'A' + '	' + @docnbr + '	' + '	' + @upc + '	' + + '	' +  + '	' +  + '	' +  + '	' +  + '	' +  convert(varchar, @units) + '	'
							set @counterD = @counterD + 1
						end
					close detail
					deallocate detail
			
			set @counterH = @counterH + 1

		end

	close header
	deallocate header
```

