# ERP.vwFactoryAddress

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["ERP.vwFactoryAddress"]
    ERP_VendorMaster(["ERP.VendorMaster"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| ERP.VendorMaster |

## View Code

```sql
CREATE VIEW [ERP].[vwFactoryAddress]
AS

-- Vendors using the BABFactoryCode and BABVendorCode fields
SELECT DISTINCT 
	vm.VENDORACCOUNTNUMBER VendorAccount
	, vm.BABFactoryCode FactoryCode
	, vm.ADDRESSDESCRIPTION AddressDescription
	, vm.BABFOBPort FOBPort
	, vm.BABVendorCode SupplierCode
	, vm.ADDRESSSTREET Street
	, vm.ADDRESSCITY City
	, vm.ADDRESSSTATEID Province
	, vm.ADDRESSCOUNTRYREGIONISOCODE Country
	, vm.PRIMARYPHONENUMBER PhoneNumber
	, CASE
        WHEN CHARINDEX(' - ', vm.ADDRESSDESCRIPTION) > 0
            THEN LEFT(vm.ADDRESSDESCRIPTION, CHARINDEX(' - ', vm.ADDRESSDESCRIPTION) - 1)
        ELSE vm.ADDRESSDESCRIPTION
      END AS VendorName
    , CASE
        WHEN CHARINDEX(' - ', vm.ADDRESSDESCRIPTION) > 0
            THEN SUBSTRING(
                     vm.ADDRESSDESCRIPTION,
                     CHARINDEX(' - ', vm.ADDRESSDESCRIPTION) + 3,
                     LEN(vm.ADDRESSDESCRIPTION)
                 )
        ELSE vm.ADDRESSDESCRIPTION
      END AS AddressName
	, vm.Entity
	, ISNULL(vm.UpdateDate,vm.InsertDate) LastModified
  FROM IntegrationStaging.ERP.VendorMaster vm with(nolock)
  WHERE 1=1
--	AND vm.BABFactoryCode IN ('USFACT','UKFACT','CHFACT','MXFACT','KRFACT','ITFACT','SVFACT')
	AND vm.BABFactoryCode <> '' 
	AND vm.BABVendorCode <> ''
	AND vm.BABFOBPort <> ''
	AND vm.ADDRESSSTREET <> ''

---- Vendors with blank BABFactoryCode and BABVendorCode fields and rely on the OrganizationPhoneticName field (vendors setup in Dynamics to have more than 1 factory address, as notated by including VendorCode and Factory code in the OrganizationPhoneticName field as 'VendorCode-FactoryCode')
--UNION
--SELECT DISTINCT 
--	vm.VENDORACCOUNTNUMBER VendorAccount
--	, substring(vm.OrganizationPhoneticName, charindex('-',vm.OrganizationPhoneticName)+1,10 ) FactoryCode
--	, vm.ADDRESSDESCRIPTION AddressDescription
--	, 'place holder for FOB port logic' FOBPort
--	, substring(vm.OrganizationPhoneticName, 1, charindex('-',vm.OrganizationPhoneticName)-1) SupplierCode
--	, vm.ADDRESSSTREET Street
--	, vm.ADDRESSCITY City
--	, vm.ADDRESSSTATEID Province
--	, vm.ADDRESSCOUNTRYREGIONISOCODE Country
--	, vm.PRIMARYPHONENUMBER PhoneNumber
--	, vm.Entity
--	, ISNULL(vm.UpdateDate,vm.InsertDate) LastModified
--  FROM IntegrationStaging.ERP.VendorMaster vm with(nolock)
--  WHERE 1=1
--	AND (vm.BABFactoryCode = '' OR vm.BABVendorCode = '')
--	AND vm.OrganizationPhoneticName like '%-%'
--	AND vm.ADDRESSSTREET <> ''
--	--AND substring(vm.OrganizationPhoneticName, charindex('-',vm.OrganizationPhoneticName)+1,10 ) in ('USFACT','UKFACT','CHFACT','MXFACT','KRFACT','ITFACT','SVFACT')


---- Vendors with blank BABFactoryCode and BABVendorCode fields and rely on the OrganizationPhoneticName field (vendors setup in Dynamics generic country factory code, joins only on the factory code, not on vendor code)
--UNION
--SELECT DISTINCT
--	vm.VENDORACCOUNTNUMBER VendorAccount
--	, 'place holder for fc' FactoryCode
--	, vm.ADDRESSDESCRIPTION AddressDescription
--	, 'place holder for FOB port logic' FOBPort
--	, substring(vm.OrganizationPhoneticName, 1, charindex('-',vm.OrganizationPhoneticName)-1) SupplierCode
--	, vm.ADDRESSSTREET Street
--	, vm.ADDRESSCITY City
--	, vm.ADDRESSSTATEID Province
--	, vm.ADDRESSCOUNTRYREGIONISOCODE Country
--	, vm.PRIMARYPHONENUMBER PhoneNumber
--	, vm.Entity
--	, ISNULL(vm.UpdateDate,vm.InsertDate) LastModified
--  FROM IntegrationStaging.ERP.VendorMaster vm with(nolock)
--  WHERE 1=1
--	AND (vm.BABFactoryCode = '' OR vm.BABVendorCode = '')
--	AND vm.OrganizationPhoneticName like '%-%'
--	AND vm.ADDRESSSTREET <> ''
	
---- Vendors with blank BABFactoryCode and BABVendorCode fields and are vendors setup in Dynamics to have only 1 factory address (as notated by only including VendorCode in the OrganizationPhoneticName field and not including '-') rely on the OrganizationPhoneticName field
--UNION
--SELECT DISTINCT 
--	vm.VENDORACCOUNTNUMBER VendorAccount
--	, 'place holder for fc' FactoryCode
--	, vm.ADDRESSDESCRIPTION AddressDescription
--	, 'place holder for FOB port logic' FOBPort
--	, CASE 
--			WHEN CHARINDEX('-', vm.OrganizationPhoneticName) > 0
--			THEN SUBSTRING(vm.OrganizationPhoneticName, 1, CHARINDEX('-', vm.OrganizationPhoneticName) - 1)
--			ELSE vm.OrganizationPhoneticName
--		END 
--	  AS SupplierCode
--	, vm.ADDRESSSTREET Street
--	, vm.ADDRESSCITY City
--	, vm.ADDRESSSTATEID Province
--	, vm.ADDRESSCOUNTRYREGIONISOCODE Country
--	, vm.PRIMARYPHONENUMBER PhoneNumber
--	, vm.Entity
--	, ISNULL(vm.UpdateDate,vm.InsertDate) LastModified
--  FROM IntegrationStaging.ERP.VendorMaster vm with(nolock)
--  LEFT JOIN IntegrationStaging.ERP.FactoryAddress fa with(nolock) 
--	ON vm.OrganizationPhoneticName = fa.VendorCode
--  WHERE 1=1
--	AND (vm.BABFactoryCode = '' OR vm.BABVendorCode = '')
--	AND vm.OrganizationPhoneticName NOT like '%-%'
--	AND vm.OrganizationPhoneticName <> ''

ERP,vwInventoryXML,create view ERP.InventoryXML

as

-------------------------------------------------------------------------------------------
--Dan Tweedie - 2017-08-11 -	Created view to output inventory as xml for Dynamics365
-------------------------------------------------------------------------------------------

with
XMLStage (XMLData) as 
	(
		select 
			0 as 'ARELINESDELETEDAFTERPOSTING',
			'WM inventory synchronization' as 'DESCRIPTION',
			0 as 'ISPOSTED',
			'WMCount' as 'JOURNALNAMEID',
			0 as 'POSTINGDETAILLEVEL',
			0 as 'RESERVATIONMODE',
			1 as 'VOUCHERNUMBERALLOCATIONRULE',
			0 as 'VOUCHERNUMBERSELECTIONRULE',
			'IM-WM' as 'VOUCHERNUMBERSEQUENCECODE',
			(
				select
					StyleCode as 'ITEMNUMBER', 
					LocationCode as 'INVENTORYSITEID',
					QTY as 'INVENTORYQUANTITY',
					'WMCount' as 'JOURNALNAMEID',
					row_number() over(order by LocationCode, StyleCode) as LINENUMBER,
					'100630' as 'OFFSETMAINACCOUNTIDDISPLAYVALUE',
					getdate() as 'TRANSACTIONDATE',
					1 as 'UNITCOSTQUANTITY'
				from ERP.WarehouseInventoryStage
				order by 5
				for xml path('InventInventoryMovementJournalEntryEntity'), Type
			)
		for xml path('InventInventoryMovementJournalHeaderEntity'), root('Document'), Type
	)
select XMLData
from XMLStage
```

