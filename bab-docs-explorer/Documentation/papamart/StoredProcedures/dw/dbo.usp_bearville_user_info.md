# dbo.usp_bearville_user_info

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.usp_bearville_user_info"]
    dbo_usp_UserInfo(["dbo.usp_UserInfo"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.usp_UserInfo |

## Stored Procedure Code

```sql
CREATE proc [dbo].[usp_bearville_user_info]
		@begin_date	datetime,
		@end_date	datetime
as
exec BABWVILLEDB01.bearville.dbo.usp_UserInfo @begin_date, @end_date
```

