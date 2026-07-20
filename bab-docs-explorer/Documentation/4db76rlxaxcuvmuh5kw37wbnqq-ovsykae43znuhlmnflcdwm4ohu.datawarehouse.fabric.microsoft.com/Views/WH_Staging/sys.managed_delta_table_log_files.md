# sys.managed_delta_table_log_files

**Database:** WH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["sys.managed_delta_table_log_files"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE   VIEW sys.managed_delta_table_log_files AS SELECT lf.commit_sequence_id, lf.file_guid, lf.xdes_ts, lf.append_only, lf.rows_inserted, lf.commit_time, lf.source_table_guid, p.source_database_guid,p.manifest_file_name, p.manifest_root, t.table_guid  FROM sys.manageddeltatablelogfiles lf  JOIN sys.manageddeltatables t  ON lf.table_id = t.table_id and t.drop_commit_time <= '1900-01-01T00:00:00' OUTER APPLY OpenRowSet(TABLE DW_PHYSICAL_METADATA_MANIFEST_FILES, t.sql_object_id, lf.commit_sequence_id, lf.source_table_guid, lf.source_database_guid) p
```

