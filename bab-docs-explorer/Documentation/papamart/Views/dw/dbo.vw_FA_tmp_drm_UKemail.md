# dbo.vw_FA_tmp_drm_UKemail

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vw_FA_tmp_drm_UKemail"]
    prefctr_email_in(["prefctr_email_in"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| prefctr_email_in |

## View Code

```sql
create view dbo.vw_FA_tmp_drm_UKemail
as
select distinct EMAIL_ADDR,EMAIL_ADDR_LC,SYS_KEY_VALUE,DATE_OPTIN, year(DATE_OPTIN) OptInYear , BRAND,COUNTRY,PURCHASE_STOREID,SYS_KEY,CUSTOMER_NUM,ATTRIBUTE_GROUPING_CODE,ATTRIBUTE_CODE,DATE_OPTOUT
--into #tmp_drm_UKemail 
from prefctr_email_in 
where purchase_storeid >=2000
and sys_key = 1 --kiosk
and date_optout is null
```

