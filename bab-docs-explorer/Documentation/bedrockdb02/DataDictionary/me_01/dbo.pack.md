# dbo.pack

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| pack_id | decimal | 9 | 0 | YES |  |  |
| pack_code | nvarchar | 40 | 0 |  |  |  |
| pack_description | nvarchar | 100 | 0 |  |  |  |
| pack_short_description | nvarchar | 40 | 0 |  |  |  |
| pack_status | smallint | 2 | 0 |  |  |  |
| pack_type | tinyint | 1 | 0 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| vendor_id | decimal | 9 | 0 |  |  |  |
| vendor_pack_code | nvarchar | 40 | 1 |  |  |  |
| vendor_upc_flag | bit | 1 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| multi_color_flag | bit | 1 | 0 |  |  |  |
| bin_location | nvarchar | 20 | 1 |  |  |  |
| document_source | tinyint | 1 | 0 |  |  |  |
| export_status | tinyint | 1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.dl_validate_import_upc_$sp](../../StoredProcedures/me_01/dbo.dl_validate_import_upc_$sp.md)
- [me_01: dbo.get_po_detail_retail_rep_$sp](../../StoredProcedures/me_01/dbo.get_po_detail_retail_rep_$sp.md)
- [me_01: dbo.imw_asn_$sp](../../StoredProcedures/me_01/dbo.imw_asn_$sp.md)
- [me_01: dbo.imw_asncomplete_$sp](../../StoredProcedures/me_01/dbo.imw_asncomplete_$sp.md)
- [me_01: dbo.insert_packs_$sp](../../StoredProcedures/me_01/dbo.insert_packs_$sp.md)
- [me_01: dbo.insert_packs_bi_$sp](../../StoredProcedures/me_01/dbo.insert_packs_bi_$sp.md)
- [me_01: dbo.no_wms_create_ss_$sp](../../StoredProcedures/me_01/dbo.no_wms_create_ss_$sp.md)
- [me_01: dbo.pi_load_retail_data_loc_$sp](../../StoredProcedures/me_01/dbo.pi_load_retail_data_loc_$sp.md)
- [me_01: dbo.pi_update_inventory_tables_$sp](../../StoredProcedures/me_01/dbo.pi_update_inventory_tables_$sp.md)
- [me_01: dbo.pocost_get_po_lines_$sp](../../StoredProcedures/me_01/dbo.pocost_get_po_lines_$sp.md)
- [me_01: dbo.populate_temp_asn_$sp](../../StoredProcedures/me_01/dbo.populate_temp_asn_$sp.md)
- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)
- [me_01: dbo.rpt_get_po_receipt_$sp](../../StoredProcedures/me_01/dbo.rpt_get_po_receipt_$sp.md)
- [me_01: dbo.rpt_get_pos_$sp](../../StoredProcedures/me_01/dbo.rpt_get_pos_$sp.md)
- [me_01: dbo.validate_import_asn_tables_$sp](../../StoredProcedures/me_01/dbo.validate_import_asn_tables_$sp.md)

