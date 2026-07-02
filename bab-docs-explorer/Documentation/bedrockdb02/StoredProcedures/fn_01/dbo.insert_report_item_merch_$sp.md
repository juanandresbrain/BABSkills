# dbo.insert_report_item_merch_$sp

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.insert_report_item_merch_$sp"]
    dbo_FNDTN_RPRT_ITEM(["dbo.FNDTN_RPRT_ITEM"]) --> SP
    dbo_FNDTN_RPRT_ITEM_CRTRN_DFLT_VAL(["dbo.FNDTN_RPRT_ITEM_CRTRN_DFLT_VAL"]) --> SP
    dbo_FNDTN_RPRT_ITEM_CRTRN_FORM_A(["dbo.FNDTN_RPRT_ITEM_CRTRN_FORM_A"]) --> SP
    dbo_insert_report_criteria_form_assoc_merch__sp(["dbo.insert_report_criteria_form_assoc_merch_$sp"]) --> SP
    dbo_T_ID(["dbo.T_ID"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FNDTN_RPRT_ITEM |
| dbo.FNDTN_RPRT_ITEM_CRTRN_DFLT_VAL |
| dbo.FNDTN_RPRT_ITEM_CRTRN_FORM_A |
| dbo.insert_report_criteria_form_assoc_merch_$sp |
| dbo.T_ID |

## Stored Procedure Code

```sql

```

