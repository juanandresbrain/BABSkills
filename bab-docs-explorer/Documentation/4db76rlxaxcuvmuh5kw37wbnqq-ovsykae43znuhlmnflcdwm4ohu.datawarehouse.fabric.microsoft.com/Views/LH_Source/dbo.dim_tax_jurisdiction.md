# dbo.dim_tax_jurisdiction

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.dim_tax_jurisdiction"]
    dbo_jumpmind_tax_authority(["dbo.jumpmind_tax_authority"]) --> VIEW
    dbo_jumpmind_tax_jurisdiction(["dbo.jumpmind_tax_jurisdiction"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.jumpmind_tax_authority |
| dbo.jumpmind_tax_jurisdiction |

## View Code

```sql
CREATE   VIEW dbo.dim_tax_jurisdiction AS SELECT     LTRIM(RTRIM(tj.geo_code))                          AS geo_code,     ta.auth_name                                        AS jurisdiction_name,     CAST(NULL AS varchar(10))                           AS state_code,            /* ⚠ TODO no source column on jumpmind_tax_authority */     CAST(NULL AS varchar(3))                            AS country_code,          /* ⚠ TODO no source column */     CASE WHEN LEFT(LTRIM(RTRIM(tj.geo_code)), 1) = '*' THEN 1 ELSE 0 END AS has_asterisk_prefix,     ta.auth_type_name                                   AS rule_name,     /* Tax type detection per build prompt §3.8 — pivots on auth_type_name        since the real source has no rule_name column. */     CASE         WHEN ta.auth_type_name LIKE '%GST%'           OR ta.auth_type_name LIKE '%HST%'           OR ta.auth_type_name LIKE '%VAT%'                                    THEN '2'         ELSE '1'     END                                                 AS tax_type,     /* Descriptive relabel */     CASE         WHEN ta.auth_type_name LIKE '%GST%' THEN 'GST Tax'         WHEN ta.auth_type_name LIKE '%HST%' THEN 'HST Tax'         WHEN ta.auth_type_name LIKE '%PST%' THEN 'PST Tax'         WHEN ta.auth_type_name LIKE '%VAT%' THEN 'VAT Tax'         ELSE 'Sales Tax'     END                                                 AS tax_type_original,     tj.authority_id                                     AS authority_id,     tj.category                                         AS category   FROM LH_Source.dbo.jumpmind_tax_jurisdiction AS tj   LEFT JOIN LH_Source.dbo.jumpmind_tax_authority AS ta     ON ta.id = tj.authority_id;
```

