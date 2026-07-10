# dbo.spRPT_SecurityReport_DBRoleMembers

**Database:** DBAUtilityMaster  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spRPT_SecurityReport_DBRoleMembers"]
    dbo_tblDBA_SecurityReport_DBRoleMembers(["dbo.tblDBA_SecurityReport_DBRoleMembers"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tblDBA_SecurityReport_DBRoleMembers |

## Stored Procedure Code

```sql
CREATE PROC [dbo].[spRPT_SecurityReport_DBRoleMembers]
AS
SELECT DISTINCT [InstanceName]
      ,[DatabaseName]
      ,[DBRoleName]
      ,[MemberName]
  FROM [DBAUtilityMaster].[dbo].[tblDBA_SecurityReport_DBRoleMembers]
  WHERE DBRoleName NOT IN ('db_datareader','db_datawriter',
  'aspnet_Membership_BasicAccess','aspnet_Profile_BasicAccess',
  'aspnet_Membership_ReportingAccess', 'aspnet_Roles_ReportingAccess', 
  'aspnet_Personalization_ReportingAccess', 'aspnet_Roles_BasicAccess',
  'aspnet_Personalization_BasicAccess','aspnet_Profile_ReportingAccess',
  'SQLAgentReaderRole', 'SQLAgentUserRole','spexec','DatabaseMailUserRole',
  'BAM_CONFIG_READER', 'BAM_EVENT_WRITER', 'BI_BearDen', 'BI_DiscountDen', 'BI_HoneyPot', 
  'BI_JackFact', 'BI_KeyMetrics', 'BI_Scorecard', 'BI_StoredProcs', 'BI_TopDen', 'BI_ValueLink',  
  'db_denydatareader', 'aspnet_Membership_FullAccess', 'aspnet_Personalization_FullAccess', 
  'aspnet_Profile_FullAccess', 'aspnet_Roles_FullAccess', 'aspnet_WebEvent_FullAccess')
  AND MemberName NOT IN ('dbo',  '##MS_PolicyEventProcessingLogin##', 'ServerGroupAdministratorRole', 
  '##MS_PolicyTsqlExecutionLogin##','PolicyAdministratorRole','MS_DataCollectorInternalUser','dc_admin',
  'dc_operator', 'dc_proxy', 'RSExecRole', 
  --'BI_BearDen', 'BI_DiscountDen', 'BI_HoneyPot', 'BI_JackFact', 'BI_KeyMetrics', 'BI_Scorecard', 'BI_TopDen', 
  'BAM_EVENT_WRITER', 'BAM_EVENT_WRITER', 'BTS_B2B_OPERATORS','BTS_HOST_USERS','BTS_ADMIN_USERS', 'BTS_BizTalkServerApplication_USERS', 
  'BTS_BTSSQLHost_USERS', 'BTS_ClubBABW_USERS', 'BTS_ClubBABWIsolated_USERS', 'BTS_eCommerceWebFeed_USERS', 'BTS_ADMIN_USERS', 
  'BTS_GoogleLocalShopping_USERS', 'BTS_BizTalkServerIsolatedHost_USERS', 'RE_ADMIN_USERS', 'BTS_OPERATORS','ServerGroupAdministratorRole')
  AND InstanceName NOT IN ('DWDEV01','WBNSCOREDEV01','WMPMDBTEST','REDPANDA')
  --AND MemberName NOT LIKE 'BAB\%'
  order by 3--j, 1, 2, 3
```

