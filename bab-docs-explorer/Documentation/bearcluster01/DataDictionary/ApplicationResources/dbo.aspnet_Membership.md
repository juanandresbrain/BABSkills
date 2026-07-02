# dbo.aspnet_Membership

**Database:** ApplicationResources  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ApplicationId | uniqueidentifier | 16 | 0 |  | YES |  |
| UserId | uniqueidentifier | 16 | 0 | YES | YES |  |
| Password | nvarchar | 256 | 0 |  |  |  |
| PasswordFormat | int | 4 | 0 |  |  |  |
| PasswordSalt | nvarchar | 256 | 0 |  |  |  |
| MobilePIN | nvarchar | 32 | 1 |  |  |  |
| Email | nvarchar | 512 | 1 |  |  |  |
| LoweredEmail | nvarchar | 512 | 1 |  |  |  |
| PasswordQuestion | nvarchar | 512 | 1 |  |  |  |
| PasswordAnswer | nvarchar | 256 | 1 |  |  |  |
| IsApproved | bit | 1 | 0 |  |  |  |
| IsLockedOut | bit | 1 | 0 |  |  |  |
| CreateDate | datetime | 8 | 0 |  |  |  |
| LastLoginDate | datetime | 8 | 0 |  |  |  |
| LastPasswordChangedDate | datetime | 8 | 0 |  |  |  |
| LastLockoutDate | datetime | 8 | 0 |  |  |  |
| FailedPasswordAttemptCount | int | 4 | 0 |  |  |  |
| FailedPasswordAttemptWindowStart | datetime | 8 | 0 |  |  |  |
| FailedPasswordAnswerAttemptCount | int | 4 | 0 |  |  |  |
| FailedPasswordAnswerAttemptWindowStart | datetime | 8 | 0 |  |  |  |
| Comment | ntext | 3000 | 1 |  |  |  |

