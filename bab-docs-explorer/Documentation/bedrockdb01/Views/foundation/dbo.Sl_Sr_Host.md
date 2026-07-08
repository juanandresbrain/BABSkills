# dbo.Sl_Sr_Host

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.Sl_Sr_Host"]
    dbo_Sr_Host(["dbo.Sr_Host"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Sr_Host |

## View Code

```sql
CREATE VIEW dbo.Sl_Sr_Host (machine_id,host_id,host_label,host_name,user_name,user_password,merge_directory)
AS SELECT machine_id,host_id,host_label,host_name,user_name,user_password,merge_directory
FROM foundation.dbo.Sr_Host
```

