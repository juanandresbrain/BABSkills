# Azure.vwPOSOutbound_tax_level

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwPOSOutbound_tax_level"]
    dbo_tax_level(["dbo.tax_level"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tax_level |

## View Code

```sql
CREATE VIEW [Azure].[vwPOSOutbound_tax_level] AS

select * from bedrockdb01.auditworks.dbo.tax_level
```

