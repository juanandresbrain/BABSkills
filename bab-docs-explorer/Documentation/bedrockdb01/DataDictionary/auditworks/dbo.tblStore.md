# dbo.tblStore

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| iStoreID | int | 4 | 0 |  |  |  |
| sStoreName | varchar | 100 | 1 |  |  |  |
| sStoreName1 | varchar | 100 | 0 |  |  |  |
| iGroup | int | 4 | 0 |  |  |  |
| sAddress1 | varchar | 100 | 0 |  |  |  |
| sAddress2 | varchar | 100 | 1 |  |  |  |
| sCity | varchar | 100 | 0 |  |  |  |
| sStateProvince | varchar | 100 | 1 |  |  |  |
| sCountry | varchar | 100 | 1 |  |  |  |
| sZip | char | 13 | 1 |  |  |  |
| sEmail | varchar | 100 | 1 |  |  |  |
| fLatitude | float | 8 | 1 |  |  |  |
| fLongitude | float | 8 | 1 |  |  |  |
| oResult | varchar | 50 | 1 |  |  |  |
| sPhone | varchar | 20 | 1 |  |  |  |
| sFax | varchar | 20 | 1 |  |  |  |
| iMinutesBetweenParties | int | 4 | 1 |  |  |  |
| dOpen | datetime | 8 | 0 |  |  |  |
| dClose | datetime | 8 | 0 |  |  |  |
| dMondayOpen | datetime | 8 | 1 |  |  |  |
| dMondayClose | datetime | 8 | 1 |  |  |  |
| dTuesdayOpen | datetime | 8 | 1 |  |  |  |
| dTuesdayClose | datetime | 8 | 1 |  |  |  |
| dWednesdayOpen | datetime | 8 | 1 |  |  |  |
| dWednesdayClose | datetime | 8 | 1 |  |  |  |
| dThursdayOpen | datetime | 8 | 1 |  |  |  |
| dThursdayClose | datetime | 8 | 1 |  |  |  |
| dFridayOpen | datetime | 8 | 1 |  |  |  |
| dFridayClose | datetime | 8 | 1 |  |  |  |
| dSaturdayOpen | datetime | 8 | 0 |  |  |  |
| dSaturdayClose | datetime | 8 | 0 |  |  |  |
| dSundayOpen | datetime | 8 | 0 |  |  |  |
| dSundayClose | datetime | 8 | 0 |  |  |  |
| iNumSurveyCards | int | 4 | 1 |  |  |  |
| dOpeningDate | datetime | 8 | 1 |  |  |  |
| iBookingParties | tinyint | 1 | 0 |  |  |  |
| iBSRBookingParties | tinyint | 1 | 0 |  |  |  |
| bOptOut | bit | 1 | 0 |  |  |  |
| iConfirmLetter | int | 4 | 0 |  |  |  |
| sWebMessage | text | 16 | 1 |  |  |  |
| sBSRMessage | text | 16 | 1 |  |  |  |
| iSneakPeak | tinyint | 1 | 1 |  |  |  |
| iDollParties | tinyint | 1 | 0 |  |  |  |
| iCoalitionStore | tinyint | 1 | 1 |  |  |  |
| iStoreBooking | tinyint | 1 | 1 |  |  |  |
| dPasswordExpire | datetime | 8 | 1 |  |  |  |
| dCoalitionDate | datetime | 8 | 1 |  |  |  |
| iBookingPriority | tinyint | 1 | 0 |  |  |  |
| iParentStore | int | 4 | 1 |  |  |  |
| iStoreTypeID | int | 4 | 1 |  |  |  |
| sCountryCode | char | 2 | 1 |  |  |  |
| iCancellationHours | int | 4 | 1 |  |  |  |
| iModificationDays | int | 4 | 1 |  |  |  |
| iDinoParties | tinyint | 1 | 0 |  |  |  |
| iPrincessParties | tinyint | 1 | 0 |  |  |  |
