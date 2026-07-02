# dbo.vwSalesAuditTranslateSettlement

**Database:** BABWeCommerce  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwSalesAuditTranslateSettlement"]
    dbo_NSBTranslate_LogTrans(["dbo.NSBTranslate_LogTrans"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.NSBTranslate_LogTrans |

## View Code

```sql
CREATE VIEW dbo.vwSalesAuditTranslateSettlement
```

