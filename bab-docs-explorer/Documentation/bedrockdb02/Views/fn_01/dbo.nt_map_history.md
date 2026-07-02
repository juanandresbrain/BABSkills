# dbo.nt_map_history

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.nt_map_history"]
    dbo_FNDTN_SCRTY_NT_MAP_HSTRY(["dbo.FNDTN_SCRTY_NT_MAP_HSTRY"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FNDTN_SCRTY_NT_MAP_HSTRY |

## View Code

```sql
CREATE VIEW dbo.nt_map_history (user_id,computer_name,instance,app_id,comp_id,ackey,nt_map_data,time_stamp)
AS SELECT USER_ID,CMPTR_NAME,INSTNC,APP_ID,CMPNY_ID,ACS_KEY,NT_MAP_DATA,TIME_STMP
FROM dbo.FNDTN_SCRTY_NT_MAP_HSTRY

dbo,Sl_Lg_Identification,create view [dbo].[Sl_Lg_Identification] (
	language_id,
	english_desc,
	display_desc,
	active_flag,
	column_position)
AS SELECT language_id,
	english_desc,
	display_desc,
	active_flag,
	column_position
FROM fn_01.dbo.Lg_Identification
```

