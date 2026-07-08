# dbo.EVNT_500041

**Database:** COMM_EVENT  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EVNT_ID | int | 4 | 0 | YES |  |  |
| EVNT_TYPE_ID | int | 4 | 0 |  |  |  |
| SRVR_NAME | nvarchar | 100 | 0 |  |  |  |
| APP_ID | decimal | 9 | 0 |  |  |  |
| PRDCT_ID | nvarchar | 60 | 0 |  |  |  |
| INSTNC_NUM | smallint | 2 | 0 |  |  |  |
| USER_ID | decimal | 9 | 0 |  |  |  |
| EVNT_POST_DTM | datetime | 8 | 0 |  |  |  |
| EVNT_CRTN_DTM | datetime | 8 | 0 |  |  |  |
| STRG_MCHNSM | nvarchar | 60 | 0 |  |  |  |
| FLD_28 | datetime | 8 | 1 |  |  |  |
| FLD_1 | smallint | 2 | 1 |  |  |  |
| FLD_2 | smallint | 2 | 1 |  |  |  |
| FLD_3 | smallint | 2 | 1 |  |  |  |
| FLD_249 | smallint | 2 | 1 |  |  |  |
| FLD_4 | smallint | 2 | 1 |  |  |  |
| FLD_5 | smallint | 2 | 1 |  |  |  |
| FLD_7 | smallint | 2 | 1 |  |  |  |
| FLD_300 | nvarchar | 100 | 1 |  |  |  |
| FLD_29 | varbinary | 2048 | 1 |  |  |  |
| FLD_134 | varbinary | 4 | 1 |  |  |  |
| FLD_247 | tinyint | 1 | 1 |  |  |  |
| FLD_248 | tinyint | 1 | 1 |  |  |  |
| FLD_136 | int | 4 | 1 |  |  |  |
| FLD_137 | smallint | 2 | 1 |  |  |  |
| FLD_138 | datetime | 8 | 1 |  |  |  |
| FLD_139 | smallint | 2 | 1 |  |  |  |
| FLD_140 | int | 4 | 1 |  |  |  |
| FLD_141 | datetime | 8 | 1 |  |  |  |
| FLD_142 | int | 4 | 1 |  |  |  |
| FLD_143 | tinyint | 1 | 1 |  |  |  |
| FLD_144 | tinyint | 1 | 1 |  |  |  |
| FLD_145 | tinyint | 1 | 1 |  |  |  |
| FLD_146 | varbinary | 6 | 1 |  |  |  |
| FLD_147 | smallint | 2 | 1 |  |  |  |
| FLD_394 | tinyint | 1 | 1 |  |  |  |
| FLD_149 | int | 4 | 1 |  |  |  |
| FLD_150 | smallint | 2 | 1 |  |  |  |
| FLD_151 | int | 4 | 1 |  |  |  |
| FLD_152 | nvarchar | 50 | 1 |  |  |  |
| FLD_153 | nvarchar | 60 | 1 |  |  |  |
| FLD_154 | nvarchar | 18 | 1 |  |  |  |
| FLD_155 | tinyint | 1 | 1 |  |  |  |
| FLD_156 | nvarchar | 80 | 1 |  |  |  |
| FLD_157 | nvarchar | 16 | 1 |  |  |  |
| FLD_406 | nvarchar | 4 | 1 |  |  |  |
| FLD_407 | nvarchar | 8 | 1 |  |  |  |
| FLD_158 | nvarchar | 4 | 1 |  |  |  |
| FLD_159 | smallint | 2 | 1 |  |  |  |
| FLD_160 | nvarchar | 80 | 1 |  |  |  |
| FLD_161 | int | 4 | 1 |  |  |  |
| FLD_162 | varbinary | 4 | 1 |  |  |  |
| FLD_414 | tinyint | 1 | 1 |  |  |  |
| FLD_415 | tinyint | 1 | 1 |  |  |  |
| FLD_163 | varbinary | 4 | 1 |  |  |  |
| FLD_416 | tinyint | 1 | 1 |  |  |  |
| FLD_417 | tinyint | 1 | 1 |  |  |  |
| FLD_164 | smallint | 2 | 1 |  |  |  |
| FLD_165 | varbinary | 24 | 1 |  |  |  |
| FLD_166 | smallint | 2 | 1 |  |  |  |
| FLD_167 | varbinary | 28 | 1 |  |  |  |
| FLD_168 | nvarchar | 50 | 1 |  |  |  |
| FLD_169 | nvarchar | 8 | 1 |  |  |  |
| FLD_170 | nvarchar | 12 | 1 |  |  |  |
| FLD_171 | nvarchar | 16 | 1 |  |  |  |
| FLD_172 | nvarchar | 12 | 1 |  |  |  |
| FLD_173 | nvarchar | 12 | 1 |  |  |  |
| FLD_174 | nvarchar | 16 | 1 |  |  |  |
| FLD_175 | tinyint | 1 | 1 |  |  |  |
| FLD_176 | nvarchar | 18 | 1 |  |  |  |
| FLD_177 | nvarchar | 40 | 1 |  |  |  |
| FLD_178 | nvarchar | 2 | 1 |  |  |  |
| FLD_179 | tinyint | 1 | 1 |  |  |  |
| FLD_180 | tinyint | 1 | 1 |  |  |  |
| FLD_181 | nvarchar | 8 | 1 |  |  |  |
| FLD_182 | nvarchar | 2 | 1 |  |  |  |
| FLD_183 | nvarchar | 8 | 1 |  |  |  |
| FLD_184 | smallint | 2 | 1 |  |  |  |
| FLD_185 | varbinary | 255 | 1 |  |  |  |
