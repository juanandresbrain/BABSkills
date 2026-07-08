# dbo.district_sa

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.district_sa"]
    ORG_CHN_HRCHY_LVL_GRP(["ORG_CHN_HRCHY_LVL_GRP"]) --> VIEW
    auditworks_parameter(["auditworks_parameter"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| ORG_CHN_HRCHY_LVL_GRP |
| auditworks_parameter |

## View Code

```sql
create view dbo.district_sa 
AS
SELECT HRCHY_LVL_GRP_CODE AS district_code,
       HRCHY_LVL_GRP_DESC AS district_name,
       convert(numeric(12,0), null) AS resource_id
  FROM auditworks_parameter p, 
       ORG_CHN_HRCHY_LVL_GRP g
 WHERE p.par_name = 'district_HRCHY_LVL_ID'
   AND p.par_bin_value = g.HRCHY_LVL_ID
```

