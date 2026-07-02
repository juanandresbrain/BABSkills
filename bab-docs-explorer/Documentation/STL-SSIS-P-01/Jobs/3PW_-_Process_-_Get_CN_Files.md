# Job: 3PW - Process - Get CN Files

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["3PW - Process - Get CN Files"]
    JOB --> InvAdj_1["Step 1: InvAdj [TSQL]"]`n    JOB --> PoReceipt_2["Step 2: PoReceipt [TSQL]"]`n    JOB --> Inventory_3["Step 3: Inventory [TSQL]"]`n    JOB --> Shipments_4["Step 4: Shipments [TSQL]"]`n```

## Steps

### Step 1: InvAdj
**Subsystem:** TSQL  

```sql
exec [WMS].[spMerchandisingFtpCN_GetInvAdjFiles]  
```

### Step 2: PoReceipt
**Subsystem:** TSQL  

```sql
exec [WMS].[spMerchandisingFtpCN_GetPoReceiptFiles]  
```

### Step 3: Inventory
**Subsystem:** TSQL  

```sql
exec [WMS].[spMerchandisingFtpCN_GetInventoryFiles]  
```

### Step 4: Shipments
**Subsystem:** TSQL  

```sql
exec [WMS].[spMerchandisingFtpCN_GetShipmentFiles]  
```


