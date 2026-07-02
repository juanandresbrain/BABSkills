# dbo.ORG_CHN_HRCHY_LVL_GRP

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| HRCHY_LVL_GRP_ID | T_ID | 16 | 0 | YES |  |  |
| HRCHY_LVL_GRP_IDNTY | T_INTEGER | 2 | 0 |  |  |  |
| HRCHY_LVL_GRP_DESC | nvarchar | 510 | 0 |  |  |  |
| HRCHY_LVL_GRP_CODE | nvarchar | 40 | 1 |  |  |  |
| GRP_MBR_CHNG | T_DATE | 8 | 1 |  |  |  |
| HRCHY_LVL_ID | T_ID | 16 | 0 |  |  |  |
| HRCHY_ID | T_ID | 16 | 0 |  |  |  |
| PRNT_HRCHY_LVL_GRP_ID | T_ID | 16 | 1 |  | YES |  |
| ACTV | T_BOOLEAN | 5 | 0 |  |  |  |

## Referenced By Stored Procedures

- [esell: dbo.SCRTY_GET_GRPS_IN_SET_$SP](../../StoredProcedures/esell/dbo.SCRTY_GET_GRPS_IN_SET_$SP.md)
- [esell: dbo.SCRTY_GET_SET_ID_$SP](../../StoredProcedures/esell/dbo.SCRTY_GET_SET_ID_$SP.md)
- [esell: esell.GETFULFILLMENTRATES](../../StoredProcedures/esell/esell.GETFULFILLMENTRATES.md)
- [esell: esell.GETNOSTOCKREPORT](../../StoredProcedures/esell/esell.GETNOSTOCKREPORT.md)
- [esell: esell.GETNOSTOCKREPORTLOCATION](../../StoredProcedures/esell/esell.GETNOSTOCKREPORTLOCATION.md)
- [esell: esell.GETORDERSTATUSREPORT](../../StoredProcedures/esell/esell.GETORDERSTATUSREPORT.md)
- [esell: esell.GETORDERSTATUSREPORTLOCATION](../../StoredProcedures/esell/esell.GETORDERSTATUSREPORTLOCATION.md)
- [esell: esell.GETORDERSUMMARY](../../StoredProcedures/esell/esell.GETORDERSUMMARY.md)
- [esell: esell.GETSKUDEMANDREPORT](../../StoredProcedures/esell/esell.GETSKUDEMANDREPORT.md)
- [esell: esell.GETSKUDEMANDREPORTLOCATION](../../StoredProcedures/esell/esell.GETSKUDEMANDREPORTLOCATION.md)

