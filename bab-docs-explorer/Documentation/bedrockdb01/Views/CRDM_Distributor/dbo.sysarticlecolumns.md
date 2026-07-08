# dbo.sysarticlecolumns

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sysarticlecolumns"]
    IHcolumns(["IHcolumns"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| IHcolumns |

## View Code

```sql
create view sysarticlecolumns (artid, colid, is_udt, is_xml, is_max ) AS SELECT article_id, publishercolumn_id, 0, 0, 0 FROM IHcolumns
```

