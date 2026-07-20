# dbo.sales_gaap_rawfromstoreserver

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sales_gaap_rawfromstoreserver"]
    dbo_sales_gaap_rawfromstoreserver(["dbo.sales_gaap_rawfromstoreserver"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sales_gaap_rawfromstoreserver |

## View Code

```sql
; CREATE   VIEW [dbo].[sales_gaap_rawfromstoreserver] AS     SELECT [store_key], [date_key], [TransactionDatetime], [location_code] COLLATE Latin1_General_CI_AS AS [location_code], [location_name] COLLATE Latin1_General_CI_AS AS [location_name], [net_sales], [entry_date], [source] COLLATE Latin1_General_CI_AS AS [source], [RTL_TRN_ID], [STORE_NO], [WORKSTATION_NO], [RTL_TRN_NO] COLLATE Latin1_General_CI_AS AS [RTL_TRN_NO], [OPERATOR_NO], [RTL_TRN_TYPE_CODE] COLLATE Latin1_General_CI_AS AS [RTL_TRN_TYPE_CODE], [ITEM_NO] COLLATE Latin1_General_CI_AS AS [ITEM_NO], [VOID_FLG], [WebOrderNumber] COLLATE Latin1_General_CI_AS AS [WebOrderNumber], [TransactionID], [isBOSISorBOPIS], [SalesAuditRegisterNumber], [SalesAuditTransactionRemark] COLLATE Latin1_General_CI_AS AS [SalesAuditTransactionRemark], [GaapSalesDW], [isGaapDW], [InsertDate], [UpdateDate]     FROM [dbo].[sales_gaap_rawfromstoreserver]
```

