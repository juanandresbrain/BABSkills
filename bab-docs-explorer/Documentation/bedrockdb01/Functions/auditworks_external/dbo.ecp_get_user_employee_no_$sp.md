# dbo.ecp_get_user_employee_no_$sp

**Database:** auditworks_external  
**Server:** bedrockdb01  
**Function Type:** Scalar Function  
**Returns:** int(4)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.ecp_get_user_employee_no_$sp"]
    EMPLY(["EMPLY"]) --> FUNC
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @user_full_name | varchar | 255 | NO |

## Table Dependencies

| Referenced Table |
|---|
| EMPLY |

## Function Code

```sql
CREATE FUNCTION [dbo].[ecp_get_user_employee_no_$sp] (@user_full_name varchar(255))
RETURNS int
AS
/* 
Function Name: ecp_get_user_employee_no_$sp 

Desc:   Retrieves employee number corresponding to user name passed in.

HISTORY:  
Date     Name           Def#    Desc
Oct30,08 Vicci         105986   Author
*/
BEGIN
  DECLARE @employee_no int,
          @employee_found tinyint

  SELECT @employee_found = 0,
         @user_full_name = COALESCE(UPPER(LTRIM(RTRIM(@user_full_name))), '')
  
  IF @user_full_name = ''
    RETURN @employee_no

  SELECT @employee_no = EMPLY_NUM
    FROM EMPLY
   WHERE @user_full_name = UPPER(COALESCE(LTRIM(RTRIM(FRST_NAME)), '') + CASE WHEN COALESCE(LTRIM(RTRIM(MDL_NAME)), '') = '' THEN '' ELSE CASE WHEN COALESCE(FRST_NAME, '') <> '' THEN ' ' ELSE '' END + LTRIM(RTRIM(MDL_NAME)) END + CASE WHEN COALESCE(LTRIM(RTRIM(LAST_NAME)), '') = '' THEN '' ELSE ' ' + LTRIM(RTRIM(LAST_NAME)) END)
  SELECT @employee_found = @@rowcount

  IF @employee_found <> 1
  BEGIN
    SELECT @employee_no = EMPLY_NUM
      FROM EMPLY
     WHERE @user_full_name = UPPER(COALESCE(LTRIM(RTRIM(LAST_NAME)), '') + CASE WHEN COALESCE(LTRIM(RTRIM(FRST_NAME)), '') = '' THEN '' ELSE CASE WHEN COALESCE(LAST_NAME, '') <> '' THEN ', ' ELSE '' END + LTRIM(RTRIM(FRST_NAME)) END + CASE WHEN COALESCE(LTRIM(RTRIM(MDL_NAME)), '') = '' THEN '' ELSE ' ' + LTRIM(RTRIM(MDL_NAME)) END)
    SELECT @employee_found = @@rowcount
  END

  IF @employee_found <> 1
  BEGIN
    SELECT @employee_no = EMPLY_NUM
      FROM EMPLY
     WHERE @user_full_name = UPPER(COALESCE(LTRIM(RTRIM(FRST_NAME)), '') + CASE WHEN COALESCE(LTRIM(RTRIM(LAST_NAME)), '') = '' THEN '' ELSE ' ' + LTRIM(RTRIM(LAST_NAME)) END)
    SELECT @employee_found = @@rowcount
  END

  IF @employee_found <> 1
  BEGIN
    SELECT @employee_no = EMPLY_NUM
      FROM EMPLY
     WHERE @user_full_name = UPPER(COALESCE(LTRIM(RTRIM(LAST_NAME)), '') + CASE WHEN COALESCE(LTRIM(RTRIM(FRST_NAME)), '') = '' THEN '' ELSE CASE WHEN COALESCE(LAST_NAME, '') <> '' THEN ', ' ELSE '' END + LTRIM(RTRIM(FRST_NAME)) END)
    SELECT @employee_found = @@rowcount
  END

  IF @employee_found <> 1
  BEGIN
    SELECT @employee_no = EMPLY_NUM
      FROM EMPLY
     WHERE @user_full_name = UPPER(LTRIM(RTRIM(LAST_NAME)))
    SELECT @employee_found = @@rowcount
  END

  IF @employee_found <> 1
  BEGIN
    SELECT @employee_no = EMPLY_NUM
      FROM EMPLY
     WHERE @user_full_name = UPPER(LTRIM(RTRIM(SHRT_NAME)))
    SELECT @employee_found = @@rowcount
  END

  IF @employee_found <> 1
  BEGIN
    SELECT @employee_no = EMPLY_NUM
      FROM EMPLY
     WHERE @user_full_name = UPPER(LTRIM(RTRIM(FRST_NAME)))
    SELECT @employee_found = @@rowcount
  END

  IF @employee_found <> 1
    SELECT @employee_no = null

/*
select UPPER(COALESCE(LTRIM(RTRIM(FRST_NAME)), '') + CASE WHEN COALESCE(LTRIM(RTRIM(MDL_NAME)), '') = '' THEN '' ELSE CASE WHEN COALESCE(FRST_NAME, '') <> '' THEN ' ' ELSE '' END + LTRIM(RTRIM(MDL_NAME)) END + CASE WHEN COALESCE(LTRIM(RTRIM(LAST_NAME)), '') = '' THEN '' ELSE ' ' + LTRIM(RTRIM(LAST_NAME)) END),
       UPPER(COALESCE(LTRIM(RTRIM(LAST_NAME)), '') + CASE WHEN COALESCE(LTRIM(RTRIM(FRST_NAME)), '') = '' THEN '' ELSE CASE WHEN COALESCE(LAST_NAME, '') <> '' THEN ', ' ELSE '' END + LTRIM(RTRIM(FRST_NAME)) END + CASE WHEN COALESCE(LTRIM(RTRIM(MDL_NAME)), '') = '' THEN '' ELSE ' ' + LTRIM(RTRIM(MDL_NAME)) END),
       UPPER(COALESCE(LTRIM(RTRIM(FRST_NAME)), '') + CASE WHEN COALESCE(LTRIM(RTRIM(LAST_NAME)), '') = '' THEN '' ELSE ' ' + LTRIM(RTRIM(LAST_NAME)) END),
       UPPER(COALESCE(LTRIM(RTRIM(LAST_NAME)), '') + CASE WHEN COALESCE(LTRIM(RTRIM(FRST_NAME)), '') = '' THEN '' ELSE CASE WHEN COALESCE(LAST_NAME, '') <> '' THEN ', ' ELSE '' END + LTRIM(RTRIM(FRST_NAME)) END),
       UPPER(LTRIM(RTRIM(LAST_NAME))),
       UPPER(LTRIM(RTRIM(FRST_NAME))),
       UPPER(LTRIM(RTRIM(SHRT_NAME)))
from EMPLY e
*/

RETURN @employee_no

END
```

