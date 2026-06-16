# internal.environment_permissions

**Database:** SSISDB  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | bigint | 8 | 0 | YES |  |  |
| sid | adt_sid | 85 | 0 |  |  |  |
| object_id | bigint | 8 | 0 |  | YES |  |
| permission_type | smallint | 2 | 0 |  |  |  |
| is_role | bit | 1 | 0 |  |  |  |
| is_deny | bit | 1 | 0 |  |  |  |
| grantor_sid | adt_sid | 85 | 0 |  |  |  |

## Referenced By Stored Procedures

- [SSISDB: catalog.revoke_permission](../../StoredProcedures/SSISDB/catalog.revoke_permission.md)
- [SSISDB: internal.init_object_permissions](../../StoredProcedures/SSISDB/internal.init_object_permissions.md)
- [SSISDB: internal.update_permission](../../StoredProcedures/SSISDB/internal.update_permission.md)

