# Job: MERCHANDISING - Process - DB Schenker PO Export

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Exports PO's to DB Schenker

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - DB Schenker PO Export"]
    JOB --> 1___Get_ASN_1["Step 1: 1 - Get ASN [TSQL]"]`n    JOB --> 2___Bulk_Insert_ASN_2["Step 2: 2 - Bulk Insert ASN [TSQL]"]`n    JOB --> 3___Select_PO_Data_3["Step 3: 3 - Select PO Data [TSQL]"]`n    JOB --> 4___Previously_Canceled_4["Step 4: 4 - Previously Canceled [TSQL]"]`n    JOB --> 5___Select_Canceled_PO_5["Step 5: 5 - Select Canceled PO [TSQL]"]`n    JOB --> 6___Line_Swap_and_Canceled_6["Step 6: 6 - Line Swap and Canceled [TSQL]"]`n    JOB --> 7___Export_7["Step 7: 7 - Export [TSQL]"]`n    JOB --> 8___Email_Summary_8["Step 8: 8 - Email Summary [TSQL]"]`n```

## Steps

### Step 1: 1 - Get ASN
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingDBSchenkerPOExport_1_GetASN
```

### Step 2: 2 - Bulk Insert ASN
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingDBSchenkerPOExport_2_BulkInsertASN
```

### Step 3: 3 - Select PO Data
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoData
```

### Step 4: 4 - Previously Canceled
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingDBSchenkerPOExport_4_PreviouslyCanceled
```

### Step 5: 5 - Select Canceled PO
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingDBSchenkerPOExport_5_SelectCanceledPO
```

### Step 6: 6 - Line Swap and Canceled
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLines
```

### Step 7: 7 - Export
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingDBSchenkerPOExport_7_Export
```

### Step 8: 8 - Email Summary
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingDBSchenkerPOExport_8_EmailSummaryAndException
```


