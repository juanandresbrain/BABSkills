# dbo.ORG_CHN_HRCHY_LVL

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| HRCHY_LVL_ID | T_ID | 16 | 0 | YES |  |  |
| HRCHY_LVL_DESC | nvarchar | 510 | 0 |  |  |  |
| SEQ_NUM | T_SEQUENCE_NUMBER | 9 | 0 |  |  |  |
| AFLTN_PRMTD | T_BOOLEAN | 5 | 0 |  |  |  |
| HRCHY_ID | T_ID | 16 | 0 |  |  |  |
| PRNT_HRCHY_LVL_ID | T_ID | 16 | 1 |  | YES |  |
| ACTV | T_BOOLEAN | 5 | 0 |  |  |  |

## Referenced By Stored Procedures

- [esell: dbo.SCRTY_GET_GRPS_IN_SET_$SP](../../StoredProcedures/esell/dbo.SCRTY_GET_GRPS_IN_SET_$SP.md)
- [esell: esell.GETFULFILLMENTRATES](../../StoredProcedures/esell/esell.GETFULFILLMENTRATES.md)
- [esell: esell.GETNOSTOCKREPORT](../../StoredProcedures/esell/esell.GETNOSTOCKREPORT.md)
- [esell: esell.GETNOSTOCKREPORTLOCATION](../../StoredProcedures/esell/esell.GETNOSTOCKREPORTLOCATION.md)
- [esell: esell.GETORDERSTATUSREPORT](../../StoredProcedures/esell/esell.GETORDERSTATUSREPORT.md)
- [esell: esell.GETORDERSTATUSREPORTLOCATION](../../StoredProcedures/esell/esell.GETORDERSTATUSREPORTLOCATION.md)
- [esell: esell.GETORDERSUMMARY](../../StoredProcedures/esell/esell.GETORDERSUMMARY.md)
- [esell: esell.GETSKUDEMANDREPORT](../../StoredProcedures/esell/esell.GETSKUDEMANDREPORT.md)
- [esell: esell.GETSKUDEMANDREPORTLOCATION](../../StoredProcedures/esell/esell.GETSKUDEMANDREPORTLOCATION.md)

