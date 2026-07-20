# dbo.vwdw_communication_channel_dim

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_communication_channel_dim"]
    dbo_communication_channel_dim(["dbo.communication_channel_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.communication_channel_dim |

## View Code

```sql
CREATE VIEW vwdw_communication_channel_dim
AS 
SELECT * FROM LH_Mart.dbo.communication_channel_dim
```

