# dbo.backupset

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| backup_set_id | int | 4 | 0 | YES |  |  |
| backup_set_uuid | uniqueidentifier | 16 | 0 |  |  |  |
| media_set_id | int | 4 | 0 |  | YES |  |
| first_family_number | tinyint | 1 | 1 |  |  |  |
| first_media_number | smallint | 2 | 1 |  |  |  |
| last_family_number | tinyint | 1 | 1 |  |  |  |
| last_media_number | smallint | 2 | 1 |  |  |  |
| catalog_family_number | tinyint | 1 | 1 |  |  |  |
| catalog_media_number | smallint | 2 | 1 |  |  |  |
| position | int | 4 | 1 |  |  |  |
| expiration_date | datetime | 8 | 1 |  |  |  |
| software_vendor_id | int | 4 | 1 |  |  |  |
| name | nvarchar | 256 | 1 |  |  |  |
| description | nvarchar | 510 | 1 |  |  |  |
| user_name | nvarchar | 256 | 1 |  |  |  |
| software_major_version | tinyint | 1 | 1 |  |  |  |
| software_minor_version | tinyint | 1 | 1 |  |  |  |
| software_build_version | smallint | 2 | 1 |  |  |  |
| time_zone | smallint | 2 | 1 |  |  |  |
| mtf_minor_version | tinyint | 1 | 1 |  |  |  |
| first_lsn | numeric | 13 | 1 |  |  |  |
| last_lsn | numeric | 13 | 1 |  |  |  |
| checkpoint_lsn | numeric | 13 | 1 |  |  |  |
| database_backup_lsn | numeric | 13 | 1 |  |  |  |
| database_creation_date | datetime | 8 | 1 |  |  |  |
| backup_start_date | datetime | 8 | 1 |  |  |  |
| backup_finish_date | datetime | 8 | 1 |  |  |  |
| type | char | 1 | 1 |  |  |  |
| sort_order | smallint | 2 | 1 |  |  |  |
| code_page | smallint | 2 | 1 |  |  |  |
| compatibility_level | tinyint | 1 | 1 |  |  |  |
| database_version | int | 4 | 1 |  |  |  |
| backup_size | numeric | 13 | 1 |  |  |  |
| database_name | nvarchar | 256 | 1 |  |  |  |
| server_name | nvarchar | 256 | 1 |  |  |  |
| machine_name | nvarchar | 256 | 1 |  |  |  |
| flags | int | 4 | 1 |  |  |  |
| unicode_locale | int | 4 | 1 |  |  |  |
| unicode_compare_style | int | 4 | 1 |  |  |  |
| collation_name | nvarchar | 256 | 1 |  |  |  |
| is_password_protected | bit | 1 | 1 |  |  |  |
| recovery_model | nvarchar | 120 | 1 |  |  |  |
| has_bulk_logged_data | bit | 1 | 1 |  |  |  |
| is_snapshot | bit | 1 | 1 |  |  |  |
| is_readonly | bit | 1 | 1 |  |  |  |
| is_single_user | bit | 1 | 1 |  |  |  |
| has_backup_checksums | bit | 1 | 1 |  |  |  |
| is_damaged | bit | 1 | 1 |  |  |  |
| begins_log_chain | bit | 1 | 1 |  |  |  |
| has_incomplete_metadata | bit | 1 | 1 |  |  |  |
| is_force_offline | bit | 1 | 1 |  |  |  |
| is_copy_only | bit | 1 | 1 |  |  |  |
| first_recovery_fork_guid | uniqueidentifier | 16 | 1 |  |  |  |
| last_recovery_fork_guid | uniqueidentifier | 16 | 1 |  |  |  |
| fork_point_lsn | numeric | 13 | 1 |  |  |  |
| database_guid | uniqueidentifier | 16 | 1 |  |  |  |
| family_guid | uniqueidentifier | 16 | 1 |  |  |  |
| differential_base_lsn | numeric | 13 | 1 |  |  |  |
| differential_base_guid | uniqueidentifier | 16 | 1 |  |  |  |
| compressed_backup_size | numeric | 13 | 1 |  |  |  |
| key_algorithm | nvarchar | 64 | 1 |  |  |  |
| encryptor_thumbprint | varbinary | 20 | 1 |  |  |  |
| encryptor_type | nvarchar | 64 | 1 |  |  |  |

