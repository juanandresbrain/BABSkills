# dbo.usp_build_temp_view_tables

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.usp_build_temp_view_tables"]
    tmp_edin_vwStore_dim_ForCube(["tmp_edin_vwStore_dim_ForCube"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| tmp_edin_vwStore_dim_ForCube |

## Stored Procedure Code

```sql
CREATE proc usp_build_temp_view_tables
as

truncate table tmp_edin_vwStore_dim_ForCube

set nocount on

insert into tmp_edin_vwStore_dim_ForCube
exec sp_helptext 'vwStore_dim_ForCube'
```

