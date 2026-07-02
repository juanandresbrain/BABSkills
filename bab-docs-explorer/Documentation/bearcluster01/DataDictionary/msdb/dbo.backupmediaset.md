# dbo.backupmediaset

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| media_set_id | int | 4 | 0 | YES |  |  |
| media_uuid | uniqueidentifier | 16 | 1 |  |  |  |
| media_family_count | tinyint | 1 | 1 |  |  |  |
| name | nvarchar | 256 | 1 |  |  |  |
| description | nvarchar | 510 | 1 |  |  |  |
| software_name | nvarchar | 256 | 1 |  |  |  |
| software_vendor_id | int | 4 | 1 |  |  |  |
| MTF_major_version | tinyint | 1 | 1 |  |  |  |
| mirror_count | tinyint | 1 | 1 |  |  |  |
| is_password_protected | bit | 1 | 1 |  |  |  |
| is_compressed | bit | 1 | 1 |  |  |  |
| is_encrypted | bit | 1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [DBAUtility: dbo.kk_SP_DeleteBackupHistory](../../StoredProcedures/DBAUtility/dbo.kk_SP_DeleteBackupHistory.md)

