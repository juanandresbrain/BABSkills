# dbo.sysextendedarticlesview

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sysextendedarticlesview"]
    sysarticles(["sysarticles"]) --> VIEW
    sysschemaarticles(["sysschemaarticles"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| sysarticles |
| sysschemaarticles |

## View Code

```sql
create view dbo.sysextendedarticlesview
                   as
                    select artid, creation_script, del_cmd, description,
                                dest_table, filter, filter_clause, ins_cmd, name, objid, pubid,
                                pre_creation_cmd, status, sync_objid, type, upd_cmd,
                                schema_option, dest_owner, ins_scripting_proc, del_scripting_proc,
                                upd_scripting_proc, custom_script, fire_triggers_on_snapshot 
                            from sysarticles

                    union all

                    select artid, creation_script, NULL, description,
                            dest_object, NULL, NULL, NULL, name, objid, pubid, 
                            pre_creation_cmd, status, NULL, type, NULL, 
                            schema_option, dest_owner, NULL, NULL, NULL, NULL, 0
                        from sysschemaarticles
```

