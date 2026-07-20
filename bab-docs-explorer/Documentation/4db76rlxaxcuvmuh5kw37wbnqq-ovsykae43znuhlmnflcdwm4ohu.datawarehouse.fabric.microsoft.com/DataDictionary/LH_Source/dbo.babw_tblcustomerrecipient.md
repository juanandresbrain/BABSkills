# dbo.babw_tblcustomerrecipient

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | int | 4 | 1 |  |  |  |
| Pull_DateStamp | datetime2 | 8 | 1 |  |  |  |
| Pull_StoreID | int | 4 | 1 |  |  |  |
| iSRecordID | int | 4 | 1 |  |  |  |
| iSLanguageID | int | 4 | 1 |  |  |  |
| iSServerID | int | 4 | 1 |  |  |  |
| sSFirstName | varchar | 8000 | 1 |  |  |  |
| sSLastName | varchar | 8000 | 1 |  |  |  |
| sSAliasName | varchar | 8000 | 1 |  |  |  |
| sSAppartment | varchar | 8000 | 1 |  |  |  |
| sSAddress1 | varchar | 8000 | 1 |  |  |  |
| sSAddress2 | varchar | 8000 | 1 |  |  |  |
| sSCity | varchar | 8000 | 1 |  |  |  |
| sSPostCode | varchar | 8000 | 1 |  |  |  |
| sSState | varchar | 8000 | 1 |  |  |  |
| sSCountry | varchar | 8000 | 1 |  |  |  |
| sSEMail | varchar | 8000 | 1 |  |  |  |
| sSGender | varchar | 8000 | 1 |  |  |  |
| dSBirthDate | datetime2 | 8 | 1 |  |  |  |
| iSBirthDay | int | 4 | 1 |  |  |  |
| iSBirthMonth | int | 4 | 1 |  |  |  |
| iSBirthYear | int | 4 | 1 |  |  |  |
| sSSendMail | varchar | 8000 | 1 |  |  |  |
| sSSendEMail | varchar | 8000 | 1 |  |  |  |
| sSJoinLoyalty | varchar | 8000 | 1 |  |  |  |
| LastTimeStamp | varbinary | 8000 | 1 |  |  |  |
| iSRecordStatus | int | 4 | 1 |  |  |  |
| iRRecordID | int | 4 | 1 |  |  |  |
| iRLanguageID | int | 4 | 1 |  |  |  |
| iRServerID | int | 4 | 1 |  |  |  |
| iRStoreID | int | 4 | 1 |  |  |  |
| iRKioskID | int | 4 | 1 |  |  |  |
| iRCustomerID | int | 4 | 1 |  |  |  |
| sRBarCodeNumber | varchar | 8000 | 1 |  |  |  |
| sRAnimalID | varchar | 8000 | 1 |  |  |  |
| sRAnimalName | varchar | 8000 | 1 |  |  |  |
| sRAnimalType | varchar | 8000 | 1 |  |  |  |
| sRAnimalBirthDate | varchar | 8000 | 1 |  |  |  |
| sRAnimalHeight | varchar | 8000 | 1 |  |  |  |
| sRAnimalWeight | varchar | 8000 | 1 |  |  |  |
| sRAnimalEyeColor | varchar | 8000 | 1 |  |  |  |
| sRAnimalFurColor | varchar | 8000 | 1 |  |  |  |
| sRAnimalImageFile | varchar | 8000 | 1 |  |  |  |
| sRRecipientType | varchar | 8000 | 1 |  |  |  |
| sRFirstName | varchar | 8000 | 1 |  |  |  |
| sRLastName | varchar | 8000 | 1 |  |  |  |
| sRAppartment | varchar | 8000 | 1 |  |  |  |
| sRAddress1 | varchar | 8000 | 1 |  |  |  |
| sRAddress2 | varchar | 8000 | 1 |  |  |  |
| sRCity | varchar | 8000 | 1 |  |  |  |
| sRPostCode | varchar | 8000 | 1 |  |  |  |
| sRState | varchar | 8000 | 1 |  |  |  |
| sRCountry | varchar | 8000 | 1 |  |  |  |
| sREMail | varchar | 8000 | 1 |  |  |  |
| sRGender | varchar | 8000 | 1 |  |  |  |
| sRBookSchedule | varchar | 8000 | 1 |  |  |  |
| sRDocumentType | varchar | 8000 | 1 |  |  |  |
| iRStoryID | int | 4 | 1 |  |  |  |
| dRBirthDate | datetime2 | 8 | 1 |  |  |  |
| iRBirthDay | int | 4 | 1 |  |  |  |
| iRBirthMonth | int | 4 | 1 |  |  |  |
| iRBirthYear | int | 4 | 1 |  |  |  |
| dRStartTime | datetime2 | 8 | 1 |  |  |  |
| dREndTime | datetime2 | 8 | 1 |  |  |  |
| sRProcessFlow | varchar | 8000 | 1 |  |  |  |
| sVersionNo | varchar | 8000 | 1 |  |  |  |
| iRRecordStatus | int | 4 | 1 |  |  |  |
| sBearDollSelect | varchar | 8000 | 1 |  |  |  |
| sCharmID | varchar | 8000 | 1 |  |  |  |
| sSMobileNumber | varchar | 8000 | 1 |  |  |  |
| sRMobileNumber | varchar | 8000 | 1 |  |  |  |
| sRAnimalGender | bit | 1 | 1 |  |  |  |
| EarTagID | varchar | 8000 | 1 |  |  |  |
| selected_language | varchar | 8000 | 1 |  |  |  |
| ParentConsent | varchar | 8000 | 1 |  |  |  |
| ParentName | varchar | 8000 | 1 |  |  |  |
| Under13 | varchar | 8000 | 1 |  |  |  |
| sRZRideModel | varchar | 8000 | 1 |  |  |  |
| sRZRideChassis | varchar | 8000 | 1 |  |  |  |
| Pin | varchar | 8000 | 1 |  |  |  |
| SFSMember | varchar | 8000 | 1 |  |  |  |
| HadSFSCard | varchar | 8000 | 1 |  |  |  |
| VirtualWorld | int | 4 | 1 |  |  |  |
| sSendBearVilleReminder | varchar | 8000 | 1 |  |  |  |
| sSendSMS | bit | 1 | 1 |  |  |  |
| firstvisit | bit | 1 | 1 |  |  |  |
