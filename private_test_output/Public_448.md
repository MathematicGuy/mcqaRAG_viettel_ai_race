<!-- image -->

## VIETTEL AI RACE

## QU Ả N LÝ API &amp; LOG

TD448

L ầ n ban hành: 1

| API                       | Phương th ứ c   | Hành độ ng              | Mô t ả chi ti ế t                                                                                                              | K ế t qu ả                     | Ghi chú                              |
|---------------------------|-----------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| /customer/update          | PATCH           | Thêm b ả n ghi          | API /customer/update s ử d ụng phương thứ c PATCH để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.       | Rollback khi l ỗ i             | Gi ớ i h ạ n rate-limit 1000 req/min |
| /invoice/export           | PATCH           | Xóa thông tin           | API /invoice/export s ử d ụng phương thứ c PATCH để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.         | Thông báo s ự ki ệ n qua Kafka | Tích h ợ p v ớ i API Gateway         |
| /security/firewall/config | GET             | Xóa thông tin           | API /security/firewall/config s ử d ụng phương thứ c GET để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Thông báo s ự ki ệ n qua Kafka | Gi ớ i h ạ n rate-limit 1000 req/min |
| /ivr/callflow             | POST            | Ki ể m tra tr ạ ng thái | API /ivr/callflow s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.   | Thông báo s ự ki ệ n qua Kafka | Có versioning v1/v2                  |
| /crm/lead/import          | PUT             | Export d ữ li ệ u       | API /crm/lead/import s ử d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.      | Thành công <1s                 | Tích h ợ p v ớ i API Gateway         |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /rpa/task/execute    | POST   | C ậ p nh ậ t c ấ u hình   | API /rpa/task/execute s ử d ụng phương thứ c POST để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.   | Log đầ y đủ                    | Tích h ợ p v ớ i API Gateway   |
|----------------------|--------|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| /customer/update     | GET    | Thêm b ả n ghi            | API /customer/update s ử d ụng phương thứ c GET để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.              | Retry t ố i đa 3 lầ n          | H ỗ tr ợ JSON và XML           |
| /network/qos/monitor | POST   | Ki ể m tra tr ạ ng thái   | API /network/qos/monitor s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Thông báo s ự ki ệ n qua Kafka | Tích h ợ p v ớ i API Gateway   |
| /invoice/export      | POST   | C ậ p nh ậ t c ấ u hình   | API /invoice/export s ử d ụng phương thứ c POST để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.     | Rollback khi l ỗ i             | Theo chu ẩ n RESTful           |
| /network/qos/monitor | GET    | Export d ữ li ệ u         | API /network/qos/monitor s ử d ụng phương thứ c GET để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.       | Thông báo s ự ki ệ n qua Kafka | H ỗ tr ợ JSON và XML           |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /rpa/task/execute         | POST   | Export d ữ li ệ u       | API /rpa/task/execute s ử d ụng phương thứ c POST để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                | Log đầ y đủ                    | Gi ớ i h ạ n rate-limit 1000 req/min   |
|---------------------------|--------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|----------------------------------------|
| /crm/lead/import          | PATCH  | Export d ữ li ệ u       | API /crm/lead/import s ử d ụng phương thứ c PATCH để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                | Rollback khi l ỗ i             | Gi ớ i h ạ n rate-limit 1000 req/min   |
| /invoice/export           | POST   | C ậ p nh ậ t c ấ u hình | API /invoice/export s ử d ụng phương thứ c POST để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.            | Thông báo s ự ki ệ n qua Kafka | H ỗ tr ợ JSON và XML                   |
| /ivr/callflow             | GET    | Xóa thông tin           | API /ivr/callflow s ử d ụng phương thứ c GET để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                         | Thông báo s ự ki ệ n qua Kafka | Gi ớ i h ạ n rate-limit 1000 req/min   |
| /security/firewall/config | DELETE | Ki ể m tra tr ạ ng thái | API /security/firewall/config s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Log đầ y đủ                    | Tích h ợ p v ớ i API Gateway           |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /ivr/callflow             | POST   | Xóa thông tin           | API /ivr/callflow s ử d ụng phương thứ c POST để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                      | Thành công <1s        | Theo chu ẩ n RESTful                 |
|---------------------------|--------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|--------------------------------------|
| /security/firewall/config | POST   | Ki ể m tra tr ạ ng thái | API /security/firewall/config s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Retry t ố i đa 3 lầ n | Gi ớ i h ạ n rate-limit 1000 req/min |
| /invoice/export           | GET    | Thêm b ả n ghi          | API /invoice/export s ử d ụng phương thứ c GET để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                    | Log đầ y đủ           | H ỗ tr ợ JSON và XML                 |
| /invoice/export           | PATCH  | Ki ể m tra tr ạ ng thái | API /invoice/export s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.          | Log đầ y đủ           | H ỗ tr ợ JSON và XML                 |
| /crm/lead/import          | PUT    | C ậ p nh ậ t c ấ u hình | API /crm/lead/import s ử d ụng phương thứ c PUT để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.          | Thành công <1s        | H ỗ tr ợ JSON và XML                 |
| /ivr/callflow             | PUT    | Thêm b ả n              | API /ivr/callflow s ử d ụng phương thứ c PUT                                                                                             | Log đầ y              | Tích h ợ p v ớ i API                 |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |        | ghi                     | để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                                                             | đủ                 | Gateway              |
|----------------------|--------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|--------------------|----------------------|
| /rpa/task/execute    | POST   | Thêm b ả n ghi          | API /rpa/task/execute s ử d ụng phương thứ c POST để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.           | Log đầ y đủ        | H ỗ tr ợ JSON và XML |
| /rpa/task/execute    | DELETE | Ki ể m tra tr ạ ng thái | API /rpa/task/execute s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Rollback khi l ỗ i | H ỗ tr ợ JSON và XML |
| /crm/lead/import     | PATCH  | Ki ể m tra tr ạ ng thái | API /crm/lead/import s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.   | Thành công <1s     | Có versioning v1/v2  |
| /crm/lead/import     | DELETE | C ậ p nh ậ t c ấ u hình | API /crm/lead/import s ử d ụng phương thứ c DELETE để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Rollback khi l ỗ i | Theo chu ẩ n RESTful |
| /network/qos/monitor | DELETE | Thêm b ả n ghi          | API /network/qos/monitor s ử d ụng phương thứ c DELETE để Thêm b ả n                                                               | Thành công <1s     | Theo chu ẩ n RESTful |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        |                         | ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                                                                                 |                       |                                      |
|---------------------------|--------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|--------------------------------------|
| /crm/lead/import          | DELETE | Thêm b ả n ghi          | API /crm/lead/import s ử d ụng phương thứ c DELETE để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                | Rollback khi l ỗ i    | Tích h ợ p v ớ i API Gateway         |
| /rpa/task/execute         | PATCH  | C ậ p nh ậ t c ấ u hình | API /rpa/task/execute s ử d ụng phương thứ c PATCH để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.       | Retry t ố i đa 3 lầ n | Có versioning v1/v2                  |
| /invoice/export           | GET    | Export d ữ li ệ u       | API /invoice/export s ử d ụng phương thứ c GET để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                 | Retry t ố i đa 3 lầ n | Gi ớ i h ạ n rate-limit 1000 req/min |
| /security/firewall/config | POST   | Ki ể m tra tr ạ ng thái | API /security/firewall/config s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Retry t ố i đa 3 lầ n | Theo chu ẩ n RESTful                 |
| /rpa/task/execute         | POST   | Ki ể m tra tr ạ ng      | API /rpa/task/execute s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c                                               | Log đầ y đủ           | Có versioning v1/v2                  |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        | thái                    | OAuth2 và log giao d ị ch chi ti ế t.                                                                                                   |                                |                                      |
|---------------------------|--------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| /security/firewall/config | GET    | Ki ể m tra tr ạ ng thái | API /security/firewall/config s ử d ụng phương thứ c GET để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Retry t ố i đa 3 lầ n          | Gi ớ i h ạ n rate-limit 1000 req/min |
| /rpa/task/execute         | GET    | Thêm b ả n ghi          | API /rpa/task/execute s ử d ụng phương thứ c GET để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                 | Log đầ y đủ                    | Tích h ợ p v ớ i API Gateway         |
| /crm/lead/import          | POST   | C ậ p nh ậ t c ấ u hình | API /crm/lead/import s ử d ụng phương thứ c POST để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.        | Rollback khi l ỗ i             | Theo chu ẩ n RESTful                 |
| /ivr/callflow             | GET    | Export d ữ li ệ u       | API /ivr/callflow s ử d ụng phương thứ c GET để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                  | Thông báo s ự ki ệ n qua Kafka | Gi ớ i h ạ n rate-limit 1000 req/min |
| /ivr/callflow             | DELETE | Thêm b ả n ghi          | API /ivr/callflow s ử d ụng phương thứ c DELETE để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao                                     | Thông báo s ự ki ệ n qua Kafka | H ỗ tr ợ JSON và XML                 |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        |                         | d ị ch chi ti ế t.                                                                                                                  |                       |                                      |
|---------------------------|--------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|-----------------------|--------------------------------------|
| /invoice/export           | PUT    | Export d ữ li ệ u       | API /invoice/export s ử d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.            | Log đầ y đủ           | H ỗ tr ợ JSON và XML                 |
| /ivr/callflow             | PATCH  | Export d ữ li ệ u       | API /ivr/callflow s ử d ụng phương thứ c PATCH để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.            | Retry t ố i đa 3 lầ n | Có versioning v1/v2                  |
| /invoice/export           | PUT    | Export d ữ li ệ u       | API /invoice/export s ử d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.            | Log đầ y đủ           | Gi ớ i h ạ n rate-limit 1000 req/min |
| /customer/update          | DELETE | Ki ể m tra tr ạ ng thái | API /customer/update s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.   | Rollback khi l ỗ i    | Có versioning v1/v2                  |
| /rpa/task/execute         | DELETE | C ậ p nh ậ t c ấ u hình | API /rpa/task/execute s ử d ụng phương thứ c DELETE để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Thành công <1s        | Theo chu ẩ n RESTful                 |
| /security/firewall/config | PUT    | Export                  | API                                                                                                                                 | Rollback              | Tích h ợ p                           |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        | d ữ li ệ u        | /security/firewall/config s ử d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.   | khi l ỗ i                      | v ớ i API Gateway                    |
|---------------------------|--------|-------------------|----------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| /rpa/task/execute         | PUT    | Export d ữ li ệ u | API /rpa/task/execute s ử d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.       | Thông báo s ự ki ệ n qua Kafka | Theo chu ẩ n RESTful                 |
| /security/firewall/config | PUT    | Thêm b ả n ghi    | API /security/firewall/config s ử d ụng phương thứ c PUT để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.  | Thông báo s ự ki ệ n qua Kafka | Theo chu ẩ n RESTful                 |
| /network/qos/monitor      | DELETE | Export d ữ li ệ u | API /network/qos/monitor s ử d ụng phương thứ c DELETE để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Log đầ y đủ                    | Gi ớ i h ạ n rate-limit 1000 req/min |
| /rpa/task/execute         | PATCH  | Thêm b ả n ghi    | API /rpa/task/execute s ử d ụng phương thứ c PATCH để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.        | Rollback khi l ỗ i             | Gi ớ i h ạ n rate-limit 1000 req/min |
| /invoice/export           | GET    | Xóa thông         | API /invoice/export s ử d ụng phương thứ c GET                                                                                   | Rollback                       | Gi ớ i h ạ n rate-limit              |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                   |        | tin                     | để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                                                              | khi l ỗ i                      | 1000 req/min                         |
|-------------------|--------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| /rpa/task/execute | PATCH  | C ậ p nh ậ t c ấ u hình | API /rpa/task/execute s ử d ụng phương thứ c PATCH để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Thành công <1s                 | Gi ớ i h ạ n rate-limit 1000 req/min |
| /ivr/callflow     | DELETE | Ki ể m tra tr ạ ng thái | API /ivr/callflow s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.     | Thông báo s ự ki ệ n qua Kafka | Gi ớ i h ạ n rate-limit 1000 req/min |
| /invoice/export   | DELETE | Thêm b ả n ghi          | API /invoice/export s ử d ụng phương thứ c DELETE để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.           | Thông báo s ự ki ệ n qua Kafka | H ỗ tr ợ JSON và XML                 |
| /rpa/task/execute | GET    | C ậ p nh ậ t c ấ u hình | API /rpa/task/execute s ử d ụng phương thứ c GET để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.   | Thành công <1s                 | Theo chu ẩ n RESTful                 |
| /ivr/callflow     | DELETE | C ậ p nh ậ t c ấ u      | API /ivr/callflow s ử d ụng phương thứ c DELETE để C ậ p nh ậ t c ấ u hình, có xác th ự c                                          | Thành công <1s                 | Theo chu ẩ n RESTful                 |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |       | hình                    | OAuth2 và log giao d ị ch chi ti ế t.                                                                                                |                    |                                      |
|----------------------|-------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------|--------------------|--------------------------------------|
| /crm/lead/import     | PUT   | Xóa thông tin           | API /crm/lead/import s ử d ụng phương thứ c PUT để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                | Thành công <1s     | Có versioning v1/v2                  |
| /crm/lead/import     | POST  | Thêm b ả n ghi          | API /crm/lead/import s ử d ụng phương thứ c POST để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.              | Thành công <1s     | Gi ớ i h ạ n rate-limit 1000 req/min |
| /network/qos/monitor | PATCH | Ki ể m tra tr ạ ng thái | API /network/qos/monitor s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Rollback khi l ỗ i | H ỗ tr ợ JSON và XML                 |
| /customer/update     | PATCH | Xóa thông tin           | API /customer/update s ử d ụng phương thứ c PATCH để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.              | Rollback khi l ỗ i | H ỗ tr ợ JSON và XML                 |
| /crm/lead/import     | POST  | Export d ữ li ệ u       | API /crm/lead/import s ử d ụng phương thứ c POST để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao                              | Log đầ y đủ        | Gi ớ i h ạ n rate-limit 1000 req/min |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |      |                         | d ị ch chi ti ế t.                                                                                                                       |                                |                                      |
|---------------------------|------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| /security/firewall/config | PUT  | Thêm b ả n ghi          | API /security/firewall/config s ử d ụng phương thứ c PUT để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.          | Thông báo s ự ki ệ n qua Kafka | Tích h ợ p v ớ i API Gateway         |
| /invoice/export           | GET  | Export d ữ li ệ u       | API /invoice/export s ử d ụng phương thứ c GET để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                 | Retry t ố i đa 3 lầ n          | Tích h ợ p v ớ i API Gateway         |
| /security/firewall/config | POST | Ki ể m tra tr ạ ng thái | API /security/firewall/config s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Rollback khi l ỗ i             | H ỗ tr ợ JSON và XML                 |
| /customer/update          | GET  | C ậ p nh ậ t c ấ u hình | API /customer/update s ử d ụng phương thứ c GET để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.          | Thành công <1s                 | Tích h ợ p v ớ i API Gateway         |
| /customer/update          | POST | Xóa thông tin           | API /customer/update s ử d ụng phương thứ c POST để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                   | Retry t ố i đa 3 lầ n          | Gi ớ i h ạ n rate-limit 1000 req/min |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /network/qos/monitor      | PUT    | Thêm b ả n ghi    | API /network/qos/monitor s ử d ụng phương thứ c PUT để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.         | Retry t ố i đa 3 lầ n          | Có versioning v1/v2                  |
|---------------------------|--------|-------------------|------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| /ivr/callflow             | DELETE | Export d ữ li ệ u | API /ivr/callflow s ử d ụng phương thứ c DELETE để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.          | Log đầ y đủ                    | Gi ớ i h ạ n rate-limit 1000 req/min |
| /invoice/export           | GET    | Xóa thông tin     | API /invoice/export s ử d ụng phương thứ c GET để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.               | Thành công <1s                 | Có versioning v1/v2                  |
| /security/firewall/config | GET    | Export d ữ li ệ u | API /security/firewall/config s ử d ụng phương thứ c GET để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Thông báo s ự ki ệ n qua Kafka | Tích h ợ p v ớ i API Gateway         |
| /ivr/callflow             | POST   | Xóa thông tin     | API /ivr/callflow s ử d ụng phương thứ c POST để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                | Log đầ y đủ                    | H ỗ tr ợ JSON và XML                 |
| /customer/update          | DELETE | Xóa thông         | API /customer/update s ử d ụng phương thứ c DELETE để Xóa thông                                                                    | Rollback khi l ỗ i             | Gi ớ i h ạ n rate-limit 1000         |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |      | tin                     | tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                                                                         |                    | req/min                      |
|---------------------------|------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------|--------------------|------------------------------|
| /security/firewall/config | POST | Thêm b ả n ghi          | API /security/firewall/config s ử d ụng phương thứ c POST để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Log đầ y đủ        | Tích h ợ p v ớ i API Gateway |
| /invoice/export           | GET  | Thêm b ả n ghi          | API /invoice/export s ử d ụng phương thứ c GET để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.            | Thành công <1s     | Theo chu ẩ n RESTful         |
| /customer/update          | PUT  | Ki ể m tra tr ạ ng thái | API /customer/update s ử d ụng phương thứ c PUT để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.   | Rollback khi l ỗ i | Tích h ợ p v ớ i API Gateway |
| /customer/update          | POST | Ki ể m tra tr ạ ng thái | API /customer/update s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.  | Log đầ y đủ        | Theo chu ẩ n RESTful         |
| /ivr/callflow             | POST | Export d ữ li ệ u       | API /ivr/callflow s ử d ụng phương thứ c POST để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao                             | Thành công <1s     | Có versioning v1/v2          |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        |                         | d ị ch chi ti ế t.                                                                                                                  |                                |                                      |
|---------------------------|--------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| /invoice/export           | DELETE | Export d ữ li ệ u       | API /invoice/export s ử d ụng phương thứ c DELETE để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.         | Rollback khi l ỗ i             | Có versioning v1/v2                  |
| /security/firewall/config | GET    | Export d ữ li ệ u       | API /security/firewall/config s ử d ụng phương thứ c GET để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.  | Retry t ố i đa 3 lầ n          | H ỗ tr ợ JSON và XML                 |
| /crm/lead/import          | PATCH  | Xóa thông tin           | API /crm/lead/import s ử d ụng phương thứ c PATCH để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.             | Thành công <1s                 | Theo chu ẩ n RESTful                 |
| /network/qos/monitor      | POST   | Ki ể m tra tr ạ ng thái | API /network/qos/monitor s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Thông báo s ự ki ệ n qua Kafka | Gi ớ i h ạ n rate-limit 1000 req/min |
| /crm/lead/import          | DELETE | Thêm b ả n ghi          | API /crm/lead/import s ử d ụng phương thứ c DELETE để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao                              | Log đầ y đủ                    | Gi ớ i h ạ n rate-limit 1000 req/min |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |      |                         | d ị ch chi ti ế t.                                                                                                                  |                    |                                      |
|----------------------|------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|--------------------|--------------------------------------|
| /crm/lead/import     | PUT  | Export d ữ li ệ u       | API /crm/lead/import s ử d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.           | Rollback khi l ỗ i | Có versioning v1/v2                  |
| /crm/lead/import     | POST | Ki ể m tra tr ạ ng thái | API /crm/lead/import s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.     | Rollback khi l ỗ i | Theo chu ẩ n RESTful                 |
| /customer/update     | GET  | Ki ể m tra tr ạ ng thái | API /customer/update s ử d ụng phương thứ c GET để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.      | Thành công <1s     | Gi ớ i h ạ n rate-limit 1000 req/min |
| /network/qos/monitor | PUT  | C ậ p nh ậ t c ấ u hình | API /network/qos/monitor s ử d ụng phương thứ c PUT để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Rollback khi l ỗ i | Theo chu ẩ n RESTful                 |
| /network/qos/monitor | PUT  | Ki ể m tra tr ạ ng thái | API /network/qos/monitor s ử d ụng phương thứ c PUT để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao                     | Thành công <1s     | Theo chu ẩ n RESTful                 |

<!-- image -->

## VIETTEL AI RACE

## QU Ả N LÝ API &amp; LOG

TD448

L ầ n ban hành: 1

|                           |        |                         | d ị ch chi ti ế t.                                                                                                                         |                       |                                      |
|---------------------------|--------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|--------------------------------------|
| /security/firewall/config | GET    | Ki ể m tra tr ạ ng thái | API /security/firewall/config s ử d ụng phương thứ c GET để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.    | Rollback khi l ỗ i    | H ỗ tr ợ JSON và XML                 |
| /security/firewall/config | GET    | C ậ p nh ậ t c ấ u hình | API /security/firewall/config s ử d ụng phương thứ c GET để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.   | Log đầ y đủ           | Gi ớ i h ạ n rate-limit 1000 req/min |
| /invoice/export           | POST   | Thêm b ả n ghi          | API /invoice/export s ử d ụng phương thứ c POST để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                     | Thành công <1s        | H ỗ tr ợ JSON và XML                 |
| /security/firewall/config | DELETE | Ki ể m tra tr ạ ng thái | API /security/firewall/config s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Retry t ố i đa 3 lầ n | Tích h ợ p v ớ i API Gateway         |
| /network/qos/monitor      | GET    | C ậ p nh ậ t c ấ u      | API /network/qos/monitor s ử d ụng phương thứ c                                                                                            | Retry t ố i đa 3 lầ n | Tích h ợ p v ớ i API                 |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                   |       | hình                    | GET để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                                          |                                | Gateway                              |
|-------------------|-------|-------------------------|------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| /rpa/task/execute | PATCH | Export d ữ li ệ u       | API /rpa/task/execute s ử d ụng phương thứ c PATCH để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Retry t ố i đa 3 lầ n          | Có versioning v1/v2                  |
| /customer/update  | PUT   | Xóa thông tin           | API /customer/update s ử d ụng phương thứ c PUT để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.        | Rollback khi l ỗ i             | H ỗ tr ợ JSON và XML                 |
| /customer/update  | PUT   | Thêm b ả n ghi          | API /customer/update s ử d ụng phương thứ c PUT để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.       | Thành công <1s                 | Có versioning v1/v2                  |
| /ivr/callflow     | GET   | Ki ể m tra tr ạ ng thái | API /ivr/callflow s ử d ụng phương thứ c GET để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.  | Rollback khi l ỗ i             | Gi ớ i h ạ n rate-limit 1000 req/min |
| /invoice/export   | PUT   | Export d ữ li ệ u       | API /invoice/export s ử d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.     | Thông báo s ự ki ệ n qua Kafka | H ỗ tr ợ JSON và XML                 |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /security/firewall/config   | DELETE   | Xóa thông tin           | API /security/firewall/config s ử d ụng phương thứ c DELETE để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.   | Rollback khi l ỗ i    | Tích h ợ p v ớ i API Gateway   |
|-----------------------------|----------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|-----------------------|--------------------------------|
| /network/qos/monitor        | DELETE   | Export d ữ li ệ u       | API /network/qos/monitor s ử d ụng phương thứ c DELETE để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.    | Thành công <1s        | Theo chu ẩ n RESTful           |
| /crm/lead/import            | PATCH    | Xóa thông tin           | API /crm/lead/import s ử d ụng phương thứ c PATCH để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.             | Thành công <1s        | Tích h ợ p v ớ i API Gateway   |
| /invoice/export             | POST     | Thêm b ả n ghi          | API /invoice/export s ử d ụng phương thứ c POST để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.              | Thành công <1s        | Theo chu ẩ n RESTful           |
| /rpa/task/execute           | POST     | C ậ p nh ậ t c ấ u hình | API /rpa/task/execute s ử d ụng phương thứ c POST để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.   | Retry t ố i đa 3 lầ n | Tích h ợ p v ớ i API Gateway   |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /crm/lead/import     | GET   | Ki ể m tra tr ạ ng thái   | API /crm/lead/import s ử d ụng phương thứ c GET để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.     | Retry t ố i đa 3 lầ n          | Theo chu ẩ n RESTful                 |
|----------------------|-------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| /network/qos/monitor | PUT   | Ki ể m tra tr ạ ng thái   | API /network/qos/monitor s ử d ụng phương thứ c PUT để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Thành công <1s                 | Tích h ợ p v ớ i API Gateway         |
| /customer/update     | POST  | C ậ p nh ậ t c ấ u hình   | API /customer/update s ử d ụng phương thứ c POST để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.   | Thành công <1s                 | H ỗ tr ợ JSON và XML                 |
| /crm/lead/import     | PUT   | Thêm b ả n ghi            | API /crm/lead/import s ử d ụng phương thứ c PUT để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.             | Retry t ố i đa 3 lầ n          | Có versioning v1/v2                  |
| /ivr/callflow        | POST  | Ki ể m tra tr ạ ng thái   | API /ivr/callflow s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.       | Thông báo s ự ki ệ n qua Kafka | Gi ớ i h ạ n rate-limit 1000 req/min |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /customer/update   | PATCH   | C ậ p nh ậ t c ấ u hình   | API /customer/update s ử d ụng phương thứ c PATCH để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.   | Log đầ y đủ                    | Tích h ợ p v ớ i API Gateway   |
|--------------------|---------|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| /invoice/export    | POST    | Ki ể m tra tr ạ ng thái   | API /invoice/export s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.      | Thành công <1s                 | H ỗ tr ợ JSON và XML           |
| /crm/lead/import   | PATCH   | C ậ p nh ậ t c ấ u hình   | API /crm/lead/import s ử d ụng phương thứ c PATCH để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.   | Rollback khi l ỗ i             | Có versioning v1/v2            |
| /customer/update   | GET     | Ki ể m tra tr ạ ng thái   | API /customer/update s ử d ụng phương thứ c GET để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.      | Thông báo s ự ki ệ n qua Kafka | Theo chu ẩ n RESTful           |
| /crm/lead/import   | PATCH   | C ậ p nh ậ t c ấ u hình   | API /crm/lead/import s ử d ụng phương thứ c PATCH để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.   | Thành công <1s                 | Tích h ợ p v ớ i API Gateway   |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /crm/lead/import          | GET   | Thêm b ả n ghi          | API /crm/lead/import s ử d ụng phương thứ c GET để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                  | Thành công <1s                 | Tích h ợ p v ớ i API Gateway   |
|---------------------------|-------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| /security/firewall/config | GET   | Ki ể m tra tr ạ ng thái | API /security/firewall/config s ử d ụng phương thứ c GET để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Thông báo s ự ki ệ n qua Kafka | Có versioning v1/v2            |
| /crm/lead/import          | PATCH | Export d ữ li ệ u       | API /crm/lead/import s ử d ụng phương thứ c PATCH để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.             | Log đầ y đủ                    | Theo chu ẩ n RESTful           |
| /network/qos/monitor      | GET   | Ki ể m tra tr ạ ng thái | API /network/qos/monitor s ử d ụng phương thứ c GET để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.      | Log đầ y đủ                    | Tích h ợ p v ớ i API Gateway   |
| /security/firewall/config | POST  | Ki ể m tra tr ạ ng thái | API /security/firewall/config s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao                   | Retry t ố i đa 3 lầ n          | H ỗ tr ợ JSON và XML           |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |        |                         | d ị ch chi ti ế t.                                                                                                                  |                                |                                      |
|----------------------|--------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| /customer/update     | POST   | Export d ữ li ệ u       | API /customer/update s ử d ụng phương thứ c POST để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.          | Retry t ố i đa 3 lầ n          | Tích h ợ p v ớ i API Gateway         |
| /ivr/callflow        | DELETE | Ki ể m tra tr ạ ng thái | API /ivr/callflow s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.      | Log đầ y đủ                    | Có versioning v1/v2                  |
| /network/qos/monitor | GET    | C ậ p nh ậ t c ấ u hình | API /network/qos/monitor s ử d ụng phương thứ c GET để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Rollback khi l ỗ i             | Gi ớ i h ạ n rate-limit 1000 req/min |
| /network/qos/monitor | PUT    | Export d ữ li ệ u       | API /network/qos/monitor s ử d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.       | Thông báo s ự ki ệ n qua Kafka | H ỗ tr ợ JSON và XML                 |
| /ivr/callflow        | PATCH  | Ki ể m tra tr ạ ng thái | API /ivr/callflow s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao                          | Rollback khi l ỗ i             | Theo chu ẩ n RESTful                 |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |       |                         | d ị ch chi ti ế t.                                                                                                              |                       |                                      |
|----------------------|-------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------|-----------------------|--------------------------------------|
| /crm/lead/import     | PUT   | C ậ p nh ậ t c ấ u hình | API /crm/lead/import s ử d ụng phương thứ c PUT để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Rollback khi l ỗ i    | H ỗ tr ợ JSON và XML                 |
| /crm/lead/import     | POST  | Xóa thông tin           | API /crm/lead/import s ử d ụng phương thứ c POST để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.          | Log đầ y đủ           | Tích h ợ p v ớ i API Gateway         |
| /network/qos/monitor | PATCH | Export d ữ li ệ u       | API /network/qos/monitor s ử d ụng phương thứ c PATCH để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Retry t ố i đa 3 lầ n | Gi ớ i h ạ n rate-limit 1000 req/min |
| /ivr/callflow        | PUT   | C ậ p nh ậ t c ấ u hình | API /ivr/callflow s ử d ụng phương thứ c PUT để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.    | Thành công <1s        | Gi ớ i h ạ n rate-limit 1000 req/min |
| /ivr/callflow        | GET   | C ậ p nh ậ t c ấ u hình | API /ivr/callflow s ử d ụng phương thứ c GET để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.    | Log đầ y đủ           | H ỗ tr ợ JSON và XML                 |
| /crm/lead/import     | PATCH | Thêm                    | API /crm/lead/import                                                                                                            | Thông                 | Theo                                 |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |        | b ả n ghi               | s ử d ụng phương thứ c PATCH để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                              | báo s ự ki ệ n qua Kafka   | chu ẩ n RESTful                      |
|----------------------|--------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------|--------------------------------------|
| /rpa/task/execute    | PATCH  | Thêm b ả n ghi          | API /rpa/task/execute s ử d ụng phương thứ c PATCH để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.        | Log đầ y đủ                | Theo chu ẩ n RESTful                 |
| /ivr/callflow        | PATCH  | Export d ữ li ệ u       | API /ivr/callflow s ử d ụng phương thứ c PATCH để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.         | Retry t ố i đa 3 lầ n      | Gi ớ i h ạ n rate-limit 1000 req/min |
| /invoice/export      | PUT    | C ậ p nh ậ t c ấ u hình | API /invoice/export s ử d ụng phương thứ c PUT để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.   | Retry t ố i đa 3 lầ n      | Gi ớ i h ạ n rate-limit 1000 req/min |
| /network/qos/monitor | DELETE | Export d ữ li ệ u       | API /network/qos/monitor s ử d ụng phương thứ c DELETE để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Retry t ố i đa 3 lầ n      | Gi ớ i h ạ n rate-limit 1000 req/min |
| /crm/lead/import     | PUT    | C ậ p nh ậ t            | API /crm/lead/import s ử d ụng phương thứ c                                                                                      | Rollback                   | Theo chu ẩ n                         |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |        | c ấ u hình              | PUT để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                                                 | khi l ỗ i                      | RESTful                              |
|----------------------|--------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| /rpa/task/execute    | POST   | C ậ p nh ậ t c ấ u hình | API /rpa/task/execute s ử d ụng phương thứ c POST để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.   | Thông báo s ự ki ệ n qua Kafka | Theo chu ẩ n RESTful                 |
| /rpa/task/execute    | DELETE | Ki ể m tra tr ạ ng thái | API /rpa/task/execute s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.  | Thành công <1s                 | H ỗ tr ợ JSON và XML                 |
| /network/qos/monitor | POST   | Ki ể m tra tr ạ ng thái | API /network/qos/monitor s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Log đầ y đủ                    | Có versioning v1/v2                  |
| /customer/update     | GET    | Xóa thông tin           | API /customer/update s ử d ụng phương thứ c GET để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.               | Thành công <1s                 | Gi ớ i h ạ n rate-limit 1000 req/min |
| /rpa/task/execute    | POST   | Ki ể m tra tr ạ ng      | API /rpa/task/execute s ử d ụng phương thứ c POST để Ki ể mtra                                                                      | Thành công                     | Gi ớ i h ạ n rate-limit 1000         |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        | thái                    | tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                                                                          | <1s                   | req/min              |
|---------------------------|--------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|----------------------|
| /security/firewall/config | DELETE | Thêm b ả n ghi          | API /security/firewall/config s ử d ụng phương thứ c DELETE để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.         | Rollback khi l ỗ i    | Có versioning v1/v2  |
| /security/firewall/config | DELETE | Xóa thông tin           | API /security/firewall/config s ử d ụng phương thứ c DELETE để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.          | Log đầ y đủ           | Theo chu ẩ n RESTful |
| /customer/update          | PATCH  | Xóa thông tin           | API /customer/update s ử d ụng phương thứ c PATCH để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                    | Retry t ố i đa 3 lầ n | Có versioning v1/v2  |
| /security/firewall/config | PATCH  | C ậ p nh ậ t c ấ u hình | API /security/firewall/config s ử d ụng phương thứ c PATCH để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Rollback khi l ỗ i    | Có versioning v1/v2  |
| /network/qos/monitor      | GET    | C ậ p nh ậ t c ấ u      | API /network/qos/monitor s ử d ụng phương thứ c                                                                                            | Rollback khi l ỗ i    | Tích h ợ p v ớ i API |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |      | hình                    | GET để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                                                      |                    | Gateway                              |
|---------------------------|------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------|--------------------|--------------------------------------|
| /customer/update          | PUT  | Ki ể m tra tr ạ ng thái | API /customer/update s ử d ụng phương thứ c PUT để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.           | Log đầ y đủ        | Tích h ợ p v ớ i API Gateway         |
| /ivr/callflow             | POST | C ậ p nh ậ t c ấ u hình | API /ivr/callflow s ử d ụng phương thứ c POST để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.            | Rollback khi l ỗ i | Gi ớ i h ạ n rate-limit 1000 req/min |
| /security/firewall/config | POST | Ki ể m tra tr ạ ng thái | API /security/firewall/config s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Log đầ y đủ        | Theo chu ẩ n RESTful                 |
| /invoice/export           | POST | Export d ữ li ệ u       | API /invoice/export s ử d ụng phương thứ c POST để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                | Rollback khi l ỗ i | Gi ớ i h ạ n rate-limit 1000 req/min |
| /security/firewall/config | POST | Xóa thông               | API /security/firewall/config                                                                                                            | Retry t ố i        | H ỗ tr ợ JSON và                     |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |        | tin                     | s ử d ụng phương thứ c POST để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                               | đa 3 lầ n                      | XML                          |
|----------------------|--------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------|--------------------------------|------------------------------|
| /crm/lead/import     | POST   | Thêm b ả n ghi          | API /crm/lead/import s ử d ụng phương thứ c POST để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.         | Thành công <1s                 | H ỗ tr ợ JSON và XML         |
| /network/qos/monitor | DELETE | Thêm b ả n ghi          | API /network/qos/monitor s ử d ụng phương thứ c DELETE để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.   | Thông báo s ự ki ệ n qua Kafka | H ỗ tr ợ JSON và XML         |
| /ivr/callflow        | DELETE | Ki ể m tra tr ạ ng thái | API /ivr/callflow s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.  | Thành công <1s                 | Có versioning v1/v2          |
| /network/qos/monitor | PATCH  | Export d ữ li ệ u       | API /network/qos/monitor s ử d ụng phương thứ c PATCH để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Retry t ố i đa 3 lầ n          | Tích h ợ p v ớ i API Gateway |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /rpa/task/execute   | PATCH   | C ậ p nh ậ t c ấ u hình   | API /rpa/task/execute s ử d ụng phương thứ c PATCH để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.   | Retry t ố i đa 3 lầ n   | Tích h ợ p v ớ i API Gateway   |
|---------------------|---------|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------|
| /crm/lead/import    | GET     | Thêm b ả n ghi            | API /crm/lead/import s ử d ụng phương thứ c GET để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.               | Log đầ y đủ             | Theo chu ẩ n RESTful           |
| /invoice/export     | DELETE  | Xóa thông tin             | API /invoice/export s ử d ụng phương thứ c DELETE để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.              | Rollback khi l ỗ i      | Theo chu ẩ n RESTful           |
| /customer/update    | GET     | Ki ể m tra tr ạ ng thái   | API /customer/update s ử d ụng phương thứ c GET để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.       | Log đầ y đủ             | Có versioning v1/v2            |
| /rpa/task/execute   | POST    | Ki ể m tra tr ạ ng thái   | API /rpa/task/execute s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.     | Log đầ y đủ             | Tích h ợ p v ớ i API Gateway   |
| /crm/lead/import    | POST    | Xóa thông                 | API /crm/lead/import s ử d ụng phương thứ c POST để Xóa thông tin,                                                                   | Thành công              | Tích h ợ p v ớ i API           |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |       | tin               | có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                                                                          | <1s                   | Gateway                              |
|----------------------|-------|-------------------|------------------------------------------------------------------------------------------------------------------------------|-----------------------|--------------------------------------|
| /network/qos/monitor | PATCH | Thêm b ả n ghi    | API /network/qos/monitor s ử d ụng phương thứ c PATCH để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Retry t ố i đa 3 lầ n | Gi ớ i h ạ n rate-limit 1000 req/min |
| /ivr/callflow        | GET   | Xóa thông tin     | API /ivr/callflow s ử d ụng phương thứ c GET để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.           | Retry t ố i đa 3 lầ n | Có versioning v1/v2                  |
| /customer/update     | PATCH | Export d ữ li ệ u | API /customer/update s ử d ụng phương thứ c PATCH để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.  | Retry t ố i đa 3 lầ n | Theo chu ẩ n RESTful                 |
| /invoice/export      | POST  | Export d ữ li ệ u | API /invoice/export s ử d ụng phương thứ c POST để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.    | Thành công <1s        | Có versioning v1/v2                  |
| /invoice/export      | PUT   | Xóa thông tin     | API /invoice/export s ử d ụng phương thứ c PUT để Xóa thông tin, có xác th ự c OAuth2 và log                                 | Log đầ y đủ           | H ỗ tr ợ JSON và XML                 |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |        |                         | giao d ị ch chi ti ế t.                                                                                                          |                                |                                      |
|----------------------|--------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| /network/qos/monitor | PATCH  | Thêm b ả n ghi          | API /network/qos/monitor s ử d ụng phương thứ c PATCH để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.     | Log đầ y đủ                    | Có versioning v1/v2                  |
| /rpa/task/execute    | GET    | Ki ể m tra tr ạ ng thái | API /rpa/task/execute s ử d ụng phương thứ c GET để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.  | Log đầ y đủ                    | Gi ớ i h ạ n rate-limit 1000 req/min |
| /customer/update     | PATCH  | Xóa thông tin           | API /customer/update s ử d ụng phương thứ c PATCH để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.          | Thành công <1s                 | Gi ớ i h ạ n rate-limit 1000 req/min |
| /invoice/export      | DELETE | Ki ể m tra tr ạ ng thái | API /invoice/export s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Retry t ố i đa 3 lầ n          | Tích h ợ p v ớ i API Gateway         |
| /rpa/task/execute    | PUT    | Thêm b ả n ghi          | API /rpa/task/execute s ử d ụng phương thứ c PUT để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.          | Thông báo s ự ki ệ n qua Kafka | Có versioning v1/v2                  |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /invoice/export      | PATCH   | Xóa thông tin           | API /invoice/export s ử d ụng phương thứ c PATCH để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                | Thành công <1s        | Tích h ợ p v ớ i API Gateway         |
|----------------------|---------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------|-----------------------|--------------------------------------|
| /ivr/callflow        | DELETE  | Thêm b ả n ghi          | API /ivr/callflow s ử d ụng phương thứ c DELETE để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                | Retry t ố i đa 3 lầ n | H ỗ tr ợ JSON và XML                 |
| /crm/lead/import     | GET     | C ậ p nh ậ t c ấ u hình | API /crm/lead/import s ử d ụng phương thứ c GET để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.       | Rollback khi l ỗ i    | H ỗ tr ợ JSON và XML                 |
| /rpa/task/execute    | DELETE  | Ki ể m tra tr ạ ng thái | API /rpa/task/execute s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.    | Retry t ố i đa 3 lầ n | Gi ớ i h ạ n rate-limit 1000 req/min |
| /network/qos/monitor | PATCH   | C ậ p nh ậ t c ấ u hình | API /network/qos/monitor s ử d ụng phương thứ c PATCH để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Retry t ố i đa 3 lầ n | Tích h ợ p v ớ i API Gateway         |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /ivr/callflow     | POST   | Export d ữ li ệ u       | API /ivr/callflow s ử d ụng phương thứ c POST để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.         | Rollback khi l ỗ i             | H ỗ tr ợ JSON và XML                 |
|-------------------|--------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| /ivr/callflow     | DELETE | C ậ p nh ậ t c ấ u hình | API /ivr/callflow s ử d ụng phương thứ c DELETE để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Thông báo s ự ki ệ n qua Kafka | H ỗ tr ợ JSON và XML                 |
| /crm/lead/import  | GET    | Xóa thông tin           | API /crm/lead/import s ử d ụng phương thứ c GET để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.           | Log đầ y đủ                    | Gi ớ i h ạ n rate-limit 1000 req/min |
| /rpa/task/execute | PUT    | Xóa thông tin           | API /rpa/task/execute s ử d ụng phương thứ c PUT để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.          | Thành công <1s                 | Theo chu ẩ n RESTful                 |
| /crm/lead/import  | PATCH  | Thêm b ả n ghi          | API /crm/lead/import s ử d ụng phương thứ c PATCH để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.        | Log đầ y đủ                    | Có versioning v1/v2                  |
| /invoice/export   | PUT    | Ki ể m tra tr ạ ng      | API /invoice/export s ử d ụng phương thứ c PUT để Ki ể mtra tr ạ ng thái,                                                       | Retry t ố i đa 3 lầ n          | Theo chu ẩ n                         |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |       | thái                    | có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                                                                                |                                | RESTful                              |
|----------------------|-------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| /ivr/callflow        | PATCH | Ki ể m tra tr ạ ng thái | API /ivr/callflow s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.      | Retry t ố i đa 3 lầ n          | H ỗ tr ợ JSON và XML                 |
| /invoice/export      | GET   | Ki ể m tra tr ạ ng thái | API /invoice/export s ử d ụng phương thứ c GET để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.      | Thông báo s ự ki ệ n qua Kafka | H ỗ tr ợ JSON và XML                 |
| /rpa/task/execute    | PATCH | C ậ p nh ậ t c ấ u hình | API /rpa/task/execute s ử d ụng phương thứ c PATCH để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Thông báo s ự ki ệ n qua Kafka | Gi ớ i h ạ n rate-limit 1000 req/min |
| /network/qos/monitor | GET   | Xóa thông tin           | API /network/qos/monitor s ử d ụng phương thứ c GET để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.          | Thành công <1s                 | H ỗ tr ợ JSON và XML                 |
| /network/qos/monitor | POST  | Export d ữ li ệ u       | API /network/qos/monitor s ử d ụng phương thứ c POST để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao                        | Thông báo s ự ki ệ n qua Kafka | H ỗ tr ợ JSON và XML                 |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        |                         | d ị ch chi ti ế t.                                                                                                                 |                                |                      |
|---------------------------|--------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|----------------------|
| /invoice/export           | PUT    | Xóa thông tin           | API /invoice/export s ử d ụng phương thứ c PUT để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.               | Rollback khi l ỗ i             | Có versioning v1/v2  |
| /security/firewall/config | DELETE | Thêm b ả n ghi          | API /security/firewall/config s ử d ụng phương thứ c DELETE để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Thông báo s ự ki ệ n qua Kafka | Theo chu ẩ n RESTful |
| /invoice/export           | PATCH  | Ki ể m tra tr ạ ng thái | API /invoice/export s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.    | Thông báo s ự ki ệ n qua Kafka | Có versioning v1/v2  |
| /network/qos/monitor      | DELETE | Export d ữ li ệ u       | API /network/qos/monitor s ử d ụng phương thứ c DELETE để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.   | Thông báo s ự ki ệ n qua Kafka | H ỗ tr ợ JSON và XML |
| /ivr/callflow             | PATCH  | Export d ữ li ệ u       | API /ivr/callflow s ử d ụng phương thứ c PATCH để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao                              | Thông báo s ự ki ệ n qua Kafka | H ỗ tr ợ JSON và XML |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        |                         | d ị ch chi ti ế t.                                                                                                                |                    |                                      |
|---------------------------|--------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------|--------------------------------------|
| /crm/lead/import          | PATCH  | C ậ p nh ậ t c ấ u hình | API /crm/lead/import s ử d ụng phương thứ c PATCH để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Thành công <1s     | Có versioning v1/v2                  |
| /ivr/callflow             | POST   | Ki ể m tra tr ạ ng thái | API /ivr/callflow s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.      | Rollback khi l ỗ i | Tích h ợ p v ớ i API Gateway         |
| /ivr/callflow             | PATCH  | Xóa thông tin           | API /ivr/callflow s ử d ụng phương thứ c PATCH để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.              | Thành công <1s     | Gi ớ i h ạ n rate-limit 1000 req/min |
| /network/qos/monitor      | DELETE | Xóa thông tin           | API /network/qos/monitor s ử d ụng phương thứ c DELETE để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.      | Log đầ y đủ        | Gi ớ i h ạ n rate-limit 1000 req/min |
| /security/firewall/config | DELETE | Ki ể m tra tr ạ ng thái | API /security/firewall/config s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao           | Rollback khi l ỗ i | H ỗ tr ợ JSON và XML                 |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        |                         | d ị ch chi ti ế t.                                                                                                                 |                                |                                      |
|---------------------------|--------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| /customer/update          | DELETE | Xóa thông tin           | API /customer/update s ử d ụng phương thứ c DELETE để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.           | Thông báo s ự ki ệ n qua Kafka | Có versioning v1/v2                  |
| /network/qos/monitor      | GET    | Thêm b ả n ghi          | API /network/qos/monitor s ử d ụng phương thứ c GET để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.         | Retry t ố i đa 3 lầ n          | Theo chu ẩ n RESTful                 |
| /crm/lead/import          | DELETE | Export d ữ li ệ u       | API /crm/lead/import s ử d ụng phương thứ c DELETE để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.       | Thành công <1s                 | Có versioning v1/v2                  |
| /invoice/export           | POST   | C ậ p nh ậ t c ấ u hình | API /invoice/export s ử d ụng phương thứ c POST để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.    | Log đầ y đủ                    | Tích h ợ p v ớ i API Gateway         |
| /security/firewall/config | GET    | Export d ữ li ệ u       | API /security/firewall/config s ử d ụng phương thứ c GET để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Log đầ y đủ                    | Gi ớ i h ạ n rate-limit 1000 req/min |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /security/firewall/config   | PATCH   | Xóa thông tin           | API /security/firewall/config s ử d ụng phương thứ c PATCH để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.   | Log đầ y đủ                    | H ỗ tr ợ JSON và XML   |
|-----------------------------|---------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|------------------------|
| /network/qos/monitor        | POST    | Export d ữ li ệ u       | API /network/qos/monitor s ử d ụng phương thứ c POST để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.     | Thông báo s ự ki ệ n qua Kafka | Theo chu ẩ n RESTful   |
| /rpa/task/execute           | DELETE  | Thêm b ả n ghi          | API /rpa/task/execute s ử d ụng phương thứ c DELETE để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.         | Thông báo s ự ki ệ n qua Kafka | Có versioning v1/v2    |
| /crm/lead/import            | PUT     | Ki ể m tra tr ạ ng thái | API /crm/lead/import s ử d ụng phương thứ c PUT để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.     | Thông báo s ự ki ệ n qua Kafka | H ỗ tr ợ JSON và XML   |
| /invoice/export             | PUT     | Thêm b ả n ghi          | API /invoice/export s ử d ụng phương thứ c PUT để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.              | Thành công <1s                 | Theo chu ẩ n RESTful   |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /ivr/callflow        | PATCH   | C ậ p nh ậ t c ấ u hình   | API /ivr/callflow s ử d ụng phương thứ c PATCH để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.   | Retry t ố i đa 3 lầ n   | Gi ớ i h ạ n rate-limit 1000 req/min   |
|----------------------|---------|---------------------------|----------------------------------------------------------------------------------------------------------------------------------|-------------------------|----------------------------------------|
| /network/qos/monitor | DELETE  | Export d ữ li ệ u         | API /network/qos/monitor s ử d ụng phương thứ c DELETE để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Rollback khi l ỗ i      | Tích h ợ p v ớ i API Gateway           |
| /customer/update     | PUT     | Xóa thông tin             | API /customer/update s ử d ụng phương thứ c PUT để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.            | Thành công <1s          | Theo chu ẩ n RESTful                   |
| /network/qos/monitor | PATCH   | Xóa thông tin             | API /network/qos/monitor s ử d ụng phương thứ c PATCH để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.      | Retry t ố i đa 3 lầ n   | Gi ớ i h ạ n rate-limit 1000 req/min   |
| /rpa/task/execute    | POST    | Xóa thông tin             | API /rpa/task/execute s ử d ụng phương thứ c POST để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.          | Retry t ố i đa 3 lầ n   | Có versioning v1/v2                    |
| /crm/lead/import     | PATCH   | Xóa thông                 | API /crm/lead/import s ử d ụng phương thứ c                                                                                      | Thông báo s ự           | Theo chu ẩ n                           |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |       | tin                     | PATCH để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                                                                | ki ệ n qua Kafka               | RESTful                              |
|---------------------------|-------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| /crm/lead/import          | PATCH | C ậ p nh ậ t c ấ u hình | API /crm/lead/import s ử d ụng phương thứ c PATCH để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.          | Thông báo s ự ki ệ n qua Kafka | H ỗ tr ợ JSON và XML                 |
| /customer/update          | PUT   | Xóa thông tin           | API /customer/update s ử d ụng phương thứ c PUT để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                      | Thông báo s ự ki ệ n qua Kafka | Gi ớ i h ạ n rate-limit 1000 req/min |
| /crm/lead/import          | POST  | Export d ữ li ệ u       | API /crm/lead/import s ử d ụng phương thứ c POST để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                 | Thông báo s ự ki ệ n qua Kafka | Theo chu ẩ n RESTful                 |
| /security/firewall/config | PATCH | C ậ p nh ậ t c ấ u hình | API /security/firewall/config s ử d ụng phương thứ c PATCH để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Retry t ố i đa 3 lầ n          | Gi ớ i h ạ n rate-limit 1000 req/min |
| /rpa/task/execute         | GET   | Thêm b ả n ghi          | API /rpa/task/execute s ử d ụng phương thứ c GET để Thêm b ả n ghi, có xác th ự c OAuth2 và                                                | Log đầ y đủ                    | Có versioning v1/v2                  |

<!-- image -->

## VIETTEL AI RACE

## QU Ả N LÝ API &amp; LOG

TD448

L ầ n ban hành: 1

|                      |       |                         | log giao d ị ch chi ti ế t.                                                                                                        |                                |                                      |
|----------------------|-------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| /network/qos/monitor | POST  | Xóa thông tin           | API /network/qos/monitor s ử d ụng phương thứ c POST để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.         | Retry t ố i đa 3 lầ n          | Gi ớ i h ạ n rate-limit 1000 req/min |
| /customer/update     | POST  | Ki ể m tra tr ạ ng thái | API /customer/update s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.    | Thông báo s ự ki ệ n qua Kafka | Theo chu ẩ n RESTful                 |
| /rpa/task/execute    | PATCH | C ậ p nh ậ t c ấ u hình | API /rpa/task/execute s ử d ụng phương thứ c PATCH để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Retry t ố i đa 3 lầ n          | H ỗ tr ợ JSON và XML                 |
| /crm/lead/import     | PUT   | Thêm b ả n ghi          | API /crm/lead/import s ử d ụng phương thứ c PUT để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.             | Retry t ố i đa 3 lầ n          | Tích h ợ p v ớ i API Gateway         |
| /invoice/export      | GET   | Xóa thông tin           | API /invoice/export s ử d ụng phương thứ c GET để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.               | Log đầ y đủ                    | H ỗ tr ợ JSON và XML                 |
| /ivr/callflow        | PUT   | Export                  | API /ivr/callflow s ử                                                                                                              | Thông                          | H ỗ tr ợ                             |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        | d ữ li ệ u              | d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                                         | báo s ự ki ệ n qua Kafka       | JSON và XML                  |
|---------------------------|--------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|------------------------------|
| /rpa/task/execute         | POST   | Xóa thông tin           | API /rpa/task/execute s ử d ụng phương thứ c POST để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                  | Log đầ y đủ                    | Theo chu ẩ n RESTful         |
| /crm/lead/import          | DELETE | C ậ p nh ậ t c ấ u hình | API /crm/lead/import s ử d ụng phương thứ c DELETE để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.       | Rollback khi l ỗ i             | Có versioning v1/v2          |
| /invoice/export           | PATCH  | Thêm b ả n ghi          | API /invoice/export s ử d ụng phương thứ c PATCH để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                  | Retry t ố i đa 3 lầ n          | Theo chu ẩ n RESTful         |
| /security/firewall/config | PUT    | C ậ p nh ậ t c ấ u hình | API /security/firewall/config s ử d ụng phương thứ c PUT để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Thông báo s ự ki ệ n qua Kafka | Tích h ợ p v ớ i API Gateway |
| /invoice/export           | POST   | C ậ p nh ậ t c ấ u      | API /invoice/export s ử d ụng phương thứ c POST để C ậ p nh ậ t c ấ u                                                                    | Thông báo s ự ki ệ n qua       | Theo chu ẩ n                 |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |     | hình                    | hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                                                                       | Kafka                          | RESTful                              |
|---------------------------|-----|-------------------------|---------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| /rpa/task/execute         | PUT | Ki ể m tra tr ạ ng thái | API /rpa/task/execute s ử d ụng phương thứ c PUT để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Rollback khi l ỗ i             | Tích h ợ p v ớ i API Gateway         |
| /network/qos/monitor      | PUT | Thêm b ả n ghi          | API /network/qos/monitor s ử d ụng phương thứ c PUT để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.      | Thông báo s ự ki ệ n qua Kafka | H ỗ tr ợ JSON và XML                 |
| /security/firewall/config | PUT | Thêm b ả n ghi          | API /security/firewall/config s ử d ụng phương thứ c PUT để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Log đầ y đủ                    | Tích h ợ p v ớ i API Gateway         |
| /crm/lead/import          | PUT | C ậ p nh ậ t c ấ u hình | API /crm/lead/import s ử d ụng phương thứ c PUT để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Thành công <1s                 | Gi ớ i h ạ n rate-limit 1000 req/min |
| /security/firewall/config | GET | Export d ữ li ệ u       | API /security/firewall/config s ử d ụng phương thứ c GET để Export d ữ li ệ u,                                                  | Rollback khi l ỗ i             | Có versioning v1/v2                  |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        |                         | có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                                                                                |                                |                                      |
|---------------------------|--------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| /rpa/task/execute         | DELETE | Ki ể m tra tr ạ ng thái | API /rpa/task/execute s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Rollback khi l ỗ i             | Gi ớ i h ạ n rate-limit 1000 req/min |
| /ivr/callflow             | POST   | Thêm b ả n ghi          | API /ivr/callflow s ử d ụng phương thứ c POST để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.               | Thành công <1s                 | H ỗ tr ợ JSON và XML                 |
| /ivr/callflow             | DELETE | C ậ p nh ậ t c ấ u hình | API /ivr/callflow s ử d ụng phương thứ c DELETE để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.    | Log đầ y đủ                    | Có versioning v1/v2                  |
| /rpa/task/execute         | DELETE | Export d ữ li ệ u       | API /rpa/task/execute s ử d ụng phương thứ c DELETE để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.      | Thông báo s ự ki ệ n qua Kafka | Theo chu ẩ n RESTful                 |
| /security/firewall/config | PUT    | Export d ữ li ệ u       | API /security/firewall/config s ử d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và                             | Thông báo s ự ki ệ n qua Kafka | Theo chu ẩ n RESTful                 |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                   |       |                         | log giao d ị ch chi ti ế t.                                                                                                      |                                |                      |
|-------------------|-------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------|--------------------------------|----------------------|
| /crm/lead/import  | POST  | C ậ p nh ậ t c ấ u hình | API /crm/lead/import s ử d ụng phương thứ c POST để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Thông báo s ự ki ệ n qua Kafka | H ỗ tr ợ JSON và XML |
| /rpa/task/execute | PATCH | Xóa thông tin           | API /rpa/task/execute s ử d ụng phương thứ c PATCH để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.         | Log đầ y đủ                    | Theo chu ẩ n RESTful |
| /invoice/export   | PATCH | Ki ể m tra tr ạ ng thái | API /invoice/export s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.  | Thành công <1s                 | H ỗ tr ợ JSON và XML |
| /crm/lead/import  | GET   | C ậ p nh ậ t c ấ u hình | API /crm/lead/import s ử d ụng phương thứ c GET để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.  | Retry t ố i đa 3 lầ n          | Có versioning v1/v2  |
| /customer/update  | GET   | Ki ể m tra tr ạ ng thái | API /customer/update s ử d ụng phương thứ c GET để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.   | Retry t ố i đa 3 lầ n          | H ỗ tr ợ JSON và XML |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /rpa/task/execute         | GET    | Thêm b ả n ghi          | API /rpa/task/execute s ử d ụng phương thứ c GET để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                     | Rollback khi l ỗ i             | Theo chu ẩ n RESTful                 |
|---------------------------|--------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| /invoice/export           | GET    | Ki ể m tra tr ạ ng thái | API /invoice/export s ử d ụng phương thứ c GET để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.               | Log đầ y đủ                    | Có versioning v1/v2                  |
| /invoice/export           | PATCH  | Thêm b ả n ghi          | API /invoice/export s ử d ụng phương thứ c PATCH để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                     | Retry t ố i đa 3 lầ n          | Tích h ợ p v ớ i API Gateway         |
| /invoice/export           | DELETE | Thêm b ả n ghi          | API /invoice/export s ử d ụng phương thứ c DELETE để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                    | Thành công <1s                 | Gi ớ i h ạ n rate-limit 1000 req/min |
| /security/firewall/config | DELETE | C ậ p nh ậ t c ấ u hình | API /security/firewall/config s ử d ụng phương thứ c DELETE để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Thông báo s ự ki ệ n qua Kafka | Gi ớ i h ạ n rate-limit 1000 req/min |
| /invoice/export           | PUT    | Xóa thông               | API /invoice/export s ử d ụng phương thứ c PUT                                                                                              | Retry t ố i                    | Theo chu ẩ n                         |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |        | tin                     | để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                                                              | đa 3 lầ n                      | RESTful                              |
|----------------------|--------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| /crm/lead/import     | POST   | Thêm b ả n ghi          | API /crm/lead/import s ử d ụng phương thứ c POST để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.            | Rollback khi l ỗ i             | H ỗ tr ợ JSON và XML                 |
| /network/qos/monitor | GET    | Thêm b ả n ghi          | API /network/qos/monitor s ử d ụng phương thứ c GET để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.         | Thành công <1s                 | Có versioning v1/v2                  |
| /ivr/callflow        | PUT    | C ậ p nh ậ t c ấ u hình | API /ivr/callflow s ử d ụng phương thứ c PUT để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.       | Thông báo s ự ki ệ n qua Kafka | Theo chu ẩ n RESTful                 |
| /rpa/task/execute    | DELETE | Ki ể m tra tr ạ ng thái | API /rpa/task/execute s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Thông báo s ự ki ệ n qua Kafka | H ỗ tr ợ JSON và XML                 |
| /rpa/task/execute    | PUT    | Thêm b ả n ghi          | API /rpa/task/execute s ử d ụng phương thứ c PUT để Thêm b ả n ghi, có xác th ự c OAuth2 và                                        | Thành công <1s                 | Gi ớ i h ạ n rate-limit 1000 req/min |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |        |                         | log giao d ị ch chi ti ế t.                                                                                                      |                                |                                      |
|----------------------|--------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| /crm/lead/import     | PATCH  | Ki ể m tra tr ạ ng thái | API /crm/lead/import s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Rollback khi l ỗ i             | Tích h ợ p v ớ i API Gateway         |
| /customer/update     | PATCH  | Xóa thông tin           | API /customer/update s ử d ụng phương thứ c PATCH để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.          | Retry t ố i đa 3 lầ n          | Theo chu ẩ n RESTful                 |
| /ivr/callflow        | POST   | Ki ể m tra tr ạ ng thái | API /ivr/callflow s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.     | Thành công <1s                 | Gi ớ i h ạ n rate-limit 1000 req/min |
| /network/qos/monitor | GET    | Xóa thông tin           | API /network/qos/monitor s ử d ụng phương thứ c GET để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.        | Thông báo s ự ki ệ n qua Kafka | Tích h ợ p v ớ i API Gateway         |
| /crm/lead/import     | DELETE | Xóa thông tin           | API /crm/lead/import s ử d ụng phương thứ c DELETE để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.         | Thông báo s ự ki ệ n qua Kafka | Tích h ợ p v ớ i API Gateway         |
| /ivr/callflow        | PUT    | Export                  | API /ivr/callflow s ử                                                                                                            | Retry t ố i                    | Theo                                 |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                   |       | d ữ li ệ u              | d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                                  | đa 3 lầ n             | chu ẩ n RESTful                      |
|-------------------|-------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------|--------------------------------------|
| /rpa/task/execute | PATCH | Ki ể m tra tr ạ ng thái | API /rpa/task/execute s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Retry t ố i đa 3 lầ n | H ỗ tr ợ JSON và XML                 |
| /rpa/task/execute | PATCH | Export d ữ li ệ u       | API /rpa/task/execute s ử d ụng phương thứ c PATCH để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.      | Rollback khi l ỗ i    | Tích h ợ p v ớ i API Gateway         |
| /crm/lead/import  | PUT   | Xóa thông tin           | API /crm/lead/import s ử d ụng phương thứ c PUT để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.             | Thành công <1s        | Theo chu ẩ n RESTful                 |
| /rpa/task/execute | PATCH | Ki ể m tra tr ạ ng thái | API /rpa/task/execute s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Retry t ố i đa 3 lầ n | Gi ớ i h ạ n rate-limit 1000 req/min |
| /crm/lead/import  | GET   | Export d ữ li ệ u       | API /crm/lead/import s ử d ụng phương thứ c GET để Export d ữ li ệ u, có xác th ự c OAuth2 và                                     | Log đầ y đủ           | Có versioning v1/v2                  |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        |                   | log giao d ị ch chi ti ế t.                                                                                                   |                                |                                      |
|---------------------------|--------|-------------------|-------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| /rpa/task/execute         | DELETE | Export d ữ li ệ u | API /rpa/task/execute s ử d ụng phương thứ c DELETE để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Thông báo s ự ki ệ n qua Kafka | Tích h ợ p v ớ i API Gateway         |
| /network/qos/monitor      | PATCH  | Thêm b ả n ghi    | API /network/qos/monitor s ử d ụng phương thứ c PATCH để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.  | Log đầ y đủ                    | Gi ớ i h ạ n rate-limit 1000 req/min |
| /invoice/export           | GET    | Export d ữ li ệ u | API /invoice/export s ử d ụng phương thứ c GET để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.      | Log đầ y đủ                    | Theo chu ẩ n RESTful                 |
| /rpa/task/execute         | DELETE | Export d ữ li ệ u | API /rpa/task/execute s ử d ụng phương thứ c DELETE để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Retry t ố i đa 3 lầ n          | Theo chu ẩ n RESTful                 |
| /security/firewall/config | PATCH  | Xóa thông tin     | API /security/firewall/config s ử d ụng phương thứ c PATCH để Xóa thông tin, có xác th ự c OAuth2                             | Thông báo s ự ki ệ n qua Kafka | Theo chu ẩ n RESTful                 |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |        |                         | và log giao d ị ch chi ti ế t.                                                                                                      |                       |                                      |
|----------------------|--------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|-----------------------|--------------------------------------|
| /customer/update     | PUT    | C ậ p nh ậ t c ấ u hình | API /customer/update s ử d ụng phương thứ c PUT để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.     | Thành công <1s        | Gi ớ i h ạ n rate-limit 1000 req/min |
| /invoice/export      | DELETE | Xóa thông tin           | API /invoice/export s ử d ụng phương thứ c DELETE để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.             | Thành công <1s        | Tích h ợ p v ớ i API Gateway         |
| /customer/update     | PUT    | Export d ữ li ệ u       | API /customer/update s ử d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.           | Thành công <1s        | Tích h ợ p v ớ i API Gateway         |
| /network/qos/monitor | POST   | Ki ể m tra tr ạ ng thái | API /network/qos/monitor s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Log đầ y đủ           | Tích h ợ p v ớ i API Gateway         |
| /invoice/export      | PUT    | Xóa thông tin           | API /invoice/export s ử d ụng phương thứ c PUT để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                | Retry t ố i đa 3 lầ n | Tích h ợ p v ớ i API Gateway         |
| /network/qos/monitor | GET    | Export                  | API                                                                                                                                 | Retry t ố i           | Tích h ợ p                           |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |      | d ữ li ệ u              | /network/qos/monitor s ử d ụng phương thứ c GET để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                | đa 3 lầ n             | v ớ i API Gateway                    |
|---------------------------|------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|--------------------------------------|
| /ivr/callflow             | GET  | Thêm b ả n ghi          | API /ivr/callflow s ử d ụng phương thứ c GET để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                      | Retry t ố i đa 3 lầ n | Gi ớ i h ạ n rate-limit 1000 req/min |
| /security/firewall/config | POST | Ki ể m tra tr ạ ng thái | API /security/firewall/config s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Thành công <1s        | H ỗ tr ợ JSON và XML                 |
| /security/firewall/config | POST | Export d ữ li ệ u       | API /security/firewall/config s ử d ụng phương thứ c POST để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.      | Log đầ y đủ           | Gi ớ i h ạ n rate-limit 1000 req/min |
| /invoice/export           | POST | Export d ữ li ệ u       | API /invoice/export s ử d ụng phương thứ c POST để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                | Thành công <1s        | Theo chu ẩ n RESTful                 |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /crm/lead/import   | PATCH   | Ki ể m tra tr ạ ng thái   | API /crm/lead/import s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.   | Retry t ố i đa 3 lầ n          | H ỗ tr ợ JSON và XML                 |
|--------------------|---------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| /rpa/task/execute  | PUT     | C ậ p nh ậ t c ấ u hình   | API /rpa/task/execute s ử d ụng phương thứ c PUT để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.   | Thông báo s ự ki ệ n qua Kafka | H ỗ tr ợ JSON và XML                 |
| /invoice/export    | PUT     | Thêm b ả n ghi            | API /invoice/export s ử d ụng phương thứ c PUT để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.              | Log đầ y đủ                    | H ỗ tr ợ JSON và XML                 |
| /crm/lead/import   | DELETE  | Thêm b ả n ghi            | API /crm/lead/import s ử d ụng phương thứ c DELETE để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.          | Thông báo s ự ki ệ n qua Kafka | Tích h ợ p v ớ i API Gateway         |
| /ivr/callflow      | PUT     | C ậ p nh ậ t c ấ u hình   | API /ivr/callflow s ử d ụng phương thứ c PUT để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.       | Retry t ố i đa 3 lầ n          | Gi ớ i h ạ n rate-limit 1000 req/min |
| /invoice/export    | PATCH   | Thêm b ả n                | API /invoice/export s ử d ụng phương thứ c PATCH để Thêm b ả n                                                                     | Thành công                     | Có versioning                        |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                   |        | ghi                     | ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                                                                       | <1s                            | v1/v2                                |
|-------------------|--------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| /rpa/task/execute | PUT    | Export d ữ li ệ u       | API /rpa/task/execute s ử d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.     | Retry t ố i đa 3 lầ n          | Có versioning v1/v2                  |
| /invoice/export   | DELETE | Thêm b ả n ghi          | API /invoice/export s ử d ụng phương thứ c DELETE để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.       | Thành công <1s                 | Tích h ợ p v ớ i API Gateway         |
| /invoice/export   | POST   | Ki ể m tra tr ạ ng thái | API /invoice/export s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Log đầ y đủ                    | Có versioning v1/v2                  |
| /customer/update  | PUT    | Thêm b ả n ghi          | API /customer/update s ử d ụng phương thứ c PUT để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.         | Thành công <1s                 | Gi ớ i h ạ n rate-limit 1000 req/min |
| /rpa/task/execute | PATCH  | Thêm b ả n ghi          | API /rpa/task/execute s ử d ụng phương thứ c PATCH để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao                         | Thông báo s ự ki ệ n qua Kafka | Theo chu ẩ n RESTful                 |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |        |                         | d ị ch chi ti ế t.                                                                                                                 |                    |                              |
|----------------------|--------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|--------------------|------------------------------|
| /network/qos/monitor | PUT    | Ki ể m tra tr ạ ng thái | API /network/qos/monitor s ử d ụng phương thứ c PUT để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Thành công <1s     | Có versioning v1/v2          |
| /invoice/export      | DELETE | Ki ể m tra tr ạ ng thái | API /invoice/export s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.   | Rollback khi l ỗ i | H ỗ tr ợ JSON và XML         |
| /ivr/callflow        | PATCH  | Ki ể m tra tr ạ ng thái | API /ivr/callflow s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.      | Log đầ y đủ        | H ỗ tr ợ JSON và XML         |
| /customer/update     | PUT    | Thêm b ả n ghi          | API /customer/update s ử d ụng phương thứ c PUT để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.             | Rollback khi l ỗ i | Có versioning v1/v2          |
| /rpa/task/execute    | DELETE | Xóa thông tin           | API /rpa/task/execute s ử d ụng phương thứ c DELETE để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.          | Log đầ y đủ        | Tích h ợ p v ớ i API Gateway |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /crm/lead/import          | DELETE   | Thêm b ả n ghi          | API /crm/lead/import s ử d ụng phương thứ c DELETE để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                | Retry t ố i đa 3 lầ n          | Gi ớ i h ạ n rate-limit 1000 req/min   |
|---------------------------|----------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|----------------------------------------|
| /crm/lead/import          | PUT      | Export d ữ li ệ u       | API /crm/lead/import s ử d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                | Thành công <1s                 | Gi ớ i h ạ n rate-limit 1000 req/min   |
| /network/qos/monitor      | POST     | Export d ữ li ệ u       | API /network/qos/monitor s ử d ụng phương thứ c POST để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.           | Rollback khi l ỗ i             | Theo chu ẩ n RESTful                   |
| /security/firewall/config | POST     | Ki ể m tra tr ạ ng thái | API /security/firewall/config s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Thông báo s ự ki ệ n qua Kafka | H ỗ tr ợ JSON và XML                   |
| /ivr/callflow             | PUT      | C ậ p nh ậ t c ấ u hình | API /ivr/callflow s ử d ụng phương thứ c PUT để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.             | Retry t ố i đa 3 lầ n          | Theo chu ẩ n RESTful                   |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /crm/lead/import          | DELETE   | C ậ p nh ậ t c ấ u hình   | API /crm/lead/import s ử d ụng phương thứ c DELETE để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.   | Retry t ố i đa 3 lầ n   | Tích h ợ p v ớ i API Gateway   |
|---------------------------|----------|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------|
| /ivr/callflow             | DELETE   | C ậ p nh ậ t c ấ u hình   | API /ivr/callflow s ử d ụng phương thứ c DELETE để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.      | Rollback khi l ỗ i      | Tích h ợ p v ớ i API Gateway   |
| /crm/lead/import          | GET      | Thêm b ả n ghi            | API /crm/lead/import s ử d ụng phương thứ c GET để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.               | Rollback khi l ỗ i      | Theo chu ẩ n RESTful           |
| /security/firewall/config | PATCH    | Export d ữ li ệ u         | API /security/firewall/config s ử d ụng phương thứ c PATCH để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Log đầ y đủ             | Có versioning v1/v2            |
| /ivr/callflow             | PUT      | Ki ể m tra tr ạ ng thái   | API /ivr/callflow s ử d ụng phương thứ c PUT để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.          | Rollback khi l ỗ i      | H ỗ tr ợ JSON và XML           |
| /network/qos/monitor      | DELETE   | Ki ể m tra                | API /network/qos/monitor                                                                                                             | Rollback                | H ỗ tr ợ JSON và               |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        | tr ạ ng thái            | s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                      | khi l ỗ i                      | XML                                  |
|---------------------------|--------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| /invoice/export           | DELETE | Xóa thông tin           | API /invoice/export s ử d ụng phương thứ c DELETE để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.           | Retry t ố i đa 3 lầ n          | Có versioning v1/v2                  |
| /network/qos/monitor      | POST   | Thêm b ả n ghi          | API /network/qos/monitor s ử d ụng phương thứ c POST để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.       | Retry t ố i đa 3 lầ n          | Gi ớ i h ạ n rate-limit 1000 req/min |
| /security/firewall/config | DELETE | Xóa thông tin           | API /security/firewall/config s ử d ụng phương thứ c DELETE để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Thông báo s ự ki ệ n qua Kafka | Theo chu ẩ n RESTful                 |
| /invoice/export           | DELETE | C ậ p nh ậ t c ấ u hình | API /invoice/export s ử d ụng phương thứ c DELETE để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Thành công <1s                 | Theo chu ẩ n RESTful                 |
| /customer/update          | PATCH  | Xóa thông               | API /customer/update s ử d ụng phương thứ c                                                                                       | Rollback                       | Tích h ợ p v ớ i API                 |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        | tin                     | PATCH để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                                                                 | khi l ỗ i             | Gateway                      |
|---------------------------|--------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|------------------------------|
| /ivr/callflow             | POST   | C ậ p nh ậ t c ấ u hình | API /ivr/callflow s ử d ụng phương thứ c POST để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.               | Retry t ố i đa 3 lầ n | Có versioning v1/v2          |
| /security/firewall/config | DELETE | C ậ p nh ậ t c ấ u hình | API /security/firewall/config s ử d ụng phương thứ c DELETE để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Retry t ố i đa 3 lầ n | Tích h ợ p v ớ i API Gateway |
| /customer/update          | DELETE | Ki ể m tra tr ạ ng thái | API /customer/update s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.           | Retry t ố i đa 3 lầ n | Có versioning v1/v2          |
| /customer/update          | PATCH  | Ki ể m tra tr ạ ng thái | API /customer/update s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.            | Log đầ y đủ           | Theo chu ẩ n RESTful         |
| /security/firewall/config | POST   | Export d ữ              | API /security/firewall/config s ử d ụng phương thứ c                                                                                        | Log đầ y đủ           | Tích h ợ p v ớ i API         |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                  |        | li ệ u                  | POST để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                                                    |                                | Gateway                              |
|------------------|--------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| /crm/lead/import | DELETE | Ki ể m tra tr ạ ng thái | API /crm/lead/import s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Retry t ố i đa 3 lầ n          | H ỗ tr ợ JSON và XML                 |
| /crm/lead/import | PATCH  | Ki ể m tra tr ạ ng thái | API /crm/lead/import s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.  | Log đầ y đủ                    | Có versioning v1/v2                  |
| /customer/update | PUT    | Export d ữ li ệ u       | API /customer/update s ử d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.         | Thông báo s ự ki ệ n qua Kafka | Tích h ợ p v ớ i API Gateway         |
| /invoice/export  | GET    | Export d ữ li ệ u       | API /invoice/export s ử d ụng phương thứ c GET để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.          | Thông báo s ự ki ệ n qua Kafka | Gi ớ i h ạ n rate-limit 1000 req/min |
| /customer/update | POST   | Thêm b ả n ghi          | API /customer/update s ử d ụng phương thứ c POST để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao                              | Retry t ố i đa 3 lầ n          | H ỗ tr ợ JSON và XML                 |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                   |        |                         | d ị ch chi ti ế t.                                                                                                               |                       |                              |
|-------------------|--------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------|-----------------------|------------------------------|
| /crm/lead/import  | DELETE | Xóa thông tin           | API /crm/lead/import s ử d ụng phương thứ c DELETE để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.         | Thành công <1s        | Có versioning v1/v2          |
| /rpa/task/execute | GET    | Thêm b ả n ghi          | API /rpa/task/execute s ử d ụng phương thứ c GET để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.          | Retry t ố i đa 3 lầ n | Có versioning v1/v2          |
| /ivr/callflow     | POST   | Thêm b ả n ghi          | API /ivr/callflow s ử d ụng phương thứ c POST để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.             | Retry t ố i đa 3 lầ n | Tích h ợ p v ớ i API Gateway |
| /customer/update  | PATCH  | Ki ể m tra tr ạ ng thái | API /customer/update s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Thành công <1s        | H ỗ tr ợ JSON và XML         |