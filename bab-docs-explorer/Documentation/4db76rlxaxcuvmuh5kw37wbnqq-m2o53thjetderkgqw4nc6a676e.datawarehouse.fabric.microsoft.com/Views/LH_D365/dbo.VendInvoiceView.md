# dbo.VendInvoiceView

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.VendInvoiceView"]
    d365LocationMapping_View(["d365LocationMapping_View"]) --> VIEW
    generaljournalaccountentry(["generaljournalaccountentry"]) --> VIEW
    generaljournalentry(["generaljournalentry"]) --> VIEW
    inventdim(["inventdim"]) --> VIEW
    inventtrans(["inventtrans"]) --> VIEW
    inventtransorigin(["inventtransorigin"]) --> VIEW
    vendpackingslipversion(["vendpackingslipversion"]) --> VIEW
    markuptrans(["markuptrans"]) --> VIEW
    product_dim_le(["product_dim_le"]) --> VIEW
    vendinvoicejour(["vendinvoicejour"]) --> VIEW
    vendinvoicetrans(["vendinvoicetrans"]) --> VIEW
    vendpackingslipjour(["vendpackingslipjour"]) --> VIEW
    vendpackingsliptrans(["vendpackingsliptrans"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| d365LocationMapping_View |
| generaljournalaccountentry |
| generaljournalentry |
| inventdim |
| inventtrans |
| inventtransorigin |
| vendpackingslipversion |
| markuptrans |
| product_dim_le |
| vendinvoicejour |
| vendinvoicetrans |
| vendpackingslipjour |
| vendpackingsliptrans |

## View Code

```sql
CREATE   VIEW  [dbo].[VendInvoiceView] 
AS 

WITH iprvouchers as (
SELECT
    mt.voucher,
    mt.transtableid,
    mt.transrecid,
	mt.currencycode,
    UPPER(REPLACE(mt.markupcode, ' ', '')) AS markupcode,
    mt.calculatedamount,
	vp.origpurchid as purchid,
	vp.packingslipid as [documentid],
	vp.deliverydate as [documentdate],
	vp.dataareaid,
	vp.inventdimid,
	vp.qty,
	vp.itemid,
	vp.valuemst as lineamount,
	vp.lineamount_w as lineamountmst,
	mt.calculatedamount as ConvertedAmount
FROM markuptrans mt
 INNER JOIN vendpackingsliptrans vp
    on vp.tableid = mt.transtableid
      AND vp.recid   = mt.transrecid
	  AND vp.costledgervoucher = mt.voucher
Where mt.calculatedamount <> 0	
) 
, apivoucher AS (
SELECT
    mt.voucher,
    mt.transtableid,
    mt.transrecid,
	mt.currencycode,
    UPPER(REPLACE(mt.markupcode, ' ', '')) AS markupcode,
    mt.calculatedamount,
	vt.purchid,
	vt.invoiceid as [documentid],
	vt.invoicedate as [documentdate],
	vt.dataareaid,
	vt.inventdimid,
	vt.qty,
	vt.itemid,
	vt.lineamount,
	vt.lineamountmst,
	--et.fxname
	CAST (mt.calculatedamount * round(vj.exchrate/100,5,1) AS DECIMAL(18, 2)) as ConvertedAmount
FROM markuptrans mt
    INNER JOIN vendinvoicetrans vt
        ON vt.tableid = mt.transtableid
       AND vt.recid   = mt.transrecid
		AND vt.itemid IS NOT NULL
INNER JOIN vendinvoicejour vj
	on vj.invoiceid = vt.invoiceid
	AND vj.dataareaid = vt.dataareaid
	AND vj.invoicedate = vt.invoicedate
	AND vj.ledgervoucher = mt.voucher
Where mt.calculatedamount <> 0 
and NOT EXISTS(Select 1 from iprvouchers ipr 
				where ipr.itemid = vt.itemid 
					and ipr.purchid = vt.origpurchid 
					and ipr.dataareaid = vt.dataareaid
					)
UNION ALL
SELECT 
    mt.voucher,
    mt.transtableid,
    mt.transrecid,
    mt.currencycode,
    UPPER(REPLACE(mt.markupcode, ' ', '')) AS markupcode,
    CASE 
        WHEN mt.markupcode = 'VenFreight' 
        THEN mt.calculatedamount * -1 
        ELSE mt.calculatedamount 
    END AS calculatedamount,

    vj.purchid,	
    vj.invoiceid AS documentid,
    vj.invoicedate AS documentdate,
    vj.dataareaid,		

    -- From vendinvoicetrans (only FIRST row)
    vt.inventdimid,
    0 as qty,--vt.qty,
    vt.itemid,	
	0.00 as invoiceamount,
	0.00 as invoiceamountmst,
	CAST ( CASE WHEN mt.markupcode = 'VenFreight' THEN mt.calculatedamount * -1 ELSE mt.calculatedamount END * round(vj.exchrate/100,5,1) AS DECIMAL(18, 2)) as ConvertedAmount
FROM markuptrans mt

INNER JOIN vendinvoicejour vj
    ON vj.tableid = mt.transtableid
    AND vj.recid = mt.transrecid 
    AND vj.ledgervoucher = mt.voucher
    AND vj.dataareaid = mt.dataareaid 

-- get only ONE row from vendinvoicetrans
OUTER APPLY (
    SELECT TOP 1 *
    FROM vendinvoicetrans vt
    WHERE vt.invoiceid = vj.invoiceid
      AND vt.invoicedate = vj.invoicedate
      AND vt.dataareaid = vj.dataareaid
    ORDER BY vt.itemid  
) vt

WHERE mt.calculatedamount <> 0

)
,CorrectionVouchers as (
	select
        vpsj.dataareaid,
        vpsj.purchid,
        vpsj.packingslipid,
		count(*) as correctioncount
        ,Max(vpsv.ledgervoucher) as voucher
    from vendpackingslipjour vpsj
    join vendpackingslipversion vpsv
      on vpsv.vendpackingslipjour = vpsj.recid
    --where vpsj.dataareaid = '1200'
		--and vpsj.purchid    = 'PO120011428'
	--and vpsv.accountingdate > '2024-01-01'
group by vpsj.purchid, vpsj.packingslipid, vpsj.dataareaid
having count(*) > 1
)
, glvoucher as 
(
Select
c.voucher
, ga.tableid as trantableid
, ga.recid as transrecid
, t.currencycode
, CASE When ga.ledgeraccount = '200050' then 'OCEANFRT'
WHEN ga.ledgeraccount = '200570' THEN 'FOBROY'
WHEN ga.ledgeraccount = '200055' THEN 'TARIFFS'
END as markupcode
,ga.accountingcurrencyamount  * -1 as ChargeAmount 
,t.referenceid as purchid
,ge.documentnumber as documentid
,ge.documentdate as documentdate
,t.dataareaid
,t.inventdimid
```

