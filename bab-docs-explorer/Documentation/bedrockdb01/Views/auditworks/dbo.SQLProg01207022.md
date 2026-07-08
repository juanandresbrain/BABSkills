# dbo.SQLProg01207022

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.SQLProg01207022"]
    dbo_IFO01780001_backlog(["dbo.IFO01780001_backlog"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.IFO01780001_backlog |

## View Code

```sql
create view SQLProg01207022 AS
SELECT CONVERT(numeric(22, 0), RIGHT(CONVERT(varchar(12), 
    C2_IFEntryN) + RIGHT('00000' + CONVERT(varchar(5), 
    C3_TrnsctnLn), 3) + RIGHT('00000' + CONVERT(varchar(5), 
    ISNULL(C20_APPLIEDBYLINEID, 0)), 3), 14)) AS identity_no, 
    C2_IFEntryN AS if_entry_no, 
    C3_TrnsctnLn AS transaction_line_id, 
    C4_TrnsctnDt AS transaction_date, 
    C5_TrnsctnN AS transaction_no, C6_LctnID AS location_id, 
    C7_Rgstr AS register_no, C8_RfrncN AS reference_no, 
    C9_TrnsctnTyp AS transaction_type, C10_StylID AS style_id, 
    C11_SKUID AS sku_id, C12_UPCN AS upc_no, 
    C13_PrcOvrrd AS price_override_flag, 
    C14_RsnCd AS reason_code, C15_Unts AS units, 
    C16_SldAtPrc AS sold_at_price, 
    C17_POSDISCOUNTTYPECODE AS pos_disc_type_code, 
    C18_POSDISCOUNTTYPEDESC AS pos_disc_type_desc, 
    C19_POSDISCOUNTAMOUNT AS pos_disc_type_amt, 
    C20_APPLIEDBYLINEID AS applied_by_line_id, 
    C21_RECORDTYPE AS record_type
FROM dbo.IFO01780001_backlog
```

