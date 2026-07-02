# Job: MERCHANDISING - Process - Get DDC Files

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Retrieves Inventory, Receipt, Adjustments and Shipment files from DDC's (west coast warehouse) FTP server.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Get DDC Files"]
    JOB --> Receipts_1["Step 1: Receipts [TSQL]"]`n    JOB --> Shipments_2["Step 2: Shipments [TSQL]"]`n    JOB --> Inventory_3["Step 3: Inventory [TSQL]"]`n    JOB --> Adjustments_4["Step 4: Adjustments [TSQL]"]`n    JOB --> File_Summary_5["Step 5: File Summary [TSQL]"]`n```

## Steps

### Step 1: Receipts
**Subsystem:** TSQL  

```sql
-- exec me_01.dbo.spMerchandisingFTPgetDDCreceipts
exec me_01.dbo.spMerchandisingFTPgetDDCreceiptsWinSCP
```

### Step 2: Shipments
**Subsystem:** TSQL  

```sql
-- exec me_01.dbo.spMerchandisingFTPgetDDCshipments
exec me_01.dbo.spMerchandisingFTPgetDDCshipmentsWinSCP
```

### Step 3: Inventory
**Subsystem:** TSQL  

```sql
-- exec me_01.dbo.spMerchandisingFTPgetDDCinventory
exec me_01.dbo.spMerchandisingFTPgetDDCinventoryWinSCP
```

### Step 4: Adjustments
**Subsystem:** TSQL  

```sql
-- exec me_01.dbo.spMerchandisingFTPgetDDCAdjustments
exec me_01.dbo.spMerchandisingFTPgetDDCAdjustmentsWinSCP
```

### Step 5: File Summary
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingSelectDDCFiles
```


