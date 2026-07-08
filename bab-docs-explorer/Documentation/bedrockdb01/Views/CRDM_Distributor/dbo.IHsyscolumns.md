# dbo.IHsyscolumns

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.IHsyscolumns"]
    IHcolumns(["IHcolumns"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| IHcolumns |

## View Code

```sql
create view IHsyscolumns (name, id, xtype, typestat, xusertype, length,  xprec, xscale, colid, xoffset, bitpos, reserved, colstat, cdefault, domain, number, colorder, autoval,  offset, collationid, language, status, type, usertype, printfmt, prec, scale, iscomputed, isoutparam, isnullable,  collation, tdscollation ) AS  SELECT ihcol.name,      ihcol.article_id,      ihcol.mapped_type,      NULL,      ihcol.mapped_type,      ihcol.mapped_length,      ihcol.mapped_prec,      ihcol.mapped_scale,      ihcol.column_id,      NULL,      NULL,      NULL,      NULL,      NULL,      NULL,      NULL,      ihcol.column_ordinal,      NULL,      NULL,      NULL,      NULL,      NULL,      0,      ihcol.mapped_type,      NULL,      ihcol.mapped_prec,      ihcol.mapped_scale,      0,      0,      0,      NULL,      NULL  FROM   IHcolumns ihcol
```

