# dbo.sysarticles

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sysarticles"]
    IHarticles(["IHarticles"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| IHarticles |

## View Code

```sql
create view sysarticles (artid, creation_script, del_cmd, description, dest_table, filter, filter_clause, ins_cmd, name, objid, pubid, pre_creation_cmd, status, sync_objid, type, upd_cmd, schema_option, dest_owner, ins_scripting_proc, del_scripting_proc, upd_scripting_proc, custom_script, fire_triggers_on_snapshot) AS  SELECT ihart.article_id, ihart.creation_script, ihart.del_cmd, ihart.description, ihart.dest_table, ihart.filter, ihart.filter_clause, ihart.ins_cmd, ihart.name, ihart.objid, ihart.publication_id, ihart.pre_creation_cmd, ihart.status, ihart.sync_objid, ihart.type, ihart.upd_cmd, ihart.schema_option, ihart.dest_owner, ihart.ins_scripting_proc, ihart.del_scripting_proc, ihart.upd_scripting_proc, ihart.custom_script, ihart.fire_triggers_on_snapshot FROM IHarticles ihart
```

