<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

| Nghi ệ p v ụ   | Lo ạ i ch ỉ tiêu      | Hành độ ng   | API/Action       | Mô t ả chi ti ế t                                                                                                            | Phương pháp đo          | K ế t qu ả mong mu ố n                                                               | Ghi chú                                                                |
|----------------|-----------------------|--------------|------------------|------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Opportunity    | Ch ỉ tiêu ch ứ c năng | Xóa          | /crm/lead/add    | Xóa d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.     |
| Campaign       | Ch ỉ tiêu b ả om ậ t  | G ắ n th ẻ   | /crm/lead/export | G ắ n th ẻ d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ                  | Ki ể m th ử hi ệ u năng | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p                   | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|         |                       |              |                  | và ghi log đầ y đủ .                                                                                                            |                         | trướ c khi t ả i.                                                                |                                                                  |
|---------|-----------------------|--------------|------------------|---------------------------------------------------------------------------------------------------------------------------------|-------------------------|----------------------------------------------------------------------------------|------------------------------------------------------------------|
| Contact | Ch ỉ tiêu hi ệu năng  | Xóa          | /crm/lead/export | Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .        | Ki ể m th ử hi ệ u năng | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch. | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.          |
| Contact | Ch ỉ tiêu ch ứ c năng | G ắ n th ẻ   | /crm/lead/export | G ắ n th ẻ d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch. | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày. |
| Contact | Ch ỉ tiêu hi ệu năng  | C ậ p nh ậ t | /crm/lead/add    | C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m                                                                            | Ki ể m th ử b ả o m ậ t | Không l ỗ i, log đầy đủ trong                                                    | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.          |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|         |                       |               |                      | validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                             |                         | AuditLog, SLA đáp ứ ng 99.99%.                                                   |                                                                     |
|---------|-----------------------|---------------|----------------------|--------------------------------------------------------------------------------------------------------------------------|-------------------------|----------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Contact | Ch ỉ tiêu hi ệu năng  | Xóa           | /crm/campaign/import | Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.     | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |
| Contact | Ch ỉ tiêu ch ứ c năng | Chuy ể n đổ i | /crm/lead/add        | Chuy ển đổ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ             | Ki ể m th ử b ả o m ậ t | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch. | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.             |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                      |               |                      | và ghi log đầ y đủ .                                                                                                            |                         |                                                                                      |                                                                        |
|-------------|----------------------|---------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Opportunity | Ch ỉ tiêu b ả om ậ t | Import        | /crm/campaign/import | Import d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.                |
| Lead        | Ch ỉ tiêu b ả om ậ t | Chuy ể n đổ i | /crm/campaign/import | Chuy ển đổ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .  | Ki ể m th ử ch ứ c năng | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Lead     | Ch ỉ tiêu ch ứ c năng   | Chuy ể n đổ i   | /crm/opportunity/delete   | Chuy ển đổ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .     | Ki ể m th ử ch ứ c năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.     | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.   |
|----------|-------------------------|-----------------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------|---------------------------|--------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| Campaign | Ch ỉ tiêu ch ứ c năng   | Chuy ể n đổ i   | /crm/campaign/import      | Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t   | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.  |
| Campaign | Ch ỉ tiêu hi ệu năng    | Export          | /crm/contact/update       | Export d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý                                               | Ki ể m th ử hi ệ u năng   | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng                            | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.              |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                      |              |                     | logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                             |                         | b ộ sang h ệ th ố ng Billing.                                                           |                                                                        |
|-------------|----------------------|--------------|---------------------|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Opportunity | Ch ỉ tiêu hi ệu năng | G ắ n th ẻ   | /crm/contact/update | G ắ n th ẻ d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Campaign    | Ch ỉ tiêu hi ệu năng | C ậ p nh ậ t | /crm/contact/update | C ậ p nh ậ t d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .  | Ki ể m th ử hi ệ u năng | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                            | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.       |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Lead        | Ch ỉ tiêu ch ứ c năng   | Chuy ể n đổ i   | /crm/contact/update     | Chuy ển đổ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .    | Ki ể m th ử b ả o m ậ t   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.   | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.   |
|-------------|-------------------------|-----------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------|------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| Contact     | Ch ỉ tiêu ch ứ c năng   | Chuy ể n đổ i   | /crm/lead/add           | Chuy ển đổ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t   | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.       | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.     |
| Opportunity | Ch ỉ tiêu b ả om ậ t    | Import          | /crm/opportunity/delete | Import d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý                                           | Ki ể m th ử b ả o m ậ t   | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c                           | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.     |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                      |     |                     | logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                   |                         | hai l ớ p trướ c khi t ả i.                                                  |                                                                  |
|----------|----------------------|-----|---------------------|---------------------------------------------------------------------------------------------------------------------------|-------------------------|------------------------------------------------------------------------------|------------------------------------------------------------------|
| Campaign | Ch ỉ tiêu hi ệu năng | Xóa | /crm/contact/update | Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i. | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày. |
| Campaign | Ch ỉ tiêu b ả om ậ t | Xóa | /crm/lead/export    | Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                 | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.          |

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

<!-- image -->

| Campaign    | Ch ỉ tiêu ch ứ c năng   | Xóa        | /crm/opportunity/delete   | Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .       | Ki ể m th ử hi ệ u năng   | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.   | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.   |
|-------------|-------------------------|------------|---------------------------|---------------------------------------------------------------------------------------------------------------------------------|---------------------------|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Opportunity | Ch ỉ tiêu b ả om ậ t    | Import     | /crm/lead/add             | Import d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng   | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.   | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.       |
| Contact     | Ch ỉ tiêu ch ứ c năng   | G ắ n th ẻ | /crm/lead/add             | G ắ n th ẻ d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý                                         | Ki ể m th ử hi ệ u năng   | Không l ỗ i, log đầy đủ trong AuditLog,                                                | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.                  |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                      |               |                      | logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                               |                         | SLA đáp ứ ng 99.99%.                                                             |                                                                        |
|-------------|----------------------|---------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------|----------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Opportunity | Ch ỉ tiêu hi ệu năng | Chuy ể n đổ i | /crm/campaign/import | Chuy ển đổ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.     | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Campaign    | Ch ỉ tiêu b ả om ậ t | Import        | /crm/campaign/import | Import d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .          | Ki ể m th ử ch ứ c năng | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch. | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Lead        | Ch ỉ tiêu hi ệu năng   | Thêm m ớ i    | /crm/contact/update     | Thêmm ớ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .        | Ki ể m th ử hi ệ u năng   | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                            | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.   |
|-------------|------------------------|---------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|---------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Campaign    | Ch ỉ tiêu hi ệu năng   | Chuy ể n đổ i | /crm/opportunity/delete | Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng   | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng. |
| Opportunity | Ch ỉ tiêu b ả om ậ t   | C ậ p nh ậ t  | /crm/lead/export        | C ậ p nh ậ t d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u                                                       | Ki ể m th ử ch ứ c năng   | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp                                         | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.   |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                       |            |                  | đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                         |                         | ứ ng 99.99%.                                                                         |                                                                        |
|----------|-----------------------|------------|------------------|----------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Lead     | Ch ỉ tiêu ch ứ c năng | Export     | /crm/lead/export | Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .         | Ki ể m th ử ch ứ c năng | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                         | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.       |
| Campaign | Ch ỉ tiêu hi ệu năng  | G ắ n th ẻ | /crm/lead/export | G ắ n th ẻ d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Contact   | Ch ỉ tiêu ch ứ c năng   | G ắ n th ẻ   | /crm/contact/update   | G ắ n th ẻ d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử ch ứ c năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.     | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.   |
|-----------|-------------------------|--------------|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Lead      | Ch ỉ tiêu ch ứ c năng   | G ắ n th ẻ   | /crm/contact/update   | G ắ n th ẻ d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .      | Ki ể m th ử ch ứ c năng   | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.                  |
| Lead      | Ch ỉ tiêu b ả om ậ t    | Xóa          | /crm/lead/add         | Xóa d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ                                  | Ki ể m th ử ch ứ c năng   | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s,                                    | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.                  |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|         |                      |              |                         | và ghi log đầ y đủ .                                                                                                              |                         | t ự độ ng retry khi l ỗ i.                                                       |                                                                        |
|---------|----------------------|--------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------|-------------------------|----------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Contact | Ch ỉ tiêu b ả om ậ t | Import       | /crm/opportunity/delete | Import d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .       | Ki ể m th ử hi ệ u năng | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch. | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.       |
| Contact | Ch ỉ tiêu hi ệu năng | C ậ p nh ậ t | /crm/lead/add           | C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                     | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Lead        | Ch ỉ tiêu b ả om ậ t   | Chuy ể n đổ i   | /crm/opportunity/delete   | Chuy ển đổ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử ch ứ c năng   | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                            | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.             |
|-------------|------------------------|-----------------|---------------------------|----------------------------------------------------------------------------------------------------------------------------------|---------------------------|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Lead        | Ch ỉ tiêu hi ệu năng   | Thêm m ớ i      | /crm/lead/add             | Thêmm ớ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .      | Ki ể m th ử ch ứ c năng   | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.    |
| Opportunity | Ch ỉ tiêu ch ứ c năng  | Export          | /crm/contact/update       | Export d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý                                          | Ki ể m th ử hi ệ u năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng                              | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                      |               |                         | logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                           |                         | rollback giao d ị ch.                                                                   |                                                                    |
|-------------|----------------------|---------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Contact     | Ch ỉ tiêu b ả om ậ t | Chuy ể n đổ i | /crm/lead/add           | Chuy ển đổ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.    | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.            |
| Opportunity | Ch ỉ tiêu hi ệu năng | Import        | /crm/opportunity/delete | Import d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử b ả o m ậ t | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng. |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Campaign   | Ch ỉ tiêu b ả om ậ t   | Xóa           | /crm/campaign/import   | Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .          | Ki ể m th ử b ả o m ậ t   | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.            | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.    |
|------------|------------------------|---------------|------------------------|------------------------------------------------------------------------------------------------------------------------------------|---------------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Campaign   | Ch ỉ tiêu hi ệu năng   | C ậ p nh ậ t  | /crm/campaign/import   | C ậ p nh ậ t d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t   | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Campaign   | Ch ỉ tiêu b ả om ậ t   | Chuy ể n đổ i | /crm/lead/export       | Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u                                                          | Ki ể m th ử b ả o m ậ t   | Đồ ng b ộ d ữ li ệ u sang DataLake trong                                                | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.     |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                      |               |                         | đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                           |                         | vòng 5s, t ự độ ng retry khi l ỗ i.                                              |                                                                        |
|-------------|----------------------|---------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|-------------------------|----------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Campaign    | Ch ỉ tiêu hi ệu năng | Chuy ể n đổ i | /crm/opportunity/delete | Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch. | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Opportunity | Ch ỉ tiêu hi ệu năng | Xóa           | /crm/campaign/import    | Xóa d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .       | Ki ể m th ử b ả o m ậ t | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                     | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.    |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

| Contact     | Ch ỉ tiêu b ả om ậ t   | Thêm m ớ i   | /crm/lead/add           | Thêmm ớ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử b ả o m ậ t   | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                            | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.                |
|-------------|------------------------|--------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------|---------------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Campaign    | Ch ỉ tiêu ch ứ c năng  | Import       | /crm/opportunity/delete | Import d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .     | Ki ể m th ử b ả o m ậ t   | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.     |
| Opportunity | Ch ỉ tiêu ch ứ c năng  | C ậ p nh ậ t | /crm/lead/add           | C ậ p nh ậ t d ữ li ệ u Opportunity trong CRM, bao g ồ m                                                                         | Ki ể m th ử hi ệ u năng   | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có                                           | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                       |        |                         | validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                              |                         | xác th ự c hai l ớ p trướ c khi t ả i.                                           |                                                                     |
|-------------|-----------------------|--------|-------------------------|---------------------------------------------------------------------------------------------------------------------------|-------------------------|----------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Campaign    | Ch ỉ tiêu ch ứ c năng | Xóa    | /crm/contact/update     | Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch. | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.  |
| Opportunity | Ch ỉ tiêu hi ệu năng  | Import | /crm/opportunity/delete | Import d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ                | Ki ể m th ử ch ứ c năng | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch. | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

|             |                       |               |                         | và ghi log đầ y đủ .                                                                                                                  |                         |                                                                                         |                                                                     |
|-------------|-----------------------|---------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Contact     | Ch ỉ tiêu ch ứ c năng | C ậ p nh ậ t  | /crm/campaign/import    | C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .     | Ki ể m th ử ch ứ c năng | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |
| Opportunity | Ch ỉ tiêu ch ứ c năng | Chuy ể n đổ i | /crm/opportunity/delete | Chuy ển đổ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.        | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.             |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Contact   | Ch ỉ tiêu hi ệu năng   | Thêm m ớ i   | /crm/campaign/import    | Thêmm ớ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử ch ứ c năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.   | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.                |
|-----------|------------------------|--------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------|---------------------------|------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Contact   | Ch ỉ tiêu ch ứ c năng  | Thêm m ớ i   | /crm/contact/update     | Thêmm ớ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử ch ứ c năng   | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                       | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Campaign  | Ch ỉ tiêu hi ệu năng   | Xóa          | /crm/opportunity/delete | Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u                                                                 | Ki ể m th ử hi ệ u năng   | Đồ ng b ộ d ữ li ệ u sang DataLake trong                                           | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.       |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|         |                       |              |                      | đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                          |                         | vòng 5s, t ự độ ng retry khi l ỗ i.                                                  |                                                                  |
|---------|-----------------------|--------------|----------------------|-----------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------|------------------------------------------------------------------|
| Contact | Ch ỉ tiêu ch ứ c năng | G ắ n th ẻ   | /crm/campaign/import | G ắ n th ẻ d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử hi ệ u năng | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.          |
| Contact | Ch ỉ tiêu b ả om ậ t  | C ậ p nh ậ t | /crm/campaign/import | C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                         | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày. |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Opportunity   | Ch ỉ tiêu hi ệu năng   | G ắ n th ẻ   | /crm/contact/update   | G ắ n th ẻ d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử b ả o m ậ t   | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                         | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.                |
|---------------|------------------------|--------------|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------|---------------------------|--------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Lead          | Ch ỉ tiêu b ả om ậ t   | G ắ n th ẻ   | /crm/campaign/import  | G ắ n th ẻ d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .          | Ki ể m th ử hi ệ u năng   | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Lead          | Ch ỉ tiêu hi ệu năng   | Xóa          | /crm/lead/add         | Xóa d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý                                                         | Ki ể m th ử b ả o m ậ t   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng                           | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                       |               |                         | logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                        |                         | rollback giao d ị ch.                                                            |                                                                     |
|----------|-----------------------|---------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------|-------------------------|----------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Lead     | Ch ỉ tiêu hi ệu năng  | G ắ n th ẻ    | /crm/contact/update     | G ắ n th ẻ d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử hi ệ u năng | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                     | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |
| Lead     | Ch ỉ tiêu ch ứ c năng | Chuy ể n đổ i | /crm/opportunity/delete | Chuy ển đổ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch. | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |
| Campaign | Ch ỉ tiêu hi ệu năng  | G ắ n th ẻ    | /crm/opportunity/delete | G ắ n th ẻ d ữ li ệ u Campaign trong CRM,                                                                                      | Ki ể m th ử             | C ả nh báo n ế u thi ế u trườ ng                                                 | D ữ li ệu đượ c backup hàng ngày,                                   |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                       |               |                         | bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                             | hi ệ u năng             | b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.                                      | lưu giữ t ố i thi ể u 30 ngày.                                     |
|----------|-----------------------|---------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Campaign | Ch ỉ tiêu hi ệu năng  | Chuy ể n đổ i | /crm/opportunity/delete | Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.            |
| Campaign | Ch ỉ tiêu ch ứ c năng | C ậ p nh ậ t  | /crm/lead/add           | C ậ p nh ậ t d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ                      | Ki ể m th ử b ả o m ậ t | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang                   | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                      |              |                         | và ghi log đầ y đủ .                                                                                                              |                         | h ệ th ố ng Billing.                                                                 |                                                                     |
|----------|----------------------|--------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Campaign | Ch ỉ tiêu hi ệu năng | Xóa          | /crm/opportunity/delete | Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .         | Ki ể m th ử b ả o m ậ t | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.             |
| Contact  | Ch ỉ tiêu hi ệu năng | C ậ p nh ậ t | /crm/lead/add           | C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Contact   | Ch ỉ tiêu ch ứ c năng   | Xóa        | /crm/lead/export        | Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .        | Ki ể m th ử b ả o m ậ t   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.     | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.             |
|-----------|-------------------------|------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------|---------------------------|--------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Contact   | Ch ỉ tiêu hi ệu năng    | G ắ n th ẻ | /crm/lead/add           | G ắ n th ẻ d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng   | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.  |
| Lead      | Ch ỉ tiêu ch ứ c năng   | G ắ n th ẻ | /crm/opportunity/delete | G ắ n th ẻ d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ                         | Ki ể m th ử hi ệ u năng   | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s,                                    | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                       |              |                     | và ghi log đầ y đủ .                                                                                                               |                         | t ự độ ng retry khi l ỗ i.                                                              |                                                                        |
|-------------|-----------------------|--------------|---------------------|------------------------------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Opportunity | Ch ỉ tiêu hi ệu năng  | Thêm m ớ i   | /crm/contact/update | Thêmm ớ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                            | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Contact     | Ch ỉ tiêu ch ứ c năng | C ậ p nh ậ t | /crm/lead/add       | C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .  | Ki ể m th ử b ả o m ậ t | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.       |

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

<!-- image -->

| Opportunity   | Ch ỉ tiêu b ả om ậ t   | Export     | /crm/lead/export    | Export d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử ch ứ c năng   | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.   | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.   |
|---------------|------------------------|------------|---------------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------|--------------------------------------------------------------------------------|----------------------------------------------------------------------|
| Opportunity   | Ch ỉ tiêu hi ệu năng   | Export     | /crm/lead/add       | Export d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử hi ệ u năng   | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                   | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.              |
| Lead          | Ch ỉ tiêu ch ứ c năng  | Thêm m ớ i | /crm/contact/update | Thêmm ớ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý                                               | Ki ể m th ử hi ệ u năng   | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ                                  | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.   |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|      |                       |            |                      | logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                      |                         | li ệu đồ ng b ộ sang h ệ th ố ng Billing.                                            |                                                                     |
|------|-----------------------|------------|----------------------|------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Lead | Ch ỉ tiêu b ả om ậ t  | G ắ n th ẻ | /crm/campaign/import | G ắ n th ẻ d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.         | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.    |
| Lead | Ch ỉ tiêu ch ứ c năng | Export     | /crm/lead/export     | Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .     | Ki ể m th ử hi ệ u năng | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Contact     | Ch ỉ tiêu hi ệu năng   | C ậ p nh ậ t   | /crm/lead/export        | C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử hi ệ u năng   | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.   | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.   |
|-------------|------------------------|----------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Opportunity | Ch ỉ tiêu hi ệu năng   | Import         | /crm/lead/export        | Import d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .     | Ki ể m th ử ch ứ c năng   | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.   | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.      |
| Contact     | Ch ỉ tiêu ch ứ c năng  | G ắ n th ẻ     | /crm/opportunity/delete | G ắ n th ẻ d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý                                             | Ki ể m th ử ch ứ c năng   | Không l ỗ i, log đầy đủ trong AuditLog,                                                   | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.   |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|      |                       |            |                         | logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                      |                         | SLA đáp ứ ng 99.99%.                                                                    |                                                                    |
|------|-----------------------|------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Lead | Ch ỉ tiêu ch ứ c năng | G ắ n th ẻ | /crm/opportunity/delete | G ắ n th ẻ d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng. |
| Lead | Ch ỉ tiêu b ả om ậ t  | Export     | /crm/lead/export        | Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .     | Ki ể m th ử hi ệ u năng | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.    | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.            |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Contact   | Ch ỉ tiêu ch ứ c năng   | Thêm m ớ i   | /crm/campaign/import    | Thêmm ớ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử hi ệ u năng   | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.         | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.    |
|-----------|-------------------------|--------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------|---------------------------|--------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Lead      | Ch ỉ tiêu hi ệu năng    | Xóa          | /crm/opportunity/delete | Xóa d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .            | Ki ể m th ử ch ứ c năng   | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Campaign  | Ch ỉ tiêu hi ệu năng    | Xóa          | /crm/lead/add           | Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u                                                                 | Ki ể m th ử ch ứ c năng   | Đồ ng b ộ d ữ li ệ u sang DataLake trong                                             | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.     |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                      |        |                      | đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                     |                         | vòng 5s, t ự độ ng retry khi l ỗ i.                                              |                                                                        |
|----------|----------------------|--------|----------------------|------------------------------------------------------------------------------------------------------------------------------|-------------------------|----------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Lead     | Ch ỉ tiêu hi ệu năng | Export | /crm/campaign/import | Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .     | Ki ể m th ử hi ệ u năng | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch. | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Campaign | Ch ỉ tiêu hi ệu năng | Import | /crm/contact/update  | Import d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.     | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.    |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

| Opportunity   | Ch ỉ tiêu ch ứ c năng   | Thêm m ớ i   | /crm/lead/export        | Thêmm ớ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử ch ứ c năng   | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.   | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.       |
|---------------|-------------------------|--------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Opportunity   | Ch ỉ tiêu hi ệu năng    | Xóa          | /crm/campaign/import    | Xóa d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .         | Ki ể m th ử hi ệ u năng   | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.      | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Contact       | Ch ỉ tiêu ch ứ c năng   | Xóa          | /crm/opportunity/delete | Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u                                                                      | Ki ể m th ử               | Thành công v ớ i th ờ i gian x ử lý <                                                     | D ữ li ệu đượ c backup hàng ngày,                                      |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                      |        |                     | đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                    | hi ệ u năng             | 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.                                    | lưu giữ t ố i thi ể u 30 ngày.                                         |
|-------------|----------------------|--------|---------------------|-----------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Contact     | Ch ỉ tiêu b ả om ậ t | Import | /crm/lead/export    | Import d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.    |
| Opportunity | Ch ỉ tiêu b ả om ậ t | Import | /crm/contact/update | Import d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ                  | Ki ể m th ử b ả o m ậ t | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.     | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                       |              |                     | và ghi log đầ y đủ .                                                                                                               |                         |                                                                                      |                                                                    |
|----------|-----------------------|--------------|---------------------|------------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Lead     | Ch ỉ tiêu ch ứ c năng | Export       | /crm/contact/update | Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .           | Ki ể m th ử b ả o m ậ t | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng. |
| Campaign | Ch ỉ tiêu hi ệu năng  | C ậ p nh ậ t | /crm/lead/export    | C ậ p nh ậ t d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.     | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.   |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Opportunity   | Ch ỉ tiêu ch ứ c năng   | Thêm m ớ i   | /crm/contact/update     | Thêmm ớ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử hi ệ u năng   | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                     | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.   |
|---------------|-------------------------|--------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------|---------------------------|----------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Opportunity   | Ch ỉ tiêu ch ứ c năng   | Export       | /crm/contact/update     | Export d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .      | Ki ể m th ử hi ệ u năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch. | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.    |
| Contact       | Ch ỉ tiêu hi ệu năng    | Xóa          | /crm/opportunity/delete | Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u                                                                      | Ki ể m th ử               | Thành công v ớ i th ờ i gian x ử lý <                                            | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.               |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|      |                      |               |                         | đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                       | ch ứ c năng             | 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.                            |                                                                     |
|------|----------------------|---------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------|-------------------------|------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Lead | Ch ỉ tiêu hi ệu năng | C ậ p nh ậ t  | /crm/opportunity/delete | C ậ p nh ậ t d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                 | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |
| Lead | Ch ỉ tiêu b ả om ậ t | Chuy ể n đổ i | /crm/lead/export        | Chuy ển đổ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i. | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.             |

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

<!-- image -->

| Campaign    | Ch ỉ tiêu b ả om ậ t   | Export       | /crm/lead/add           | Export d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .      | Ki ể m th ử ch ứ c năng   | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.   | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.    |
|-------------|------------------------|--------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Contact     | Ch ỉ tiêu ch ứ c năng  | C ậ p nh ậ t | /crm/lead/export        | C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.       | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.     |
| Opportunity | Ch ỉ tiêu b ả om ậ t   | G ắ n th ẻ   | /crm/opportunity/delete | G ắ n th ẻ d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u                                                        | Ki ể m th ử hi ệ u năng   | Không l ỗ i, log đầy đủ trong AuditLog,                                                | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                      |               |                         | đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                           |                         | SLA đáp ứ ng 99.99%.                                                                    |                                                                  |
|----------|----------------------|---------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------|
| Campaign | Ch ỉ tiêu hi ệu năng | Chuy ể n đổ i | /crm/contact/update     | Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.          |
| Campaign | Ch ỉ tiêu b ả om ậ t | Import        | /crm/opportunity/delete | Import d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .       | Ki ể m th ử b ả o m ậ t | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày. |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Campaign   | Ch ỉ tiêu hi ệu năng   | Thêm m ớ i   | /crm/opportunity/delete   | Thêmm ớ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử hi ệ u năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.   | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.    |
|------------|------------------------|--------------|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------|------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Contact    | Ch ỉ tiêu hi ệu năng   | Xóa          | /crm/campaign/import      | Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .          | Ki ể m th ử ch ứ c năng   | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.       | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |
| Campaign   | Ch ỉ tiêu b ả om ậ t   | Export       | /crm/lead/export          | Export d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u                                                               | Ki ể m th ử hi ệ u năng   | Đồ ng b ộ d ữ li ệ u sang DataLake trong                                           | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.  |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                       |            |                      | đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                            |                         | vòng 5s, t ự độ ng retry khi l ỗ i.                                              |                                                                    |
|-------------|-----------------------|------------|----------------------|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------|----------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Opportunity | Ch ỉ tiêu ch ứ c năng | G ắ n th ẻ | /crm/lead/add        | G ắ n th ẻ d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                     | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.   |
| Contact     | Ch ỉ tiêu b ả om ậ t  | G ắ n th ẻ | /crm/campaign/import | G ắ n th ẻ d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .     | Ki ể m th ử ch ứ c năng | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch. | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng. |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Lead    | Ch ỉ tiêu hi ệu năng   | C ậ p nh ậ t   | /crm/contact/update     | C ậ p nh ậ t d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử hi ệ u năng   | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.   | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.   |
|---------|------------------------|----------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Lead    | Ch ỉ tiêu hi ệu năng   | Import         | /crm/lead/export        | Import d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .         | Ki ể m th ử b ả o m ậ t   | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.      | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.            |
| Contact | Ch ỉ tiêu ch ứ c năng  | Export         | /crm/opportunity/delete | Export d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý                                              | Ki ể m th ử b ả o m ậ t   | Không l ỗ i, log đầy đủ trong AuditLog,                                                   | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|         |                       |        |                  | logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                  |                         | SLA đáp ứ ng 99.99%.                                                                    |                                                                        |
|---------|-----------------------|--------|------------------|--------------------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Contact | Ch ỉ tiêu b ả om ậ t  | Xóa    | /crm/lead/add    | Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.    | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Lead    | Ch ỉ tiêu ch ứ c năng | Export | /crm/lead/export | Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.     |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Lead    | Ch ỉ tiêu b ả om ậ t   | C ậ p nh ậ t   | /crm/contact/update     | C ậ p nh ậ t d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử hi ệ u năng   | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.     | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.   |
|---------|------------------------|----------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------|---------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------|
| Lead    | Ch ỉ tiêu b ả om ậ t   | C ậ p nh ậ t   | /crm/lead/add           | C ậ p nh ậ t d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử ch ứ c năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch. | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.  |
| Contact | Ch ỉ tiêu b ả om ậ t   | Thêm m ớ i     | /crm/opportunity/delete | Thêmm ớ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý                                           | Ki ể m th ử ch ứ c năng   | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c                         | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.     |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                      |               |               | logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                            |                         | hai l ớ p trướ c khi t ả i.                                                      |                                                                     |
|----------|----------------------|---------------|---------------|------------------------------------------------------------------------------------------------------------------------------------|-------------------------|----------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Campaign | Ch ỉ tiêu hi ệu năng | Chuy ể n đổ i | /crm/lead/add | Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch. | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.  |
| Contact  | Ch ỉ tiêu hi ệu năng | Thêm m ớ i    | /crm/lead/add | Thêmm ớ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .     | Ki ể m th ử b ả o m ậ t | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch. | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Contact   | Ch ỉ tiêu ch ứ c năng   | Export        | /crm/opportunity/delete   | Export d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử ch ứ c năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.        | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.       |
|-----------|-------------------------|---------------|---------------------------|-------------------------------------------------------------------------------------------------------------------------------|---------------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Lead      | Ch ỉ tiêu b ả om ậ t    | Import        | /crm/opportunity/delete   | Import d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .      | Ki ể m th ử ch ứ c năng   | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Campaign  | Ch ỉ tiêu b ả om ậ t    | Chuy ể n đổ i | /crm/lead/add             | Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý                                    | Ki ể m th ử hi ệ u năng   | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng                               | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.    |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                      |               |                      | logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                           |                         | b ộ sang h ệ th ố ng Billing.                                                        |                                                                    |
|----------|----------------------|---------------|----------------------|-----------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Campaign | Ch ỉ tiêu b ả om ậ t | Import        | /crm/campaign/import | Import d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .      | Ki ể m th ử hi ệ u năng | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.         | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng. |
| Contact  | Ch ỉ tiêu b ả om ậ t | Chuy ể n đổ i | /crm/lead/add        | Chuy ển đổ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.   |

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

<!-- image -->

| Opportunity   | Ch ỉ tiêu ch ứ c năng   | Xóa          | /crm/lead/add       | Xóa d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử ch ứ c năng   | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.     | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.    |
|---------------|-------------------------|--------------|---------------------|--------------------------------------------------------------------------------------------------------------------------------|---------------------------|----------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Contact       | Ch ỉ tiêu hi ệu năng    | Xóa          | /crm/contact/update | Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .       | Ki ể m th ử hi ệ u năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch. | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Opportunity   | Ch ỉ tiêu hi ệu năng    | C ậ p nh ậ t | /crm/lead/export    | C ậ p nh ậ t d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u                                                   | Ki ể m th ử ch ứ c năng   | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng                        | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.                |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|         |                      |        |                         | đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                    |                         | b ộ sang h ệ th ố ng Billing.                                                    |                                                         |
|---------|----------------------|--------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------|-------------------------|----------------------------------------------------------------------------------|---------------------------------------------------------|
| Contact | Ch ỉ tiêu b ả om ậ t | Import | /crm/lead/export        | Import d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch. | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel. |
| Lead    | Ch ỉ tiêu hi ệu năng | Export | /crm/opportunity/delete | Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .    | Ki ể m th ử ch ứ c năng | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch. | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel. |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Lead        | Ch ỉ tiêu ch ứ c năng   | Thêm m ớ i   | /crm/campaign/import    | Thêmm ớ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .        | Ki ể m th ử hi ệ u năng   | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.   | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.   |
|-------------|-------------------------|--------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|---------------------------|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Campaign    | Ch ỉ tiêu b ả om ậ t    | C ậ p nh ậ t | /crm/campaign/import    | C ậ p nh ậ t d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng   | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                           | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.   |
| Opportunity | Ch ỉ tiêu hi ệu năng    | Export       | /crm/opportunity/delete | Export d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u                                                             | Ki ể m th ử b ả o m ậ t   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng                             | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.   |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|         |                       |              |                      | đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                          |                         | rollback giao d ị ch.                                                                   |                                                                    |
|---------|-----------------------|--------------|----------------------|-----------------------------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Contact | Ch ỉ tiêu b ả om ậ t  | C ậ p nh ậ t | /crm/contact/update  | C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.        | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng. |
| Contact | Ch ỉ tiêu ch ứ c năng | Import       | /crm/campaign/import | Import d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .       | Ki ể m th ử b ả o m ậ t | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.            |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

| Campaign   | Ch ỉ tiêu hi ệu năng   | Xóa        | /crm/campaign/import    | Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .       | Ki ể m th ử ch ứ c năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.   | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.   |
|------------|------------------------|------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------|---------------------------|------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Campaign   | Ch ỉ tiêu hi ệu năng   | Thêm m ớ i | /crm/lead/export        | Thêmm ớ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.   | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.               |
| Contact    | Ch ỉ tiêu hi ệu năng   | Thêm m ớ i | /crm/opportunity/delete | Thêmm ớ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u                                                           | Ki ể m th ử b ả o m ậ t   | Không l ỗ i, log đầy đủ trong AuditLog,                                            | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.      |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                       |               |                      | đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                           |                         | SLA đáp ứ ng 99.99%.                                                                 |                                                                     |
|-------------|-----------------------|---------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Opportunity | Ch ỉ tiêu hi ệu năng  | Import        | /crm/lead/add        | Import d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .    | Ki ể m th ử b ả o m ậ t | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |
| Campaign    | Ch ỉ tiêu ch ứ c năng | Chuy ể n đổ i | /crm/campaign/import | Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.     | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.    |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Lead        | Ch ỉ tiêu hi ệu năng   | C ậ p nh ậ t   | /crm/contact/update   | C ậ p nh ậ t d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .    | Ki ể m th ử ch ứ c năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.   | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.   |
|-------------|------------------------|----------------|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------|------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| Contact     | Ch ỉ tiêu ch ứ c năng  | Chuy ể n đổ i  | /crm/lead/add         | Chuy ển đổ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng   | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.       | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.   |
| Opportunity | Ch ỉ tiêu b ả om ậ t   | Xóa            | /crm/campaign/import  | Xóa d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý                                              | Ki ể m th ử b ả o m ậ t   | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c                           | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.  |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                      |        |                         | logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                      |                         | hai l ớ p trướ c khi t ả i.                                                  |                                                                        |
|----------|----------------------|--------|-------------------------|------------------------------------------------------------------------------------------------------------------------------|-------------------------|------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Campaign | Ch ỉ tiêu b ả om ậ t | Export | /crm/lead/add           | Export d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i. | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Contact  | Ch ỉ tiêu b ả om ậ t | Export | /crm/opportunity/delete | Export d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .  | Ki ể m th ử hi ệ u năng | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i. | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Opportunity   | Ch ỉ tiêu ch ứ c năng   | Xóa    | /crm/contact/update     | Xóa d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử ch ứ c năng   | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.   | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.   |
|---------------|-------------------------|--------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------|---------------------------|--------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Contact       | Ch ỉ tiêu hi ệu năng    | Import | /crm/opportunity/delete | Import d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .    | Ki ể m th ử ch ứ c năng   | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.   | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.    |
| Contact       | Ch ỉ tiêu hi ệu năng    | Xóa    | /crm/lead/export        | Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý                                               | Ki ể m th ử ch ứ c năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng                     | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.    |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                       |            |                         | logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                            |                         | rollback giao d ị ch.                                                                   |                                                                    |
|-------------|-----------------------|------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Opportunity | Ch ỉ tiêu b ả om ậ t  | Thêm m ớ i | /crm/campaign/import    | Thêmm ớ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng. |
| Contact     | Ch ỉ tiêu ch ứ c năng | Import     | /crm/opportunity/delete | Import d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .        | Ki ể m th ử b ả o m ậ t | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.            | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

| Lead    | Ch ỉ tiêu hi ệu năng   | Thêm m ớ i    | /crm/lead/add    | Thêmm ớ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .     | Ki ể m th ử b ả o m ậ t   | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.   | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.   |
|---------|------------------------|---------------|------------------|---------------------------------------------------------------------------------------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| Contact | Ch ỉ tiêu hi ệu năng   | G ắ n th ẻ    | /crm/lead/add    | G ắ n th ẻ d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.          | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.  |
| Contact | Ch ỉ tiêu hi ệu năng   | Chuy ể n đổ i | /crm/lead/export | Chuy ển đổ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý                                       | Ki ể m th ử ch ứ c năng   | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c                                  | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.   |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                      |        |                         | logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                      |                         | hai l ớ p trướ c khi t ả i.                                                  |                                                                     |
|----------|----------------------|--------|-------------------------|------------------------------------------------------------------------------------------------------------------------------|-------------------------|------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Campaign | Ch ỉ tiêu b ả om ậ t | Import | /crm/opportunity/delete | Import d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                 | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |
| Lead     | Ch ỉ tiêu hi ệu năng | Xóa    | /crm/lead/add           | Xóa d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .        | Ki ể m th ử b ả o m ậ t | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i. | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.  |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

| Lead     | Ch ỉ tiêu b ả om ậ t   | Chuy ể n đổ i   | /crm/lead/add        | Chuy ển đổ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử b ả o m ậ t   | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                            | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.                |
|----------|------------------------|-----------------|----------------------|----------------------------------------------------------------------------------------------------------------------------------|---------------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Lead     | Ch ỉ tiêu ch ứ c năng  | C ậ p nh ậ t    | /crm/campaign/import | C ậ p nh ậ t d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử b ả o m ậ t   | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.     |
| Campaign | Ch ỉ tiêu ch ứ c năng  | C ậ p nh ậ t    | /crm/contact/update  | C ậ p nh ậ t d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý                                       | Ki ể m th ử hi ệ u năng   | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp                                         | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                       |            |                     | logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                            |                         | ứ ng 99.99%.                                                                         |                                                                     |
|-------------|-----------------------|------------|---------------------|------------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Opportunity | Ch ỉ tiêu hi ệu năng  | Thêm m ớ i | /crm/contact/update | Thêmm ớ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.  |
| Campaign    | Ch ỉ tiêu ch ứ c năng | G ắ n th ẻ | /crm/lead/add       | G ắ n th ẻ d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử hi ệ u năng | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.         | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

| Lead        | Ch ỉ tiêu b ả om ậ t   | Xóa           | /crm/lead/export     | Xóa d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .             | Ki ể m th ử hi ệ u năng   | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.   | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.                |
|-------------|------------------------|---------------|----------------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Contact     | Ch ỉ tiêu b ả om ậ t   | C ậ p nh ậ t  | /crm/campaign/import | C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t   | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                           | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.     |
| Opportunity | Ch ỉ tiêu hi ệu năng   | Chuy ể n đổ i | /crm/campaign/import | Chuy ển đổ i d ữ li ệ u Opportunity trong CRM, bao g ồ m                                                                          | Ki ể m th ử hi ệ u năng   | Đồ ng b ộ d ữ li ệ u sang DataLake trong                                               | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|      |                       |              |                      | validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                   |                         | vòng 5s, t ự độ ng retry khi l ỗ i.                                          |                                                                        |
|------|-----------------------|--------------|----------------------|--------------------------------------------------------------------------------------------------------------------------------|-------------------------|------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Lead | Ch ỉ tiêu hi ệu năng  | C ậ p nh ậ t | /crm/campaign/import | C ậ p nh ậ t d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i. | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Lead | Ch ỉ tiêu ch ứ c năng | Export       | /crm/lead/export     | Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .       | Ki ể m th ử b ả o m ậ t | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng                  | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.       |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                       |               |                      |                                                                                                                              |                         | retry khi l ỗ i.                                                                 |                                                                        |
|----------|-----------------------|---------------|----------------------|------------------------------------------------------------------------------------------------------------------------------|-------------------------|----------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Contact  | Ch ỉ tiêu ch ứ c năng | Import        | /crm/campaign/import | Import d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .  | Ki ể m th ử ch ứ c năng | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                     | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.    |
| Campaign | Ch ỉ tiêu hi ệu năng  | Export        | /crm/lead/add        | Export d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch. | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Lead     | Ch ỉ tiêu hi ệu năng  | Chuy ể n đổ i | /crm/lead/add        | Chuy ển đổ i d ữ li ệ u Lead trong CRM, bao g ồ m                                                                            | Ki ể m th ử             | Xu ấ t báo cáo chi ti ết dướ i                                                   | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.                |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                       |               |                         | validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                          | ch ứ c năng             | d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.                                |                                                                  |
|-------------|-----------------------|---------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------|------------------------------------------------------------------|
| Opportunity | Ch ỉ tiêu hi ệu năng  | Chuy ể n đổ i | /crm/opportunity/delete | Chuy ển đổ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày. |
| Campaign    | Ch ỉ tiêu ch ứ c năng | Xóa           | /crm/contact/update     | Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ                                  | Ki ể m th ử ch ứ c năng | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang                   | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.          |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

|             |                      |               |                      | và ghi log đầ y đủ .                                                                                                                |                         | h ệ th ố ng Billing.                                                             |                                                                    |
|-------------|----------------------|---------------|----------------------|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------|----------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Contact     | Ch ỉ tiêu b ả om ậ t | Chuy ể n đổ i | /crm/campaign/import | Chuy ển đổ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử b ả o m ậ t | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.     | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.   |
| Opportunity | Ch ỉ tiêu b ả om ậ t | G ắ n th ẻ    | /crm/contact/update  | G ắ n th ẻ d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch. | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng. |
| Contact     | Ch ỉ tiêu b ả om ậ t | Thêm m ớ i    | /crm/campaign/import | Thêmm ớ i d ữ li ệ u Contact                                                                                                        | Ki ể m th ử             | C ả nh báo n ế u thi ế u                                                         | D ữ li ệu đượ c backup hàng ngày,                                  |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                      |            |                     | trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                              | hi ệ u năng             | trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.            | lưu giữ t ố i thi ể u 30 ngày.                                         |
|-------------|----------------------|------------|---------------------|--------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------|------------------------------------------------------------------------|
| Contact     | Ch ỉ tiêu b ả om ậ t | Thêm m ớ i | /crm/contact/update | Thêmm ớ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.       | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.    |
| Opportunity | Ch ỉ tiêu b ả om ậ t | Export     | /crm/contact/update | Export d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ                     | Ki ể m th ử b ả o m ậ t | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                       |            |                         | và ghi log đầ y đủ .                                                                                                           |                         | h ệ th ố ng Billing.                                                                 |                                                                        |
|----------|-----------------------|------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Contact  | Ch ỉ tiêu hi ệu năng  | Thêm m ớ i | /crm/opportunity/delete | Thêmm ớ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Campaign | Ch ỉ tiêu ch ứ c năng | Export     | /crm/lead/export        | Export d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử hi ệ u năng | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.     | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Lead     | Ch ỉ tiêu b ả om ậ t  | Import     | /crm/contact/update     | Import d ữ li ệ u Lead trong                                                                                                   | Ki ể m th ử             | C ả nh báo n ế u thi ế u                                                             | D ữ li ệu đượ c backup hàng ngày,                                      |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|      |                      |               |                  | CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                              | hi ệ u năng             | trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.                                 | lưu giữ t ố i thi ể u 30 ngày.                                      |
|------|----------------------|---------------|------------------|--------------------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Lead | Ch ỉ tiêu hi ệu năng | Import        | /crm/lead/export | Import d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |
| Lead | Ch ỉ tiêu b ả om ậ t | Chuy ể n đổ i | /crm/lead/export | Chuy ển đổ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ                | Ki ể m th ử hi ệ u năng | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp                                         | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.             |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|      |                      |              |                         | và ghi log đầ y đủ .                                                                                                           |                         | ứ ng 99.99%.                                                 |                                                                        |
|------|----------------------|--------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------|------------------------------------------------------------------------|
| Lead | Ch ỉ tiêu hi ệu năng | G ắ n th ẻ   | /crm/lead/add           | G ắ n th ẻ d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử ch ứ c năng | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%. | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Lead | Ch ỉ tiêu hi ệu năng | C ậ p nh ậ t | /crm/opportunity/delete | C ậ p nh ậ t d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%. | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.    |
| Lead | Ch ỉ tiêu b ả om ậ t | Export       | /crm/lead/export        | Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u                                                                | Ki ể m th ử hi ệ u năng | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c,               | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.     |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                       |        |                     | đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                     |                         | h ệ th ố ng rollback giao d ị ch.                                                       |                                                                     |
|----------|-----------------------|--------|---------------------|------------------------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Campaign | Ch ỉ tiêu b ả om ậ t  | Xóa    | /crm/contact/update | Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .    | Ki ể m th ử ch ứ c năng | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.        | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.             |
| Campaign | Ch ỉ tiêu ch ứ c năng | Export | /crm/lead/export    | Export d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Contact   | Ch ỉ tiêu ch ứ c năng   | Import     | /crm/campaign/import   | Import d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử hi ệ u năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.   | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.   |
|-----------|-------------------------|------------|------------------------|-------------------------------------------------------------------------------------------------------------------------------|---------------------------|------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Lead      | Ch ỉ tiêu hi ệu năng    | Thêm m ớ i | /crm/lead/export       | Thêmm ớ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử ch ứ c năng   | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.       | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.         |
| Campaign  | Ch ỉ tiêu hi ệu năng    | G ắ n th ẻ | /crm/lead/export       | G ắ n th ẻ d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý                                      | Ki ể m th ử hi ệ u năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng                         | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.       |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                       |               |                      | logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                            |                         | rollback giao d ị ch.                                                                   |                                                                    |
|----------|-----------------------|---------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Lead     | Ch ỉ tiêu ch ứ c năng | Export        | /crm/campaign/import | Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .           | Ki ể m th ử hi ệ u năng | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng. |
| Campaign | Ch ỉ tiêu hi ệu năng  | Chuy ể n đổ i | /crm/lead/export     | Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.    | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng. |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Contact     | Ch ỉ tiêu ch ứ c năng   | Thêm m ớ i   | /crm/contact/update   | Thêmm ớ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .        | Ki ể m th ử hi ệ u năng   | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.    | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.   |
|-------------|-------------------------|--------------|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------|---------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Opportunity | Ch ỉ tiêu b ả om ậ t    | C ậ p nh ậ t | /crm/contact/update   | C ậ p nh ậ t d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng   | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.               |
| Campaign    | Ch ỉ tiêu b ả om ậ t    | Xóa          | /crm/lead/export      | Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m                                                                                          | Ki ể m th ử b ả o m ậ t   | Đồ ng b ộ d ữ li ệ u sang DataLake                                                      | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.    |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                      |               |                      | validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                             |                         | trong vòng 5s, t ự độ ng retry khi l ỗ i.                                    |                                                                    |
|----------|----------------------|---------------|----------------------|--------------------------------------------------------------------------------------------------------------------------|-------------------------|------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Contact  | Ch ỉ tiêu b ả om ậ t | Xóa           | /crm/lead/export     | Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i. | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.   |
| Campaign | Ch ỉ tiêu b ả om ậ t | Chuy ể n đổ i | /crm/campaign/import | Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ            | Ki ể m th ử b ả o m ậ t | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang           | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                      |              |                      | và ghi log đầ y đủ .                                                                                                                  |                         | h ệ th ố ng Billing.                                                                    |                                                                  |
|-------------|----------------------|--------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------|
| Campaign    | Ch ỉ tiêu b ả om ậ t | Thêm m ớ i   | /crm/campaign/import | Thêmm ớ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .       | Ki ể m th ử hi ệ u năng | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                            | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày. |
| Opportunity | Ch ỉ tiêu hi ệu năng | C ậ p nh ậ t | /crm/campaign/import | C ậ p nh ậ t d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày. |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Contact   | Ch ỉ tiêu ch ứ c năng   | C ậ p nh ậ t   | /crm/opportunity/delete   | C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử hi ệ u năng   | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.         | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.       |
|-----------|-------------------------|----------------|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------|---------------------------|--------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Campaign  | Ch ỉ tiêu ch ứ c năng   | Xóa            | /crm/campaign/import      | Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .           | Ki ể m th ử b ả o m ậ t   | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Campaign  | Ch ỉ tiêu hi ệu năng    | G ắ n th ẻ     | /crm/lead/export          | G ắ n th ẻ d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u                                                             | Ki ể m th ử hi ệ u năng   | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ                                        | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                       |               |               | đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                            |                         | li ệu đồ ng b ộ sang h ệ th ố ng Billing.                                        |                                                         |
|-------------|-----------------------|---------------|---------------|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------|----------------------------------------------------------------------------------|---------------------------------------------------------|
| Campaign    | Ch ỉ tiêu ch ứ c năng | Chuy ể n đổ i | /crm/lead/add | Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .  | Ki ể m th ử hi ệ u năng | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch. | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel. |
| Opportunity | Ch ỉ tiêu hi ệu năng  | G ắ n th ẻ    | /crm/lead/add | G ắ n th ẻ d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch. | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel. |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Contact   | Ch ỉ tiêu b ả om ậ t   | Import     | /crm/lead/add        | Import d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .     | Ki ể m th ử b ả o m ậ t   | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.   | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.    |
|-----------|------------------------|------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Campaign  | Ch ỉ tiêu b ả om ậ t   | Thêm m ớ i | /crm/campaign/import | Thêmm ớ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng   | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                              | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.    |
| Contact   | Ch ỉ tiêu hi ệu năng   | Xóa        | /crm/lead/add        | Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý                                                | Ki ể m th ử b ả o m ậ t   | Đồ ng b ộ d ữ li ệ u sang DataLake trong                                                  | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                       |               |                      | logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                            |                         | vòng 5s, t ự độ ng retry khi l ỗ i.                                                     |                                                                     |
|----------|-----------------------|---------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Campaign | Ch ỉ tiêu ch ứ c năng | Chuy ể n đổ i | /crm/lead/export     | Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.    | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.    |
| Lead     | Ch ỉ tiêu hi ệu năng  | Xóa           | /crm/campaign/import | Xóa d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .              | Ki ể m th ử ch ứ c năng | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

| Lead     | Ch ỉ tiêu hi ệu năng   | Xóa    | /crm/contact/update   | Xóa d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .        | Ki ể m th ử ch ứ c năng   | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.            | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.   |
|----------|------------------------|--------|-----------------------|------------------------------------------------------------------------------------------------------------------------------|---------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Campaign | Ch ỉ tiêu hi ệu năng   | Export | /crm/lead/add         | Export d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t   | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.   |
| Lead     | Ch ỉ tiêu ch ứ c năng  | Export | /crm/lead/add         | Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý                                             | Ki ể m th ử b ả o m ậ t   | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ                                           | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                       |               |                      | logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                            |                         | li ệu đồ ng b ộ sang h ệ th ố ng Billing.                                            |                                                                        |
|-------------|-----------------------|---------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Campaign    | Ch ỉ tiêu ch ứ c năng | Chuy ể n đổ i | /crm/lead/add        | Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                         | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Opportunity | Ch ỉ tiêu ch ứ c năng | Chuy ể n đổ i | /crm/campaign/import | Chuy ển đổ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ                   | Ki ể m th ử b ả o m ậ t | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.                |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                      |              |                         | và ghi log đầ y đủ .                                                                                                                  |                         |                                                                              |                                                                     |
|-------------|----------------------|--------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------|------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Opportunity | Ch ỉ tiêu b ả om ậ t | C ậ p nh ậ t | /crm/opportunity/delete | C ậ p nh ậ t d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i. | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.  |
| Campaign    | Ch ỉ tiêu b ả om ậ t | G ắ n th ẻ   | /crm/campaign/import    | G ắ n th ẻ d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .      | Ki ể m th ử b ả o m ậ t | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                 | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Campaign   | Ch ỉ tiêu hi ệu năng   | C ậ p nh ậ t   | /crm/campaign/import   | C ậ p nh ậ t d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử b ả o m ậ t   | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.   | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.   |
|------------|------------------------|----------------|------------------------|--------------------------------------------------------------------------------------------------------------------------------------|---------------------------|--------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Lead       | Ch ỉ tiêu ch ứ c năng  | Import         | /crm/campaign/import   | Import d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .             | Ki ể m th ử ch ứ c năng   | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                   | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.               |
| Contact    | Ch ỉ tiêu b ả om ậ t   | Import         | /crm/lead/export       | Import d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ                               | Ki ể m th ử hi ệ u năng   | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c                       | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.   |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|      |                       |              |                  | và ghi log đầ y đủ .                                                                                                           |                         | hai l ớ p trướ c khi t ả i.                                                          |                                                                        |
|------|-----------------------|--------------|------------------|--------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Lead | Ch ỉ tiêu hi ệu năng  | Thêm m ớ i   | /crm/lead/add    | Thêmm ớ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .    | Ki ể m th ử hi ệ u năng | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Lead | Ch ỉ tiêu ch ứ c năng | C ậ p nh ậ t | /crm/lead/export | C ậ p nh ậ t d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.     | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.       |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Lead        | Ch ỉ tiêu ch ứ c năng   | G ắ n th ẻ   | /crm/contact/update   | G ắ n th ẻ d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .    | Ki ể m th ử hi ệ u năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.        | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.   |
|-------------|-------------------------|--------------|-----------------------|---------------------------------------------------------------------------------------------------------------------------------|---------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Campaign    | Ch ỉ tiêu b ả om ậ t    | Thêm m ớ i   | /crm/lead/export      | Thêmm ớ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng   | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.            |
| Opportunity | Ch ỉ tiêu ch ứ c năng   | Export       | /crm/lead/add         | Export d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý                                         | Ki ể m th ử ch ứ c năng   | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s,                                       | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.            |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                       |            |                         | logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                     |                         | t ự độ ng retry khi l ỗ i.                                                              |                                                                     |
|----------|-----------------------|------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Campaign | Ch ỉ tiêu hi ệu năng  | Xóa        | /crm/opportunity/delete | Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử hi ệ u năng | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |
| Lead     | Ch ỉ tiêu ch ứ c năng | Thêm m ớ i | /crm/lead/add           | Thêmm ớ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.    | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.  |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Campaign   | Ch ỉ tiêu b ả om ậ t   | Export        | /crm/contact/update   | Export d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử ch ứ c năng   | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                         | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.   |
|------------|------------------------|---------------|-----------------------|--------------------------------------------------------------------------------------------------------------------------------|---------------------------|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Lead       | Ch ỉ tiêu b ả om ậ t   | Chuy ể n đổ i | /crm/contact/update   | Chuy ển đổ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng   | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.    |
| Campaign   | Ch ỉ tiêu ch ứ c năng  | Xóa           | /crm/lead/export      | Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u                                                               | Ki ể m th ử hi ệ u năng   | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có                                        | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.    |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|         |                       |            |                         | đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                        |                         | xác th ự c hai l ớ p trướ c khi t ả i.                                               |                                                                    |
|---------|-----------------------|------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Contact | Ch ỉ tiêu hi ệu năng  | G ắ n th ẻ | /crm/opportunity/delete | G ắ n th ẻ d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.            |
| Lead    | Ch ỉ tiêu ch ứ c năng | Import     | /crm/campaign/import    | Import d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .        | Ki ể m th ử b ả o m ậ t | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.     | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng. |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Contact   | Ch ỉ tiêu b ả om ậ t   | G ắ n th ẻ   | /crm/campaign/import    | G ắ n th ẻ d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử ch ứ c năng   | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                            | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.                |
|-----------|------------------------|--------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Lead      | Ch ỉ tiêu hi ệu năng   | C ậ p nh ậ t | /crm/opportunity/delete | C ậ p nh ậ t d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .    | Ki ể m th ử ch ứ c năng   | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Lead      | Ch ỉ tiêu hi ệu năng   | Export       | /crm/opportunity/delete | Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ                               | Ki ể m th ử b ả o m ậ t   | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c                                | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.                |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                      |            |                         | và ghi log đầ y đủ .                                                                                                               |                         | hai l ớ p trướ c khi t ả i.                                                          |                                                                        |
|-------------|----------------------|------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Contact     | Ch ỉ tiêu hi ệu năng | Thêm m ớ i | /crm/opportunity/delete | Thêmm ớ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .     | Ki ể m th ử b ả o m ậ t | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Opportunity | Ch ỉ tiêu b ả om ậ t | Thêm m ớ i | /crm/lead/export        | Thêmm ớ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.         | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.     |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Contact   | Ch ỉ tiêu ch ứ c năng   | C ậ p nh ậ t   | /crm/lead/add        | C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử ch ứ c năng   | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.   | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.   |
|-----------|-------------------------|----------------|----------------------|-------------------------------------------------------------------------------------------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Lead      | Ch ỉ tiêu ch ứ c năng   | Chuy ể n đổ i  | /crm/campaign/import | Chuy ển đổ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .      | Ki ể m th ử ch ứ c năng   | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                              | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.                  |
| Lead      | Ch ỉ tiêu ch ứ c năng   | Import         | /crm/lead/export     | Import d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ                                 | Ki ể m th ử b ả o m ậ t   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng                                | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.   |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                      |              |                      | và ghi log đầ y đủ .                                                                                                           |                         | rollback giao d ị ch.                                                            |                                                                        |
|-------------|----------------------|--------------|----------------------|--------------------------------------------------------------------------------------------------------------------------------|-------------------------|----------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Lead        | Ch ỉ tiêu b ả om ậ t | C ậ p nh ậ t | /crm/contact/update  | C ậ p nh ậ t d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch. | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Lead        | Ch ỉ tiêu hi ệu năng | Export       | /crm/lead/add        | Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .       | Ki ể m th ử ch ứ c năng | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                     | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.     |
| Opportunity | Ch ỉ tiêu hi ệu năng | G ắ n th ẻ   | /crm/campaign/import | G ắ n th ẻ d ữ li ệ u Opportunity trong CRM, bao g ồ m                                                                         | Ki ể m th ử b ả o m ậ t | Thành công v ớ i th ờ i gian x ử lý <                                            | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                      |        |                         | validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                             |                         | 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.                                       |                                                                  |
|-------------|----------------------|--------|-------------------------|--------------------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------|
| Lead        | Ch ỉ tiêu b ả om ậ t | Export | /crm/opportunity/delete | Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày. |
| Opportunity | Ch ỉ tiêu hi ệu năng | Xóa    | /crm/opportunity/delete | Xóa d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ                  | Ki ể m th ử b ả o m ậ t | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang                      | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                      |            |                         | và ghi log đầ y đủ .                                                                                                             |                         | h ệ th ố ng Billing.                                         |                                                                    |
|----------|----------------------|------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------|--------------------------------------------------------------------|
| Campaign | Ch ỉ tiêu hi ệu năng | Thêm m ớ i | /crm/opportunity/delete | Thêmm ớ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .  | Ki ể m th ử ch ứ c năng | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%. | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng. |
| Campaign | Ch ỉ tiêu hi ệu năng | G ắ n th ẻ | /crm/lead/export        | G ắ n th ẻ d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%. | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.   |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Opportunity   | Ch ỉ tiêu b ả om ậ t   | Thêm m ớ i    | /crm/contact/update     | Thêmm ớ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .    | Ki ể m th ử ch ứ c năng   | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.   | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.                |
|---------------|------------------------|---------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------|---------------------------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Opportunity   | Ch ỉ tiêu b ả om ậ t   | Chuy ể n đổ i | /crm/opportunity/delete | Chuy ển đổ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng   | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.   | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Campaign      | Ch ỉ tiêu b ả om ậ t   | C ậ p nh ậ t  | /crm/lead/export        | C ậ p nh ậ t d ữ li ệ u Campaign trong CRM,                                                                                           | Ki ể m th ử               | Đồ ng b ộ d ữ li ệ u sang                                                              | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA                             |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                       |            |                     | bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                           | hi ệ u năng             | DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.                                      | để t ự độ ng hóa quy trình.                                         |
|----------|-----------------------|------------|---------------------|----------------------------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Campaign | Ch ỉ tiêu ch ứ c năng | G ắ n th ẻ | /crm/lead/add       | G ắ n th ẻ d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.  |
| Campaign | Ch ỉ tiêu hi ệu năng  | Xóa        | /crm/contact/update | Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ                             | Ki ể m th ử ch ứ c năng | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp                                         | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                      |            |                         | và ghi log đầ y đủ .                                                                                                         |                         | ứ ng 99.99%.                                                                     |                                                                        |
|----------|----------------------|------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------|-------------------------|----------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Lead     | Ch ỉ tiêu b ả om ậ t | G ắ n th ẻ | /crm/contact/update     | G ắ n th ẻ d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch. | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Contact  | Ch ỉ tiêu hi ệu năng | Import     | /crm/opportunity/delete | Import d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .  | Ki ể m th ử hi ệ u năng | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                     | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.       |
| Campaign | Ch ỉ tiêu hi ệu năng | Xóa        | /crm/opportunity/delete | Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m                                                                                 | Ki ể m th ử hi ệ u năng | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c,                                   | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|         |                       |            |                  | validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                |                         | h ệ th ố ng rollback giao d ị ch.                                                       |                                                                     |
|---------|-----------------------|------------|------------------|-----------------------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Contact | Ch ỉ tiêu ch ứ c năng | Xóa        | /crm/lead/export | Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .    | Ki ể m th ử b ả o m ậ t | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |
| Lead    | Ch ỉ tiêu ch ứ c năng | Thêm m ớ i | /crm/lead/export | Thêmm ớ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                            | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.             |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Contact   | Ch ỉ tiêu hi ệu năng   | Thêm m ớ i   | /crm/contact/update   | Thêmm ớ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử b ả o m ậ t   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.   | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.   |
|-----------|------------------------|--------------|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|---------------------------|------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| Contact   | Ch ỉ tiêu hi ệu năng   | Xóa          | /crm/lead/add         | Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .         | Ki ể m th ử ch ứ c năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.   | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.     |
| Campaign  | Ch ỉ tiêu ch ứ c năng  | Import       | /crm/contact/update   | Import d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý                                             | Ki ể m th ử ch ứ c năng   | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c                           | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.  |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                       |              |                     | logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                           |                         | hai l ớ p trướ c khi t ả i.                                                             |                                                                        |
|----------|-----------------------|--------------|---------------------|-----------------------------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Campaign | Ch ỉ tiêu ch ứ c năng | Import       | /crm/contact/update | Import d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .      | Ki ể m th ử ch ứ c năng | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Contact  | Ch ỉ tiêu b ả om ậ t  | C ậ p nh ậ t | /crm/lead/add       | C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.            | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.       |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Contact   | Ch ỉ tiêu ch ứ c năng   | G ắ n th ẻ   | /crm/lead/export        | G ắ n th ẻ d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử b ả o m ậ t   | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.         | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.     |
|-----------|-------------------------|--------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------|--------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Lead      | Ch ỉ tiêu hi ệu năng    | G ắ n th ẻ   | /crm/contact/update     | G ắ n th ẻ d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .      | Ki ể m th ử ch ứ c năng   | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.       |
| Lead      | Ch ỉ tiêu ch ứ c năng   | Xóa          | /crm/opportunity/delete | Xóa d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý                                                     | Ki ể m th ử ch ứ c năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng                           | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                       |              |                         | logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                               |                         | rollback giao d ị ch.                                                            |                                                                        |
|-------------|-----------------------|--------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------|----------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Opportunity | Ch ỉ tiêu b ả om ậ t  | C ậ p nh ậ t | /crm/campaign/import    | C ậ p nh ậ t d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch. | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Lead        | Ch ỉ tiêu ch ứ c năng | Export       | /crm/opportunity/delete | Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .              | Ki ể m th ử hi ệ u năng | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                     | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.    |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

| Lead     | Ch ỉ tiêu hi ệu năng   | Xóa    | /crm/opportunity/delete   | Xóa d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .        | Ki ể m th ử ch ứ c năng   | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.     | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.   |
|----------|------------------------|--------|---------------------------|------------------------------------------------------------------------------------------------------------------------------|---------------------------|----------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Campaign | Ch ỉ tiêu ch ứ c năng  | Import | /crm/lead/export          | Import d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch. | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.      |
| Contact  | Ch ỉ tiêu ch ứ c năng  | Import | /crm/contact/update       | Import d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý                                          | Ki ể m th ử ch ứ c năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng                       | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.                  |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|         |                      |            |                         | logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                        |                         | rollback giao d ị ch.                                        |                                                                    |
|---------|----------------------|------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------|--------------------------------------------------------------------|
| Contact | Ch ỉ tiêu hi ệu năng | Thêm m ớ i | /crm/opportunity/delete | Thêmm ớ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%. | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng. |
| Lead    | Ch ỉ tiêu hi ệu năng | Export     | /crm/lead/add           | Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .       | Ki ể m th ử hi ệ u năng | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%. | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.   |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Contact     | Ch ỉ tiêu hi ệu năng   | Xóa          | /crm/contact/update     | Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử b ả o m ậ t   | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                 | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.   |
|-------------|------------------------|--------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------|---------------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------|
| Lead        | Ch ỉ tiêu ch ứ c năng  | Export       | /crm/opportunity/delete | Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử ch ứ c năng   | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i. | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.   |
| Opportunity | Ch ỉ tiêu b ả om ậ t   | C ậ p nh ậ t | /crm/lead/add           | C ậ p nh ậ t d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u                                               | Ki ể m th ử ch ứ c năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng                   | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.   |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                      |        |                         | đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                     |                         | rollback giao d ị ch.                                                                |                                                                     |
|-------------|----------------------|--------|-------------------------|------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Campaign    | Ch ỉ tiêu hi ệu năng | Import | /crm/opportunity/delete | Import d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                         | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.             |
| Opportunity | Ch ỉ tiêu b ả om ậ t | Xóa    | /crm/lead/add           | Xóa d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

<!-- image -->

| Campaign   | Ch ỉ tiêu b ả om ậ t   | Thêm m ớ i   | /crm/lead/add        | Thêmm ớ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử hi ệ u năng   | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.   | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.       |
|------------|------------------------|--------------|----------------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Lead       | Ch ỉ tiêu ch ứ c năng  | Thêm m ớ i   | /crm/campaign/import | Thêmm ớ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .       | Ki ể m th ử b ả o m ậ t   | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                              | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Lead       | Ch ỉ tiêu hi ệu năng   | Thêm m ớ i   | /crm/campaign/import | Thêmm ớ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ                            | Ki ể m th ử b ả o m ậ t   | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s,                                         | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.       |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                       |               |                  | và ghi log đầ y đủ .                                                                                                                  |                         | t ự độ ng retry khi l ỗ i.                                                           |                                                         |
|-------------|-----------------------|---------------|------------------|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------|---------------------------------------------------------|
| Opportunity | Ch ỉ tiêu ch ứ c năng | Chuy ể n đổ i | /crm/lead/export | Chuy ển đổ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.     | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel. |
| Opportunity | Ch ỉ tiêu ch ứ c năng | Xóa           | /crm/lead/add    | Xóa d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .          | Ki ể m th ử hi ệ u năng | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

| Opportunity   | Ch ỉ tiêu hi ệu năng   | Chuy ể n đổ i   | /crm/lead/add    | Chuy ển đổ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử ch ứ c năng   | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.   | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.       |
|---------------|------------------------|-----------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Contact       | Ch ỉ tiêu b ả om ậ t   | C ậ p nh ậ t    | /crm/lead/add    | C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .       | Ki ể m th ử hi ệ u năng   | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                              | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Opportunity   | Ch ỉ tiêu hi ệu năng   | Export          | /crm/lead/export | Export d ữ li ệ u Opportunity trong CRM, bao g ồ m                                                                                      | Ki ể m th ử               | Không l ỗ i, log đầy đủ trong                                                             | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.                |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|         |                      |               |                         | validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                      | hi ệ u năng             | AuditLog, SLA đáp ứ ng 99.99%.                                                          |                                                                     |
|---------|----------------------|---------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Contact | Ch ỉ tiêu b ả om ậ t | C ậ p nh ậ t  | /crm/contact/update     | C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.             |
| Lead    | Ch ỉ tiêu hi ệu năng | Chuy ể n đổ i | /crm/opportunity/delete | Chuy ển đổ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .    | Ki ể m th ử b ả o m ậ t | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng                             | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                      |            |                      |                                                                                                                                    |                         | retry khi l ỗ i.                                                             |                                                                        |
|-------------|----------------------|------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------|-------------------------|------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Opportunity | Ch ỉ tiêu b ả om ậ t | Xóa        | /crm/campaign/import | Xóa d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .       | Ki ể m th ử ch ứ c năng | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                 | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Opportunity | Ch ỉ tiêu b ả om ậ t | Thêm m ớ i | /crm/lead/export     | Thêmm ớ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i. | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.    |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Lead        | Ch ỉ tiêu hi ệu năng   | Xóa           | /crm/contact/update     | Xóa d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                 | Ki ể m th ử ch ứ c năng   | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.   | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.   |
|-------------|------------------------|---------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Opportunity | Ch ỉ tiêu b ả om ậ t   | Chuy ể n đổ i | /crm/opportunity/delete | Chuy ển đổ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.          | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.         |
| Campaign    | Ch ỉ tiêu hi ệu năng   | C ậ p nh ậ t  | /crm/lead/add           | C ậ p nh ậ t d ữ li ệ u Campaign trong CRM, bao g ồ m                                                                                 | Ki ể m th ử               | Đồ ng b ộ d ữ li ệ u sang DataLake                                                        | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.       |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                      |            |                  | validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                    | hi ệ u năng             | trong vòng 5s, t ự độ ng retry khi l ỗ i.                    |                                                                     |
|-------------|----------------------|------------|------------------|---------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------|---------------------------------------------------------------------|
| Opportunity | Ch ỉ tiêu hi ệu năng | Import     | /crm/lead/add    | Import d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%. | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |
| Opportunity | Ch ỉ tiêu hi ệu năng | G ắ n th ẻ | /crm/lead/export | G ắ n th ẻ d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ                  | Ki ể m th ử b ả o m ậ t | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%. | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.    |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                       |              |                     | và ghi log đầ y đủ .                                                                                                            |                         |                                                                                         |                                                                  |
|-------------|-----------------------|--------------|---------------------|---------------------------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------|
| Lead        | Ch ỉ tiêu ch ứ c năng | C ậ p nh ậ t | /crm/lead/add       | C ậ p nh ậ t d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .  | Ki ể m th ử ch ứ c năng | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.          |
| Opportunity | Ch ỉ tiêu hi ệu năng  | Import       | /crm/lead/export    | Import d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.    | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày. |
| Contact     | Ch ỉ tiêu b ả om ậ t  | Xóa          | /crm/contact/update | Xóa d ữ li ệ u Contact trong                                                                                                    | Ki ể m th ử             | C ả nh báo n ế u thi ế u                                                                | K ế t qu ả đượ c g ử i mail và SMS cho                           |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|      |                      |            |                         | CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                              | hi ệ u năng             | trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.                      | qu ả n tr ị viên ph ụ trách.                                     |
|------|----------------------|------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------|-------------------------|------------------------------------------------------------------------------|------------------------------------------------------------------|
| Lead | Ch ỉ tiêu b ả om ậ t | Import     | /crm/opportunity/delete | Import d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i. | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày. |
| Lead | Ch ỉ tiêu b ả om ậ t | G ắ n th ẻ | /crm/lead/add           | G ắ n th ẻ d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ                  | Ki ể m th ử b ả o m ậ t | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang           | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                       |            |                      | và ghi log đầ y đủ .                                                                                                            |                         | h ệ th ố ng Billing.                                                                 |                                                                     |
|----------|-----------------------|------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Lead     | Ch ỉ tiêu hi ệu năng  | G ắ n th ẻ | /crm/lead/export     | G ắ n th ẻ d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .    | Ki ể m th ử hi ệ u năng | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |
| Campaign | Ch ỉ tiêu ch ứ c năng | Thêm m ớ i | /crm/campaign/import | Thêmm ớ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.             |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Opportunity   | Ch ỉ tiêu b ả om ậ t   | Chuy ể n đổ i   | /crm/opportunity/delete   | Chuy ển đổ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .   | Ki ể m th ử b ả o m ậ t   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.   | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.   |
|---------------|------------------------|-----------------|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|---------------------------|------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| Opportunity   | Ch ỉ tiêu b ả om ậ t   | Export          | /crm/opportunity/delete   | Export d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .         | Ki ể m th ử ch ứ c năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.   | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.     |
| Opportunity   | Ch ỉ tiêu b ả om ậ t   | Xóa             | /crm/campaign/import      | Xóa d ữ li ệ u Opportunity trong CRM, bao g ồ m                                                                                         | Ki ể m th ử b ả o m ậ t   | Đồ ng b ộ d ữ li ệ u sang DataLake                                                 | K ế t qu ả đượ c g ử i mail và SMS cho                               |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                      |        |                     | validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                 |                         | trong vòng 5s, t ự độ ng retry khi l ỗ i.                                            | qu ả n tr ị viên ph ụ trách.                                       |
|----------|----------------------|--------|---------------------|------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Lead     | Ch ỉ tiêu hi ệu năng | Xóa    | /crm/lead/add       | Xóa d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .        | Ki ể m th ử hi ệ u năng | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.     | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng. |
| Campaign | Ch ỉ tiêu b ả om ậ t | Export | /crm/contact/update | Export d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử b ả o m ậ t | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i. | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.   |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Campaign    | Ch ỉ tiêu ch ứ c năng   | Chuy ể n đổ i   | /crm/contact/update   | Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .    | Ki ể m th ử b ả o m ậ t   | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.   | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.   |
|-------------|-------------------------|-----------------|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------|---------------------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Opportunity | Ch ỉ tiêu hi ệu năng    | Chuy ể n đổ i   | /crm/lead/export      | Chuy ển đổ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng   | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                   | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.       |
| Campaign    | Ch ỉ tiêu ch ứ c năng   | Thêm m ớ i      | /crm/lead/add         | Thêmm ớ i d ữ li ệ u Campaign trong CRM, bao g ồ m                                                                                    | Ki ể m th ử               | Đồ ng b ộ d ữ li ệ u sang DataLake                                             | K ế t qu ả đượ c g ử i mail và SMS cho                                   |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                       |            |                     | validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                     | ch ứ c năng             | trong vòng 5s, t ự độ ng retry khi l ỗ i.                                        | qu ả n tr ị viên ph ụ trách.                                       |
|----------|-----------------------|------------|---------------------|----------------------------------------------------------------------------------------------------------------------------------|-------------------------|----------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Lead     | Ch ỉ tiêu ch ứ c năng | Export     | /crm/contact/update | Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .         | Ki ể m th ử hi ệ u năng | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch. | Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng. |
| Campaign | Ch ỉ tiêu hi ệu năng  | G ắ n th ẻ | /crm/contact/update | G ắ n th ẻ d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.     | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.            |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Contact   | Ch ỉ tiêu ch ứ c năng   | Xóa    | /crm/lead/add        | Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .    | Ki ể m th ử b ả o m ậ t   | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.   | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.                |
|-----------|-------------------------|--------|----------------------|-----------------------------------------------------------------------------------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Contact   | Ch ỉ tiêu hi ệu năng    | Import | /crm/campaign/import | Import d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng   | Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.              | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |
| Contact   | Ch ỉ tiêu hi ệu năng    | Export | /crm/lead/export     | Export d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý                                         | Ki ể m th ử hi ệ u năng   | Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có                                             | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                       |            |                     | logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                             |                         | xác th ự c hai l ớ p trướ c khi t ả i.                                                  |                                                                     |
|-------------|-----------------------|------------|---------------------|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Opportunity | Ch ỉ tiêu b ả om ậ t  | G ắ n th ẻ | /crm/contact/update | G ắ n th ẻ d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.             |
| Lead        | Ch ỉ tiêu ch ứ c năng | Import     | /crm/lead/export    | Import d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .            | Ki ể m th ử b ả o m ậ t | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.                            | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |

<!-- image -->

## VIETTEL AI RACE

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

| Contact     | Ch ỉ tiêu hi ệu năng   | Xóa        | /crm/opportunity/delete   | Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .           | Ki ể m th ử ch ứ c năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.   | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.    |
|-------------|------------------------|------------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------|---------------------------|------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Opportunity | Ch ỉ tiêu hi ệu năng   | Thêm m ớ i | /crm/lead/export          | Thêmm ớ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.   | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.    |
| Campaign    | Ch ỉ tiêu b ả om ậ t   | Thêm m ớ i | /crm/opportunity/delete   | Thêmm ớ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u                                                             | Ki ể m th ử hi ệ u năng   | Đồ ng b ộ d ữ li ệ u sang DataLake trong                                           | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                      |            |                         | đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                           |                         | vòng 5s, t ự độ ng retry khi l ỗ i.                                                     |                                                                     |
|-------------|----------------------|------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Opportunity | Ch ỉ tiêu b ả om ậ t | Thêm m ớ i | /crm/lead/export        | Thêmm ớ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing. | D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.    |
| Lead        | Ch ỉ tiêu hi ệu năng | Export     | /crm/opportunity/delete | Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .           | Ki ể m th ử ch ứ c năng | Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang                      | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                       |               |                         |                                                                                                                                    |                         | h ệ th ố ng Billing.                                         |                                                                     |
|----------|-----------------------|---------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------|---------------------------------------------------------------------|
| Campaign | Ch ỉ tiêu b ả om ậ t  | Xóa           | /crm/lead/add           | Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .          | Ki ể m th ử ch ứ c năng | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%. | K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách. |
| Campaign | Ch ỉ tiêu ch ứ c năng | Chuy ể n đổ i | /crm/opportunity/delete | Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử ch ứ c năng | Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%. | Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.             |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

| Contact     | Ch ỉ tiêu hi ệu năng   | Export     | /crm/lead/add    | Export d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .        | Ki ể m th ử b ả o m ậ t   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.   | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.   |
|-------------|------------------------|------------|------------------|------------------------------------------------------------------------------------------------------------------------------------|---------------------------|------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Opportunity | Ch ỉ tiêu hi ệu năng   | Thêm m ớ i | /crm/lead/export | Thêmm ớ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.   | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.   |