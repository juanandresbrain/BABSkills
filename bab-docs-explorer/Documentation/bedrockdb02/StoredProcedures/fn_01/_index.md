# Stored Procedures: fn_01

| Schema | Name | Table Dependencies |
|---|---|---|
| dbo | [Cs_GetCsFileID](dbo.Cs_GetCsFileID.md) | dbo.Cs_ExportReg, dbo.Sr_History |
| dbo | [Cs_ResubmitTransmission](dbo.Cs_ResubmitTransmission.md) | dbo.Cs_ReTransmission |
| dbo | [Cs_ReTransmissionStart](dbo.Cs_ReTransmissionStart.md) | dbo.Cs_FileStat, dbo.Cs_ReTransmission, dbo.Sv_GetNextID |
| dbo | [Cs_TransmissionResults](dbo.Cs_TransmissionResults.md) | dbo.Cs_ExportReg, dbo.Cs_FileStat, dbo.Cs_Service, dbo.Sr_Parameter |
| dbo | [Cs_TransmissionStart](dbo.Cs_TransmissionStart.md) | dbo.Cs_ExportReg, dbo.Cs_FileStat, dbo.Ex_OutputStat, dbo.Sr_History, dbo.Sv_GetNextID |
| dbo | [Cs_ValidateTransmission](dbo.Cs_ValidateTransmission.md) | dbo.Cs_FileStat, dbo.Cs_ReTransmission, dbo.Cs_ValidateTransmission |
| Linda Zenebisis | [july 5, 2002    'validation was not working for linked retransmissons](Linda_Zenebisis.july_5,_2002_'validation_was_not_working_for_linked_retransmissons.md) |  |
| dbo | [dt_addtosourcecontrol](dbo.dt_addtosourcecontrol.md) |  |
| dbo | [dt_addtosourcecontrol_u](dbo.dt_addtosourcecontrol_u.md) |  |
| dbo | [dt_adduserobject](dbo.dt_adduserobject.md) |  |
| ** | [Add an object to the dtproperties table](.Add_an_object_to_the_dtproperties_table.md) |  |
| dbo | [dt_adduserobject_vcs](dbo.dt_adduserobject_vcs.md) |  |
| dbo | [dt_checkinobject](dbo.dt_checkinobject.md) |  |
| declare @iReturnValue | [int](declare_@iReturnValue.int.md) |  |
| dbo | [dt_checkinobject_u](dbo.dt_checkinobject_u.md) |  |
| dbo | [dt_checkoutobject](dbo.dt_checkoutobject.md) |  |
| dbo | [dt_checkoutobject_u](dbo.dt_checkoutobject_u.md) |  |
| dbo | [dt_displayoaerror](dbo.dt_displayoaerror.md) |  |
| dbo | [dt_displayoaerror_u](dbo.dt_displayoaerror_u.md) |  |
| dbo | [dt_droppropertiesbyid](dbo.dt_droppropertiesbyid.md) |  |
| ** | [Drop one or all the associated properties of an object or an attribute](.Drop_one_or_all_the_associated_properties_of_an_object_or_an_attribute.md) |  |
| ** | [dt_dropproperties objid, null or '' -- drop all properties of the object itself](.dt_dropproperties_objid,_null_or_''_--_drop_all_properties_of_the_object_itself.md) |  |
| ** | [dt_dropproperties objid, property -- drop the property](.dt_dropproperties_objid,_property_--_drop_the_property.md) |  |
| dbo | [dt_dropuserobjectbyid](dbo.dt_dropuserobjectbyid.md) |  |
| ** | [Drop an object from the dbo.dtproperties table](Drop_an_object_from_the_dbo.dtproperties_table.md) |  |
| dbo | [dt_generateansiname](dbo.dt_generateansiname.md) |  |
| ** | [Generate an ansi name that is unique in the dtproperties.value column](Generate_an_ansi_name_that_is_unique_in_the_dtproperties.value_column.md) |  |
| dbo | [dt_getobjwithprop](dbo.dt_getobjwithprop.md) |  |
| ** | [Retrieve the owner object(s) of a given property](.Retrieve_the_owner_object_s_of_a_given_property.md) |  |
| dbo | [dt_getobjwithprop_u](dbo.dt_getobjwithprop_u.md) |  |
| ** | [Retrieve the owner object(s) of a given property](.Retrieve_the_owner_object_s_of_a_given_property.md) |  |
| dbo | [dt_getpropertiesbyid](dbo.dt_getpropertiesbyid.md) |  |
| ** | [Retrieve properties by id's](.Retrieve_properties_by_id's.md) |  |
| ** | [dt_getproperties objid, null or '' -- retrieve all properties of the object itself](.dt_getproperties_objid,_null_or_''_--_retrieve_all_properties_of_the_object_itself.md) |  |
| ** | [dt_getproperties objid, property -- retrieve the property specified](.dt_getproperties_objid,_property_--_retrieve_the_property_specified.md) |  |
| dbo | [dt_getpropertiesbyid_u](dbo.dt_getpropertiesbyid_u.md) |  |
| ** | [Retrieve properties by id's](.Retrieve_properties_by_id's.md) |  |
| ** | [dt_getproperties objid, null or '' -- retrieve all properties of the object itself](.dt_getproperties_objid,_null_or_''_--_retrieve_all_properties_of_the_object_itself.md) |  |
| ** | [dt_getproperties objid, property -- retrieve the property specified](.dt_getproperties_objid,_property_--_retrieve_the_property_specified.md) |  |
| dbo | [dt_getpropertiesbyid_vcs](dbo.dt_getpropertiesbyid_vcs.md) |  |
| dbo | [dt_getpropertiesbyid_vcs_u](dbo.dt_getpropertiesbyid_vcs_u.md) |  |
| dbo | [dt_isundersourcecontrol](dbo.dt_isundersourcecontrol.md) |  |
| if (@vchProjectName = '') | [set @vchProjectName](if_@vchProjectName_=_''_.set_@vchProjectName.md) |  |
| if (@vchSourceSafeINI = '') set @vchSourceSafeINI | [= null](if_@vchSourceSafeINI_=_''_set_@vchSourceSafeINI.=_null.md) |  |
| if (@vchServerName = '') | [set @vchServerName](if_@vchServerName_=_''_.set_@vchServerName.md) |  |
| if (@vchDatabaseName = '') | [set @vchDatabaseName](if_@vchDatabaseName_=_''_.set_@vchDatabaseName.md) |  |
| dbo | [dt_isundersourcecontrol_u](dbo.dt_isundersourcecontrol_u.md) |  |
| dbo | [dt_removefromsourcecontrol](dbo.dt_removefromsourcecontrol.md) |  |
| dbo | [dt_setpropertybyid](dbo.dt_setpropertybyid.md) |  |
| ** | [If the property already exists, reset the value; otherwise add property](.If_the_property_already_exists,_reset_the_value;_otherwise_add_property.md) |  |
| dbo | [dt_setpropertybyid_u](dbo.dt_setpropertybyid_u.md) |  |
| ** | [If the property already exists, reset the value; otherwise add property](.If_the_property_already_exists,_reset_the_value;_otherwise_add_property.md) |  |
| dbo | [dt_validateloginparams](dbo.dt_validateloginparams.md) |  |
| dbo | [dt_validateloginparams_u](dbo.dt_validateloginparams_u.md) |  |
| dbo | [dt_vcsenabled](dbo.dt_vcsenabled.md) |  |
| dbo | [dt_verstamp006](dbo.dt_verstamp006.md) |  |
| ** | [This procedure returns the version number of the stored](.This_procedure_returns_the_version_number_of_the_stored.md) |  |
| ** | [Visual Database Tools.  Version is 7.0.00.](Visual_Database_Tools_Version_is_7_0_00..md) |  |
| dbo | [dt_verstamp007](dbo.dt_verstamp007.md) |  |
| ** | [This procedure returns the version number of the stored](.This_procedure_returns_the_version_number_of_the_stored.md) |  |
| ** | [Version is 7.0.05.](Version_is_7_0_05..md) |  |
| dbo | [dt_whocheckedout](dbo.dt_whocheckedout.md) |  |
| dbo | [dt_whocheckedout_u](dbo.dt_whocheckedout_u.md) |  |
| dbo | [Ex_AddThread](dbo.Ex_AddThread.md) | dbo.Ex_ServerThread |
| /* | [Author: Chris Carveth](.Author_Chris_Carveth.md) |  |
| /* | [Creation Date: 29-June-1998](.Creation_Date_29-June-1998.md) |  |
| /* | [Comments: Adds a Thread to Ex_ServerThread](.Comments_Adds_a_Thread_to_Ex_ServerThread.md) |  |
| dbo | [Ex_ExecutionDone](dbo.Ex_ExecutionDone.md) | dbo.Ex_ExecutionHistory, dbo.Ex_ServerMain |
| /* | [Author: Chris Carveth](.Author_Chris_Carveth.md) |  |
| /* | [Creation Date: 17-June-1998](.Creation_Date_17-June-1998.md) |  |
| /* | [Comments: Updates Ex_ExecutionHistory](.Comments_Updates_Ex_ExecutionHistory.md) |  |
| dbo | [Ex_ExecutionStart](dbo.Ex_ExecutionStart.md) | dbo.Ex_ExecutionHistory, dbo.Ex_ServerMain, dbo.Ex_ServerThread, dbo.Sv_GetNextID |
| /* | [*/](..md) |  |
| /* | [Author: Chris Carveth                             */](.Author_Chris_Carveth.md) |  |
| /* | [Creation Date: 19-June-1998                       */](.Creation_Date_19-June-1998.md) |  |
| /* | [Comments: Updates Ex_ExecutionHistory             */](.Comments_Updates_Ex_ExecutionHistory.md) |  |
| dbo | [Ex_GetNextFileNum](dbo.Ex_GetNextFileNum.md) | dbo.Ex_OutputNumber |
| dbo | [Ex_LockJob](dbo.Ex_LockJob.md) | dbo.Ex_ServerMain |
| /* | [Author: Chris Carveth](.Author_Chris_Carveth.md) |  |
| /* | [Creation Date: 23-June-1998](.Creation_Date_23-June-1998.md) |  |
| /* | [Comments: Updates Ex_ServerMain locked](.Comments_Updates_Ex_ServerMain_locked.md) |  |
| dbo | [Ex_OutputStat_Backup](dbo.Ex_OutputStat_Backup.md) | dbo.Ex_OutputStat |
| dbo | [Ex_OutputStat_ByJob](dbo.Ex_OutputStat_ByJob.md) | dbo.Ex_OutputStat, dbo.Sr_History |
| declare OutputStatCursor cursor | [for](declare_OutputStatCursor_cursor.for.md) |  |
| dbo | [Ex_OutputStat_Final](dbo.Ex_OutputStat_Final.md) | dbo.Ex_OutputStat |
| dbo | [Ex_OutputStat_Merge](dbo.Ex_OutputStat_Merge.md) | dbo.Ex_OutputStat |
| dbo | [Ex_OutputStat_Work](dbo.Ex_OutputStat_Work.md) | dbo.Ex_OutputStat |
| dbo | [Ex_OutputStat_Work_40](dbo.Ex_OutputStat_Work_40.md) | dbo.Ex_OutputStat |
| dbo | [Ex_StatusRequest](dbo.Ex_StatusRequest.md) | dbo.Ex_ServerThread |
| /* | [Author: Chris Carveth](.Author_Chris_Carveth.md) |  |
| /* | [Creation Date: 29-June-1998](.Creation_Date_29-June-1998.md) |  |
| /* | [Comments: Updates Ex_ServerThread](.Comments_Updates_Ex_ServerThread.md) |  |
| dbo | [Ex_UnLockJob](dbo.Ex_UnLockJob.md) | dbo.Ex_ServerMain |
| /* | [Author: Chris Carveth](.Author_Chris_Carveth.md) |  |
| /* | [Creation Date: 23-June-1998](.Creation_Date_23-June-1998.md) |  |
| /* | [Comments: Updates Ex_ServerMain locked](.Comments_Updates_Ex_ServerMain_locked.md) |  |
| dbo | [FNDTN_ADD_USER_GRP_MBRSHP_$SP](dbo.FNDTN_ADD_USER_GRP_MBRSHP_$SP.md) | dbo.FNDTN_SCRTY_GRP_USER |
| dbo | [FNDTN_ADD_USER_SSN_EX_PS](dbo.FNDTN_ADD_USER_SSN_EX_PS.md) | dbo.FNDTN_SCRTY_SSN, dbo.FNDTN_SCRTY_SSN_FLD |
| dbo | [FNDTN_ADD_USER_SSN_PS](dbo.FNDTN_ADD_USER_SSN_PS.md) | dbo.FNDTN_SCRTY_SSN |
| dbo | [FNDTN_BOF_CNTXT_CTGRY_PS](dbo.FNDTN_BOF_CNTXT_CTGRY_PS.md) | dbo.FNDTN_BOF_NEXT_ID |
| @i_table_id | [int](@i_table_id.int.md) |  |
| Tim Nishikawa | [June 02 2003 - Corrected table name to Bof_NextId](Tim_Nishikawa.June_02_2003_-_Corrected_table_name_to_Bof_NextId.md) |  |
| Tim Nishikawa | [Feb 17 2004  - Renamed parameter to match the Oracle version of proc.](Tim_Nishikawa_Feb_17_2004_-_Renamed_parameter_to_match_the_Oracle_version_of_proc..md) |  |
| DECLARE | [@next_id](DECLARE.@next_id.md) |  |
| dbo | [FNDTN_GET_EXPRD_SSN_PR](dbo.FNDTN_GET_EXPRD_SSN_PR.md) | dbo.FNDTN_SCRTY_SSN |
| dbo | [FNDTN_GET_MODULES_FOR_ROLE_$SP](dbo.FNDTN_GET_MODULES_FOR_ROLE_$SP.md) | dbo.app_ackey |
| dbo | [FNDTN_LOCK_SSN_PU](dbo.FNDTN_LOCK_SSN_PU.md) | dbo.FNDTN_SCRTY_SSN |
| dbo | [FNDTN_PROD_INFO_PR](dbo.FNDTN_PROD_INFO_PR.md) | dbo.FNDTN_PROD_INFO, dbo.FNDTN_SCRTY_DB_RLTNS |
| /* | [*/](..md) |  |
| /* | [Author:](.Author.md) |  |
| /* | [Creation Date:](.Creation_Date.md) |  |
| /* | [Comments:](.Comments.md) |  |
| dbo | [FNDTN_RGSTR_TBL_$SP](dbo.FNDTN_RGSTR_TBL_$SP.md) | dbo.FNDTN_TBL_LIST |
| /* Procedure | [: FNDTN_REGISTER_TABLE_$SP](Procedure._FNDTN_REGISTER_TABLE_$SP.md) |  |
| /* Author | [: Ian Kendrick](Author._Ian_Kendrick.md) |  |
| /* Date | [: 25 Feb 2005](Date._25_Feb_2005.md) |  |
| /* Purpose | [: Register a table created for a session with foundation](Purpose._Register_a_table_created_for_a_session_with_foundation.md) |  |
| dbo | [FNDTN_RPRT_APP_ASSIGN](dbo.FNDTN_RPRT_APP_ASSIGN.md) | dbo.FNDTN_RPRT_SRVR_APP_A, dbo.FNDTN_SCRTY_PROD_INFO |
| dbo | [FNDTN_SCRTY_APP_INFO_EX_PS](dbo.FNDTN_SCRTY_APP_INFO_EX_PS.md) | dbo.FNDTN_SCRTY_APP_INFO, dbo.FNDTN_SCRTY_SSN |
| /* | [Author:](.Author.md) |  |
| /* | [Creation Date:](.Creation_Date.md) |  |
| /* | [Comments:           adds or updates row      */](.Comments_adds_or_updates_row.md) |  |
| dbo | [FNDTN_SCRTY_APP_INFO_PS](dbo.FNDTN_SCRTY_APP_INFO_PS.md) | dbo.FNDTN_SCRTY_APP_INFO, dbo.FNDTN_SCRTY_SSN |
| /* | [Author:](.Author.md) |  |
| /* | [Creation Date:](.Creation_Date.md) |  |
| /* | [Comments:           adds or updates row      */](.Comments_adds_or_updates_row.md) |  |
| dbo | [FNDTN_SCRTY_SSN_EX_PS](dbo.FNDTN_SCRTY_SSN_EX_PS.md) | dbo.FNDTN_SCRTY_SSN, dbo.FNDTN_SCRTY_SSN_LOG |
| dbo | [FNDTN_SCRTY_SSN_PS](dbo.FNDTN_SCRTY_SSN_PS.md) | dbo.FNDTN_SCRTY_SSN, dbo.FNDTN_SCRTY_SSN_LOG |
| dbo | [FNDTN_SCRTY_VALIDATE_SESSION_PU](dbo.FNDTN_SCRTY_VALIDATE_SESSION_PU.md) | dbo.FNDTN_SCRTY_SSN |
| dbo | [FNDTN_SCRTY_VLDT_SSN_PU](dbo.FNDTN_SCRTY_VLDT_SSN_PU.md) | dbo.FNDTN_SCRTY_SSN |
| dbo | [FNDTN_SL_OBJECT_PU](dbo.FNDTN_SL_OBJECT_PU.md) | dbo.FNDTN_SL_OBJCT |
| dbo | [FNDTN_SRVC_CHNG_STTS_$SP](dbo.FNDTN_SRVC_CHNG_STTS_$SP.md) | dbo.FNDTN_SRVC_EXEC, dbo.FNDTN_SRVC_MGR_SRVC, dbo.T_INTEGER, dbo.T_LONG_INTEGER |
| dbo | [FNDTN_SRVC_STPD_$SP](dbo.FNDTN_SRVC_STPD_$SP.md) | dbo.FNDTN_SRVC_EXEC, dbo.FNDTN_SRVC_MGR_SRVC, dbo.T_DATETIME, dbo.T_INTEGER, dbo.T_LONG_INTEGER |
| dbo | [FNDTN_SRVC_STRTD_$SP](dbo.FNDTN_SRVC_STRTD_$SP.md) | dbo.FNDTN_SRVC_EXEC, dbo.FNDTN_SRVC_MGR_SRVC, dbo.T_LONG_INTEGER |
| dbo | [FNDTN_SRVC_UPDTNG_$SP](dbo.FNDTN_SRVC_UPDTNG_$SP.md) | dbo.FNDTN_SRVC_EXEC, dbo.FNDTN_SRVC_MGR_SRVC, dbo.T_INTEGER, dbo.T_LONG_INTEGER |
| dbo | [FNDTN_SYNC_LOCK_$SP](dbo.FNDTN_SYNC_LOCK_$SP.md) | dbo.FNDTN_SYNC_LOCK |
| /* Procedure | [: FNDTN_SYNC_LOCK_$SP](Procedure._FNDTN_SYNC_LOCK_$SP.md) |  |
| /* Author | [: Ian Kendrick](Author._Ian_Kendrick.md) |  |
| /* Date | [: 12 Jan 2005](Date._12_Jan_2005.md) |  |
| /* Purpose | [: Put a lock into the FNDTN_SYNC_LOCK table](Purpose._Put_a_lock_into_the_FNDTN_SYNC_LOCK_table.md) |  |
| dbo | [FNDTN_SYNC_LOCK_EXTND_TIME_$SP](dbo.FNDTN_SYNC_LOCK_EXTND_TIME_$SP.md) | dbo.FNDTN_SYNC_LOCK |
| /* Procedure | [: FNDTN_SYNC_LOCK_EXTND_TIME_$SP](Procedure._FNDTN_SYNC_LOCK_EXTND_TIME_$SP.md) |  |
| /* Author | [: Ian Kendrick](Author._Ian_Kendrick.md) |  |
| /* Date | [: 22 Feb 2005](Date._22_Feb_2005.md) |  |
| /* Purpose | [: Extend existing locks expiry date](Purpose._Extend_existing_locks_expiry_date.md) |  |
| dbo | [FNDTN_SYNC_MASS_LOCK_$SP](dbo.FNDTN_SYNC_MASS_LOCK_$SP.md) | dbo.FNDTN_SYNC_LOCK |
| /* Procedure | [: FNDTN_SYNC_MASS_LOCK_$SP](Procedure._FNDTN_SYNC_MASS_LOCK_$SP.md) |  |
| /* Author | [: Ian Kendrick](Author._Ian_Kendrick.md) |  |
| /* Date | [: 12 Jan 2005](Date._12_Jan_2005.md) |  |
| /* Purpose | [: Put multiple locks into the FNDTN_SYNC_LOCK table](Purpose._Put_multiple_locks_into_the_FNDTN_SYNC_LOCK_table.md) |  |
| dbo | [FNDTN_SYNC_RLS_GUID_$SP](dbo.FNDTN_SYNC_RLS_GUID_$SP.md) | dbo.FNDTN_SYNC_LOCK |
| /* Procedure | [: FNDTN_SYNC_RELEASE GUID_$SP](Procedure._FNDTN_SYNC_RELEASE_GUID_$SP.md) |  |
| /* Author | [: Ian Kendrick](Author._Ian_Kendrick.md) |  |
| /* Date | [: 12 Jan 2005](Date._12_Jan_2005.md) |  |
| /* Purpose | [: Release a single lock in FNDTN_SYNC_LOCK by ID](Purpose._Release_a_single_lock_in_FNDTN_SYNC_LOCK_by_ID.md) |  |
| dbo | [FNDTN_SYNC_RLS_JOB_$SP](dbo.FNDTN_SYNC_RLS_JOB_$SP.md) | dbo.FNDTN_SYNC_LOCK |
| /* Procedure | [: FNDTN_SYNC_RELEASE GUID_$SP](Procedure._FNDTN_SYNC_RELEASE_GUID_$SP.md) |  |
| /* Author | [: Ian Kendrick](Author._Ian_Kendrick.md) |  |
| /* Date | [: 13 Jan 2005](Date._13_Jan_2005.md) |  |
| /* Purpose | [: Release a all locks for a job / execution id](Purpose._Release_a_all_locks_for_a_job_execution_id.md) |  |
| dbo | [FNDTN_SYNC_RLS_SRV_$SP](dbo.FNDTN_SYNC_RLS_SRV_$SP.md) | dbo.FNDTN_SYNC_LOCK |
| /* Procedure | [: FNDTN_SYNC_RLS_SRV_$SP](Procedure._FNDTN_SYNC_RLS_SRV_$SP.md) |  |
| /* Author | [: Ian Kendrick](Author._Ian_Kendrick.md) |  |
| /* Date | [: 13 Jan 2005](Date._13_Jan_2005.md) |  |
| /* Purpose | [: Release a all locks for a service / machine /date](Purpose._Release_a_all_locks_for_a_service_machine_date.md) |  |
| dbo | [FNDTN_SYNC_RLS_SRV_ND_$SP](dbo.FNDTN_SYNC_RLS_SRV_ND_$SP.md) | dbo.FNDTN_SYNC_LOCK |
| /* Procedure | [: FNDTN_SYNC_RLS_SRV_ND_$SP](Procedure._FNDTN_SYNC_RLS_SRV_ND_$SP.md) |  |
| /* Author | [: Ian Kendrick](Author._Ian_Kendrick.md) |  |
| /* Date | [: 13 Jan 2005](Date._13_Jan_2005.md) |  |
| /* Purpose | [: Release a all locks for a service / machine](Purpose._Release_a_all_locks_for_a_service_machine.md) |  |
| dbo | [FNDTN_SYNC_RLS_SRV_SGMNT_$SP](dbo.FNDTN_SYNC_RLS_SRV_SGMNT_$SP.md) | dbo.FNDTN_SYNC_LOCK |
| /* Procedure | [: FNDTN_SYNC_RLS_SRV_SGMNT_$SP](Procedure._FNDTN_SYNC_RLS_SRV_SGMNT_$SP.md) |  |
| /* Author | [: Ian Kendrick](Author._Ian_Kendrick.md) |  |
| /* Date | [: 13 Jan 2005](Date._13_Jan_2005.md) |  |
| /* Purpose | [: Release a all locks for a service / segment / date](Purpose._Release_a_all_locks_for_a_service_segment_date.md) |  |
| dbo | [FNDTN_SYNC_RLS_SRV_SGMT_ND_$SP](dbo.FNDTN_SYNC_RLS_SRV_SGMT_ND_$SP.md) | dbo.FNDTN_SYNC_LOCK |
| /* Procedure | [: FNDTN_SYNC_RLS_SRV_SGMT_ND_$SP](Procedure._FNDTN_SYNC_RLS_SRV_SGMT_ND_$SP.md) |  |
| /* Author | [: Ian Kendrick](Author._Ian_Kendrick.md) |  |
| /* Date | [: 13 Jan 2005](Date._13_Jan_2005.md) |  |
| /* Purpose | [: Release a all locks for a service / segment](Purpose._Release_a_all_locks_for_a_service_segment.md) |  |
| dbo | [FNDTN_UNRGSTR_TBL_$SP](dbo.FNDTN_UNRGSTR_TBL_$SP.md) | dbo.FNDTN_TBL_LIST |
| /* Procedure | [: FNDTN_UNREGISTER_TABLE_$SP](Procedure._FNDTN_UNREGISTER_TABLE_$SP.md) |  |
| /* Author | [: Ian Kendrick](Author._Ian_Kendrick.md) |  |
| /* Date | [: 25 Feb 2005](Date._25_Feb_2005.md) |  |
| /* Purpose | [: Unregister a table created for a session with foundation](Purpose._Unregister_a_table_created_for_a_session_with_foundation.md) |  |
| dbo | [insert_report_criteria_form_assoc_merch_$sp](dbo.insert_report_criteria_form_assoc_merch_$sp.md) | dbo.FNDTN_RPRT_ITEM, dbo.FNDTN_RPRT_ITEM_CRTRN_FORM_A, dbo.insert_report_criteria_form_default_merch_$sp, dbo.T_ID |
| -- | [@criteria_list type_criteria_list_merch READONLY,](--.@criteria_list_type_criteria_list_merch_READONLY,.md) |  |
| dbo | [insert_report_criteria_form_assoc_webim_$sp](dbo.insert_report_criteria_form_assoc_webim_$sp.md) | dbo.criteria_list_webim, dbo.FNDTN_RPRT_ITEM, dbo.FNDTN_RPRT_ITEM_CRTRN_FORM_A, dbo.insert_report_criteria_form_default_webim_$sp, dbo.T_ID |
| dbo | [insert_report_criteria_form_default_merch_$sp](dbo.insert_report_criteria_form_default_merch_$sp.md) | dbo.FNDTN_RPRT_ITEM, dbo.FNDTN_RPRT_ITEM_CRTRN_DFLT_VAL, dbo.T_ID |
| -- | [@criteria_list type_criteria_list_merch READONLY,](--.@criteria_list_type_criteria_list_merch_READONLY,.md) |  |
| dbo | [insert_report_criteria_form_default_webim_$sp](dbo.insert_report_criteria_form_default_webim_$sp.md) | dbo.criteria_list_webim, dbo.FNDTN_RPRT_ITEM, dbo.FNDTN_RPRT_ITEM_CRTRN_DFLT_VAL, dbo.T_ID |
| dbo | [insert_report_item_merch_$sp](dbo.insert_report_item_merch_$sp.md) | dbo.FNDTN_RPRT_ITEM, dbo.FNDTN_RPRT_ITEM_CRTRN_DFLT_VAL, dbo.FNDTN_RPRT_ITEM_CRTRN_FORM_A, dbo.insert_report_criteria_form_assoc_merch_$sp, dbo.T_ID |
| -- | [@criteria_list type_criteria_list_merch READONLY,](--.@criteria_list_type_criteria_list_merch_READONLY,.md) |  |
| dbo | [insert_report_item_webim_$sp](dbo.insert_report_item_webim_$sp.md) | dbo.criteria_list_webim, dbo.FNDTN_RPRT_ITEM, dbo.FNDTN_RPRT_ITEM_CRTRN_DFLT_VAL, dbo.FNDTN_RPRT_ITEM_CRTRN_FORM_A, dbo.insert_report_criteria_form_assoc_webim_$sp, dbo.T_ID |
| dbo | [Md_AddImplementation](dbo.Md_AddImplementation.md) | dbo.Md_Database, dbo.Md_DatabaseGroup, dbo.Md_TopicDatabaseAlias |
| /* | [*/](..md) |  |
| /* | [Author: Linda Zenebisis](.Author_Linda_Zenebisis.md) |  |
| /* | [Creation Date: 12-February-2001              */](.Creation_Date_12-February-2001.md) |  |
| /* | [Comments:  adds or updates implementations   */](.Comments_adds_or_updates_implementations.md) |  |
| dbo | [Md_GetMiddleTable1](dbo.Md_GetMiddleTable1.md) | dbo.Md_Table, dbo.Md_TableLink3Ways |
| /* | [*/](..md) |  |
| /* | [Author : Ashraf Zaid                       */](.Author_Ashraf_Zaid.md) |  |
| /* | [Creation Date : 24 Nov 1997                */](.Creation_Date_24_Nov_1997.md) |  |
| /* | [Comments : Return a middle table           */](.Comments_Return_a_middle_table.md) |  |
| /* | [required to link the 2 input    */](.required_to_link_the_2_input.md) |  |
| /* | [Modified Feb 24 2000 part of 3.5 to use    */](Modified_Feb_24_2000_part_of_3.5_to_use.md) |  |
| dbo | [Md_LoadLanguage](dbo.Md_LoadLanguage.md) | dbo.Lg_DependentDesc, dbo.Lg_Identification, dbo.Md_Field, dbo.Md_FieldGroup, dbo.Md_Topic |
| --   Creation Date: | [16-May-2005](--_Creation_Date_.16-May-2005.md) |  |
| dbo | [Md_PrepareTableLinks](dbo.Md_PrepareTableLinks.md) | dbo.Md_Table, dbo.Md_TableExclusive, dbo.Md_TableLink, dbo.Md_TableLink3Ways, dbo.Md_TableLink4Ways |
| /* | [*/](..md) |  |
| /* | [Author : Ashraf Zaid                         */](.Author_Ashraf_Zaid.md) |  |
| /* | [Creation Date : Feb 10 2000                  */](.Creation_Date_Feb_10_2000.md) |  |
| /* | [Comments : Rebuild the table                 */](.Comments_Rebuild_the_table.md) |  |
| /* | [*/](..md) |  |
| dbo | [Md_UpdateExtendedField](dbo.Md_UpdateExtendedField.md) | dbo.Md_Field, dbo.Md_FieldGrouping, dbo.Md_Table |
| dbo | [remove_report_item_merch_$sp](dbo.remove_report_item_merch_$sp.md) | dbo.FNDTN_RPRT_ITEM, dbo.FNDTN_RPRT_ITEM_CRTRN_DFLT_VAL, dbo.FNDTN_RPRT_ITEM_CRTRN_FORM_A, dbo.T_ID |
| dbo | [remove_report_item_webim_$sp](dbo.remove_report_item_webim_$sp.md) | dbo.FNDTN_RPRT_ITEM, dbo.FNDTN_RPRT_ITEM_CRTRN_DFLT_VAL, dbo.FNDTN_RPRT_ITEM_CRTRN_FORM_A, dbo.T_ID |
| dbo | [Sl_Sr_ExecutionError](dbo.Sl_Sr_ExecutionError.md) | dbo.Sl_Sr_Error |
| /* | [*/](..md) |  |
| /* | [Author: Chris Carveth](.Author_Chris_Carveth.md) |  |
| /* | [Creation Date: 05-March-1999                 */](.Creation_Date_05-March-1999.md) |  |
| /* | [Comments:                                    */](.Comments.md) |  |
| dbo | [Sl_Sv_DeleteOutput](dbo.Sl_Sv_DeleteOutput.md) | dbo.Sl_Sv_Output |
| @i_output_id | [int](@i_output_id.int.md) |  |
| dbo | [Sl_Sv_GetNextID](dbo.Sl_Sv_GetNextID.md) | dbo.Sl_Sv_NextID |
| create proc dbo.Sl_Sv_GetNextID @i_table_id | [int](create_proc_dbo_Sl_Sv_GetNextID_@i_table_id.int.md) |  |
| Tim Nishikawa | [Feb 17 2004   - renamed parameter to match Oracle version of proc.](Tim_Nishikawa_Feb_17_2004_-_renamed_parameter_to_match_Oracle_version_of_proc..md) |  |
| DECLARE | [@next_id](DECLARE.@next_id.md) |  |
| dbo | [Sl_Sv_GetNextID_Ex](dbo.Sl_Sv_GetNextID_Ex.md) | dbo.Sl_Sv_NextID |
| create proc dbo.Sl_Sv_GetNextID_Ex @table_id | [int, @number_of_ids](create_proc_dbo_Sl_Sv_GetNextID_Ex_@table_id.int,_@number_of_ids.md) |  |
| DECLARE | [@next_id](DECLARE.@next_id.md) |  |
| dbo | [Sr_ActivateJob](dbo.Sr_ActivateJob.md) | dbo.Sr_Job |
| /* | [*/](..md) |  |
| /* | [Author](.Author.md) |  |
| /* | [Creation Date       07/25/00                 */](.Creation_Date_07_25_00.md) |  |
| /* | [Comments                                     */](.Comments.md) |  |
| /* | [*/](..md) |  |
| dbo | [Sr_ActivateObject](dbo.Sr_ActivateObject.md) | dbo.Sr_ActivateJob, dbo.Sr_Job |
| 25-JUL-2000 | [Andrea Nagy](25-JUL-2000.Andrea_Nagy.md) |  |
| /* | [Enter all variables cursors and constants following](.Enter_all_variables_cursors_and_constants_following.md) |  |
| dbo | [Sr_AddJob](dbo.Sr_AddJob.md) | dbo.Sr_Job, dbo.Sv_GetNextID |
| @MachineId int, @ServerId | [int](@MachineId_int,_@ServerId.int.md) |  |
| /* | [*/](..md) |  |
| /* | [Author: Adam Whiston                         */](.Author_Adam_Whiston.md) |  |
| /* | [Creation Date: 19-Feb-1999                   */](.Creation_Date_19-Feb-1999.md) |  |
| /* | [Comments: Adds a job to Sr_Job](.Comments_Adds_a_job_to_Sr_Job.md) |  |
| dbo | [Sr_AddServer](dbo.Sr_AddServer.md) | dbo.Sr_Server |
| /* | [*/](..md) |  |
| /* | [Author: Adam Whiston                         */](.Author_Adam_Whiston.md) |  |
| /* | [Creation Date: 19-Feb-1999                   */](.Creation_Date_19-Feb-1999.md) |  |
| /* | [Comments: Adds a Server to Sr_Server](.Comments_Adds_a_Server_to_Sr_Server.md) |  |
| dbo | [Sr_CleanTrace](dbo.Sr_CleanTrace.md) | dbo.Sr_Trace |
| dbo | [Sr_CompatibilityCheck](dbo.Sr_CompatibilityCheck.md) | dbo.Sr_Job, dbo.Sr_Parameter |
| dbo | [Sr_DebugTrace](dbo.Sr_DebugTrace.md) | dbo.Sr_Trace |
| /* | [*/](..md) |  |
| /* | [Author: Andrea Nagy](.Author_Andrea_Nagy.md) |  |
| /* | [Creation Date: 12-April-1999                 */](.Creation_Date_12-April-1999.md) |  |
| /* | [Comments:                                    */](.Comments.md) |  |
| dbo | [Sr_ExecutionDone](dbo.Sr_ExecutionDone.md) | dbo.FNDTN_SYNC_RLS_JOB_$SP, dbo.Sr_Error, dbo.Sr_History, dbo.Sr_Job |
| /* | [*/](..md) |  |
| /* | [Author: Chris Carveth](.Author_Chris_Carveth.md) |  |
| /* | [Creation Date: 01-March-1999                 */](.Creation_Date_01-March-1999.md) |  |
| /* | [Comments: Updates Sr_History                 */](.Comments_Updates_Sr_History.md) |  |
| dbo | [Sr_ExecutionError](dbo.Sr_ExecutionError.md) | dbo.Sr_Error |
| /* | [*/](..md) |  |
| /* | [Author: Chris Carveth](.Author_Chris_Carveth.md) |  |
| /* | [Creation Date: 05-March-1999                 */](.Creation_Date_05-March-1999.md) |  |
| /* | [Comments:                                    */](.Comments.md) |  |
| dbo | [Sr_ExecutionStart](dbo.Sr_ExecutionStart.md) | dbo.Sr_History, dbo.Sr_Job, dbo.Sr_Server, dbo.Sv_GetNextID |
| /* | [*/](..md) |  |
| /* | [Author: Chris Carveth                        */](.Author_Chris_Carveth.md) |  |
| /* | [Creation Date: 01-March-1999                 */](.Creation_Date_01-March-1999.md) |  |
| /* | [Comments: Updates Sr_History                 */](.Comments_Updates_Sr_History.md) |  |
| dbo | [Sr_GetNextJob](dbo.Sr_GetNextJob.md) | dbo.Sr_Job, dbo.Sr_Machine, dbo.Sr_Server, dbo.Work_Job |
| /* | [*/](..md) |  |
| /* | [Author: Chris Carveth                        */](.Author_Chris_Carveth.md) |  |
| /* | [Creation Date: 01-March-1999                 */](.Creation_Date_01-March-1999.md) |  |
| /* | [Comments: Updates Sr_History                 */](.Comments_Updates_Sr_History.md) |  |
| dbo | [Sr_HistoryCleanup](dbo.Sr_HistoryCleanup.md) | dbo.Sr_History, dbo.Sr_Parameter |
| /* | [*/](..md) |  |
| /* | [Author: Andrea Nagy                          */](.Author_Andrea_Nagy.md) |  |
| /* | [Creation Date: 07-April-99                   */](.Creation_Date_07-April-99.md) |  |
| /* | [Comments: Deletes Sr_History                 */](.Comments_Deletes_Sr_History.md) |  |
| dbo | [Sr_JobNeedRerun](dbo.Sr_JobNeedRerun.md) | dbo.Sr_Job, dbo.Sr_JobCheckpointInfo |
| /* | [*/](..md) |  |
| /* | [Author: Bing Zhu                        */](.Author_Bing_Zhu.md) |  |
| /* | [Creation Date: 26-Sept-2005                 */](.Creation_Date_26-Sept-2005.md) |  |
| /* | [Comments: Support clustering                 */](.Comments_Support_clustering.md) |  |
| dbo | [Sr_KillJob](dbo.Sr_KillJob.md) | dbo.Sr_History, dbo.Sr_Job, dbo.Sr_Server |
| Author | [Michael Orsoni](Author.Michael_Orsoni.md) |  |
| Comments: | [Sends command to kill job](Comments_.Sends_command_to_kill_job.md) |  |
| dbo | [Sr_LockJob](dbo.Sr_LockJob.md) | dbo.Sr_Job |
| /* | [Author: Chris Carveth](.Author_Chris_Carveth.md) |  |
| /* | [Creation Date: 23-June-1998](.Creation_Date_23-June-1998.md) |  |
| /* | [Comments: Updates Ex_ServerMain locked](.Comments_Updates_Ex_ServerMain_locked.md) |  |
| dbo | [Sr_MachineDone](dbo.Sr_MachineDone.md) | dbo.Sr_History, dbo.Sr_Machine |
| /* | [*/](..md) |  |
| /* | [Author: Chris Carveth](.Author_Chris_Carveth.md) |  |
| /* | [Creation Date: 01-March-1999                 */](.Creation_Date_01-March-1999.md) |  |
| /* | [Comments: Updates Sr_History                 */](.Comments_Updates_Sr_History.md) |  |
| dbo | [Sr_MachineDoneInterrupted](dbo.Sr_MachineDoneInterrupted.md) | dbo.Sr_History |
| /* | [*/](..md) |  |
| /* | [Author: Bing Zhu](.Author_Bing_Zhu.md) |  |
| /* | [Creation Date: 12-FEB-2001                   */](.Creation_Date_12-FEB-2001.md) |  |
| /* | [Comments: Updates Sr_History                 */](.Comments_Updates_Sr_History.md) |  |
| dbo | [Sr_MachineStart](dbo.Sr_MachineStart.md) | dbo.Sr_History, dbo.Sr_Machine, dbo.Sr_Parameter, dbo.Sv_GetNextID |
| /* | [*/](..md) |  |
| /* | [Author: Chris Carveth                        */](.Author_Chris_Carveth.md) |  |
| /* | [Creation Date: 01-March-1999                 */](.Creation_Date_01-March-1999.md) |  |
| /* | [Comments: Updates Sr_History                 */](.Comments_Updates_Sr_History.md) |  |
| dbo | [Sr_RemoveJob](dbo.Sr_RemoveJob.md) | dbo.Sr_Job |
| /* | [*/](..md) |  |
| /* | [Author: Tim Nishikawa                        */](.Author_Tim_Nishikawa.md) |  |
| /* | [Creation Date: 03-December-1999              */](.Creation_Date_03-December-1999.md) |  |
| /* | [Comments: Deletes job from Sr_Job and        */](.Comments_Deletes_job_from_Sr_Job_and.md) |  |
| dbo | [Sr_RemoveServer](dbo.Sr_RemoveServer.md) | dbo.Sr_Job, dbo.Sr_Server, dbo.Sr_Server_LANG |
| /* | [Author: Adam Whiston](.Author_Adam_Whiston.md) |  |
| /* | [Creation Date: 22-Feb-1999](.Creation_Date_22-Feb-1999.md) |  |
| /* | [Comments: Removes a Server from Sr_Server &](.Comments_Removes_a_Server_from_Sr_Server_&.md) |  |
| dbo | [Sr_ServerDone](dbo.Sr_ServerDone.md) | dbo.Sr_History |
| /* | [*/](..md) |  |
| /* | [Author: Chris Carveth](.Author_Chris_Carveth.md) |  |
| /* | [Creation Date: 01-March-1999                 */](.Creation_Date_01-March-1999.md) |  |
| /* | [Comments: Updates Sr_History                 */](.Comments_Updates_Sr_History.md) |  |
| dbo | [Sr_ServerStart](dbo.Sr_ServerStart.md) | dbo.Sr_History, dbo.Sr_Parameter, dbo.Sv_GetNextID |
| /* | [*/](..md) |  |
| /* | [Author: Chris Carveth                        */](.Author_Chris_Carveth.md) |  |
| /* | [Creation Date: 01-March-1999                 */](.Creation_Date_01-March-1999.md) |  |
| /* | [Comments: Updates Sr_History                 */](.Comments_Updates_Sr_History.md) |  |
| dbo | [Sr_StandAlone](dbo.Sr_StandAlone.md) | dbo.Sr_Job |
| /* | [*/](..md) |  |
| /* | [Author: Chris Carveth](.Author_Chris_Carveth.md) |  |
| /* | [Creation Date: 05-Nov-1999                       */](.Creation_Date_05-Nov-1999.md) |  |
| /* | [Comments:                                        */](.Comments.md) |  |
| dbo | [Sr_StatusRequest](dbo.Sr_StatusRequest.md) | dbo.Sr_Server |
| /* | [*/](..md) |  |
| /* | [Author: Adam Whiston                         */](.Author_Adam_Whiston.md) |  |
| /* | [Creation Date: 1-April-1999](.Creation_Date_1-April-1999.md) |  |
| /* | [Comments: Updates Sr_Server](.Comments_Updates_Sr_Server.md) |  |
| dbo | [Sr_TraceError](dbo.Sr_TraceError.md) | dbo.Sr_Trace |
| /* | [*/](..md) |  |
| /* | [Author: Chris Carveth](.Author_Chris_Carveth.md) |  |
| /* | [Creation Date: 05-March-1999                 */](.Creation_Date_05-March-1999.md) |  |
| /* | [Comments:                                    */](.Comments.md) |  |
| dbo | [Sv_AddNewFolder](dbo.Sv_AddNewFolder.md) | dbo.Sv_GetNextID, dbo.Sv_UserFolder |
| dbo | [Sv_AddObjToFolder](dbo.Sv_AddObjToFolder.md) | dbo.Sv_FolderItem |
| dbo | [Sv_AddObjToFolderFromFolder](dbo.Sv_AddObjToFolderFromFolder.md) | dbo.Sv_FolderItem |
| dbo | [Sv_AddObjToFolderFromMail](dbo.Sv_AddObjToFolderFromMail.md) | dbo.Sv_FolderItem, dbo.Sv_Mail |
| dbo | [Sv_AddObjToFolderType](dbo.Sv_AddObjToFolderType.md) | dbo.Sv_FolderItem, dbo.Sv_UserFolder |
| dbo | [Sv_Admin_AddUserToSv18](dbo.Sv_Admin_AddUserToSv18.md) | dbo.Lg_Identification, dbo.Sv_GetNextID, dbo.Sv_User |
| dbo | [Sv_Admin_AddUserToTopic](dbo.Sv_Admin_AddUserToTopic.md) | dbo.Md_DatabaseGroup, dbo.Sv_UserTopic |
| dbo | [Sv_AutoTargetFolder](dbo.Sv_AutoTargetFolder.md) | dbo.Sv_UserFolder |
| DECLARE | [@folderid int,](DECLARE.@folderid_int,.md) |  |
| dbo | [Sv_CacheAllocate](dbo.Sv_CacheAllocate.md) | dbo.Sv_OutputCache, dbo.Sv_Parameter |
| @final_maxfiles | [int,](@final_maxfiles.int,.md) |  |
| dbo | [Sv_CacheFindFileID](dbo.Sv_CacheFindFileID.md) | dbo.Sv_OutputCache |
| IF ISNULL(@found_file_id, 0) > 0 | [/* IF file was found then... */](IF_ISNULL_@found_file_id,_0_0_IF_file_was_found_then_..md) |  |
| endofproc: | [/* end of procedure */](endofproc_._end_of_procedure.md) |  |
| dbo | [Sv_CleanDependency](dbo.Sv_CleanDependency.md) | dbo.Sv_Deleted, dbo.Sv_DeletedDependency, dbo.Sv_Object, dbo.Sv_ObjectDependency |
| -- | [Author:   Chris Carveth](--.Author_Chris_Carveth.md) |  |
| -- | [Creation  Date: 15-Feb-1998](--.Creation_Date_15-Feb-1998.md) |  |
| -- | [Comments: Deletes rows in Sv_ObjectDependency](--.Comments_Deletes_rows_in_Sv_ObjectDependency.md) |  |
| dbo | [Sv_CompleteSchedule](dbo.Sv_CompleteSchedule.md) | dbo.Sv_Output, dbo.Sv_Schedule |
| dbo | [Sv_DeleteObjectOutput](dbo.Sv_DeleteObjectOutput.md) | dbo.Sv_Output |
| @object_id | [int](@object_id.int.md) |  |
| dbo | [Sv_DeleteOldOutputs](dbo.Sv_DeleteOldOutputs.md) | dbo.Sv_Output |
| @object_id | [int,](@object_id.int,.md) |  |
| dbo | [Sv_DeleteOutput](dbo.Sv_DeleteOutput.md) | dbo.Sv_Output |
| @output_id | [int](@output_id.int.md) |  |
| dbo | [Sv_GetNextID](dbo.Sv_GetNextID.md) | dbo.Sv_NextID |
| @table_id | [int](@table_id.int.md) |  |
| DECLARE | [@next_id](DECLARE.@next_id.md) |  |
| dbo | [Sv_GetObjRefCount](dbo.Sv_GetObjRefCount.md) | dbo.Sv_FolderItem, dbo.Sv_Mail |
| dbo | [Sv_LockSchedule](dbo.Sv_LockSchedule.md) | dbo.Sv_Schedule |
| @object_id | [int,](@object_id.int,.md) |  |
| @db_group_id | [int](@db_group_id.int.md) |  |
| dbo | [Sv_Login](dbo.Sv_Login.md) | dbo.Sv_UserSession |
| /* | [*/](..md) |  |
| /* | [Author   Andrea Nagy                         */](.Author_Andrea_Nagy.md) |  |
| /* | [Creation Date  21-JUL-2000                   */](.Creation_Date_21-JUL-2000.md) |  |
| /* | [Comments   Logs the SV user into the SV      */](.Comments_Logs_the_SV_user_into_the_SV.md) |  |
| /* | [*/](..md) |  |
| dbo | [Sv_Logout](dbo.Sv_Logout.md) | dbo.Sv_UserSession |
| /* | [*/](..md) |  |
| /* | [Author   Andrea Nagy                         */](.Author_Andrea_Nagy.md) |  |
| /* | [Creation Date  21-JUL-2000                   */](.Creation_Date_21-JUL-2000.md) |  |
| /* | [Comments   Logs the SV user out of the APP   */](.Comments_Logs_the_SV_user_out_of_the_APP.md) |  |
| /* | [*/](..md) |  |
| dbo | [Sv_ObjCountByName](dbo.Sv_ObjCountByName.md) | dbo.Sv_FolderItem, dbo.Sv_Object |
| DECLARE | [@result int](DECLARE.@result_int.md) |  |
| dbo | [Sv_OutputIndexLabel_Add](dbo.Sv_OutputIndexLabel_Add.md) | dbo.Sv_OutputIndexLabel |
| /* | [*/](..md) |  |
| /* | [Author : Ashraf Zaid                                      */](.Author_Ashraf_Zaid.md) |  |
| /* | [Creation Date : Jan 10 2001                               */](.Creation_Date_Jan_10_2001.md) |  |
| /* | [Comments : Insert one record in Sv_OutputIndexLabel       */](.Comments_Insert_one_record_in_Sv_OutputIndexLabel.md) |  |
| dbo | [Sv_SaveStatistic](dbo.Sv_SaveStatistic.md) | dbo.Sv_GetNextID, dbo.Sv_Object, dbo.Sv_Statistic |
| dbo | [Sv_UpdateNextID](dbo.Sv_UpdateNextID.md) | dbo.Cs_ExportReg, dbo.Cs_FileStat, dbo.Cs_Service, dbo.Ex_ExecutionHistory, dbo.Ex_ServerMain, dbo.Sr_History, dbo.Sr_Host, dbo.Sr_Job, dbo.Sv_Categories, dbo.Sv_Deleted, dbo.Sv_File, dbo.Sv_Mail, dbo.Sv_NextID, dbo.Sv_Object, dbo.Sv_Output, dbo.Sv_OutputNote, dbo.Sv_Picture, dbo.Sv_Reminder, dbo.Sv_Statistic, dbo.Sv_User, dbo.Sv_UserFolder, dbo.Sv_UserGroup, dbo.Tr_Directory, dbo.Tr_Parameter, dbo.Tr_PollFile, dbo.Tr_PollFileHistory |
| dbo | [Sv_UpdateScheduleStatus](dbo.Sv_UpdateScheduleStatus.md) | dbo.Sv_Schedule |
| dbo | [Target_Login](dbo.Target_Login.md) | dbo.Sv_UserSession |
| /* | [*/](..md) |  |
| /* | [Author   Andrea Nagy                         */](.Author_Andrea_Nagy.md) |  |
| /* | [Creation Date  21-JUL-2000                   */](.Creation_Date_21-JUL-2000.md) |  |
| /* | [Comments   Logs the SV user into the target  */](.Comments_Logs_the_SV_user_into_the_target.md) |  |
| /* | [DB                           */](.DB.md) |  |
| dbo | [Target_Logout](dbo.Target_Logout.md) | dbo.Sv_UserSession |
| /* | [*/](..md) |  |
| /* | [Author   Andrea Nagy                         */](.Author_Andrea_Nagy.md) |  |
| /* | [Creation Date  21-JUL-2000                   */](.Creation_Date_21-JUL-2000.md) |  |
| /* | [Comments   Logs the SV user out of the       */](.Comments_Logs_the_SV_user_out_of_the.md) |  |
| /* | [target DB                        */](.target_DB.md) |  |
| dbo | [Tr_AddPollFile](dbo.Tr_AddPollFile.md) | dbo.Sv_GetNextID, dbo.Tr_Directory, dbo.Tr_PollFile |
| /* | [*/](..md) |  |
| /* | [Author: Michael Orsoni](.Author_Michael_Orsoni.md) |  |
| /* | [Creation Date: 10-March-2000                 */](.Creation_Date_10-March-2000.md) |  |
| /* | [Comments:                                    */](.Comments.md) |  |
| dbo | [Tr_CloseDir](dbo.Tr_CloseDir.md) | dbo.Tr_Directory |
| Author | [Michael Orsoni](Author.Michael_Orsoni.md) |  |
| Comments: | [Update Translate history table](Comments_.Update_Translate_history_table.md) |  |
| dbo | [Tr_ClosePollFile](dbo.Tr_ClosePollFile.md) | dbo.Sv_GetNextID, dbo.Tr_PollFile, dbo.Tr_PollFileHistory |
| /* | [*/](..md) |  |
| /* | [Author: Michael Orsoni](.Author_Michael_Orsoni.md) |  |
| /* | [Creation Date: 10-March-2000                 */](.Creation_Date_10-March-2000.md) |  |
| /* | [Comments:                                    */](.Comments.md) |  |
| dbo | [Tr_DirError](dbo.Tr_DirError.md) | dbo.Tr_Directory, dbo.Tr_Parameter, dbo.Tr_PollFile, dbo.Tr_PollFileHistory |
| DECLARE | [@DirID  int,](DECLARE.@DirID_int,.md) |  |
| dbo | [Tr_FileError](dbo.Tr_FileError.md) | dbo.Tr_Directory, dbo.Tr_Parameter, dbo.Tr_PollFile |
| DECLARE | [@PollID  int,](DECLARE.@PollID_int,.md) |  |
| dbo | [Tr_GetNextPollFile](dbo.Tr_GetNextPollFile.md) | dbo.Tr_Directory, dbo.Tr_PollFile |
| /* | [*/](..md) |  |
| /* | [Author: Michael Orsoni](.Author_Michael_Orsoni.md) |  |
| /* | [Creation Date: 10-March-2000                 */](.Creation_Date_10-March-2000.md) |  |
| /* | [Comments:                                    */](.Comments.md) |  |
| dbo | [Tr_IsDirDoneAndNotClosed](dbo.Tr_IsDirDoneAndNotClosed.md) | dbo.Tr_Directory, dbo.Tr_Parameter, dbo.Tr_PollFile, dbo.Tr_PollFileHistory |
| Author | [Michael Orsoni](Author.Michael_Orsoni.md) |  |
| Comments: | [Look for any files that are unprocessed in specified directory](Comments_.Look_for_any_files_that_are_unprocessed_in_specified_directory.md) |  |
| dbo | [Tr_MoveError](dbo.Tr_MoveError.md) | dbo.Tr_Directory, dbo.Tr_PollFileHistory |
| DECLARE | [@PollID  int](DECLARE.@PollID_int.md) |  |
| dbo | [Tr_PollFileError](dbo.Tr_PollFileError.md) | dbo.Sv_GetNextID, dbo.Tr_Directory, dbo.Tr_PollFileHistory |
| /* | [*/](..md) |  |
| /* | [Author: Michael Orsoni](.Author_Michael_Orsoni.md) |  |
| /* | [Creation Date: 10-March-2000                 */](.Creation_Date_10-March-2000.md) |  |
| /* | [Comments:                                    */](.Comments.md) |  |
| dbo | [Tr_ProcessError](dbo.Tr_ProcessError.md) | dbo.Sr_Job, dbo.Tr_Directory, dbo.Tr_PollFile |
| DECLARE | [@ExecID  int,](DECLARE.@ExecID_int,.md) |  |
| dbo | [Tr_ShouldWaitOnTPDirs](dbo.Tr_ShouldWaitOnTPDirs.md) | dbo.Tr_Directory |
| dbo | [Web_AddUser](dbo.Web_AddUser.md) | dbo.Lg_Identification, dbo.Sv_GetNextID, dbo.Sv_User, dbo.Sv_UserTopic |
| /* | [*/](..md) |  |
| /* | [Author: MICHAELO                             */](.Author_MICHAELO.md) |  |
| /* | [Creation Date: 07/01                         */](.Creation_Date_07_01.md) |  |
| /* | [Comments:                                    */](.Comments.md) |  |
