# Job: MERCHANDISING - Process - Intercompany Transfer UDA and CBR

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Creates CBR for the transfers, creates UDA for the transfers + shipments as requested by Lisa V.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Intercompany Transfer UDA and CBR"]
    JOB --> one_1["Step 1: one [TSQL]"]`n    JOB --> two_2["Step 2: two [TSQL]"]`n```

## Steps

### Step 1: one
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingProcessAutoReceiveInterCompanyTransfers
```

### Step 2: two
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingOutputSelectInterCompanyTransfersUDA
MERCHANDISING - Process - Inventory Interface Summary	Yes	Summarizes data processed from the warehouses through our interfaces into Merch. 
Includes:
PO Receipts
Shipments	1	PO Receipts	TSQL	exec me_01.dbo.spMerchandisingSelectPOReceiptSummary
MERCHANDISING - Process - Inventory Interface Summary	Yes	Summarizes data processed from the warehouses through our interfaces into Merch. 
Includes:
PO Receipts
Shipments	2	Shipments	TSQL	exec me_01.dbo.spMerchandisingSelectShipmentSummary
MERCHANDISING - Process - Inventory Interface Summary	Yes	Summarizes data processed from the warehouses through our interfaces into Merch. 
Includes:
PO Receipts
Shipments	3	Shrink Adjustments	TSQL	exec me_01.dbo.spMerchandisingSelectShrinkAdjustmentSummary
MERCHANDISING - Process - Inventory Interface Summary	Yes	Summarizes data processed from the warehouses through our interfaces into Merch. 
Includes:
PO Receipts
Shipments	4	Carton Batch Receipts	TSQL	exec me_01.dbo.spMerchandisingSelectCBRSummary
MERCHANDISING - Process - Inventory Interface Summary	Yes	Summarizes data processed from the warehouses through our interfaces into Merch. 
Includes:
PO Receipts
Shipments	5	DDC Summary Email	TSQL	exec me_01.dbo.spMerchandisingReportDDCFileSummaries
```


