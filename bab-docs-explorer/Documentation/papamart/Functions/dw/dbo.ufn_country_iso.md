# dbo.ufn_country_iso

**Database:** dw  
**Server:** papamart  
**Function Type:** Scalar Function  
**Returns:** char(100)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.ufn_country_iso"]
    tblKioskCountryMapping(["tblKioskCountryMapping"]) --> FUNC
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @country | varchar | 100 | NO |

## Table Dependencies

| Referenced Table |
|---|
| tblKioskCountryMapping |

## Function Code

```sql
CREATE function [dbo].[ufn_country_iso] (@country varchar(100))
returns char(100)
as
begin
	declare @country_iso char(100)
		if @country in (select sKioskCountry from tblKioskCountryMapping)
			select @country_iso = (select distinct sCountry from tblKioskCountryMapping where sKioskCountry = @country)
		else
			select @country_iso = @country
	return(@country_iso)
end

/*

select * from tblKioskCountryMapping
where sKioskCountry like 'ERIE%'


insert into tblKioskCountryMapping (sKioskCountry,sCountry)
	select 'ERIE','US'


select dbo.ufn_country_iso(country) as country, sum(cnt) as record_count, count(*) as country_permutation_count from tmp_edin_countries_in_prefc_email_in
group by dbo.ufn_country_iso(country)
--having sum(cnt) > 100
order by 2 desc

select top 1000 dbo.ufn_country_iso_edin(country) as country from PREFCTR_EMAIL_IN
group by dbo.ufn_country_iso_edin(country)
--having sum(cnt) > 100
order by 2 desc


select * from tmp_edin_countries_in_prefc_email_in


select * from tmp_edin_countries_in_prefc_email_in
order by 2 desc


select 'else if @country = ''' + [Column 0] + ''' set @country_iso = ''' + [Column 1] + '''' from tmp_edin_country_iso_codes

*/
```

