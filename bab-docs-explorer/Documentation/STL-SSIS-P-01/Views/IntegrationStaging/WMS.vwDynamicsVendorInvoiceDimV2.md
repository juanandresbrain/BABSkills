# WMS.vwDynamicsVendorInvoiceDimV2

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WMS.vwDynamicsVendorInvoiceDimV2"]
    erp_VendorMaster(["erp.VendorMaster"]) --> VIEW
    ERP_WarehouseMaster(["ERP.WarehouseMaster"]) --> VIEW
    WMS_DynamicsVendorInvoiceJournalLineStage(["WMS.DynamicsVendorInvoiceJournalLineStage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| erp.VendorMaster |
| ERP.WarehouseMaster |
| WMS.DynamicsVendorInvoiceJournalLineStage |

## View Code

```sql
CREATE view [WMS].[vwDynamicsVendorInvoiceDimV2]

as

with VendorMaster as (
select Entity,
VENDORACCOUNTNUMBER, 
VENDORORGANIZATIONNAME, 
VENDORSEARCHNAME,
PRIMARYEMAILADDRESS,
DEFAULTVENDORPAYMENTMETHODNAME,
DEFAULTPAYMENTTERMSNAME
from erp.VendorMaster v

),

MaxVendorEntry as (
select AccountDisplayValue, 
Company, 
SUBSTRING(vjl.OffsetAccountDisplayValue, CHARINDEX('-',OffsetAccountDisplayValue)+1,4)as StoreNumberExtract, 
max([Date]) as [MaxDate]
from  [WMS].[DynamicsVendorInvoiceJournalLineStage] VJL
where right(OffsetAccountDisplayValue,5) <> '-----' -- Appears to be non store location 
and OffsetAccountDisplayValue <> '' -- No location invoiced 
group by 
AccountDisplayValue, 
Company, 
SUBSTRING(vjl.OffsetAccountDisplayValue, CHARINDEX('-',OffsetAccountDisplayValue)+1,4)
), 


VendorLines as (

select
RemittanceAddressDescription, 
FullPrimaryRemittanceAddress, 
AccountDisplayValue, 
Company, 
OffsetAccountDisplayValue, 
SUBSTRING(vjl.OffsetAccountDisplayValue, CHARINDEX('-',OffsetAccountDisplayValue)+1,4)as StoreNumberExtract, 
[Date], 
   substring(OffsetAccountDisplayValue, p1.Pos,6)   AS MainAccount
  ,substring(OffsetAccountDisplayValue, P1.Pos + 7, 4)  AS Store
  ,substring(OffsetAccountDisplayValue, P2.Pos + 8, 4)  AS CostCenter
  ,substring(OffsetAccountDisplayValue, P3.Pos + 9, 2)  AS BusinessStream
  ,substring(OffsetAccountDisplayValue, P4.Pos + 10, 5)  AS ProjectID
  ,substring(OffsetAccountDisplayValue, P5.Pos + 11, 5)  AS ProjectCategory
from  [WMS].[DynamicsVendorInvoiceJournalLineStage] VJL
  CROSS APPLY (SELECT 1)            AS P1(Pos)
  CROSS APPLY (SELECT P1.Pos+4)     AS P2(Pos)
  CROSS APPLY (SELECT P2.Pos+4)     AS P3(Pos)
  CROSS APPLY (SELECT P3.Pos+2)     AS P4(Pos)
  CROSS APPLY (SELECT P4.Pos+5)     AS P5(Pos)
  CROSS APPLY (SELECT P5.Pos+6)     AS P6(Pos)
where right(OffsetAccountDisplayValue,5) <> '-----' -- Appears to be non store location 
and OffsetAccountDisplayValue <> '' -- No location invoiced 
group by 
RemittanceAddressDescription, 
FullPrimaryRemittanceAddress, 
AccountDisplayValue, 
Company, 
OffsetAccountDisplayValue, 
SUBSTRING(vjl.OffsetAccountDisplayValue, CHARINDEX('-',OffsetAccountDisplayValue)+1,4),
[Date], 
p1.Pos, 
p2.Pos, 
p3.Pos, 
p4.Pos, 
p5.Pos,
P6.pos
), 

WarehouseMaster as (
select WarehouseId, WarehouseName, Entity
from [ERP].[WarehouseMaster] w
where isnumeric(Warehouseid) = 1
and WarehouseId not in ('10') -- Lingering warehouse from initial Dynamics implementation

), 

Summary1 as (

select 
vm.VENDORACCOUNTNUMBER as VendorAccount, 
vm.VENDORORGANIZATIONNAME as VendorName, 
vm.VENDORSEARCHNAME as SearchName,
vm.PRIMARYEMAILADDRESS as RemittanceEmail,
vl.RemittanceAddressDescription as RemittanceLocation, 
vl.FullPrimaryRemittanceAddress as RemittanceAddress, 
vm.DEFAULTVENDORPAYMENTMETHODNAME as MethodOfPayment,
vm.DEFAULTPAYMENTTERMSNAME as TermsOfPayment, 
isnull(wm.WarehouseId,vl.StoreNumberExtract) as StoreNumber , 
isnull(wm.WarehouseName,'Store Name Not Found') as StoreName, 
--vl.StoreNumberExtract, 
vl.OffsetAccountDisplayValue, 
vl.Company, 
vl.[Date], 
vl.MainAccount as DefaultAccountLedger,
vl.Store, 
vl.CostCenter,
vl.BusinessStream, 
vl.ProjectID, 
vl.ProjectCategory
--, rs.*
from VendorLines vl 
join MaxVendorEntry mve on mve.AccountDisplayValue=vl.AccountDisplayValue	
	and mve.Company=vl.Company
	and mve.StoreNumberExtract=vl.StoreNumberExtract
	and mve.MaxDate=vl.[Date]
left join VendorMaster vm on vm.VENDORACCOUNTNUMBER=vl.AccountDisplayValue
	and vm.Entity=vl.company
left join WarehouseMaster wm on wm.WarehouseId=vl.StoreNumberExtract 
	and wm.Entity=vl.company
group by vm.VENDORACCOUNTNUMBER, 
vm.VENDORORGANIZATIONNAME , 
vm.VENDORSEARCHNAME ,
vm.PRIMARYEMAILADDRESS ,
vl.RemittanceAddressDescription , 
vl.FullPrimaryRemittanceAddress , 
vm.DEFAULTVENDORPAYMENTMETHODNAME ,
vm.DEFAULTPAYMENTTERMSNAME , 
isnull(wm.WarehouseId,vl.StoreNumberExtract) , 
isnull(wm.WarehouseName,'Store Name Not Found'), 
--vl.StoreNumberExtract, 
vl.OffsetAccountDisplayValue, 
vl.Company,
vl.[Date], 
vl.MainAccount, 
vl.Store, 
vl.CostCenter, 
vl.BusinessStream, 
vl.ProjectID, 
vl.ProjectCategory
--order by vl.Company, 1, 9
--order by vl.Company, 9, 1
) 

select
VendorAccount, 
VendorName, 
SearchName, 
RemittanceEmail, 
RemittanceLocation, 
RemittanceAddress, 
MethodOfPayment, 
TermsOfPayment, 
StoreNumber, 
StoreName, 
Company, 
Date, 
OffsetAccountDisplayValue,
replace(DefaultAccountLedger,'-','') as DefaultAccountLedger, 
--replace (Store,'-','') as  Store,
replace(CostCenter,'-','') as CostCenter, 
replace(BusinessStream,'-','') as BusinessStream,
replace(ProjectID,'-','') as ProjectID,
replace(ProjectCategory,'-','') as ProjectCategory


from Summary1
```

