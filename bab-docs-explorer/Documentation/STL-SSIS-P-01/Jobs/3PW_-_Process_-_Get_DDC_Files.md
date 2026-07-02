# Job: 3PW - Process - Get DDC Files

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["3PW - Process - Get DDC Files"]
    JOB --> Receipts_1["Step 1: Receipts [TSQL]"]`n    JOB --> Shipments_2["Step 2: Shipments [TSQL]"]`n    JOB --> Inventory_3["Step 3: Inventory [TSQL]"]`n    JOB --> Adjustments_4["Step 4: Adjustments [TSQL]"]`n```

## Steps

### Step 1: Receipts
**Subsystem:** TSQL  

```sql
exec [WMS].[spMerchandisingFTPgetDDCreceiptsWinSCP]  
```

### Step 2: Shipments
**Subsystem:** TSQL  

```sql
exec [WMS].[spMerchandisingFTPgetDDCshipmentsWinSCP]  
```

### Step 3: Inventory
**Subsystem:** TSQL  

```sql
exec [WMS].[spMerchandisingFTPgetDDCinventoryWinSCP]  
```

### Step 4: Adjustments
**Subsystem:** TSQL  

```sql
exec [WMS].[spMerchandisingFTPgetDDCAdjustmentsWinSCP]  
```


