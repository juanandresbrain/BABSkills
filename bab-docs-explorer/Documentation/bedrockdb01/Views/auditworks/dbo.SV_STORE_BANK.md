# dbo.SV_STORE_BANK

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.SV_STORE_BANK"]
    ORG_BANK(["ORG_BANK"]) --> VIEW
    ORG_BANK_ACNT(["ORG_BANK_ACNT"]) --> VIEW
    ORG_BANK_BRNCH(["ORG_BANK_BRNCH"]) --> VIEW
    SV_STORES(["SV_STORES"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| ORG_BANK |
| ORG_BANK_ACNT |
| ORG_BANK_BRNCH |
| SV_STORES |

## View Code

```sql
create view [dbo].[SV_STORE_BANK] AS 
SELECT o.ORG_CHN_NUM, o.PRMRY_BANK_ACNT_ID, b.BANK_SHRT_NAME, c.BANK_BRNCH_SHRT_NAME, BANK_BRNCH_NUM,
b.INSTN_NUM, a.BANK_ACNT_NUM, a.BANK_ACNT_DESC, a.GL_RFRNC_NUM
FROM SV_STORES o      
LEFT OUTER JOIN ORG_BANK_ACNT a
ON o.PRMRY_BANK_ACNT_ID = a.BANK_ACNT_ID
LEFT OUTER JOIN ORG_BANK b
on b.BANK_ID = a.BANK_ID
LEFT OUTER JOIN ORG_BANK_BRNCH c
ON a.BANK_BRNCH_ID = c.BANK_BRNCH_ID
```

