# Stored Procedures: master

| Schema | Name | Table Dependencies |
|---|---|---|
| dbo | [c_stp_print_tickets_$sp](dbo.c_stp_print_tickets_$sp.md) | dbo.attribute, dbo.attribute_set, dbo.c_stp_detail, dbo.c_stp_header, dbo.c_stp_location, dbo.c_temp_ib_price, dbo.c_temp_tp_results, dbo.dist_detail, dbo.distribution, dbo.entity_attribute_set, dbo.ib_inventory, dbo.ib_inventory_total, dbo.ib_price, dbo.jurisdiction, dbo.location, dbo.price_change, dbo.price_change_style, dbo.sku, dbo.spt_values, dbo.style, dbo.style_retail, dbo.transfer, dbo.transfer_detail |
| dbo | [CommandExecute](dbo.CommandExecute.md) | dbo.CommandLog |
| dbo | [DatabaseBackup](dbo.DatabaseBackup.md) | dbo.backupset, dbo.CommandExecute, dbo.log_shipping_primary_databases, dbo.log_shipping_secondary_databases, dbo.Queue, dbo.QueueDatabase, dbo.tmpDatabases, sys.dm_db_log_stats, sys.dm_os_host_info |
| dbo | [DatabaseIntegrityCheck](dbo.DatabaseIntegrityCheck.md) | dbo.CommandExecute, dbo.CommandLog, dbo.Queue, dbo.QueueDatabase, sys.dm_os_host_info |
| dbo | [IndexOptimize](dbo.IndexOptimize.md) | dbo.CommandExecute, dbo.Queue, dbo.QueueDatabase, sys.dm_os_host_info |
| dbo | [sp_BlitzCache](dbo.sp_BlitzCache.md) | dbo.p, n.query, n.value, QueryPlan.exist, QueryPlan.value |
| dbo | [sp_help_revlogin](dbo.sp_help_revlogin.md) | dbo.sp_hexadecimal |
| dbo | [sp_hexadecimal](dbo.sp_hexadecimal.md) |  |
| dbo | [sp_MScleanupmergepublisher](dbo.sp_MScleanupmergepublisher.md) |  |
| dbo | [sp_MSrepl_startup](dbo.sp_MSrepl_startup.md) |  |
| dbo | [sp_who3](dbo.sp_who3.md) |  |
| dbo | [spDatabaseBackupOnDemand](dbo.spDatabaseBackupOnDemand.md) | dbo.backupset, dbo.CommandExecute, dbo.log_shipping_primary_databases, dbo.log_shipping_secondary_databases, dbo.Queue, dbo.QueueDatabase, dbo.tmpDatabases, sys.dm_db_log_stats, sys.dm_os_host_info |
| dbo | [usp_who5](dbo.usp_who5.md) |  |
| -- | [Stored Procedure Details: Listing Of Standard Details Related To The Stored Procedure](--.Stored_Procedure_Details_Listing_Of_Standard_Details_Related_To_The_Stored_Procedure.md) |  |
| -- | [Purpose: Return Information Regarding Current Users / Sessions / Processes On A SQL Server Instance](--.Purpose_Return_Information_Regarding_Current_Users_Sessions_Processes_On_A_SQL_Server_Instance.md) |  |
| -- | [Create Date (MM/DD/YYYY): 10/27/2009](--.Create_Date_MM_DD_YYYY_10_27_2009.md) |  |
| -- | [Developer: Sean Smith (s.smith.sql AT gmail DOT com)](--_Developer_Sean_Smith_s_smith.sql_AT_gmail_DOT_com.md) |  |
| -- | [Additional Notes: N/A](--.Additional_Notes_N_A.md) |  |
| -- | [Modification History: Listing Of All Modifications Since Original Implementation](--.Modification_History_Listing_Of_All_Modifications_Since_Original_Implementation.md) |  |
| -- | [Description: Converted Script To Dynamic-SQL](--.Description_Converted_Script_To_Dynamic-SQL.md) |  |
| -- | [: Minor Changes To Code Style](--._Minor_Changes_To_Code_Style.md) |  |
| -- | [: Added "@Database_Name" Filter Variable](--._Added_@Database_Name_Filter_Variable.md) |  |
| -- | [: Added "Last_Wait_Type", "Query_Plan", And "Wait_Type" Fields To Output](--._Added_Last_Wait_Type_,_Query_Plan_,_And_Wait_Type_Fields_To_Output.md) |  |
| -- | [Date (MM/DD/YYYY): 08/08/2011](--.Date_MM_DD_YYYY_08_08_2011.md) |  |
| -- | [Developer: Sean Smith (s.smith.sql AT gmail DOT com)](--_Developer_Sean_Smith_s_smith.sql_AT_gmail_DOT_com.md) |  |
| -- | [Additional Notes: N/A](--.Additional_Notes_N_A.md) |  |
| -- | [Description: Renamed Input Variables](--.Description_Renamed_Input_Variables.md) |  |
| -- | [: Added "Plan_Cache_Object_Type", "Plan_Object_Type", "Plan_Times_Used", And "Plan_Size_MB" Fields To Output](--._Added_Plan_Cache_Object_Type_,_Plan_Object_Type_,_Plan_Times_Used_,_And_Plan_Size_MB_Fields_To_Output.md) |  |
| -- | [: Changed Help Output From RAISERROR To PRINT](--._Changed_Help_Output_From_RAISERROR_To_PRINT.md) |  |
| -- | [: Merged "I?" And "O?" Help Parameters Into "?"](--._Merged_I_And_O_Help_Parameters_Into.md) |  |
| -- | [: Added "C" Type "@Filter" Option](--._Added_C_Type_@Filter_Option.md) |  |
| -- | [: Rewrote Time Calculation Logic](--._Rewrote_Time_Calculation_Logic.md) |  |
| -- | [Date (MM/DD/YYYY): 11/09/2011](--.Date_MM_DD_YYYY_11_09_2011.md) |  |
| -- | [Developer: Sean Smith (s.smith.sql AT gmail DOT com)](--_Developer_Sean_Smith_s_smith.sql_AT_gmail_DOT_com.md) |  |
| -- | [Additional Notes: N/A](--.Additional_Notes_N_A.md) |  |
| -- | [Description: Expanded "Running" Type Indicators](--.Description_Expanded_Running_Type_Indicators.md) |  |
| -- | [: Added System Reserved SPID Indicator To "SPECID"](--._Added_System_Reserved_SPID_Indicator_To_SPECID.md) |  |
| -- | [: Added "SQL_Statement_Current" And "End_Of_Batch" Fields To Output](--._Added_SQL_Statement_Current_And_End_Of_Batch_Fields_To_Output.md) |  |
| -- | [Date (MM/DD/YYYY): 02/01/2012](--.Date_MM_DD_YYYY_02_01_2012.md) |  |
| -- | [Developer: Sean Smith (s.smith.sql AT gmail DOT com)](--_Developer_Sean_Smith_s_smith.sql_AT_gmail_DOT_com.md) |  |
| -- | [Additional Notes: N/A](--.Additional_Notes_N_A.md) |  |
| -- | [Description: Minor Code Formatting Changes](--.Description_Minor_Code_Formatting_Changes.md) |  |
| -- | [: Bug Fixes](--._Bug_Fixes.md) |  |
| -- | [: Changes To Date Calculation Method](--._Changes_To_Date_Calculation_Method.md) |  |
| -- | [Date (MM/DD/YYYY): 08/19/2013](--.Date_MM_DD_YYYY_08_19_2013.md) |  |
| -- | [Developer: Sean Smith (s.smith.sql AT gmail DOT com)](--_Developer_Sean_Smith_s_smith.sql_AT_gmail_DOT_com.md) |  |
| -- | [Additional Notes: N/A](--.Additional_Notes_N_A.md) |  |
| -- | [Description: Added "Batch_Pct", "Command_Completion", "Command_Pct", "Command_Time_Left", "Deadlock_Priority", "Isolation_Level", "Last_Row_Count", "Lock_Details", "Lock_Timeout_Seconds", And "Previous_Error" Fields To Output](--.Description_Added_Batch_Pct_,_Command_Completion_,_Command_Pct_,_Command_Time_Left_,_Deadlock_Priority_,_Isolation_Level_,_Last_Row_Count_,_Lock_Details_,_Lock_Timeout_Seconds_,_And_Previous_Error_Fields_To_Output.md) |  |
| -- | [Date (MM/DD/YYYY): 11/24/2013](--.Date_MM_DD_YYYY_11_24_2013.md) |  |
| -- | [Developer: Sean Smith (s.smith.sql AT gmail DOT com)](--_Developer_Sean_Smith_s_smith.sql_AT_gmail_DOT_com.md) |  |
| -- | [Additional Notes: N/A](--.Additional_Notes_N_A.md) |  |
| -- | [Description: Massive Rewrite Of Entire Stored Procedure](--.Description_Massive_Rewrite_Of_Entire_Stored_Procedure.md) |  |
| -- | [Date (MM/DD/YYYY): 11/28/2015](--.Date_MM_DD_YYYY_11_28_2015.md) |  |
| -- | [Developer: Sean Smith (s.smith.sql AT gmail DOT com)](--_Developer_Sean_Smith_s_smith.sql_AT_gmail_DOT_com.md) |  |
| -- | [Additional Notes: N/A](--.Additional_Notes_N_A.md) |  |
| -- | [Main Query: Create Procedure](--.Main_Query_Create_Procedure.md) |  |
| -- | [Error Trapping: Check If "@Filter" Parameter Is An Input / Output Help Request](--.Error_Trapping_Check_If_@Filter_Parameter_Is_An_Input_Output_Help_Request.md) |  |
| -- | [Declarations / Sets: Declare And Set Variables](--.Declarations_Sets_Declare_And_Set_Variables.md) |  |
| -- | [Main Query: Final Display / Output](--.Main_Query_Final_Display_Output.md) |  |
