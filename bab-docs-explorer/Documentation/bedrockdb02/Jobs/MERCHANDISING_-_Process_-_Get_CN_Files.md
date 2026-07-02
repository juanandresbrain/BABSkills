# Job: MERCHANDISING - Process - Get CN Files

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Downloads files from Shanghai DC, sends email summary

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Get CN Files"]
    JOB --> InvAdj_1["Step 1: InvAdj [TSQL]"]`n    JOB --> Receipts_2["Step 2: Receipts [TSQL]"]`n    JOB --> Inventory_3["Step 3: Inventory [TSQL]"]`n    JOB --> Shipments_4["Step 4: Shipments [TSQL]"]`n    JOB --> Inactive_Step____Move_3980_Files_to_Sub_Directory_5["Step 5: Inactive Step -  Move 3980 Files to Sub Directory [TSQL]"]`n    JOB --> Summary_6["Step 6: Summary [TSQL]"]`n```

## Steps

### Step 1: InvAdj
**Subsystem:** TSQL  

```sql
exec spMerchandisingFtpCN_GetInvAdjFiles
```

### Step 2: Receipts
**Subsystem:** TSQL  

```sql
exec spMerchandisingFtpCN_GetPoReceiptFiles
```

### Step 3: Inventory
**Subsystem:** TSQL  

```sql
exec spMerchandisingFtpCN_GetInventoryFiles
```

### Step 4: Shipments
**Subsystem:** TSQL  

```sql
exec spMerchandisingFtpCN_GetShipmentFiles
```

### Step 5: Inactive Step -  Move 3980 Files to Sub Directory
**Subsystem:** TSQL  

```sql
/*
Added on 06/18/2021
Ocean East Logisitics was not to send sync files for 3980 until week of 6/28/2021
Beginning 6/18/21 they were sending them anyway  with only a handful of styles, which would have caused massive shrink in Aptos Merchandising
Temporarily moving these to seperate directory until 3980 integrations are live 

Remarked out on 7/1/2021 as we were given the green light to process 3980 files, keeping it here in case needed in the near future 



declare @moveInventory varchar(1000)


select @moveInventory = 'move \\kermode\FileRepository\MERCHANDISING\CN_Distro\INBOUND\INVENTORY\*3980.csv \\kermode\FileRepository\MERCHANDISING\CN_Distro\INBOUND\INVENTORY\3980'

exec master..xp_cmdshell @moveInventory



*/


```

### Step 6: Summary
**Subsystem:** TSQL  

```sql
-- exec spMerchandisingFTPCNGetFileSummary -- Remarked out on 7/29/2021 by TimC, I was the only one receiving the email as MerchAdmin had previously opted out
```


