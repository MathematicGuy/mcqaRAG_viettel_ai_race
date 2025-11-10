<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

| Module   | Lo ạ i log     | M ức độ   | Hành độ ng          | Mô t ả chi ti ế t                                                                                                   | K ế t qu ả                 | Ghi chú                     |
|----------|----------------|-----------|---------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------|-----------------------------|
| RPA      | TransactionLog | Critical  | Xu ấ t log          | H ệ th ố ng RPA Xu ấ t log lo ạ i TransactionLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.      | Có ch ỉ s ố th ố ng kê     | G ử i log sang ELK          |
| CRM      | TransactionLog | Error     | Nén và lưu tr ữ log | H ệ th ố ng CRM Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Có ch ỉ s ố th ố ng kê     | Theo chu ẩ n syslog RFC5424 |
| Billing  | PerformanceLog | Error     | Phân tích log       | H ệ th ố ng Billing Phân tích log lo ạ i PerformanceLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.  | Không m ấ t mát d ữ li ệ u | Có dashboard Grafana        |
| Infra    | TransactionLog | Critical  | Xóa log             | H ệ th ố ng Infra Xóa log lo ạ i TransactionLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.       | Không m ấ t mát d ữ li ệ u | Theo chu ẩ n syslog RFC5424 |
| QA       | AuditLog       | Warning   | Xu ấ t              | H ệ th ố ng QA Xu ấ t                                                                                               | Không                      | Có dashboard                |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|         |                |         | log                 | log lo ạ i AuditLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                                     | m ấ t mát d ữ li ệ u           | Grafana                        |
|---------|----------------|---------|---------------------|----------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| IPCC    | PerformanceLog | Fatal   | Nén và lưu tr ữ log | H ệ th ố ng IPCC Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Tích h ợ p c ả nh báo realtime | Có dashboard Grafana           |
| IPCC    | ErrorLog       | Info    | Xóa log             | H ệ th ố ng IPCC Xóa log lo ạ i ErrorLog v ớ im ứ c Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.                  | Log đượ c mã hóa AES- 256      | Có dashboard Grafana           |
| Billing | ErrorLog       | Warning | Xóa log             | H ệ th ố ng Billing Xóa log lo ạ i ErrorLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.            | Có th ể truy xu ấ t khi c ầ n  | T ự độ ng xóa log sau 180 ngày |
| CRM     | AuditLog       | Error   | G ử i log sang SIEM | H ệ th ố ng CRM G ử i log sang SIEM lo ạ i AuditLog v ớ i m ứ c Error, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.     | Tích h ợ p c ả nh báo realtime | Theo chu ẩ n syslog RFC5424    |
| Infra   | AuditLog       | Error   | G ử i log           | H ệ th ố ng Infra G ử i log sang SIEM lo ạ i                                                                         | Không m ấ t mát                | Theo chu ẩ n syslog            |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|         |                |       | sang SIEM           | AuditLog v ớ im ứ c Error, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.                                           | d ữ li ệ u                    | RFC5424                        |
|---------|----------------|-------|---------------------|----------------------------------------------------------------------------------------------------------------|-------------------------------|--------------------------------|
| RPA     | PerformanceLog | Fatal | Xu ấ t log          | H ệ th ố ng RPA Xu ấ t log lo ạ i PerformanceLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.    | Có th ể truy xu ấ t khi c ầ n | T ự độ ng xóa log sau 180 ngày |
| QA      | AccessLog      | Info  | Nén và lưu tr ữ log | H ệ th ố ng QA Nén và lưu trữ log lo ạ i AccessLog v ớ i m ứ c Info, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày. | Log đượ c mã hóa AES- 256     | T ự độ ng xóa log sau 180 ngày |
| Billing | ErrorLog       | Info  | Xu ấ t log          | H ệ th ố ng Billing Xu ấ t log lo ạ i ErrorLog v ớ im ứ c Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.      | Có ch ỉ s ố th ố ng kê        | Phân quy ề n chi ti ế t        |
| IVR     | TransactionLog | Fatal | Xóa log             | H ệ th ố ng IVR Xóa log lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.       | Có ch ỉ s ố th ố ng kê        | Phân quy ề n chi ti ế t        |
| IVR     | PerformanceLog | Error | Xóa log             | H ệ th ố ng IVR Xóa log lo ạ i PerformanceLog                                                                  | Có ch ỉ s ố th ố ng           | G ử i log sang ELK             |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|       |           |          |                     | v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                                                       | kê                             |                             |
|-------|-----------|----------|---------------------|------------------------------------------------------------------------------------------------------------------|--------------------------------|-----------------------------|
| IPCC  | AuditLog  | Error    | Nén và lưu tr ữ log | H ệ th ố ng IPCC Nén và lưu trữ log lo ạ i AuditLog v ớ i m ứ c Error, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày. | Có th ể truy xu ấ t khi c ầ n  | Theo chu ẩ n syslog RFC5424 |
| Infra | AccessLog | Warning  | Xu ấ t log          | H ệ th ố ng Infra Xu ấ t log lo ạ i AccessLog v ớ i m ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.      | Có ch ỉ s ố th ố ng kê         | G ử i log sang ELK          |
| QA    | AccessLog | Warning  | Nén và lưu tr ữ log | H ệ th ố ng QA Nén và lưu trữ log lo ạ i AccessLog v ớ i m ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Tích h ợ p c ả nh báo realtime | Phân quy ề n chi ti ế t     |
| Infra | ErrorLog  | Critical | Xu ấ t log          | H ệ th ố ng Infra Xu ấ t log lo ạ i ErrorLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.      | Có th ể truy xu ấ t khi c ầ n  | G ử i log sang ELK          |
| QA    | AuditLog  | Error    | Xóa log             | H ệ th ố ng QA Xóa log lo ạ i AuditLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i                                 | Tích h ợ p c ả nh báo          | Phân quy ề n chi ti ế t     |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|       |                |          |                     | thi ể u 90 ngày.                                                                                                     | realtime                       |                                |
|-------|----------------|----------|---------------------|----------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| CRM   | AuditLog       | Fatal    | Xóa log             | H ệ th ố ng CRM Xóa log lo ạ i AuditLog v ớ im ứ c Fatal, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.                  | Có ch ỉ s ố th ố ng kê         | Phân quy ề n chi ti ế t        |
| CRM   | PerformanceLog | Warning  | Xu ấ t log          | H ệ th ố ng CRM Xu ấ t log lo ạ i PerformanceLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.        | Có ch ỉ s ố th ố ng kê         | Theo chu ẩ n syslog RFC5424    |
| Infra | TransactionLog | Critical | Xu ấ t log          | H ệ th ố ng Infra Xu ấ t log lo ạ i TransactionLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.     | Tích h ợ p c ả nh báo realtime | T ự độ ng xóa log sau 180 ngày |
| IPCC  | TransactionLog | Error    | Nén và lưu tr ữ log | H ệ th ố ng IPCC Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Tích h ợ p c ả nh báo realtime | Phân quy ề n chi ti ế t        |
| IPCC  | PerformanceLog | Fatal    | Xóa log             | H ệ th ố ng IPCC Xóa log lo ạ i PerformanceLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i                             | Có ch ỉ s ố th ố ng kê         | Phân quy ề n chi ti ế t        |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|         |                |          |                     | thi ể u 90 ngày.                                                                                                 |                            |                                |
|---------|----------------|----------|---------------------|------------------------------------------------------------------------------------------------------------------|----------------------------|--------------------------------|
| Billing | AccessLog      | Fatal    | Phân tích log       | H ệ th ố ng Billing Phân tích log lo ạ i AccessLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.  | Log đượ c mã hóa AES- 256  | T ự độ ng xóa log sau 180 ngày |
| RPA     | ErrorLog       | Fatal    | Xóa log             | H ệ th ố ng RPA Xóa log lo ạ i ErrorLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.               | Log đượ c mã hóa AES- 256  | Có dashboard Grafana           |
| Infra   | TransactionLog | Info     | Xu ấ t log          | H ệ th ố ng Infra Xu ấ t log lo ạ i TransactionLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.     | Không m ấ t mát d ữ li ệ u | Theo chu ẩ n syslog RFC5424    |
| IVR     | ErrorLog       | Warning  | Xu ấ t log          | H ệ th ố ng IVR Xu ấ t log lo ạ i ErrorLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.          | Log đượ c mã hóa AES- 256  | Có dashboard Grafana           |
| QA      | AuditLog       | Warning  | G ử i log sang SIEM | H ệ th ố ng QA G ử i log sang SIEM lo ạ i AuditLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày. | Có ch ỉ s ố th ố ng kê     | T ự độ ng xóa log sau 180 ngày |
| Infra   | PerformanceLog | Critical | Phân                | H ệ th ố ng Infra                                                                                                | Có ch ỉ                    | Theo chu ẩ n                   |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|       |                |          | tích log            | Phân tích log lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                    | s ố th ố ng kê                 | syslog RFC5424          |
|-------|----------------|----------|---------------------|----------------------------------------------------------------------------------------------------------------------|--------------------------------|-------------------------|
| QA    | AuditLog       | Critical | Xu ấ t log          | H ệ th ố ng QA Xu ấ t log lo ạ i AuditLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.              | Log đượ c mã hóa AES- 256      | G ử i log sang ELK      |
| IPCC  | TransactionLog | Error    | Nén và lưu tr ữ log | H ệ th ố ng IPCC Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Tích h ợ p c ả nh báo realtime | G ử i log sang ELK      |
| RPA   | PerformanceLog | Critical | Phân tích log       | H ệ th ố ng RPA Phân tích log lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.    | Có ch ỉ s ố th ố ng kê         | Có dashboard Grafana    |
| Infra | AuditLog       | Info     | Xóa log             | H ệ th ố ng Infra Xóa log lo ạ i AuditLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                  | Log đượ c mã hóa AES- 256      | Có dashboard Grafana    |
| RPA   | ErrorLog       | Fatal    | Xóa log             | H ệ th ố ng RPA Xóa log lo ạ i ErrorLog v ớ im ứ c Fatal, d ữ                                                        | Tích h ợ p c ả nh              | Phân quy ề n chi ti ế t |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|         |                |          |                     | li ệu lưu trữ t ố i thi ể u 90 ngày.                                                                                    | báo realtime                   |                             |
|---------|----------------|----------|---------------------|-------------------------------------------------------------------------------------------------------------------------|--------------------------------|-----------------------------|
| Billing | ErrorLog       | Info     | G ử i log sang SIEM | H ệ th ố ng Billing G ử i log sang SIEM lo ạ i ErrorLog v ớ i m ứ c Info, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.     | Tích h ợ p c ả nh báo realtime | Phân quy ề n chi ti ế t     |
| CRM     | PerformanceLog | Critical | G ử i log sang SIEM | H ệ th ố ng CRM G ử i log sang SIEM lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Log đượ c mã hóa AES- 256      | G ử i log sang ELK          |
| Billing | TransactionLog | Error    | Nén và lưu tr ữ log | H ệ th ố ng Billing Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Log đượ c mã hóa AES- 256      | G ử i log sang ELK          |
| CRM     | TransactionLog | Error    | Phân tích log       | H ệ th ố ng CRM Phân tích log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.          | Tích h ợ p c ả nh báo realtime | Theo chu ẩ n syslog RFC5424 |
| IVR     | AuditLog       | Critical | Xu ấ t log          | H ệ th ố ng IVR Xu ấ t log lo ạ i AuditLog v ớ im ứ c Critical,                                                         | Không m ấ t mát                | G ử i log sang ELK          |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|       |                |          |                     | d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                                                                                | d ữ li ệ u                    |                                |
|-------|----------------|----------|---------------------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------|--------------------------------|
| CRM   | ErrorLog       | Info     | Xu ấ t log          | H ệ th ố ng CRM Xu ấ t log lo ạ i ErrorLog v ớ im ứ c Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.                   | Không m ấ t mát d ữ li ệ u    | T ự độ ng xóa log sau 180 ngày |
| IPCC  | ErrorLog       | Fatal    | Phân tích log       | H ệ th ố ng IPCC Phân tích log lo ạ i ErrorLog v ớ im ứ c Fatal, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.              | Không m ấ t mát d ữ li ệ u    | T ự độ ng xóa log sau 180 ngày |
| QA    | AuditLog       | Error    | Nén và lưu tr ữ log | H ệ th ố ng QA Nén và lưu trữ log lo ạ i AuditLog v ớ im ứ c Error, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.           | Log đượ c mã hóa AES- 256     | T ự độ ng xóa log sau 180 ngày |
| CRM   | TransactionLog | Critical | G ử i log sang SIEM | H ệ th ố ng CRM G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Có th ể truy xu ấ t khi c ầ n | T ự độ ng xóa log sau 180 ngày |
| Infra | ErrorLog       | Warning  | Nén và lưu tr ữ     | H ệ th ố ng Infra Nén và lưu trữ log lo ạ i ErrorLog v ớ im ứ c Warning, d ữ li ệ u                                     | Log đượ c mã hóa AES-         | Theo chu ẩ n syslog RFC5424    |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|         |                |         | log                 | lưu trữ t ố i thi ể u 90 ngày.                                                                                       | 256                            |                             |
|---------|----------------|---------|---------------------|----------------------------------------------------------------------------------------------------------------------|--------------------------------|-----------------------------|
| RPA     | TransactionLog | Error   | G ử i log sang SIEM | H ệ th ố ng RPA G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Có th ể truy xu ấ t khi c ầ n  | Theo chu ẩ n syslog RFC5424 |
| QA      | ErrorLog       | Error   | Xu ấ t log          | H ệ th ố ng QA Xu ấ t log lo ạ i ErrorLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                 | Không m ấ t mát d ữ li ệ u     | G ử i log sang ELK          |
| QA      | AccessLog      | Info    | Xu ấ t log          | H ệ th ố ng QA Xu ấ t log lo ạ i AccessLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                 | Không m ấ t mát d ữ li ệ u     | Phân quy ề n chi ti ế t     |
| CRM     | AccessLog      | Fatal   | G ử i log sang SIEM | H ệ th ố ng CRM G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.    | Tích h ợ p c ả nh báo realtime | Theo chu ẩ n syslog RFC5424 |
| Billing | PerformanceLog | Warning | Nén và lưu tr ữ log | H ệ th ố ng Billing Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i             | Tích h ợ p c ả nh báo realtime | Có dashboard Grafana        |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|         |           |         |                     | thi ể u 90 ngày.                                                                                                     |                                |                                |
|---------|-----------|---------|---------------------|----------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| IPCC    | AccessLog | Error   | G ử i log sang SIEM | H ệ th ố ng IPCC G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Error, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.   | Log đượ c mã hóa AES- 256      | Có dashboard Grafana           |
| Billing | AuditLog  | Warning | Xu ấ t log          | H ệ th ố ng Billing Xu ấ t log lo ạ i AuditLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.         | Không m ấ t mát d ữ li ệ u     | Có dashboard Grafana           |
| Billing | AuditLog  | Error   | Xu ấ t log          | H ệ th ố ng Billing Xu ấ t log lo ạ i AuditLog v ớ im ứ c Error, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.           | Không m ấ t mát d ữ li ệ u     | T ự độ ng xóa log sau 180 ngày |
| Billing | AccessLog | Fatal   | Nén và lưu tr ữ log | H ệ th ố ng Billing Nén và lưu trữ log lo ạ i AccessLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày. | Tích h ợ p c ả nh báo realtime | T ự độ ng xóa log sau 180 ngày |
| CRM     | AccessLog | Warning | Nén và lưu tr ữ log | H ệ th ố ng CRM Nén và lưu trữ log lo ạ i AccessLog v ớ i m ứ c Warning, d ữ li ệu lưu trữ t ố i                     | Tích h ợ p c ả nh báo realtime | T ự độ ng xóa log sau 180 ngày |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|       |                |          |                     | thi ể u 90 ngày.                                                                                                |                                |                                |
|-------|----------------|----------|---------------------|-----------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| Infra | AccessLog      | Fatal    | Phân tích log       | H ệ th ố ng Infra Phân tích log lo ạ i AccessLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.   | Tích h ợ p c ả nh báo realtime | Có dashboard Grafana           |
| IPCC  | TransactionLog | Info     | Xóa log             | H ệ th ố ng IPCC Xóa log lo ạ i TransactionLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.        | Log đượ c mã hóa AES- 256      | T ự độ ng xóa log sau 180 ngày |
| QA    | AccessLog      | Error    | Nén và lưu tr ữ log | H ệ th ố ng QA Nén và lưu trữ log lo ạ i AccessLog v ớ i m ứ c Error, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày. | Có ch ỉ s ố th ố ng kê         | Có dashboard Grafana           |
| IPCC  | ErrorLog       | Error    | Phân tích log       | H ệ th ố ng IPCC Phân tích log lo ạ i ErrorLog v ớ im ứ c Error, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.      | Tích h ợ p c ả nh báo realtime | G ử i log sang ELK             |
| Infra | ErrorLog       | Critical | Phân tích log       | H ệ th ố ng Infra Phân tích log lo ạ i ErrorLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90        | Không m ấ t mát d ữ li ệ u     | Phân quy ề n chi ti ế t        |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|         |                |         |                     | ngày.                                                                                                               |                            |                                |
|---------|----------------|---------|---------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------|--------------------------------|
| IVR     | AccessLog      | Warning | Phân tích log       | H ệ th ố ng IVR Phân tích log lo ạ i AccessLog v ớ i m ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.        | Không m ấ t mát d ữ li ệ u | Có dashboard Grafana           |
| IVR     | TransactionLog | Error   | Nén và lưu tr ữ log | H ệ th ố ng IVR Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Có ch ỉ s ố th ố ng kê     | Theo chu ẩ n syslog RFC5424    |
| QA      | ErrorLog       | Error   | G ử i log sang SIEM | H ệ th ố ng QA G ử i log sang SIEM lo ạ i ErrorLog v ớ im ứ c Error, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.      | Log đượ c mã hóa AES- 256  | G ử i log sang ELK             |
| RPA     | TransactionLog | Fatal   | Phân tích log       | H ệ th ố ng RPA Phân tích log lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.      | Có ch ỉ s ố th ố ng kê     | T ự độ ng xóa log sau 180 ngày |
| Billing | AccessLog      | Fatal   | G ử i log sang SIEM | H ệ th ố ng Billing G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90     | Không m ấ t mát d ữ li ệ u | T ự độ ng xóa log sau 180 ngày |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|         |                |       |                     | ngày.                                                                                                               |                               |                             |
|---------|----------------|-------|---------------------|---------------------------------------------------------------------------------------------------------------------|-------------------------------|-----------------------------|
| CRM     | TransactionLog | Info  | Phân tích log       | H ệ th ố ng CRM Phân tích log lo ạ i TransactionLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.       | Có ch ỉ s ố th ố ng kê        | G ử i log sang ELK          |
| Billing | ErrorLog       | Info  | Nén và lưu tr ữ log | H ệ th ố ng Billing Nén và lưu trữ log lo ạ i ErrorLog v ớ i m ứ c Info, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.  | Có ch ỉ s ố th ố ng kê        | Theo chu ẩ n syslog RFC5424 |
| RPA     | TransactionLog | Fatal | Nén và lưu tr ữ log | H ệ th ố ng RPA Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Có th ể truy xu ấ t khi c ầ n | G ử i log sang ELK          |
| Infra   | ErrorLog       | Info  | Xóa log             | H ệ th ố ng Infra Xóa log lo ạ i ErrorLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                 | Log đượ c mã hóa AES- 256     | Có dashboard Grafana        |
| IVR     | ErrorLog       | Info  | Nén và lưu tr ữ log | H ệ th ố ng IVR Nén và lưu trữ log lo ạ i ErrorLog v ớ im ứ c Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.       | Không m ấ t mát d ữ li ệ u    | Theo chu ẩ n syslog RFC5424 |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

| IPCC   | AuditLog       | Error   | G ử i log sang SIEM   | H ệ th ố ng IPCC G ử i log sang SIEM lo ạ i AuditLog v ớ i m ứ c Error, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.   | Tích h ợ p c ả nh báo realtime   | Phân quy ề n chi ti ế t     |
|--------|----------------|---------|-----------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------|-----------------------------|
| QA     | TransactionLog | Fatal   | G ử i log sang SIEM   | H ệ th ố ng QA G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Có th ể truy xu ấ t khi c ầ n    | Có dashboard Grafana        |
| Infra  | AuditLog       | Warning | Xóa log               | H ệ th ố ng Infra Xóa log lo ạ i AuditLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.              | Có th ể truy xu ấ t khi c ầ n    | Theo chu ẩ n syslog RFC5424 |
| IVR    | ErrorLog       | Warning | G ử i log sang SIEM   | H ệ th ố ng IVR G ử i log sang SIEM lo ạ i ErrorLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.   | Tích h ợ p c ả nh báo realtime   | Theo chu ẩ n syslog RFC5424 |
| IVR    | AuditLog       | Fatal   | Xu ấ t log            | H ệ th ố ng IVR Xu ấ t log lo ạ i AuditLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.               | Không m ấ t mát d ữ li ệ u       | Có dashboard Grafana        |
| Infra  | PerformanceLog | Info    | Nén và lưu            | H ệ th ố ng Infra Nén và lưu trữ log lo ạ i PerformanceLog                                                          | Không m ấ t mát                  | Phân quy ề n chi ti ế t     |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|         |                |          | tr ữ log            | v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                                                               | d ữ li ệ u                     |                                |
|---------|----------------|----------|---------------------|-------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| Billing | PerformanceLog | Error    | Xu ấ t log          | H ệ th ố ng Billing Xu ấ t log lo ạ i PerformanceLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.         | Log đượ c mã hóa AES- 256      | G ử i log sang ELK             |
| CRM     | TransactionLog | Error    | Nén và lưu tr ữ log | H ệ th ố ng CRM Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.     | Có th ể truy xu ấ t khi c ầ n  | Có dashboard Grafana           |
| QA      | TransactionLog | Fatal    | Xu ấ t log          | H ệ th ố ng QA Xu ấ t log lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.              | Có ch ỉ s ố th ố ng kê         | Phân quy ề n chi ti ế t        |
| RPA     | TransactionLog | Critical | G ử i log sang SIEM | H ệ th ố ng RPA G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Tích h ợ p c ả nh báo realtime | T ự độ ng xóa log sau 180 ngày |
| QA      | TransactionLog | Critical | Phân tích           | H ệ th ố ng QA Phân tích log lo ạ i TransactionLog                                                                      | Có ch ỉ s ố th ố ng            | Theo chu ẩ n syslog            |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|         |                |          | log                 | v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                                                              | kê                            | RFC5424                        |
|---------|----------------|----------|---------------------|----------------------------------------------------------------------------------------------------------------------------|-------------------------------|--------------------------------|
| CRM     | AccessLog      | Fatal    | G ử i log sang SIEM | H ệ th ố ng CRM G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.          | Log đượ c mã hóa AES- 256     | T ự độ ng xóa log sau 180 ngày |
| Billing | PerformanceLog | Critical | Nén và lưu tr ữ log | H ệ th ố ng Billing Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Có th ể truy xu ấ t khi c ầ n | Phân quy ề n chi ti ế t        |
| QA      | TransactionLog | Error    | Xu ấ t log          | H ệ th ố ng QA Xu ấ t log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                 | Có ch ỉ s ố th ố ng kê        | G ử i log sang ELK             |
| Billing | AccessLog      | Info     | Xóa log             | H ệ th ố ng Billing Xóa log lo ạ i AccessLog v ớ i m ứ c Info, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.                   | Không m ấ t mát d ữ li ệ u    | Có dashboard Grafana           |
| CRM     | AuditLog       | Warning  | Nén và lưu          | H ệ th ố ng CRM Nén và lưu trữ log lo ạ i AuditLog v ớ i                                                                   | Có ch ỉ s ố th ố ng           | Phân quy ề n chi ti ế t        |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|         |                |       | tr ữ log            | m ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                                                                | kê                            |                                |
|---------|----------------|-------|---------------------|------------------------------------------------------------------------------------------------------------------------|-------------------------------|--------------------------------|
| Billing | AccessLog      | Info  | Xóa log             | H ệ th ố ng Billing Xóa log lo ạ i AccessLog v ớ i m ứ c Info, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.               | Có ch ỉ s ố th ố ng kê        | T ự độ ng xóa log sau 180 ngày |
| IVR     | AccessLog      | Error | Xóa log             | H ệ th ố ng IVR Xóa log lo ạ i AccessLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                    | Không m ấ t mát d ữ li ệ u    | T ự độ ng xóa log sau 180 ngày |
| IVR     | AccessLog      | Error | Xóa log             | H ệ th ố ng IVR Xóa log lo ạ i AccessLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                    | Có th ể truy xu ấ t khi c ầ n | G ử i log sang ELK             |
| Billing | TransactionLog | Info  | Nén và lưu tr ữ log | H ệ th ố ng Billing Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Không m ấ t mát d ữ li ệ u    | G ử i log sang ELK             |
| Billing | TransactionLog | Error | Xóa log             | H ệ th ố ng Billing Xóa log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i                            | Log đượ c mã hóa AES-         | Phân quy ề n chi ti ế t        |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|         |                |          |                     | thi ể u 90 ngày.                                                                                                          | 256                            |                             |
|---------|----------------|----------|---------------------|---------------------------------------------------------------------------------------------------------------------------|--------------------------------|-----------------------------|
| Infra   | AccessLog      | Info     | Xóa log             | H ệ th ố ng Infra Xóa log lo ạ i AccessLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                      | Có ch ỉ s ố th ố ng kê         | G ử i log sang ELK          |
| RPA     | ErrorLog       | Critical | Xóa log             | H ệ th ố ng RPA Xóa log lo ạ i ErrorLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                     | Log đượ c mã hóa AES- 256      | G ử i log sang ELK          |
| Billing | TransactionLog | Warning  | Nén và lưu tr ữ log | H ệ th ố ng Billing Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Tích h ợ p c ả nh báo realtime | Theo chu ẩ n syslog RFC5424 |
| Infra   | PerformanceLog | Fatal    | Xóa log             | H ệ th ố ng Infra Xóa log lo ạ i PerformanceLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                | Có th ể truy xu ấ t khi c ầ n  | Có dashboard Grafana        |
| Infra   | TransactionLog | Warning  | G ử i log sang SIEM | H ệ th ố ng Infra G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.  | Không m ấ t mát d ữ li ệ u     | Phân quy ề n chi ti ế t     |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

| IPCC    | PerformanceLog   | Critical   | Nén và lưu tr ữ log   | H ệ th ố ng IPCC Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.   | Tích h ợ p c ả nh báo realtime   | Phân quy ề n chi ti ế t   |
|---------|------------------|------------|-----------------------|---------------------------------------------------------------------------------------------------------------------------|----------------------------------|---------------------------|
| IPCC    | TransactionLog   | Error      | G ử i log sang SIEM   | H ệ th ố ng IPCC G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.     | Tích h ợ p c ả nh báo realtime   | Có dashboard Grafana      |
| RPA     | AccessLog        | Fatal      | G ử i log sang SIEM   | H ệ th ố ng RPA G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.         | Có ch ỉ s ố th ố ng kê           | G ử i log sang ELK        |
| IVR     | AccessLog        | Critical   | Phân tích log         | H ệ th ố ng IVR Phân tích log lo ạ i AccessLog v ớ i m ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.             | Tích h ợ p c ả nh báo realtime   | Phân quy ề n chi ti ế t   |
| Billing | AuditLog         | Critical   | Xóa log               | H ệ th ố ng Billing Xóa log lo ạ i AuditLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90                      | Có ch ỉ s ố th ố ng kê           | G ử i log sang ELK        |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|         |                |          |                     | ngày.                                                                                                                   |                                |                                |
|---------|----------------|----------|---------------------|-------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| QA      | AccessLog      | Fatal    | G ử i log sang SIEM | H ệ th ố ng QA G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.        | Tích h ợ p c ả nh báo realtime | Có dashboard Grafana           |
| Billing | TransactionLog | Info     | G ử i log sang SIEM | H ệ th ố ng Billing G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Có th ể truy xu ấ t khi c ầ n  | T ự độ ng xóa log sau 180 ngày |
| Billing | AccessLog      | Warning  | Nén và lưu tr ữ log | H ệ th ố ng Billing Nén và lưu trữ log lo ạ i AccessLog v ớ i m ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.   | Log đượ c mã hóa AES- 256      | Phân quy ề n chi ti ế t        |
| IPCC    | ErrorLog       | Error    | Xóa log             | H ệ th ố ng IPCC Xóa log lo ạ i ErrorLog v ớ im ứ c Error, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.                    | Tích h ợ p c ả nh báo realtime | T ự độ ng xóa log sau 180 ngày |
| RPA     | TransactionLog | Critical | Phân tích log       | H ệ th ố ng RPA Phân tích log lo ạ i TransactionLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i                        | Có th ể truy xu ấ t khi c ầ n  | G ử i log sang ELK             |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|         |                |         |                     | thi ể u 90 ngày.                                                                                                  |                                |                                |
|---------|----------------|---------|---------------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| Billing | AuditLog       | Error   | Phân tích log       | H ệ th ố ng Billing Phân tích log lo ạ i AuditLog v ớ im ứ c Error, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.     | Có ch ỉ s ố th ố ng kê         | Phân quy ề n chi ti ế t        |
| QA      | TransactionLog | Info    | Nén và lưu tr ữ log | H ệ th ố ng QA Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Có ch ỉ s ố th ố ng kê         | T ự độ ng xóa log sau 180 ngày |
| CRM     | AuditLog       | Info    | Phân tích log       | H ệ th ố ng CRM Phân tích log lo ạ i AuditLog v ớ im ứ c Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.          | Có th ể truy xu ấ t khi c ầ n  | Có dashboard Grafana           |
| QA      | TransactionLog | Warning | Phân tích log       | H ệ th ố ng QA Phân tích log lo ạ i TransactionLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.   | Tích h ợ p c ả nh báo realtime | Phân quy ề n chi ti ế t        |
| Billing | TransactionLog | Fatal   | Xu ấ t log          | H ệ th ố ng Billing Xu ấ t log lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i                    | Tích h ợ p c ả nh báo realtime | G ử i log sang ELK             |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|         |                |          |                     | thi ể u 90 ngày.                                                                                                        |                            |                                |
|---------|----------------|----------|---------------------|-------------------------------------------------------------------------------------------------------------------------|----------------------------|--------------------------------|
| Infra   | AccessLog      | Warning  | Xóa log             | H ệ th ố ng Infra Xóa log lo ạ i AccessLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                 | Có ch ỉ s ố th ố ng kê     | T ự độ ng xóa log sau 180 ngày |
| Billing | TransactionLog | Info     | G ử i log sang SIEM | H ệ th ố ng Billing G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Không m ấ t mát d ữ li ệ u | Phân quy ề n chi ti ế t        |
| CRM     | AccessLog      | Critical | Nén và lưu tr ữ log | H ệ th ố ng CRM Nén và lưu trữ log lo ạ i AccessLog v ớ i m ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.      | Không m ấ t mát d ữ li ệ u | T ự độ ng xóa log sau 180 ngày |
| QA      | ErrorLog       | Warning  | Xóa log             | H ệ th ố ng QA Xóa log lo ạ i ErrorLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                     | Không m ấ t mát d ữ li ệ u | T ự độ ng xóa log sau 180 ngày |
| Infra   | TransactionLog | Error    | Nén và lưu tr ữ log | H ệ th ố ng Infra Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.   | Có ch ỉ s ố th ố ng kê     | T ự độ ng xóa log sau 180 ngày |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

| IPCC   | AuditLog       | Error   | Nén và lưu tr ữ log   | H ệ th ố ng IPCC Nén và lưu trữ log lo ạ i AuditLog v ớ i m ứ c Error, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.     | Có th ể truy xu ấ t khi c ầ n   | G ử i log sang ELK             |
|--------|----------------|---------|-----------------------|----------------------------------------------------------------------------------------------------------------------|---------------------------------|--------------------------------|
| QA     | AccessLog      | Fatal   | Nén và lưu tr ữ log   | H ệ th ố ng QA Nén và lưu trữ log lo ạ i AccessLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.      | Có ch ỉ s ố th ố ng kê          | G ử i log sang ELK             |
| CRM    | PerformanceLog | Error   | G ử i log sang SIEM   | H ệ th ố ng CRM G ử i log sang SIEM lo ạ i PerformanceLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Có ch ỉ s ố th ố ng kê          | Theo chu ẩ n syslog RFC5424    |
| RPA    | TransactionLog | Fatal   | Nén và lưu tr ữ log   | H ệ th ố ng RPA Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.  | Không m ấ t mát d ữ li ệ u      | Có dashboard Grafana           |
| CRM    | AuditLog       | Warning | Phân tích log         | H ệ th ố ng CRM Phân tích log lo ạ i AuditLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.          | Có th ể truy xu ấ t khi c ầ n   | T ự độ ng xóa log sau 180 ngày |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

| Infra   | ErrorLog       | Critical   | Nén và lưu tr ữ log   | H ệ th ố ng Infra Nén và lưu trữ log lo ạ i ErrorLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.    | Không m ấ t mát d ữ li ệ u     | G ử i log sang ELK          |
|---------|----------------|------------|-----------------------|------------------------------------------------------------------------------------------------------------------------|--------------------------------|-----------------------------|
| RPA     | PerformanceLog | Critical   | Nén và lưu tr ữ log   | H ệ th ố ng RPA Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Tích h ợ p c ả nh báo realtime | Có dashboard Grafana        |
| IPCC    | AuditLog       | Warning    | Phân tích log         | H ệ th ố ng IPCC Phân tích log lo ạ i AuditLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.           | Có th ể truy xu ấ t khi c ầ n  | Theo chu ẩ n syslog RFC5424 |
| Billing | AccessLog      | Info       | Xu ấ t log            | H ệ th ố ng Billing Xu ấ t log lo ạ i AccessLog v ớ i m ứ c Info, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.            | Không m ấ t mát d ữ li ệ u     | Theo chu ẩ n syslog RFC5424 |
| Billing | AccessLog      | Warning    | Xu ấ t log            | H ệ th ố ng Billing Xu ấ t log lo ạ i AccessLog v ớ i m ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.          | Có th ể truy xu ấ t khi c ầ n  | Theo chu ẩ n syslog RFC5424 |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

| QA    | TransactionLog   | Warning   | Xu ấ t log          | H ệ th ố ng QA Xu ấ t log lo ạ i TransactionLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.          | Có ch ỉ s ố th ố ng kê        | T ự độ ng xóa log sau 180 ngày   |
|-------|------------------|-----------|---------------------|-----------------------------------------------------------------------------------------------------------------------|-------------------------------|----------------------------------|
| IVR   | AccessLog        | Warning   | G ử i log sang SIEM | H ệ th ố ng IVR G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.    | Có th ể truy xu ấ t khi c ầ n | Phân quy ề n chi ti ế t          |
| IVR   | ErrorLog         | Warning   | Xóa log             | H ệ th ố ng IVR Xóa log lo ạ i ErrorLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                  | Có th ể truy xu ấ t khi c ầ n | T ự độ ng xóa log sau 180 ngày   |
| IPCC  | AuditLog         | Fatal     | Xóa log             | H ệ th ố ng IPCC Xóa log lo ạ i AuditLog v ớ im ứ c Fatal, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.                  | Có th ể truy xu ấ t khi c ầ n | Có dashboard Grafana             |
| Infra | TransactionLog   | Error     | Nén và lưu tr ữ log | H ệ th ố ng Infra Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Không m ấ t mát d ữ li ệ u    | Phân quy ề n chi ti ế t          |
| Infra | AuditLog         | Error     | Nén và              | H ệ th ố ng Infra Nén và lưu trữ log lo ạ i                                                                           | Tích h ợ p                    | Theo chu ẩ n syslog              |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|       |                |          | lưu tr ữ log        | AuditLog v ớ im ứ c Error, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.                                                     | c ả nh báo realtime            | RFC5424                        |
|-------|----------------|----------|---------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| IPCC  | PerformanceLog | Critical | G ử i log sang SIEM | H ệ th ố ng IPCC G ử i log sang SIEM lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Log đượ c mã hóa AES- 256      | T ự độ ng xóa log sau 180 ngày |
| Infra | PerformanceLog | Warning  | Phân tích log       | H ệ th ố ng Infra Phân tích log lo ạ i PerformanceLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.       | Tích h ợ p c ả nh báo realtime | T ự độ ng xóa log sau 180 ngày |
| Infra | AccessLog      | Fatal    | Xóa log             | H ệ th ố ng Infra Xóa log lo ạ i AccessLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                    | Có th ể truy xu ấ t khi c ầ n  | Có dashboard Grafana           |
| QA    | PerformanceLog | Critical | Phân tích log       | H ệ th ố ng QA Phân tích log lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.         | Không m ấ t mát d ữ li ệ u     | Theo chu ẩ n syslog RFC5424    |
| Infra | PerformanceLog | Critical | Xóa log             | H ệ th ố ng Infra Xóa log lo ạ i PerformanceLog                                                                          | Có th ể truy xu ấ t khi        | Theo chu ẩ n syslog            |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|      |                |          |                     | v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                                                      | c ầ n                          | RFC5424                        |
|------|----------------|----------|---------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| QA   | PerformanceLog | Fatal    | Nén và lưu tr ữ log | H ệ th ố ng QA Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Có ch ỉ s ố th ố ng kê         | G ử i log sang ELK             |
| RPA  | ErrorLog       | Warning  | Nén và lưu tr ữ log | H ệ th ố ng RPA Nén và lưu trữ log lo ạ i ErrorLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.   | Tích h ợ p c ả nh báo realtime | T ự độ ng xóa log sau 180 ngày |
| IPCC | ErrorLog       | Critical | Xóa log             | H ệ th ố ng IPCC Xóa log lo ạ i ErrorLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.            | Có th ể truy xu ấ t khi c ầ n  | Phân quy ề n chi ti ế t        |
| QA   | AccessLog      | Fatal    | Xóa log             | H ệ th ố ng QA Xóa log lo ạ i AccessLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                 | Có ch ỉ s ố th ố ng kê         | Theo chu ẩ n syslog RFC5424    |
| RPA  | AuditLog       | Warning  | Nén và lưu tr ữ     | H ệ th ố ng RPA Nén và lưu trữ log lo ạ i AuditLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90         | Log đượ c mã hóa AES-          | Theo chu ẩ n syslog RFC5424    |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|         |                |         | log                 | ngày.                                                                                                                  | 256                            |                                |
|---------|----------------|---------|---------------------|------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| QA      | AuditLog       | Fatal   | G ử i log sang SIEM | H ệ th ố ng QA G ử i log sang SIEM lo ạ i AuditLog v ớ im ứ c Fatal, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.         | Có th ể truy xu ấ t khi c ầ n  | Có dashboard Grafana           |
| CRM     | PerformanceLog | Warning | G ử i log sang SIEM | H ệ th ố ng CRM G ử i log sang SIEM lo ạ i PerformanceLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Có th ể truy xu ấ t khi c ầ n  | Có dashboard Grafana           |
| RPA     | TransactionLog | Fatal   | G ử i log sang SIEM | H ệ th ố ng RPA G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.   | Tích h ợ p c ả nh báo realtime | T ự độ ng xóa log sau 180 ngày |
| Billing | AuditLog       | Warning | Nén và lưu tr ữ log | H ệ th ố ng Billing Nén và lưu trữ log lo ạ i AuditLog v ớ i m ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.   | Có ch ỉ s ố th ố ng kê         | T ự độ ng xóa log sau 180 ngày |
| IPCC    | AuditLog       | Error   | Nén và lưu tr ữ     | H ệ th ố ng IPCC Nén và lưu trữ log lo ạ i AuditLog v ớ i m ứ c Error, d ữ li ệ u lưu trữ t ố i thi ể u 90             | Log đượ c mã hóa AES-          | G ử i log sang ELK             |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|         |                |          | log                 | ngày.                                                                                                                   | 256                            |                             |
|---------|----------------|----------|---------------------|-------------------------------------------------------------------------------------------------------------------------|--------------------------------|-----------------------------|
| IPCC    | PerformanceLog | Warning  | Nén và lưu tr ữ log | H ệ th ố ng IPCC Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.  | Log đượ c mã hóa AES- 256      | Có dashboard Grafana        |
| IPCC    | TransactionLog | Warning  | G ử i log sang SIEM | H ệ th ố ng IPCC G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Log đượ c mã hóa AES- 256      | G ử i log sang ELK          |
| IVR     | PerformanceLog | Warning  | Phân tích log       | H ệ th ố ng IVR Phân tích log lo ạ i PerformanceLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.        | Có ch ỉ s ố th ố ng kê         | Có dashboard Grafana        |
| Infra   | AccessLog      | Critical | Phân tích log       | H ệ th ố ng Infra Phân tích log lo ạ i AccessLog v ớ i m ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.         | Tích h ợ p c ả nh báo realtime | Theo chu ẩ n syslog RFC5424 |
| Billing | PerformanceLog | Warning  | Nén và lưu tr ữ     | H ệ th ố ng Billing Nén và lưu trữ log lo ạ i PerformanceLog                                                            | Có th ể truy xu ấ t khi        | Phân quy ề n chi ti ế t     |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|       |                |         | log                 | v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                                                          | c ầ n                      |                                |
|-------|----------------|---------|---------------------|-----------------------------------------------------------------------------------------------------------------------|----------------------------|--------------------------------|
| QA    | AccessLog      | Warning | G ử i log sang SIEM | H ệ th ố ng QA G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.     | Có ch ỉ s ố th ố ng kê     | Theo chu ẩ n syslog RFC5424    |
| QA    | PerformanceLog | Warning | G ử i log sang SIEM | H ệ th ố ng QA G ử i log sang SIEM lo ạ i PerformanceLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Có ch ỉ s ố th ố ng kê     | Có dashboard Grafana           |
| IPCC  | PerformanceLog | Fatal   | Xu ấ t log          | H ệ th ố ng IPCC Xu ấ t log lo ạ i PerformanceLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.          | Không m ấ t mát d ữ li ệ u | T ự độ ng xóa log sau 180 ngày |
| Infra | AccessLog      | Fatal   | G ử i log sang SIEM | H ệ th ố ng Infra G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.   | Có ch ỉ s ố th ố ng kê     | G ử i log sang ELK             |
| IPCC  | ErrorLog       | Error   | G ử i log sang      | H ệ th ố ng IPCC G ử i log sang SIEM lo ạ i ErrorLog v ớ i m ứ c Error, d ữ li ệ u                                    | Có th ể truy xu ấ t khi    | T ự độ ng xóa log sau 180 ngày |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|         |                |          | SIEM                | lưu trữ t ố i thi ể u 90 ngày.                                                                                              | c ầ n                          |                                |
|---------|----------------|----------|---------------------|-----------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| IVR     | AuditLog       | Critical | Nén và lưu tr ữ log | H ệ th ố ng IVR Nén và lưu trữ log lo ạ i AuditLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.           | Log đượ c mã hóa AES- 256      | Có dashboard Grafana           |
| Billing | TransactionLog | Critical | G ử i log sang SIEM | H ệ th ố ng Billing G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Có ch ỉ s ố th ố ng kê         | G ử i log sang ELK             |
| RPA     | PerformanceLog | Critical | Phân tích log       | H ệ th ố ng RPA Phân tích log lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.           | Có th ể truy xu ấ t khi c ầ n  | Theo chu ẩ n syslog RFC5424    |
| IPCC    | AccessLog      | Fatal    | G ử i log sang SIEM | H ệ th ố ng IPCC G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.          | Tích h ợ p c ả nh báo realtime | Phân quy ề n chi ti ế t        |
| Infra   | AuditLog       | Critical | Nén và lưu tr ữ     | H ệ th ố ng Infra Nén và lưu trữ log lo ạ i AuditLog v ớ im ứ c Critical, d ữ li ệu lưu                                     | Tích h ợ p c ả nh báo          | T ự độ ng xóa log sau 180 ngày |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|         |                |          | log                 | tr ữ t ố i thi ể u 90 ngày.                                                                                           | realtime                       |                                |
|---------|----------------|----------|---------------------|-----------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| Billing | AccessLog      | Error    | Xóa log             | H ệ th ố ng Billing Xóa log lo ạ i AccessLog v ớ i m ứ c Error, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.             | Không m ấ t mát d ữ li ệ u     | Phân quy ề n chi ti ế t        |
| QA      | AuditLog       | Critical | Xu ấ t log          | H ệ th ố ng QA Xu ấ t log lo ạ i AuditLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.               | Log đượ c mã hóa AES- 256      | Theo chu ẩ n syslog RFC5424    |
| QA      | PerformanceLog | Warning  | G ử i log sang SIEM | H ệ th ố ng QA G ử i log sang SIEM lo ạ i PerformanceLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Có th ể truy xu ấ t khi c ầ n  | Phân quy ề n chi ti ế t        |
| Infra   | ErrorLog       | Error    | Xóa log             | H ệ th ố ng Infra Xóa log lo ạ i ErrorLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                  | Không m ấ t mát d ữ li ệ u     | T ự độ ng xóa log sau 180 ngày |
| CRM     | AccessLog      | Info     | Xóa log             | H ệ th ố ng CRM Xóa log lo ạ i AccessLog v ớ i m ứ c Info, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.                  | Tích h ợ p c ả nh báo realtime | T ự độ ng xóa log sau 180 ngày |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

| IPCC   | AccessLog      | Fatal   | G ử i log sang SIEM   | H ệ th ố ng IPCC G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.   | Tích h ợ p c ả nh báo realtime   | G ử i log sang ELK             |
|--------|----------------|---------|-----------------------|----------------------------------------------------------------------------------------------------------------------|----------------------------------|--------------------------------|
| QA     | AuditLog       | Fatal   | Nén và lưu tr ữ log   | H ệ th ố ng QA Nén và lưu trữ log lo ạ i AuditLog v ớ im ứ c Fatal, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.        | Có th ể truy xu ấ t khi c ầ n    | T ự độ ng xóa log sau 180 ngày |
| RPA    | ErrorLog       | Fatal   | Xóa log               | H ệ th ố ng RPA Xóa log lo ạ i ErrorLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                   | Log đượ c mã hóa AES- 256        | Theo chu ẩ n syslog RFC5424    |
| CRM    | TransactionLog | Info    | Xu ấ t log            | H ệ th ố ng CRM Xu ấ t log lo ạ i TransactionLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.           | Log đượ c mã hóa AES- 256        | G ử i log sang ELK             |
| Infra  | PerformanceLog | Info    | Xu ấ t log            | H ệ th ố ng Infra Xu ấ t log lo ạ i PerformanceLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.         | Log đượ c mã hóa AES- 256        | Theo chu ẩ n syslog RFC5424    |
| Infra  | TransactionLog | Warning | G ử i log             | H ệ th ố ng Infra G ử i log sang SIEM lo ạ i                                                                         | Tích h ợ p                       | Theo chu ẩ n syslog            |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|         |                |          | sang SIEM           | TransactionLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                                        | c ả nh báo realtime           | RFC5424                        |
|---------|----------------|----------|---------------------|--------------------------------------------------------------------------------------------------------------------|-------------------------------|--------------------------------|
| IVR     | AuditLog       | Warning  | Xu ấ t log          | H ệ th ố ng IVR Xu ấ t log lo ạ i AuditLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.            | Có th ể truy xu ấ t khi c ầ n | T ự độ ng xóa log sau 180 ngày |
| Billing | ErrorLog       | Warning  | Xóa log             | H ệ th ố ng Billing Xóa log lo ạ i ErrorLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.          | Có th ể truy xu ấ t khi c ầ n | Phân quy ề n chi ti ế t        |
| IPCC    | PerformanceLog | Critical | Phân tích log       | H ệ th ố ng IPCC Phân tích log lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Không m ấ t mát d ữ li ệ u    | T ự độ ng xóa log sau 180 ngày |
| RPA     | ErrorLog       | Error    | Nén và lưu tr ữ log | H ệ th ố ng RPA Nén và lưu trữ log lo ạ i ErrorLog v ớ im ứ c Error, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.     | Không m ấ t mát d ữ li ệ u    | G ử i log sang ELK             |
| RPA     | TransactionLog | Critical | Xu ấ t log          | H ệ th ố ng RPA Xu ấ t log lo ạ i TransactionLog v ớ im ứ c Critical,                                              | Không m ấ t mát d ữ li ệ u    | Có dashboard Grafana           |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|     |                |          |                     | d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                                                                             |                                |                                |
|-----|----------------|----------|---------------------|----------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| RPA | AuditLog       | Critical | Nén và lưu tr ữ log | H ệ th ố ng RPA Nén và lưu trữ log lo ạ i AuditLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.    | Có ch ỉ s ố th ố ng kê         | Phân quy ề n chi ti ế t        |
| QA  | ErrorLog       | Fatal    | Phân tích log       | H ệ th ố ng QA Phân tích log lo ạ i ErrorLog v ớ im ứ c Fatal, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.             | Tích h ợ p c ả nh báo realtime | G ử i log sang ELK             |
| RPA | TransactionLog | Error    | G ử i log sang SIEM | H ệ th ố ng RPA G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Log đượ c mã hóa AES- 256      | G ử i log sang ELK             |
| RPA | ErrorLog       | Warning  | Phân tích log       | H ệ th ố ng RPA Phân tích log lo ạ i ErrorLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.          | Có ch ỉ s ố th ố ng kê         | T ự độ ng xóa log sau 180 ngày |
| CRM | PerformanceLog | Info     | Xóa log             | H ệ th ố ng CRM Xóa log lo ạ i PerformanceLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i                               | Có ch ỉ s ố th ố ng kê         | Phân quy ề n chi ti ế t        |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|       |                |          |                     | thi ể u 90 ngày.                                                                                                      |                               |                                |
|-------|----------------|----------|---------------------|-----------------------------------------------------------------------------------------------------------------------|-------------------------------|--------------------------------|
| Infra | AccessLog      | Fatal    | Nén và lưu tr ữ log | H ệ th ố ng Infra Nén và lưu trữ log lo ạ i AccessLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.    | Có ch ỉ s ố th ố ng kê        | Theo chu ẩ n syslog RFC5424    |
| IVR   | ErrorLog       | Critical | Phân tích log       | H ệ th ố ng IVR Phân tích log lo ạ i ErrorLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.          | Có ch ỉ s ố th ố ng kê        | Theo chu ẩ n syslog RFC5424    |
| Infra | PerformanceLog | Error    | Nén và lưu tr ữ log | H ệ th ố ng Infra Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Có ch ỉ s ố th ố ng kê        | G ử i log sang ELK             |
| IPCC  | TransactionLog | Info     | G ử i log sang SIEM | H ệ th ố ng IPCC G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.  | Có th ể truy xu ấ t khi c ầ n | Phân quy ề n chi ti ế t        |
| IPCC  | ErrorLog       | Error    | Nén và lưu tr ữ     | H ệ th ố ng IPCC Nén và lưu trữ log lo ạ i ErrorLog v ớ i m ứ c Error, d ữ li ệ u lưu trữ t ố i thi ể u 90            | Có ch ỉ s ố th ố ng kê        | T ự độ ng xóa log sau 180 ngày |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|       |                |          | log                 | ngày.                                                                                                                   |                                |                                |
|-------|----------------|----------|---------------------|-------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| RPA   | PerformanceLog | Error    | G ử i log sang SIEM | H ệ th ố ng RPA G ử i log sang SIEM lo ạ i PerformanceLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.    | Log đượ c mã hóa AES- 256      | T ự độ ng xóa log sau 180 ngày |
| Infra | ErrorLog       | Critical | Xóa log             | H ệ th ố ng Infra Xóa log lo ạ i ErrorLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                 | Tích h ợ p c ả nh báo realtime | G ử i log sang ELK             |
| IVR   | PerformanceLog | Critical | G ử i log sang SIEM | H ệ th ố ng IVR G ử i log sang SIEM lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Không m ấ t mát d ữ li ệ u     | Theo chu ẩ n syslog RFC5424    |
| Infra | AuditLog       | Error    | G ử i log sang SIEM | H ệ th ố ng Infra G ử i log sang SIEM lo ạ i AuditLog v ớ im ứ c Error, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.       | Log đượ c mã hóa AES- 256      | Theo chu ẩ n syslog RFC5424    |
| IVR   | ErrorLog       | Critical | Xóa log             | H ệ th ố ng IVR Xóa log lo ạ i ErrorLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                   | Không m ấ t mát d ữ li ệ u     | Phân quy ề n chi ti ế t        |
| QA    | PerformanceLog | Fatal    | Nén                 | H ệ th ố ng QA Nén                                                                                                      | Có th ể                        | T ự độ ng xóa                  |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|         |                |          | và lưu tr ữ log   | và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                   | truy xu ấ t khi c ầ n          | log sau 180 ngày               |
|---------|----------------|----------|-------------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| RPA     | TransactionLog | Critical | Phân tích log     | H ệ th ố ng RPA Phân tích log lo ạ i TransactionLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Không m ấ t mát d ữ li ệ u     | G ử i log sang ELK             |
| RPA     | PerformanceLog | Fatal    | Xóa log           | H ệ th ố ng RPA Xóa log lo ạ i PerformanceLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.          | Không m ấ t mát d ữ li ệ u     | Phân quy ề n chi ti ế t        |
| Billing | ErrorLog       | Fatal    | Xóa log           | H ệ th ố ng Billing Xóa log lo ạ i ErrorLog v ớ im ứ c Fatal, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.           | Có ch ỉ s ố th ố ng kê         | Phân quy ề n chi ti ế t        |
| RPA     | AccessLog      | Fatal    | Xóa log           | H ệ th ố ng RPA Xóa log lo ạ i AccessLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.               | Tích h ợ p c ả nh báo realtime | T ự độ ng xóa log sau 180 ngày |
| CRM     | AccessLog      | Warning  | Xu ấ t log        | H ệ th ố ng CRM Xu ấ t log lo ạ i AccessLog v ớ i                                                                 | Có th ể truy xu ấ t khi        | G ử i log sang ELK             |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|      |                |         |                     | m ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                                                                | c ầ n                         |                                |
|------|----------------|---------|---------------------|------------------------------------------------------------------------------------------------------------------------|-------------------------------|--------------------------------|
| IVR  | PerformanceLog | Warning | G ử i log sang SIEM | H ệ th ố ng IVR G ử i log sang SIEM lo ạ i PerformanceLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Có th ể truy xu ấ t khi c ầ n | T ự độ ng xóa log sau 180 ngày |
| IPCC | PerformanceLog | Error   | Nén và lưu tr ữ log | H ệ th ố ng IPCC Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.   | Có th ể truy xu ấ t khi c ầ n | Có dashboard Grafana           |
| QA   | TransactionLog | Error   | Nén và lưu tr ữ log | H ệ th ố ng QA Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.     | Có ch ỉ s ố th ố ng kê        | T ự độ ng xóa log sau 180 ngày |
| QA   | AccessLog      | Error   | Phân tích log       | H ệ th ố ng QA Phân tích log lo ạ i AccessLog v ớ i m ứ c Error, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.             | Có ch ỉ s ố th ố ng kê        | G ử i log sang ELK             |
| RPA  | AuditLog       | Info    | Phân tích           | H ệ th ố ng RPA Phân tích log lo ạ i AuditLog v ớ im ứ c                                                               | Có th ể truy xu ấ t khi       | Phân quy ề n chi ti ế t        |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|         |                |         | log                 | Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.                                                                     | c ầ n                         |                      |
|---------|----------------|---------|---------------------|---------------------------------------------------------------------------------------------------------------------|-------------------------------|----------------------|
| Billing | ErrorLog       | Fatal   | Nén và lưu tr ữ log | H ệ th ố ng Billing Nén và lưu trữ log lo ạ i ErrorLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày. | Không m ấ t mát d ữ li ệ u    | Có dashboard Grafana |
| CRM     | TransactionLog | Info    | Nén và lưu tr ữ log | H ệ th ố ng CRM Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.  | Log đượ c mã hóa AES- 256     | G ử i log sang ELK   |
| Billing | TransactionLog | Fatal   | Xóa log             | H ệ th ố ng Billing Xóa log lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.        | Có ch ỉ s ố th ố ng kê        | G ử i log sang ELK   |
| CRM     | TransactionLog | Error   | Xu ấ t log          | H ệ th ố ng CRM Xu ấ t log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.         | Có th ể truy xu ấ t khi c ầ n | G ử i log sang ELK   |
| Infra   | AccessLog      | Warning | G ử i log sang      | H ệ th ố ng Infra G ử i log sang SIEM lo ạ i AccessLog v ớ i                                                        | Có ch ỉ s ố th ố ng           | Có dashboard Grafana |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|       |                |          | SIEM                | m ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                                                               | kê                             |                                |
|-------|----------------|----------|---------------------|-----------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| IPCC  | AuditLog       | Fatal    | G ử i log sang SIEM | H ệ th ố ng IPCC G ử i log sang SIEM lo ạ i AuditLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.     | Không m ấ t mát d ữ li ệ u     | G ử i log sang ELK             |
| CRM   | TransactionLog | Warning  | Nén và lưu tr ữ log | H ệ th ố ng CRM Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Có ch ỉ s ố th ố ng kê         | G ử i log sang ELK             |
| IVR   | AccessLog      | Error    | Xu ấ t log          | H ệ th ố ng IVR Xu ấ t log lo ạ i AccessLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                | Có th ể truy xu ấ t khi c ầ n  | T ự độ ng xóa log sau 180 ngày |
| CRM   | TransactionLog | Critical | Xóa log             | H ệ th ố ng CRM Xóa log lo ạ i TransactionLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.           | Tích h ợ p c ả nh báo realtime | G ử i log sang ELK             |
| Infra | TransactionLog | Fatal    | Nén và lưu tr ữ     | H ệ th ố ng Infra Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ                                      | Không m ấ t mát d ữ li ệ u     | Theo chu ẩ n syslog RFC5424    |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|         |                |          | log                 | li ệu lưu trữ t ố i thi ể u 90 ngày.                                                                                 |                               |                                |
|---------|----------------|----------|---------------------|----------------------------------------------------------------------------------------------------------------------|-------------------------------|--------------------------------|
| IPCC    | PerformanceLog | Critical | Xu ấ t log          | H ệ th ố ng IPCC Xu ấ t log lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.      | Log đượ c mã hóa AES- 256     | G ử i log sang ELK             |
| Billing | TransactionLog | Fatal    | Xóa log             | H ệ th ố ng Billing Xóa log lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.         | Có th ể truy xu ấ t khi c ầ n | G ử i log sang ELK             |
| Infra   | AccessLog      | Fatal    | Xóa log             | H ệ th ố ng Infra Xóa log lo ạ i AccessLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                | Log đượ c mã hóa AES- 256     | T ự độ ng xóa log sau 180 ngày |
| IPCC    | TransactionLog | Info     | G ử i log sang SIEM | H ệ th ố ng IPCC G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Log đượ c mã hóa AES- 256     | G ử i log sang ELK             |
| IPCC    | AccessLog      | Error    | Phân tích log       | H ệ th ố ng IPCC Phân tích log lo ạ i AccessLog v ớ i m ứ c Error, d ữ li ệ u lưu trữ t ố i thi ể u 90               | Có ch ỉ s ố th ố ng kê        | G ử i log sang ELK             |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|         |                |         |                     | ngày.                                                                                                                    |                                |                                |
|---------|----------------|---------|---------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| Infra   | PerformanceLog | Warning | G ử i log sang SIEM | H ệ th ố ng Infra G ử i log sang SIEM lo ạ i PerformanceLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Log đượ c mã hóa AES- 256      | G ử i log sang ELK             |
| IPCC    | PerformanceLog | Warning | G ử i log sang SIEM | H ệ th ố ng IPCC G ử i log sang SIEM lo ạ i PerformanceLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.  | Không m ấ t mát d ữ li ệ u     | T ự độ ng xóa log sau 180 ngày |
| Billing | AccessLog      | Error   | Nén và lưu tr ữ log | H ệ th ố ng Billing Nén và lưu trữ log lo ạ i AccessLog v ớ i m ứ c Error, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.     | Tích h ợ p c ả nh báo realtime | T ự độ ng xóa log sau 180 ngày |
| Billing | PerformanceLog | Info    | G ử i log sang SIEM | H ệ th ố ng Billing G ử i log sang SIEM lo ạ i PerformanceLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.  | Tích h ợ p c ả nh báo realtime | Có dashboard Grafana           |
| CRM     | ErrorLog       | Fatal   | Xu ấ t log          | H ệ th ố ng CRM Xu ấ t log lo ạ i ErrorLog v ớ im ứ c Fatal, d ữ li ệu lưu                                               | Có ch ỉ s ố th ố ng            | Theo chu ẩ n syslog RFC5424    |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|         |                |          |                     | tr ữ t ố i thi ể u 90 ngày.                                                                                           | kê                            |                                |
|---------|----------------|----------|---------------------|-----------------------------------------------------------------------------------------------------------------------|-------------------------------|--------------------------------|
| Billing | ErrorLog       | Critical | Nén và lưu tr ữ log | H ệ th ố ng Billing Nén và lưu trữ log lo ạ i ErrorLog v ớ i m ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Có th ể truy xu ấ t khi c ầ n | T ự độ ng xóa log sau 180 ngày |
| CRM     | ErrorLog       | Critical | Phân tích log       | H ệ th ố ng CRM Phân tích log lo ạ i ErrorLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.          | Có th ể truy xu ấ t khi c ầ n | Có dashboard Grafana           |
| QA      | AuditLog       | Fatal    | G ử i log sang SIEM | H ệ th ố ng QA G ử i log sang SIEM lo ạ i AuditLog v ớ im ứ c Fatal, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.        | Không m ấ t mát d ữ li ệ u    | Có dashboard Grafana           |
| QA      | PerformanceLog | Fatal    | Phân tích log       | H ệ th ố ng QA Phân tích log lo ạ i PerformanceLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.         | Có ch ỉ s ố th ố ng kê        | T ự độ ng xóa log sau 180 ngày |
| Infra   | TransactionLog | Critical | Xu ấ t log          | H ệ th ố ng Infra Xu ấ t log lo ạ i TransactionLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i                       | Có ch ỉ s ố th ố ng kê        | T ự độ ng xóa log sau 180 ngày |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|         |                |          |               | thi ể u 90 ngày.                                                                                                   |                                |                         |
|---------|----------------|----------|---------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------|-------------------------|
| CRM     | AuditLog       | Critical | Phân tích log | H ệ th ố ng CRM Phân tích log lo ạ i AuditLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.       | Có ch ỉ s ố th ố ng kê         | Phân quy ề n chi ti ế t |
| Billing | AuditLog       | Warning  | Xu ấ t log    | H ệ th ố ng Billing Xu ấ t log lo ạ i AuditLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.       | Log đượ c mã hóa AES- 256      | Phân quy ề n chi ti ế t |
| IPCC    | AccessLog      | Warning  | Phân tích log | H ệ th ố ng IPCC Phân tích log lo ạ i AccessLog v ớ i m ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.      | Có th ể truy xu ấ t khi c ầ n  | Có dashboard Grafana    |
| Billing | PerformanceLog | Critical | Xu ấ t log    | H ệ th ố ng Billing Xu ấ t log lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Log đượ c mã hóa AES- 256      | G ử i log sang ELK      |
| RPA     | AuditLog       | Critical | Xu ấ t log    | H ệ th ố ng RPA Xu ấ t log lo ạ i AuditLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90                | Tích h ợ p c ả nh báo realtime | Có dashboard Grafana    |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|     |          |          |                     | ngày.                                                                                                             |                               |                                |
|-----|----------|----------|---------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------|--------------------------------|
| CRM | AuditLog | Critical | Nén và lưu tr ữ log | H ệ th ố ng CRM Nén và lưu trữ log lo ạ i AuditLog v ớ i m ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Không m ấ t mát d ữ li ệ u    | Phân quy ề n chi ti ế t        |
| RPA | AuditLog | Info     | Xu ấ t log          | H ệ th ố ng RPA Xu ấ t log lo ạ i AuditLog v ớ im ứ c Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.             | Có th ể truy xu ấ t khi c ầ n | Có dashboard Grafana           |
| RPA | ErrorLog | Critical | Xu ấ t log          | H ệ th ố ng RPA Xu ấ t log lo ạ i ErrorLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.         | Không m ấ t mát d ữ li ệ u    | T ự độ ng xóa log sau 180 ngày |
| RPA | ErrorLog | Error    | Xu ấ t log          | H ệ th ố ng RPA Xu ấ t log lo ạ i ErrorLog v ớ im ứ c Error, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.            | Không m ấ t mát d ữ li ệ u    | Phân quy ề n chi ti ế t        |
| QA  | AuditLog | Critical | Xóa log             | H ệ th ố ng QA Xóa log lo ạ i AuditLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.              | Có th ể truy xu ấ t khi c ầ n | Theo chu ẩ n syslog RFC5424    |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

| IVR   | AccessLog      | Info     | G ử i log sang SIEM   | H ệ th ố ng IVR G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Info, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.      | Có th ể truy xu ấ t khi c ầ n   | Phân quy ề n chi ti ế t        |
|-------|----------------|----------|-----------------------|-----------------------------------------------------------------------------------------------------------------------|---------------------------------|--------------------------------|
| QA    | TransactionLog | Warning  | G ử i log sang SIEM   | H ệ th ố ng QA G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Log đượ c mã hóa AES- 256       | T ự độ ng xóa log sau 180 ngày |
| Infra | AccessLog      | Critical | Phân tích log         | H ệ th ố ng Infra Phân tích log lo ạ i AccessLog v ớ i m ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.       | Có ch ỉ s ố th ố ng kê          | Theo chu ẩ n syslog RFC5424    |
| RPA   | ErrorLog       | Info     | G ử i log sang SIEM   | H ệ th ố ng RPA G ử i log sang SIEM lo ạ i ErrorLog v ớ im ứ c Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.        | Có ch ỉ s ố th ố ng kê          | G ử i log sang ELK             |
| CRM   | AccessLog      | Warning  | G ử i log sang SIEM   | H ệ th ố ng CRM G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.    | Có th ể truy xu ấ t khi c ầ n   | Có dashboard Grafana           |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

| RPA     | TransactionLog   | Error    | Xóa log             | H ệ th ố ng RPA Xóa log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.         | Không m ấ t mát d ữ li ệ u     | Phân quy ề n chi ti ế t        |
|---------|------------------|----------|---------------------|------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| RPA     | ErrorLog         | Fatal    | G ử i log sang SIEM | H ệ th ố ng RPA G ử i log sang SIEM lo ạ i ErrorLog v ớ im ứ c Fatal, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.  | Có th ể truy xu ấ t khi c ầ n  | Theo chu ẩ n syslog RFC5424    |
| RPA     | AuditLog         | Critical | Xóa log             | H ệ th ố ng RPA Xóa log lo ạ i AuditLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.            | Tích h ợ p c ả nh báo realtime | T ự độ ng xóa log sau 180 ngày |
| CRM     | ErrorLog         | Warning  | Nén và lưu tr ữ log | H ệ th ố ng CRM Nén và lưu trữ log lo ạ i ErrorLog v ớ i m ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Không m ấ t mát d ữ li ệ u     | Có dashboard Grafana           |
| Infra   | TransactionLog   | Info     | Xóa log             | H ệ th ố ng Infra Xóa log lo ạ i TransactionLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.        | Log đượ c mã hóa AES- 256      | G ử i log sang ELK             |
| Billing | PerformanceLog   | Info     | Nén và              | H ệ th ố ng Billing Nén và lưu trữ log                                                                           | Không m ấ t mát                | G ử i log sang                 |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|         |                |          | lưu tr ữ log   | lo ạ i PerformanceLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                                  | d ữ li ệ u                     | ELK                            |
|---------|----------------|----------|----------------|------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| Infra   | PerformanceLog | Fatal    | Phân tích log  | H ệ th ố ng Infra Phân tích log lo ạ i PerformanceLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Có th ể truy xu ấ t khi c ầ n  | Phân quy ề n chi ti ế t        |
| IPCC    | TransactionLog | Critical | Xóa log        | H ệ th ố ng IPCC Xóa log lo ạ i TransactionLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.     | Log đượ c mã hóa AES- 256      | G ử i log sang ELK             |
| IPCC    | PerformanceLog | Error    | Xóa log        | H ệ th ố ng IPCC Xóa log lo ạ i PerformanceLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.        | Tích h ợ p c ả nh báo realtime | G ử i log sang ELK             |
| Billing | ErrorLog       | Warning  | Xóa log        | H ệ th ố ng Billing Xóa log lo ạ i ErrorLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.        | Tích h ợ p c ả nh báo realtime | T ự độ ng xóa log sau 180 ngày |
| IVR     | ErrorLog       | Fatal    | G ử i log      | H ệ th ố ng IVR G ử i log sang SIEM lo ạ i                                                                       | Log đượ c                      | Có dashboard                   |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|         |                |          | sang SIEM           | ErrorLog v ớ im ứ c Fatal, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.                                              | mã hóa AES- 256                | Grafana                     |
|---------|----------------|----------|---------------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------|-----------------------------|
| CRM     | PerformanceLog | Error    | Xu ấ t log          | H ệ th ố ng CRM Xu ấ t log lo ạ i PerformanceLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.       | Tích h ợ p c ả nh báo realtime | Theo chu ẩ n syslog RFC5424 |
| Billing | TransactionLog | Critical | Xóa log             | H ệ th ố ng Billing Xóa log lo ạ i TransactionLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.   | Log đượ c mã hóa AES- 256      | Phân quy ề n chi ti ế t     |
| QA      | ErrorLog       | Fatal    | Phân tích log       | H ệ th ố ng QA Phân tích log lo ạ i ErrorLog v ớ im ứ c Fatal, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.          | Có ch ỉ s ố th ố ng kê         | Có dashboard Grafana        |
| Infra   | AuditLog       | Fatal    | G ử i log sang SIEM | H ệ th ố ng Infra G ử i log sang SIEM lo ạ i AuditLog v ớ im ứ c Fatal, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày. | Log đượ c mã hóa AES- 256      | G ử i log sang ELK          |
| QA      | AuditLog       | Critical | Xu ấ t log          | H ệ th ố ng QA Xu ấ t log lo ạ i AuditLog v ớ im ứ c Critical,                                                    | Có ch ỉ s ố th ố ng            | Theo chu ẩ n syslog         |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|       |                |          |                     | d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                                                                            | kê                             | RFC5424                        |
|-------|----------------|----------|---------------------|---------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| QA    | PerformanceLog | Error    | G ử i log sang SIEM | H ệ th ố ng QA G ử i log sang SIEM lo ạ i PerformanceLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Có ch ỉ s ố th ố ng kê         | T ự độ ng xóa log sau 180 ngày |
| Infra | TransactionLog | Info     | Xóa log             | H ệ th ố ng Infra Xóa log lo ạ i TransactionLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.           | Không m ấ t mát d ữ li ệ u     | T ự độ ng xóa log sau 180 ngày |
| IVR   | PerformanceLog | Fatal    | Nén và lưu tr ữ log | H ệ th ố ng IVR Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Tích h ợ p c ả nh báo realtime | Có dashboard Grafana           |
| CRM   | TransactionLog | Info     | Xóa log             | H ệ th ố ng CRM Xóa log lo ạ i TransactionLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.             | Có th ể truy xu ấ t khi c ầ n  | G ử i log sang ELK             |
| CRM   | AccessLog      | Critical | Phân tích log       | H ệ th ố ng CRM Phân tích log lo ạ i AccessLog v ớ i m ứ c Critical, d ữ li ệu lưu trữ t ố i                        | Log đượ c mã hóa AES-          | Theo chu ẩ n syslog RFC5424    |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|         |                |         |                     | thi ể u 90 ngày.                                                                                                   | 256                            |                                |
|---------|----------------|---------|---------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| RPA     | AccessLog      | Error   | Xóa log             | H ệ th ố ng RPA Xóa log lo ạ i AccessLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                | Không m ấ t mát d ữ li ệ u     | Có dashboard Grafana           |
| RPA     | AuditLog       | Info    | Xu ấ t log          | H ệ th ố ng RPA Xu ấ t log lo ạ i AuditLog v ớ im ứ c Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.              | Có ch ỉ s ố th ố ng kê         | G ử i log sang ELK             |
| Infra   | ErrorLog       | Warning | Phân tích log       | H ệ th ố ng Infra Phân tích log lo ạ i ErrorLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.      | Tích h ợ p c ả nh báo realtime | T ự độ ng xóa log sau 180 ngày |
| CRM     | PerformanceLog | Info    | Nén và lưu tr ữ log | H ệ th ố ng CRM Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Có th ể truy xu ấ t khi c ầ n  | Có dashboard Grafana           |
| Billing | AuditLog       | Error   | Nén và lưu tr ữ log | H ệ th ố ng Billing Nén và lưu trữ log lo ạ i AuditLog v ớ i m ứ c Error, d ữ li ệ u lưu trữ t ố i thi ể u 90      | Log đượ c mã hóa AES- 256      | Phân quy ề n chi ti ế t        |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|       |                |          |                     | ngày.                                                                                                              |                                |                                |
|-------|----------------|----------|---------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| IVR   | TransactionLog | Error    | Phân tích log       | H ệ th ố ng IVR Phân tích log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.     | Không m ấ t mát d ữ li ệ u     | T ự độ ng xóa log sau 180 ngày |
| QA    | TransactionLog | Fatal    | Nén và lưu tr ữ log | H ệ th ố ng QA Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Tích h ợ p c ả nh báo realtime | T ự độ ng xóa log sau 180 ngày |
| Infra | AuditLog       | Warning  | Xu ấ t log          | H ệ th ố ng Infra Xu ấ t log lo ạ i AuditLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.         | Không m ấ t mát d ữ li ệ u     | Phân quy ề n chi ti ế t        |
| IPCC  | PerformanceLog | Info     | Phân tích log       | H ệ th ố ng IPCC Phân tích log lo ạ i PerformanceLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.     | Log đượ c mã hóa AES- 256      | T ự độ ng xóa log sau 180 ngày |
| IVR   | PerformanceLog | Critical | Phân tích log       | H ệ th ố ng IVR Phân tích log lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i                   | Có ch ỉ s ố th ố ng kê         | Theo chu ẩ n syslog RFC5424    |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|         |                |          |                     | thi ể u 90 ngày.                                                                                                    |                                |                             |
|---------|----------------|----------|---------------------|---------------------------------------------------------------------------------------------------------------------|--------------------------------|-----------------------------|
| Infra   | ErrorLog       | Critical | Nén và lưu tr ữ log | H ệ th ố ng Infra Nén và lưu trữ log lo ạ i ErrorLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày. | Tích h ợ p c ả nh báo realtime | Phân quy ề n chi ti ế t     |
| QA      | ErrorLog       | Info     | G ử i log sang SIEM | H ệ th ố ng QA G ử i log sang SIEM lo ạ i ErrorLog v ớ im ứ c Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.       | Không m ấ t mát d ữ li ệ u     | Theo chu ẩ n syslog RFC5424 |
| IVR     | ErrorLog       | Fatal    | Xóa log             | H ệ th ố ng IVR Xóa log lo ạ i ErrorLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                  | Tích h ợ p c ả nh báo realtime | Có dashboard Grafana        |
| Billing | ErrorLog       | Info     | G ử i log sang SIEM | H ệ th ố ng Billing G ử i log sang SIEM lo ạ i ErrorLog v ớ i m ứ c Info, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày. | Có th ể truy xu ấ t khi c ầ n  | Theo chu ẩ n syslog RFC5424 |
| Infra   | TransactionLog | Fatal    | Xóa log             | H ệ th ố ng Infra Xóa log lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.          | Log đượ c mã hóa AES- 256      | Phân quy ề n chi ti ế t     |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

| Billing   | TransactionLog   | Fatal   | Xu ấ t log          | H ệ th ố ng Billing Xu ấ t log lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.   | Không m ấ t mát d ữ li ệ u     | G ử i log sang ELK          |
|-----------|------------------|---------|---------------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------|-----------------------------|
| IPCC      | ErrorLog         | Warning | Xóa log             | H ệ th ố ng IPCC Xóa log lo ạ i ErrorLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.            | Tích h ợ p c ả nh báo realtime | Phân quy ề n chi ti ế t     |
| IVR       | AccessLog        | Error   | G ử i log sang SIEM | H ệ th ố ng IVR G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Error, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày. | Log đượ c mã hóa AES- 256      | G ử i log sang ELK          |
| Infra     | PerformanceLog   | Fatal   | Phân tích log       | H ệ th ố ng Infra Phân tích log lo ạ i PerformanceLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.  | Log đượ c mã hóa AES- 256      | Theo chu ẩ n syslog RFC5424 |
| Infra     | AuditLog         | Error   | G ử i log sang SIEM | H ệ th ố ng Infra G ử i log sang SIEM lo ạ i AuditLog v ớ im ứ c Error, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày. | Log đượ c mã hóa AES- 256      | Phân quy ề n chi ti ế t     |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

| Infra   | AccessLog      | Warning   | Xóa log             | H ệ th ố ng Infra Xóa log lo ạ i AccessLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.            | Có ch ỉ s ố th ố ng kê     | G ử i log sang ELK             |
|---------|----------------|-----------|---------------------|--------------------------------------------------------------------------------------------------------------------|----------------------------|--------------------------------|
| IVR     | ErrorLog       | Error     | G ử i log sang SIEM | H ệ th ố ng IVR G ử i log sang SIEM lo ạ i ErrorLog v ớ im ứ c Error, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.    | Có ch ỉ s ố th ố ng kê     | G ử i log sang ELK             |
| Infra   | ErrorLog       | Info      | Nén và lưu tr ữ log | H ệ th ố ng Infra Nén và lưu trữ log lo ạ i ErrorLog v ớ im ứ c Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.    | Không m ấ t mát d ữ li ệ u | Theo chu ẩ n syslog RFC5424    |
| QA      | TransactionLog | Fatal     | Nén và lưu tr ữ log | H ệ th ố ng QA Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Log đượ c mã hóa AES- 256  | T ự độ ng xóa log sau 180 ngày |
| RPA     | AccessLog      | Info      | Xóa log             | H ệ th ố ng RPA Xóa log lo ạ i AccessLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                 | Không m ấ t mát d ữ li ệ u | Có dashboard Grafana           |
| RPA     | ErrorLog       | Error     | Xu ấ t log          | H ệ th ố ng RPA Xu ấ t log lo ạ i ErrorLog v ớ im ứ c                                                              | Có ch ỉ s ố th ố ng        | Theo chu ẩ n syslog            |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|         |                |          |                     | Error, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.                                                                         | kê                        | RFC5424                        |
|---------|----------------|----------|---------------------|--------------------------------------------------------------------------------------------------------------------------|---------------------------|--------------------------------|
| Infra   | ErrorLog       | Critical | Nén và lưu tr ữ log | H ệ th ố ng Infra Nén và lưu trữ log lo ạ i ErrorLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.      | Log đượ c mã hóa AES- 256 | Có dashboard Grafana           |
| IPCC    | TransactionLog | Critical | G ử i log sang SIEM | H ệ th ố ng IPCC G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Có ch ỉ s ố th ố ng kê    | Theo chu ẩ n syslog RFC5424    |
| Infra   | PerformanceLog | Info     | G ử i log sang SIEM | H ệ th ố ng Infra G ử i log sang SIEM lo ạ i PerformanceLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.    | Log đượ c mã hóa AES- 256 | Phân quy ề n chi ti ế t        |
| RPA     | PerformanceLog | Fatal    | Nén và lưu tr ữ log | H ệ th ố ng RPA Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.      | Có ch ỉ s ố th ố ng kê    | T ự độ ng xóa log sau 180 ngày |
| Billing | AuditLog       | Critical | Xu ấ t log          | H ệ th ố ng Billing Xu ấ t log lo ạ i AuditLog v ớ im ứ c                                                                | Có ch ỉ s ố th ố ng       | Phân quy ề n chi ti ế t        |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|      |           |         |                     | Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.                                                            | kê                             |                             |
|------|-----------|---------|---------------------|----------------------------------------------------------------------------------------------------------------|--------------------------------|-----------------------------|
| IVR  | AuditLog  | Info    | G ử i log sang SIEM | H ệ th ố ng IVR G ử i log sang SIEM lo ạ i AuditLog v ớ im ứ c Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày. | Tích h ợ p c ả nh báo realtime | G ử i log sang ELK          |
| RPA  | AuditLog  | Warning | Xu ấ t log          | H ệ th ố ng RPA Xu ấ t log lo ạ i AuditLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.       | Log đượ c mã hóa AES- 256      | Có dashboard Grafana        |
| IPCC | AuditLog  | Info    | Phân tích log       | H ệ th ố ng IPCC Phân tích log lo ạ i AuditLog v ớ im ứ c Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.      | Có ch ỉ s ố th ố ng kê         | Theo chu ẩ n syslog RFC5424 |
| IVR  | AccessLog | Fatal   | Xu ấ t log          | H ệ th ố ng IVR Xu ấ t log lo ạ i AccessLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.         | Không m ấ t mát d ữ li ệ u     | Theo chu ẩ n syslog RFC5424 |
| RPA  | ErrorLog  | Warning | Nén và lưu tr ữ     | H ệ th ố ng RPA Nén và lưu trữ log lo ạ i ErrorLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90     | Tích h ợ p c ả nh báo          | G ử i log sang ELK          |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

|       |                |         | log                 | ngày.                                                                                                             | realtime                       |                                |
|-------|----------------|---------|---------------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| QA    | AuditLog       | Warning | Xóa log             | H ệ th ố ng QA Xóa log lo ạ i AuditLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.               | Có th ể truy xu ấ t khi c ầ n  | T ự độ ng xóa log sau 180 ngày |
| IPCC  | ErrorLog       | Info    | Phân tích log       | H ệ th ố ng IPCC Phân tích log lo ạ i ErrorLog v ớ im ứ c Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.         | Tích h ợ p c ả nh báo realtime | G ử i log sang ELK             |
| IVR   | ErrorLog       | Warning | Phân tích log       | H ệ th ố ng IVR Phân tích log lo ạ i ErrorLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.       | Không m ấ t mát d ữ li ệ u     | Phân quy ề n chi ti ế t        |
| Infra | TransactionLog | Warning | Xu ấ t log          | H ệ th ố ng Infra Xu ấ t log lo ạ i TransactionLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.   | Có ch ỉ s ố th ố ng kê         | Theo chu ẩ n syslog RFC5424    |
| RPA   | AccessLog      | Fatal   | G ử i log sang SIEM | H ệ th ố ng RPA G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày. | Có th ể truy xu ấ t khi c ầ n  | G ử i log sang ELK             |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

| CRM     | ErrorLog       | Fatal    | Xóa log             | H ệ th ố ng CRM Xóa log lo ạ i ErrorLog v ớ im ứ c Fatal, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.                        | Log đượ c mã hóa AES- 256     | T ự độ ng xóa log sau 180 ngày   |
|---------|----------------|----------|---------------------|----------------------------------------------------------------------------------------------------------------------------|-------------------------------|----------------------------------|
| IPCC    | ErrorLog       | Critical | Xu ấ t log          | H ệ th ố ng IPCC Xu ấ t log lo ạ i ErrorLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.                 | Không m ấ t mát d ữ li ệ u    | Theo chu ẩ n syslog RFC5424      |
| RPA     | AuditLog       | Info     | Nén và lưu tr ữ log | H ệ th ố ng RPA Nén và lưu trữ log lo ạ i AuditLog v ớ im ứ c Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.              | Có th ể truy xu ấ t khi c ầ n | Theo chu ẩ n syslog RFC5424      |
| Billing | PerformanceLog | Critical | Nén và lưu tr ữ log | H ệ th ố ng Billing Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Log đượ c mã hóa AES- 256     | G ử i log sang ELK               |
| Infra   | AccessLog      | Critical | Xu ấ t log          | H ệ th ố ng Infra Xu ấ t log lo ạ i AccessLog v ớ i m ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.               | Có ch ỉ s ố th ố ng kê        | Phân quy ề n chi ti ế t          |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

| IVR     | AccessLog      | Critical   | Xu ấ t log          | H ệ th ố ng IVR Xu ấ t log lo ạ i AccessLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                | Không m ấ t mát d ữ li ệ u     | G ử i log sang ELK             |
|---------|----------------|------------|---------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| Billing | TransactionLog | Error      | G ử i log sang SIEM | H ệ th ố ng Billing G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày. | Log đượ c mã hóa AES- 256      | T ự độ ng xóa log sau 180 ngày |
| CRM     | AccessLog      | Info       | Xu ấ t log          | H ệ th ố ng CRM Xu ấ t log lo ạ i AccessLog v ớ i m ứ c Info, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.                  | Tích h ợ p c ả nh báo realtime | T ự độ ng xóa log sau 180 ngày |
| CRM     | PerformanceLog | Critical   | Xóa log             | H ệ th ố ng CRM Xóa log lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.              | Tích h ợ p c ả nh báo realtime | Theo chu ẩ n syslog RFC5424    |
| CRM     | PerformanceLog | Fatal      | Nén và lưu tr ữ log | H ệ th ố ng CRM Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.      | Có ch ỉ s ố th ố ng kê         | T ự độ ng xóa log sau 180 ngày |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

| Billing   | TransactionLog   | Fatal   | Nén và lưu tr ữ log   | H ệ th ố ng Billing Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.   | Không m ấ t mát d ữ li ệ u     | T ự độ ng xóa log sau 180 ngày   |
|-----------|------------------|---------|-----------------------|---------------------------------------------------------------------------------------------------------------------------|--------------------------------|----------------------------------|
| Infra     | AuditLog         | Fatal   | G ử i log sang SIEM   | H ệ th ố ng Infra G ử i log sang SIEM lo ạ i AuditLog v ớ im ứ c Fatal, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.         | Có ch ỉ s ố th ố ng kê         | Có dashboard Grafana             |
| CRM       | PerformanceLog   | Error   | Nén và lưu tr ữ log   | H ệ th ố ng CRM Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.       | Tích h ợ p c ả nh báo realtime | Theo chu ẩ n syslog RFC5424      |