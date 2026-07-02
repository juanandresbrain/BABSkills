# dbo.employee

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| employee_id | decimal | 9 | 0 |  |  |  |
| employee_code | nvarchar | 40 | 0 |  |  |  |
| employee_home_location | decimal | 9 | 1 |  |  |  |
| employee_lastname | nvarchar | 60 | 0 |  |  |  |
| employee_firstname | nvarchar | 60 | 0 |  |  |  |
| employee_fullpart_flag | bit | 1 | 0 |  |  |  |
| employee_permtemp_flag | bit | 1 | 0 |  |  |  |
| employee_alternate_no | int | 4 | 1 |  |  |  |
| employee_house_account_no | decimal | 9 | 1 |  |  |  |
| employee_hired_date | smalldatetime | 4 | 0 |  |  |  |
| employee_discount | decimal | 5 | 1 |  |  |  |
| employee_max_discount | decimal | 5 | 1 |  |  |  |
| security_user_id | int | 4 | 1 |  |  |  |
| nt_user_name | nvarchar | 60 | 1 |  |  |  |
| domain_name | nvarchar | 60 | 1 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| employee_sin | nvarchar | 18 | 1 |  |  |  |
| last_modified_date | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingEmployeeDeactivateActivate](../../StoredProcedures/me_01/dbo.spMerchandisingEmployeeDeactivateActivate.md)
- [USICOAL: dbo.NOR_SEL_EMPLOYEES](../../StoredProcedures/USICOAL/dbo.NOR_SEL_EMPLOYEES.md)
- [USICOAL: dbo.NSB_SP_EMPL_FILE](../../StoredProcedures/USICOAL/dbo.NSB_SP_EMPL_FILE.md)
- [USICOAL: dbo.NSB_SP_EMPL_PROD1](../../StoredProcedures/USICOAL/dbo.NSB_SP_EMPL_PROD1.md)
- [USICOAL: dbo.NSB_SP_EMPL_PROD2](../../StoredProcedures/USICOAL/dbo.NSB_SP_EMPL_PROD2.md)
- [USICOAL: dbo.NSB_SP_EMPL_PROD3](../../StoredProcedures/USICOAL/dbo.NSB_SP_EMPL_PROD3.md)
- [USICOAL: dbo.NSB_SP_LP_MAN_KEY_CARD1](../../StoredProcedures/USICOAL/dbo.NSB_SP_LP_MAN_KEY_CARD1.md)
- [USICOAL: dbo.NSB_SP_LP_NON_SALE1](../../StoredProcedures/USICOAL/dbo.NSB_SP_LP_NON_SALE1.md)
- [USICOAL: dbo.NSB_SP_LP_SUSP_TRN2](../../StoredProcedures/USICOAL/dbo.NSB_SP_LP_SUSP_TRN2.md)
- [USICOAL: dbo.NSB_SP_LP_VOID_ITEMS](../../StoredProcedures/USICOAL/dbo.NSB_SP_LP_VOID_ITEMS.md)
- [USICOAL: dbo.NSB_SP_LP_VOID_TENDER](../../StoredProcedures/USICOAL/dbo.NSB_SP_LP_VOID_TENDER.md)
- [USICOAL: dbo.NSB_SP_LP_VOID_TRN2](../../StoredProcedures/USICOAL/dbo.NSB_SP_LP_VOID_TRN2.md)
- [USICOAL: dbo.NSB_SP_MAN_KEY_CARD1](../../StoredProcedures/USICOAL/dbo.NSB_SP_MAN_KEY_CARD1.md)
- [USICOAL: dbo.NSB_SP_NON_MRCH2](../../StoredProcedures/USICOAL/dbo.NSB_SP_NON_MRCH2.md)
- [USICOAL: dbo.NSB_SP_NON_SALE1](../../StoredProcedures/USICOAL/dbo.NSB_SP_NON_SALE1.md)
- [USICOAL: dbo.NSB_SP_NOT_ON_FILE](../../StoredProcedures/USICOAL/dbo.NSB_SP_NOT_ON_FILE.md)
- [USICOAL: dbo.NSB_SP_PRICE_OVRD1](../../StoredProcedures/USICOAL/dbo.NSB_SP_PRICE_OVRD1.md)
- [USICOAL: dbo.NSB_SP_PRICE_OVRD2](../../StoredProcedures/USICOAL/dbo.NSB_SP_PRICE_OVRD2.md)
- [USICOAL: dbo.NSB_SP_PRICE_OVRD3](../../StoredProcedures/USICOAL/dbo.NSB_SP_PRICE_OVRD3.md)
- [USICOAL: dbo.NSB_SP_SUSP_TRN1](../../StoredProcedures/USICOAL/dbo.NSB_SP_SUSP_TRN1.md)
- [USICOAL: dbo.NSB_SP_SUSP_TRN2](../../StoredProcedures/USICOAL/dbo.NSB_SP_SUSP_TRN2.md)
- [USICOAL: dbo.NSB_SP_TRAN_DISC1](../../StoredProcedures/USICOAL/dbo.NSB_SP_TRAN_DISC1.md)
- [USICOAL: dbo.NSB_SP_TRAN_DISC2](../../StoredProcedures/USICOAL/dbo.NSB_SP_TRAN_DISC2.md)
- [USICOAL: dbo.NSB_SP_VOID_TRN1](../../StoredProcedures/USICOAL/dbo.NSB_SP_VOID_TRN1.md)
- [USICOAL: dbo.NSB_SP_VOID_TRN2](../../StoredProcedures/USICOAL/dbo.NSB_SP_VOID_TRN2.md)
- [USICOAL: dbo.RPT_EMPL_PROD_EXCL_TAX1](../../StoredProcedures/USICOAL/dbo.RPT_EMPL_PROD_EXCL_TAX1.md)
- [USICOAL: dbo.RPT_EMPL_PROD_EXCL_TAX2](../../StoredProcedures/USICOAL/dbo.RPT_EMPL_PROD_EXCL_TAX2.md)
- [USICOAL: dbo.RPT_EMPL_PROD_EXCL_TAX3](../../StoredProcedures/USICOAL/dbo.RPT_EMPL_PROD_EXCL_TAX3.md)
- [USICOAL: dbo.RPT_GET_EMPL](../../StoredProcedures/USICOAL/dbo.RPT_GET_EMPL.md)
- [USICOAL: dbo.RPT_SALESPERSON_PROD1](../../StoredProcedures/USICOAL/dbo.RPT_SALESPERSON_PROD1.md)
- [USICOAL: dbo.RPT_SALESPERSON_PROD2](../../StoredProcedures/USICOAL/dbo.RPT_SALESPERSON_PROD2.md)
- [USICOAL: dbo.RPT_SELECT_EMPL_FILL_ALL](../../StoredProcedures/USICOAL/dbo.RPT_SELECT_EMPL_FILL_ALL.md)

