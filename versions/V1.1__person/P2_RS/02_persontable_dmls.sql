DECLARE @DEPLOY_DMLS NVARCHAR(50)
SET @DEPLOY_DMLS = 'no'

IF @DEPLOY_DMLS = 'yes'
BEGIN
  INSERT INTO [dbo].[Person] ([Title],[FirstName],[MiddleName],[LastName],[Suffix]) VALUES('Mr', 'Bruce', 'L.', 'Wayne', 'II')
END