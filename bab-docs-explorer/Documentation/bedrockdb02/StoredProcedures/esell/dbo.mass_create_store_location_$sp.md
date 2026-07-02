# dbo.mass_create_store_location_$sp

**Database:** esell  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.mass_create_store_location_$sp"]
    dbo_ADT_TRL_DTL(["dbo.ADT_TRL_DTL"]) --> SP
    dbo_ADT_TRL_HDR(["dbo.ADT_TRL_HDR"]) --> SP
    dbo_ADT_TRL_QRY(["dbo.ADT_TRL_QRY"]) --> SP
    dbo_ORG_CHN_LOC(["dbo.ORG_CHN_LOC"]) --> SP
    dbo_ORG_CHN_LOC_FNCTN(["dbo.ORG_CHN_LOC_FNCTN"]) --> SP
    dbo_ORG_CHN_LOC_FNCTN_A(["dbo.ORG_CHN_LOC_FNCTN_A"]) --> SP
    dbo_T_LONG_INTEGER(["dbo.T_LONG_INTEGER"]) --> SP
    dbo_to_hex(["dbo.to_hex"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ADT_TRL_DTL |
| dbo.ADT_TRL_HDR |
| dbo.ADT_TRL_QRY |
| dbo.ORG_CHN_LOC |
| dbo.ORG_CHN_LOC_FNCTN |
| dbo.ORG_CHN_LOC_FNCTN_A |
| dbo.T_LONG_INTEGER |
| dbo.to_hex |

## Stored Procedure Code

```sql

```

