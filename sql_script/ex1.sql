USE [ex1]
GO
SET IDENTITY_INSERT [dbo].[account_bank] ON 

INSERT [dbo].[account_bank] ([id], [name], [acc_no], [balance]) VALUES (1, N'Vu Dinh Linh', N'123452319', 100000000)
SET IDENTITY_INSERT [dbo].[account_bank] OFF
GO
