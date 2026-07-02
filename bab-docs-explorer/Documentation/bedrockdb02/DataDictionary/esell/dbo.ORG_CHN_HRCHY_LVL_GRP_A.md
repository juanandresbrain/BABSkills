# dbo.ORG_CHN_HRCHY_LVL_GRP_A

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| HRCHY_LVL_GRP_ID | T_ID | 16 | 0 | YES |  |  |
| ORG_CHN_NUM | T_LONG_INTEGER | 4 | 0 | YES |  |  |
| HRCHY_LVL_ID | T_ID | 16 | 0 |  |  |  |
| HRCHY_ID | T_ID | 16 | 0 |  |  |  |
| VRTL | T_BOOLEAN | 5 | 0 |  |  |  |
| FDN_CSTMZTN_DATA | nvarchar | 4000 | 1 |  |  |  |

## Referenced By Stored Procedures

- [esell: esell.GETFULFILLMENTRATES](../../StoredProcedures/esell/esell.GETFULFILLMENTRATES.md)
- [esell: esell.GETNOSTOCKREPORT](../../StoredProcedures/esell/esell.GETNOSTOCKREPORT.md)
- [esell: esell.GETNOSTOCKREPORTLOCATION](../../StoredProcedures/esell/esell.GETNOSTOCKREPORTLOCATION.md)
- [esell: esell.GETORDERSTATUSREPORT](../../StoredProcedures/esell/esell.GETORDERSTATUSREPORT.md)
- [esell: esell.GETORDERSTATUSREPORTLOCATION](../../StoredProcedures/esell/esell.GETORDERSTATUSREPORTLOCATION.md)
- [esell: esell.GETORDERSUMMARY](../../StoredProcedures/esell/esell.GETORDERSUMMARY.md)
- [esell: esell.GETSKUDEMANDREPORT](../../StoredProcedures/esell/esell.GETSKUDEMANDREPORT.md)
- [esell: esell.GETSKUDEMANDREPORTLOCATION](../../StoredProcedures/esell/esell.GETSKUDEMANDREPORTLOCATION.md)

