<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| Tên ứ ng d ụ ng     | Ch ức năng             | API/Action              | Mô t ả                                                 | K ế t qu ả mong mu ố n   | Ghi chú                               |
|---------------------|------------------------|-------------------------|--------------------------------------------------------|--------------------------|---------------------------------------|
| BCCS2-Core          | Validate IVRPrompt     | /ivrprompt/validate     | Validate d ữ li ệ u IVRPrompt trong BCCS2-Core.        | Thông báo qua SMS        | Có cơ ch ế rollback                   |
| Infra-Server        | Config QoS             | /qos/config             | Config d ữ li ệ u QoS trong Infra-Server.              | Hi ể n th ị báo cáo      | Có cơ ch ế rollback                   |
| RPA-Engine          | Delete CustomerProfile | /customerprofile/delete | Delete d ữ li ệ u CustomerProfile trong RPA-Engine.    | C ả nh báo               | K ế t n ố i v ớ i h ệ th ố ng Billing |
| QA- Automation      | Generate AgentStatus   | /agentstatus/generate   | Generate d ữ li ệ u AgentStatus trong QA-Automation.   | L ỗ i nghiêm tr ọ ng     | D ữ li ệ u backup m ỗ i ngày          |
| Security- Firewall  | Config ClusterNode     | /clusternode/config     | Config d ữ li ệ u ClusterNode trong Security-Firewall. | Không l ỗ i              | Tích h ợ p v ớ i CRM                  |
| Security- Firewall  | Update Queue           | /queue/update           | Update d ữ li ệ u Queue trong Security-Firewall.       | Ghi log đầy đủ           | Theo quy đị nh Viettel                |
| IPCC- ContactCenter | Insert AccountLock     | /accountlock/insert     | Insert d ữ li ệ u AccountLock trong                    | Không l ỗ i              | Ch ỉ dùng                             |

<!-- image -->

TD444

L ầ n ban hành: 1

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

|                     |                        |                         | IPCC- ContactCenter.                                   |                     | cho admin                             |
|---------------------|------------------------|-------------------------|--------------------------------------------------------|---------------------|---------------------------------------|
| IVR-System          | Monitor ClusterNode    | /clusternode/monitor    | Monitor d ữ li ệ u ClusterNode trong IVR-System.       | Thông báo qua email | Ch ạ y theo l ị ch cron               |
| Infra-Server        | Import Contact         | /contact/import         | Import d ữ li ệ u Contact trong Infra- Server.         | Hi ể n th ị báo cáo | Có cơ ch ế rollback                   |
| IPCC- ContactCenter | Insert Blacklist       | /blacklist/insert       | Insert d ữ li ệ u Blacklist trong IPCC- ContactCenter. | Thông báo qua SMS   | K ế t n ố i v ớ i h ệ th ố ng Billing |
| Security- Firewall  | Import Blacklist       | /blacklist/import       | Import d ữ li ệ u Blacklist trong Security-Firewall.   | T ự độ ng retry     | D ữ li ệ u backup m ỗ i ngày          |
| QA- Automation      | Schedule PackagePlan   | /packageplan/schedule   | Schedule d ữ li ệ u PackagePlan trong QA-Automation.   | Thông báo qua SMS   | Ch ạ y theo l ị ch cron               |
| RPA-Engine          | Analyze Blacklist      | /blacklist/analyze      | Analyze d ữ li ệ u Blacklist trong RPA- Engine.        | Ghi log đầy đủ      | Tích h ợ p v ớ i CRM                  |
| Infra-Server        | Analyze VPN            | /vpn/analyze            | Analyze d ữ li ệ u VPN trong Infra- Server.            | Không l ỗ i         | Có cơ ch ế rollback                   |
| Infra-Network       | Analyze FirewallPolicy | /firewallpolicy/analyze | Analyze d ữ li ệ u FirewallPolicy trong Infra-Network. | Thông báo           | Ch ạ y theo                           |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

|                     |                     |                      |                                                           | qua SMS              | l ị ch cron                           |
|---------------------|---------------------|----------------------|-----------------------------------------------------------|----------------------|---------------------------------------|
| BCCS2-Core          | Import Opportunity  | /opportunity/import  | Import d ữ li ệ u Opportunity trong BCCS2-Core.           | T ự độ ng retry      | K ế t n ố i v ớ i h ệ th ố ng Billing |
| IPCC- ContactCenter | Analyze AgentStatus | /agentstatus/analyze | Analyze d ữ li ệ u AgentStatus trong IPCC- ContactCenter. | C ả nh báo           | Theo chu ẩ n ISO 27001                |
| CRM- Platform       | Insert IVRPrompt    | /ivrprompt/insert    | Insert d ữ li ệ u IVRPrompt trong CRM-Platform.           | Hi ể n th ị báo cáo  | Yêu c ầ u xác th ự c ngườ i dùng      |
| BCCS2-Core          | Import CDRReport    | /cdrreport/import    | Import d ữ li ệ u CDRReport trong BCCS2-Core.             | C ả nh báo           | Ch ỉ dùng cho admin                   |
| CRM- Platform       | Analyze QoS         | /qos/analyze         | Analyze d ữ li ệ u QoS trong CRM- Platform.               | C ả nh báo           | Tích h ợ p v ớ i CRM                  |
| BCCS2-Core          | Update Campaign     | /campaign/update     | Update d ữ li ệ u Campaign trong BCCS2-Core.              | L ỗ i nghiêm tr ọ ng | Ch ạ y theo l ị ch cron               |
| Infra-Network       | Export AccountLock  | /accountlock/export  | Export d ữ li ệ u AccountLock trong Infra-Network.        | Hi ể n th ị báo cáo  | Ch ạ y theo l ị ch cron               |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| CRM- Platform      | Analyze TransactionLog   | /transactionlog/analyze   | Analyze d ữ li ệ u TransactionLog trong CRM- Platform.   | Không l ỗ i          | Tích h ợ p v ớ i CRM                  |
|--------------------|--------------------------|---------------------------|----------------------------------------------------------|----------------------|---------------------------------------|
| CRM- Platform      | Config KPIReport         | /kpireport/config         | Config d ữ li ệ u KPIReport trong CRM-Platform.          | Đồ ng b ộ d ữ li ệ u | Theo chu ẩ n ISO 27001                |
| RPA-Engine         | Optimize Campaign        | /campaign/optimize        | Optimize d ữ li ệ u Campaign trong RPA-Engine.           | Thông báo qua email  | Ch ỉ dùng cho admin                   |
| IVR-System         | Delete Queue             | /queue/delete             | Delete d ữ li ệ u Queue trong IVR-System.                | T ự độ ng retry      | K ế t n ố i v ớ i h ệ th ố ng Billing |
| RPA-Engine         | Delete AgentStatus       | /agentstatus/delete       | Delete d ữ li ệ u AgentStatus trong RPA-Engine.          | Thông báo qua SMS    | Tích h ợ p v ớ i CRM                  |
| BCCS2- Billing     | Schedule AgentStatus     | /agentstatus/schedule     | Schedule d ữ li ệ u AgentStatus trong BCCS2-Billing.     | Đồ ng b ộ d ữ li ệ u | D ữ li ệ u backup m ỗ i ngày          |
| CRM- Platform      | Validate CustomerProfile | /customerprofile/validate | Validate d ữ li ệ u CustomerProfile trong CRM- Platform. | L ỗ i nghiêm tr ọ ng | Tích h ợ p v ớ i CRM                  |
| Security- Firewall | Update VPN               | /vpn/update               | Update d ữ li ệ u VPN trong Security- Firewall.          | Ghi log đầy đủ       | Tích h ợ p v ớ i CRM                  |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| IVR-System          | Schedule Invoice        | /invoice/schedule        | Schedule d ữ li ệ u Invoice trong IVR- System.           | Không l ỗ i          | Tích h ợ p v ớ i CRM         |
|---------------------|-------------------------|--------------------------|----------------------------------------------------------|----------------------|------------------------------|
| BCCS2-Core          | Search Whitelist        | /whitelist/search        | Search d ữ li ệ u Whitelist trong BCCS2-Core.            | Ghi log đầy đủ       | Theo chu ẩ n ISO 27001       |
| BCCS2-Core          | Optimize PackagePlan    | /packageplan/optimize    | Optimize d ữ li ệ u PackagePlan trong BCCS2-Core.        | Hi ể n th ị báo cáo  | Theo chu ẩ n ISO 27001       |
| Infra-Server        | Optimize VPN            | /vpn/optimize            | Optimize d ữ li ệ u VPN trong Infra- Server.             | Thông báo qua email  | D ữ li ệ u backup m ỗ i ngày |
| IVR-System          | Schedule QoS            | /qos/schedule            | Schedule d ữ li ệ u QoS trong IVR- System.               | Hi ể n th ị báo cáo  | Tích h ợ p v ớ i CRM         |
| CRM- Platform       | Optimize IVRPrompt      | /ivrprompt/optimize      | Optimize d ữ li ệ u IVRPrompt trong CRM-Platform.        | Thông báo qua email  | B ả o m ậ t 2 l ớ p          |
| IPCC- ContactCenter | Optimize KPIReport      | /kpireport/optimize      | Optimize d ữ li ệ u KPIReport trong IPCC- ContactCenter. | L ỗ i nghiêm tr ọ ng | B ả o m ậ t 2 l ớ p          |
| Infra-Server        | Schedule FirewallPolicy | /firewallpolicy/schedule | Schedule d ữ li ệ u FirewallPolicy trong Infra-Server.   | T ự độ ng retry      | Có cơ ch ế rollback          |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| Security- Firewall   | Schedule QoS          | /qos/schedule          | Schedule d ữ li ệ u QoS trong Security- Firewall.        | Thông báo qua SMS    | Ch ạ y theo l ị ch cron               |
|----------------------|-----------------------|------------------------|----------------------------------------------------------|----------------------|---------------------------------------|
| RPA-Engine           | Optimize KPIReport    | /kpireport/optimize    | Optimize d ữ li ệ u KPIReport trong RPA-Engine.          | L ỗ i nghiêm tr ọ ng | Ch ạ y theo l ị ch cron               |
| IPCC- ContactCenter  | Update KPIReport      | /kpireport/update      | Update d ữ li ệ u KPIReport trong IPCC- ContactCenter.   | T ự độ ng retry      | K ế t n ố i v ớ i h ệ th ố ng Billing |
| RPA-Engine           | Config FirewallPolicy | /firewallpolicy/config | Config d ữ li ệ u FirewallPolicy trong RPA-Engine.       | Thành công           | Theo quy đị nh Viettel                |
| Security- Firewall   | Optimize ClusterNode  | /clusternode/optimize  | Optimize d ữ li ệ u ClusterNode trong Security-Firewall. | Ghi log đầy đủ       | Ch ỉ dùng cho admin                   |
| Infra-Network        | Schedule SwitchConfig | /switchconfig/schedule | Schedule d ữ li ệ u SwitchConfig trong Infra-Network.    | Thông báo qua email  | Ch ạ y theo l ị ch cron               |
| RPA-Engine           | Analyze KPIReport     | /kpireport/analyze     | Analyze d ữ li ệ u KPIReport trong RPA-Engine.           | Không l ỗ i          | D ữ li ệ u backup m ỗ i ngày          |
| QA- Automation       | Config IVRPrompt      | /ivrprompt/config      | Config d ữ li ệ u IVRPrompt trong QA-Automation.         | Không l ỗ i          | K ế t n ố i v ớ i h ệ                 |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

|                |                        |                         |                                                     |                      | th ố ng Billing              |
|----------------|------------------------|-------------------------|-----------------------------------------------------|----------------------|------------------------------|
| QA- Automation | Monitor Invoice        | /invoice/monitor        | Monitor d ữ li ệ u Invoice trong QA- Automation.    | C ả nh báo           | Theo chu ẩ n ISO 27001       |
| IVR-System     | Insert CustomerProfile | /customerprofile/insert | Insert d ữ li ệ u CustomerProfile trong IVR-System. | Hi ể n th ị báo cáo  | B ả o m ậ t 2 l ớ p          |
| IVR-System     | Optimize QoS           | /qos/optimize           | Optimize d ữ li ệ u QoS trong IVR- System.          | Hi ể n th ị báo cáo  | Ch ỉ dùng cho admin          |
| BCCS2- Billing | Schedule Invoice       | /invoice/schedule       | Schedule d ữ li ệ u Invoice trong BCCS2-Billing.    | Đồ ng b ộ d ữ li ệ u | D ữ li ệ u backup m ỗ i ngày |
| BCCS2- Billing | Search DebtControl     | /debtcontrol/search     | Search d ữ li ệ u DebtControl trong BCCS2-Billing.  | C ả nh báo           | Tích h ợ p v ớ i CRM         |
| IVR-System     | Optimize Lead          | /lead/optimize          | Optimize d ữ li ệ u Lead trong IVR- System.         | Không l ỗ i          | Ch ỉ dùng cho admin          |
| RPA-Engine     | Config Lead            | /lead/config            | Config d ữ li ệ u Lead trong RPA-Engine.            | C ả nh báo           | Ch ỉ dùng cho admin          |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| Security- Firewall   | Monitor ClusterNode   | /clusternode/monitor   | Monitor d ữ li ệ u ClusterNode trong Security-Firewall.   | Thông báo qua SMS    | Ch ạ y theo l ị ch cron               |
|----------------------|-----------------------|------------------------|-----------------------------------------------------------|----------------------|---------------------------------------|
| Security- Firewall   | Update QoS            | /qos/update            | Update d ữ li ệ u QoS trong Security- Firewall.           | Ghi log đầy đủ       | Theo chu ẩ n ISO 27001                |
| RPA-Engine           | Import Blacklist      | /blacklist/import      | Import d ữ li ệ u Blacklist trong RPA- Engine.            | Ghi log đầy đủ       | Tích h ợ p v ớ i CRM                  |
| RPA-Engine           | Delete StorageVolume  | /storagevolume/delete  | Delete d ữ li ệ u StorageVolume trong RPA-Engine.         | T ự độ ng retry      | B ả o m ậ t 2 l ớ p                   |
| RPA-Engine           | Generate Invoice      | /invoice/generate      | Generate d ữ li ệ u Invoice trong RPA- Engine.            | Không l ỗ i          | Ch ỉ dùng cho admin                   |
| Infra-Network        | Search CDRReport      | /cdrreport/search      | Search d ữ li ệ u CDRReport trong Infra-Network.          | Đồ ng b ộ d ữ li ệ u | Ch ạ y theo l ị ch cron               |
| BCCS2-Core           | Optimize DebtControl  | /debtcontrol/optimize  | Optimize d ữ li ệ u DebtControl trong BCCS2-Core.         | Thông báo qua email  | Yêu c ầ u xác th ự c ngườ i dùng      |
| Infra-Network        | Delete Campaign       | /campaign/delete       | Delete d ữ li ệ u Campaign trong Infra-Network.           | Thành công           | K ế t n ố i v ớ i h ệ th ố ng Billing |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| Infra-Network      | Delete CustomerProfile   | /customerprofile/delete   | Delete d ữ li ệ u CustomerProfile trong Infra-Network.   | Không l ỗ i          | Ch ạ y theo l ị ch cron          |
|--------------------|--------------------------|---------------------------|----------------------------------------------------------|----------------------|----------------------------------|
| BCCS2-Core         | Monitor TransactionLog   | /transactionlog/monitor   | Monitor d ữ li ệ u TransactionLog trong BCCS2-Core.      | Hi ể n th ị báo cáo  | Yêu c ầ u xác th ự c ngườ i dùng |
| QA- Automation     | Export Contact           | /contact/export           | Export d ữ li ệ u Contact trong QA- Automation.          | Hi ể n th ị báo cáo  | Yêu c ầ u xác th ự c ngườ i dùng |
| Security- Firewall | Delete Contact           | /contact/delete           | Delete d ữ li ệ u Contact trong Security-Firewall.       | Ghi log đầy đủ       | Theo chu ẩ n ISO 27001           |
| Security- Firewall | Search Whitelist         | /whitelist/search         | Search d ữ li ệ u Whitelist trong Security-Firewall.     | L ỗ i nghiêm tr ọ ng | Ch ỉ dùng cho admin              |
| BCCS2- Billing     | Import Contact           | /contact/import           | Import d ữ li ệ u Contact trong BCCS2-Billing.           | C ả nh báo           | Theo quy đị nh Viettel           |
| Infra-Server       | Insert APIGateway        | /apigateway/insert        | Insert d ữ li ệ u APIGateway trong Infra-Server.         | Không l ỗ i          | Theo quy đị nh Viettel           |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| QA- Automation     | Optimize TransactionLog   | /transactionlog/optimize   | Optimize d ữ li ệ u TransactionLog trong QA- Automation.   | Thành công           | Tích h ợ p v ớ i CRM                  |
|--------------------|---------------------------|----------------------------|------------------------------------------------------------|----------------------|---------------------------------------|
| Infra-Network      | Optimize Opportunity      | /opportunity/optimize      | Optimize d ữ li ệ u Opportunity trong Infra-Network.       | Không l ỗ i          | K ế t n ố i v ớ i h ệ th ố ng Billing |
| RPA-Engine         | Update PackagePlan        | /packageplan/update        | Update d ữ li ệ u PackagePlan trong RPA-Engine.            | L ỗ i nghiêm tr ọ ng | Theo chu ẩ n ISO 27001                |
| BCCS2-Core         | Generate Invoice          | /invoice/generate          | Generate d ữ li ệ u Invoice trong BCCS2-Core.              | Thông báo qua email  | K ế t n ố i v ớ i h ệ th ố ng Billing |
| BCCS2-Core         | Import SwitchConfig       | /switchconfig/import       | Import d ữ li ệ u SwitchConfig trong BCCS2-Core.           | Không l ỗ i          | Theo chu ẩ n ISO 27001                |
| Security- Firewall | Schedule Campaign         | /campaign/schedule         | Schedule d ữ li ệ u Campaign trong Security-Firewall.      | T ự độ ng retry      | Yêu c ầ u xác th ự c ngườ i dùng      |
| BCCS2- Billing     | Update Whitelist          | /whitelist/update          | Update d ữ li ệ u Whitelist trong BCCS2-Billing.           | T ự độ ng retry      | Theo chu ẩ n ISO 27001                |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| QA- Automation     | Insert DataLake       | /datalake/insert       | Insert d ữ li ệ u DataLake trong QA- Automation.         | Ghi log đầy đủ       | Yêu c ầ u xác th ự c ngườ i dùng      |
|--------------------|-----------------------|------------------------|----------------------------------------------------------|----------------------|---------------------------------------|
| CRM- Platform      | Import CDRReport      | /cdrreport/import      | Import d ữ li ệ u CDRReport trong CRM-Platform.          | T ự độ ng retry      | Ch ạ y theo l ị ch cron               |
| QA- Automation     | Config AgentStatus    | /agentstatus/config    | Config d ữ li ệ u AgentStatus trong QA-Automation.       | Hi ể n th ị báo cáo  | K ế t n ố i v ớ i h ệ th ố ng Billing |
| IVR-System         | Search CDRReport      | /cdrreport/search      | Search d ữ li ệ u CDRReport trong IVR-System.            | L ỗ i nghiêm tr ọ ng | D ữ li ệ u backup m ỗ i ngày          |
| Infra-Network      | Validate SwitchConfig | /switchconfig/validate | Validate d ữ li ệ u SwitchConfig trong Infra-Network.    | Thông báo qua SMS    | Yêu c ầ u xác th ự c ngườ i dùng      |
| BCCS2- Billing     | Monitor ClusterNode   | /clusternode/monitor   | Monitor d ữ li ệ u ClusterNode trong BCCS2-Billing.      | Thông báo qua SMS    | Tích h ợ p v ớ i CRM                  |
| Security- Firewall | Validate Opportunity  | /opportunity/validate  | Validate d ữ li ệ u Opportunity trong Security-Firewall. | Thông báo qua SMS    | Ch ỉ dùng cho admin                   |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| Security- Firewall   | Schedule Whitelist   | /whitelist/schedule   | Schedule d ữ li ệ u Whitelist trong Security-Firewall.   | Đồ ng b ộ d ữ li ệ u   | Tích h ợ p v ớ i CRM                  |
|----------------------|----------------------|-----------------------|----------------------------------------------------------|------------------------|---------------------------------------|
| BCCS2- Billing       | Delete APIGateway    | /apigateway/delete    | Delete d ữ li ệ u APIGateway trong BCCS2-Billing.        | Thành công             | Theo quy đị nh Viettel                |
| Infra-Network        | Search ClusterNode   | /clusternode/search   | Search d ữ li ệ u ClusterNode trong Infra-Network.       | Đồ ng b ộ d ữ li ệ u   | Theo quy đị nh Viettel                |
| BCCS2-Core           | Config Contact       | /contact/config       | Config d ữ li ệ u Contact trong BCCS2-Core.              | Thông báo qua email    | Yêu c ầ u xác th ự c ngườ i dùng      |
| IPCC- ContactCenter  | Config Contact       | /contact/config       | Config d ữ li ệ u Contact trong IPCC- ContactCenter.     | Thành công             | Ch ỉ dùng cho admin                   |
| QA- Automation       | Config CDRReport     | /cdrreport/config     | Config d ữ li ệ u CDRReport trong QA-Automation.         | Không l ỗ i            | K ế t n ố i v ớ i h ệ th ố ng Billing |
| BCCS2-Core           | Schedule KPIReport   | /kpireport/schedule   | Schedule d ữ li ệ u KPIReport trong BCCS2-Core.          | Thông báo qua SMS      | Ch ạ y theo l ị ch cron               |
| Infra-Network        | Delete IVRPrompt     | /ivrprompt/delete     | Delete d ữ li ệ u IVRPrompt trong Infra-Network.         | T ự độ ng retry        | D ữ li ệ u backup                     |

<!-- image -->

TD444

L ầ n ban hành: 1

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

|                    |                        |                         |                                                          |                     | m ỗ i ngày                       |
|--------------------|------------------------|-------------------------|----------------------------------------------------------|---------------------|----------------------------------|
| Security- Firewall | Validate DebtControl   | /debtcontrol/validate   | Validate d ữ li ệ u DebtControl trong Security-Firewall. | Thành công          | Có cơ ch ế rollback              |
| BCCS2-Core         | Optimize Lead          | /lead/optimize          | Optimize d ữ li ệ u Lead trong BCCS2- Core.              | Thông báo qua SMS   | Theo quy đị nh Viettel           |
| RPA-Engine         | Validate Opportunity   | /opportunity/validate   | Validate d ữ li ệ u Opportunity trong RPA-Engine.        | C ả nh báo          | Có cơ ch ế rollback              |
| IVR-System         | Update DataLake        | /datalake/update        | Update d ữ li ệ u DataLake trong IVR-System.             | Không l ỗ i         | Theo chu ẩ n ISO 27001           |
| Infra-Server       | Config CustomerProfile | /customerprofile/config | Config d ữ li ệ u CustomerProfile trong Infra-Server.    | Thông báo qua SMS   | Yêu c ầ u xác th ự c ngườ i dùng |
| BCCS2- Billing     | Validate StorageVolume | /storagevolume/validate | Validate d ữ li ệ u StorageVolume trong BCCS2- Billing.  | Thông báo qua email | Theo quy đị nh Viettel           |
| CRM- Platform      | Analyze APIGateway     | /apigateway/analyze     | Analyze d ữ li ệ u APIGateway trong CRM-Platform.        | T ự độ ng retry     | Theo quy đị nh Viettel           |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| Infra-Network      | Search Contact        | /contact/search        | Search d ữ li ệ u Contact trong Infra- Network.      | Hi ể n th ị báo cáo   | Theo quy đị nh Viettel           |
|--------------------|-----------------------|------------------------|------------------------------------------------------|-----------------------|----------------------------------|
| Infra-Network      | Monitor QoS           | /qos/monitor           | Monitor d ữ li ệ u QoS trong Infra-Network.          | L ỗ i nghiêm tr ọ ng  | Ch ạ y theo l ị ch cron          |
| Security- Firewall | Update KPIReport      | /kpireport/update      | Update d ữ li ệ u KPIReport trong Security-Firewall. | Thông báo qua SMS     | Yêu c ầ u xác th ự c ngườ i dùng |
| RPA-Engine         | Export StorageVolume  | /storagevolume/export  | Export d ữ li ệ u StorageVolume trong RPA-Engine.    | T ự độ ng retry       | D ữ li ệ u backup m ỗ i ngày     |
| IVR-System         | Config PackagePlan    | /packageplan/config    | Config d ữ li ệ u PackagePlan trong IVR-System.      | C ả nh báo            | Theo quy đị nh Viettel           |
| CRM- Platform      | Update FirewallPolicy | /firewallpolicy/update | Update d ữ li ệ u FirewallPolicy trong CRM-Platform. | Thành công            | Tích h ợ p v ớ i CRM             |
| QA- Automation     | Analyze Blacklist     | /blacklist/analyze     | Analyze d ữ li ệ u Blacklist trong QA- Automation.   | Không l ỗ i           | D ữ li ệ u backup m ỗ i ngày     |
| CRM- Platform      | Insert AgentStatus    | /agentstatus/insert    | Insert d ữ li ệ u AgentStatus trong CRM-Platform.    | T ự độ ng retry       | B ả o m ậ t 2 l ớ p              |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| BCCS2-Core          | Config DataLake    | /datalake/config    | Config d ữ li ệ u DataLake trong BCCS2-Core.           | Ghi log đầy đủ       | K ế t n ố i v ớ i h ệ th ố ng Billing   |
|---------------------|--------------------|---------------------|--------------------------------------------------------|----------------------|-----------------------------------------|
| IPCC- ContactCenter | Generate Invoice   | /invoice/generate   | Generate d ữ li ệ u Invoice trong IPCC- ContactCenter. | Thành công           | Yêu c ầ u xác th ự c ngườ i dùng        |
| BCCS2-Core          | Update DebtControl | /debtcontrol/update | Update d ữ li ệ u DebtControl trong BCCS2-Core.        | T ự độ ng retry      | Tích h ợ p v ớ i CRM                    |
| BCCS2- Billing      | Optimize IVRPrompt | /ivrprompt/optimize | Optimize d ữ li ệ u IVRPrompt trong BCCS2-Billing.     | L ỗ i nghiêm tr ọ ng | D ữ li ệ u backup m ỗ i ngày            |
| BCCS2-Core          | Update IVRPrompt   | /ivrprompt/update   | Update d ữ li ệ u IVRPrompt trong BCCS2-Core.          | Thành công           | B ả o m ậ t 2 l ớ p                     |
| IVR-System          | Validate CDRReport | /cdrreport/validate | Validate d ữ li ệ u CDRReport trong IVR-System.        | L ỗ i nghiêm tr ọ ng | Có cơ ch ế rollback                     |
| IPCC- ContactCenter | Insert Blacklist   | /blacklist/insert   | Insert d ữ li ệ u Blacklist trong IPCC- ContactCenter. | Ghi log đầy đủ       | Có cơ ch ế rollback                     |
| BCCS2-Core          | Import PackagePlan | /packageplan/import | Import d ữ li ệ u PackagePlan trong BCCS2-Core.        | L ỗ i nghiêm tr ọ ng | Theo quy đị nh Viettel                  |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| QA- Automation      | Delete IVRPrompt       | /ivrprompt/delete       | Delete d ữ li ệ u IVRPrompt trong QA-Automation.         | C ả nh báo           | Theo chu ẩ n ISO 27001                |
|---------------------|------------------------|-------------------------|----------------------------------------------------------|----------------------|---------------------------------------|
| QA- Automation      | Import Opportunity     | /opportunity/import     | Import d ữ li ệ u Opportunity trong QA-Automation.       | Ghi log đầy đủ       | D ữ li ệ u backup m ỗ i ngày          |
| RPA-Engine          | Delete Promotion       | /promotion/delete       | Delete d ữ li ệ u Promotion trong RPA-Engine.            | C ả nh báo           | Yêu c ầ u xác th ự c ngườ i dùng      |
| IVR-System          | Update Campaign        | /campaign/update        | Update d ữ li ệ u Campaign trong IVR-System.             | Không l ỗ i          | Tích h ợ p v ớ i CRM                  |
| IPCC- ContactCenter | Optimize CDRReport     | /cdrreport/optimize     | Optimize d ữ li ệ u CDRReport trong IPCC- ContactCenter. | Thông báo qua email  | K ế t n ố i v ớ i h ệ th ố ng Billing |
| Infra-Network       | Monitor VPN            | /vpn/monitor            | Monitor d ữ li ệ u VPN trong Infra- Network.             | Thành công           | Tích h ợ p v ớ i CRM                  |
| RPA-Engine          | Import IVRPrompt       | /ivrprompt/import       | Import d ữ li ệ u IVRPrompt trong RPA-Engine.            | Không l ỗ i          | Theo chu ẩ n ISO 27001                |
| BCCS2- Billing      | Validate StorageVolume | /storagevolume/validate | Validate d ữ li ệ u StorageVolume trong BCCS2- Billing.  | Đồ ng b ộ d ữ li ệ u | Ch ỉ dùng cho admin                   |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| QA- Automation     | Delete Invoice       | /invoice/delete       | Delete d ữ li ệ u Invoice trong QA- Automation.        | Ghi log đầy đủ       | Yêu c ầ u xác th ự c ngườ i dùng      |
|--------------------|----------------------|-----------------------|--------------------------------------------------------|----------------------|---------------------------------------|
| BCCS2-Core         | Update PackagePlan   | /packageplan/update   | Update d ữ li ệ u PackagePlan trong BCCS2-Core.        | T ự độ ng retry      | Ch ỉ dùng cho admin                   |
| CRM- Platform      | Search Campaign      | /campaign/search      | Search d ữ li ệ u Campaign trong CRM-Platform.         | Đồ ng b ộ d ữ li ệ u | Tích h ợ p v ớ i CRM                  |
| BCCS2- Billing     | Insert VPN           | /vpn/insert           | Insert d ữ li ệ u VPN trong BCCS2- Billing.            | L ỗ i nghiêm tr ọ ng | D ữ li ệ u backup m ỗ i ngày          |
| IVR-System         | Schedule ClusterNode | /clusternode/schedule | Schedule d ữ li ệ u ClusterNode trong IVR-System.      | Thông báo qua email  | K ế t n ố i v ớ i h ệ th ố ng Billing |
| Security- Firewall | Optimize KPIReport   | /kpireport/optimize   | Optimize d ữ li ệ u KPIReport trong Security-Firewall. | C ả nh báo           | Tích h ợ p v ớ i CRM                  |
| Infra-Server       | Analyze Promotion    | /promotion/analyze    | Analyze d ữ li ệ u Promotion trong Infra-Server.       | T ự độ ng retry      | Theo chu ẩ n ISO 27001                |
| BCCS2- Billing     | Export IVRPrompt     | /ivrprompt/export     | Export d ữ li ệ u IVRPrompt trong BCCS2-Billing.       | Thành công           | Ch ạ y theo l ị ch cron               |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| Security- Firewall   | Insert DebtControl    | /debtcontrol/insert    | Insert d ữ li ệ u DebtControl trong Security-Firewall.   | Không l ỗ i          | Theo quy đị nh Viettel                |
|----------------------|-----------------------|------------------------|----------------------------------------------------------|----------------------|---------------------------------------|
| QA- Automation       | Schedule KPIReport    | /kpireport/schedule    | Schedule d ữ li ệ u KPIReport trong QA-Automation.       | T ự độ ng retry      | Theo chu ẩ n ISO 27001                |
| Infra-Server         | Monitor Whitelist     | /whitelist/monitor     | Monitor d ữ li ệ u Whitelist trong Infra-Server.         | Thông báo qua email  | Ch ạ y theo l ị ch cron               |
| Infra-Server         | Config FirewallPolicy | /firewallpolicy/config | Config d ữ li ệ u FirewallPolicy trong Infra-Server.     | Thông báo qua SMS    | K ế t n ố i v ớ i h ệ th ố ng Billing |
| Infra-Network        | Monitor Lead          | /lead/monitor          | Monitor d ữ li ệ u Lead trong Infra- Network.            | Không l ỗ i          | D ữ li ệ u backup m ỗ i ngày          |
| IPCC- ContactCenter  | Delete PackagePlan    | /packageplan/delete    | Delete d ữ li ệ u PackagePlan trong IPCC- ContactCenter. | Đồ ng b ộ d ữ li ệ u | Yêu c ầ u xác th ự c ngườ i dùng      |
| BCCS2-Core           | Generate AccountLock  | /accountlock/generate  | Generate d ữ li ệ u AccountLock trong BCCS2-Core.        | Thông báo qua email  | Yêu c ầ u xác th ự c ngườ i dùng      |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| IVR-System          | Config IVRPrompt       | /ivrprompt/config       | Config d ữ li ệ u IVRPrompt trong IVR-System.               | Ghi log đầy đủ       | B ả o m ậ t 2 l ớ p     |
|---------------------|------------------------|-------------------------|-------------------------------------------------------------|----------------------|-------------------------|
| Infra-Network       | Optimize Opportunity   | /opportunity/optimize   | Optimize d ữ li ệ u Opportunity trong Infra-Network.        | Đồ ng b ộ d ữ li ệ u | Ch ỉ dùng cho admin     |
| Infra-Network       | Monitor Contact        | /contact/monitor        | Monitor d ữ li ệ u Contact trong Infra- Network.            | Không l ỗ i          | Ch ạ y theo l ị ch cron |
| Security- Firewall  | Import Campaign        | /campaign/import        | Import d ữ li ệ u Campaign trong Security-Firewall.         | Thành công           | Ch ỉ dùng cho admin     |
| Infra-Network       | Schedule AgentStatus   | /agentstatus/schedule   | Schedule d ữ li ệ u AgentStatus trong Infra-Network.        | Hi ể n th ị báo cáo  | Theo chu ẩ n ISO 27001  |
| Security- Firewall  | Import CustomerProfile | /customerprofile/import | Import d ữ li ệ u CustomerProfile trong Security- Firewall. | Thông báo qua SMS    | Theo quy đị nh Viettel  |
| IPCC- ContactCenter | Delete QoS             | /qos/delete             | Delete d ữ li ệ u QoS trong IPCC- ContactCenter.            | Ghi log đầy đủ       | Theo quy đị nh Viettel  |
| Infra-Server        | Validate Lead          | /lead/validate          | Validate d ữ li ệ u Lead trong Infra- Server.               | Đồ ng b ộ d ữ li ệ u | Có cơ ch ế rollback     |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| BCCS2- Billing      | Delete CustomerProfile   | /customerprofile/delete   | Delete d ữ li ệ u CustomerProfile trong BCCS2- Billing.   | Hi ể n th ị báo cáo   | Có cơ ch ế rollback                   |
|---------------------|--------------------------|---------------------------|-----------------------------------------------------------|-----------------------|---------------------------------------|
| BCCS2- Billing      | Generate AccountLock     | /accountlock/generate     | Generate d ữ li ệ u AccountLock trong BCCS2-Billing.      | Thành công            | K ế t n ố i v ớ i h ệ th ố ng Billing |
| CRM- Platform       | Delete PackagePlan       | /packageplan/delete       | Delete d ữ li ệ u PackagePlan trong CRM-Platform.         | Ghi log đầy đủ        | Ch ạ y theo l ị ch cron               |
| CRM- Platform       | Validate Opportunity     | /opportunity/validate     | Validate d ữ li ệ u Opportunity trong CRM-Platform.       | Ghi log đầy đủ        | Có cơ ch ế rollback                   |
| Infra-Network       | Optimize Promotion       | /promotion/optimize       | Optimize d ữ li ệ u Promotion trong Infra-Network.        | Không l ỗ i           | B ả o m ậ t 2 l ớ p                   |
| IPCC- ContactCenter | Search DebtControl       | /debtcontrol/search       | Search d ữ li ệ u DebtControl trong IPCC- ContactCenter.  | Ghi log đầy đủ        | Tích h ợ p v ớ i CRM                  |
| RPA-Engine          | Generate AgentStatus     | /agentstatus/generate     | Generate d ữ li ệ u AgentStatus trong RPA-Engine.         | Không l ỗ i           | Tích h ợ p v ớ i CRM                  |
| Infra-Server        | Config VPN               | /vpn/config               | Config d ữ li ệ u VPN trong Infra-Server.                 | Đồ ng b ộ d ữ li ệ u  | Ch ỉ dùng cho admin                   |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| Security- Firewall   | Update ClusterNode      | /clusternode/update      | Update d ữ li ệ u ClusterNode trong Security-Firewall.       | Không l ỗ i         | Theo quy đị nh Viettel                |
|----------------------|-------------------------|--------------------------|--------------------------------------------------------------|---------------------|---------------------------------------|
| RPA-Engine           | Config IVRPrompt        | /ivrprompt/config        | Config d ữ li ệ u IVRPrompt trong RPA-Engine.                | Thông báo qua SMS   | Có cơ ch ế rollback                   |
| CRM- Platform        | Search DataLake         | /datalake/search         | Search d ữ li ệ u DataLake trong CRM-Platform.               | Ghi log đầy đủ      | Ch ỉ dùng cho admin                   |
| Security- Firewall   | Optimize TransactionLog | /transactionlog/optimize | Optimize d ữ li ệ u TransactionLog trong Security- Firewall. | Thông báo qua email | D ữ li ệ u backup m ỗ i ngày          |
| IPCC- ContactCenter  | Schedule Invoice        | /invoice/schedule        | Schedule d ữ li ệ u Invoice trong IPCC- ContactCenter.       | Thành công          | K ế t n ố i v ớ i h ệ th ố ng Billing |
| BCCS2-Core           | Update TransactionLog   | /transactionlog/update   | Update d ữ li ệ u TransactionLog trong BCCS2-Core.           | Thông báo qua SMS   | Ch ỉ dùng cho admin                   |
| BCCS2-Core           | Delete TransactionLog   | /transactionlog/delete   | Delete d ữ li ệ u TransactionLog trong BCCS2-Core.           | Ghi log đầy đủ      | B ả o m ậ t 2 l ớ p                   |
| IVR-System           | Config VPN              | /vpn/config              | Config d ữ li ệ u VPN trong IVR-System.                      | Không l ỗ i         | Ch ỉ dùng cho admin                   |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| CRM- Platform   | Generate ClusterNode   | /clusternode/generate   | Generate d ữ li ệ u ClusterNode trong CRM-Platform.   | Không l ỗ i          | B ả o m ậ t 2 l ớ p                   |
|-----------------|------------------------|-------------------------|-------------------------------------------------------|----------------------|---------------------------------------|
| BCCS2-Core      | Optimize Lead          | /lead/optimize          | Optimize d ữ li ệ u Lead trong BCCS2- Core.           | L ỗ i nghiêm tr ọ ng | K ế t n ố i v ớ i h ệ th ố ng Billing |
| IVR-System      | Update CustomerProfile | /customerprofile/update | Update d ữ li ệ u CustomerProfile trong IVR-System.   | Thông báo qua email  | Theo chu ẩ n ISO 27001                |
| Infra-Network   | Schedule AccountLock   | /accountlock/schedule   | Schedule d ữ li ệ u AccountLock trong Infra-Network.  | L ỗ i nghiêm tr ọ ng | Ch ỉ dùng cho admin                   |
| BCCS2-Core      | Search ClusterNode     | /clusternode/search     | Search d ữ li ệ u ClusterNode trong BCCS2-Core.       | Đồ ng b ộ d ữ li ệ u | Tích h ợ p v ớ i CRM                  |
| BCCS2- Billing  | Monitor Opportunity    | /opportunity/monitor    | Monitor d ữ li ệ u Opportunity trong BCCS2-Billing.   | Thông báo qua SMS    | Yêu c ầ u xác th ự c ngườ i dùng      |
| RPA-Engine      | Import Campaign        | /campaign/import        | Import d ữ li ệ u Campaign trong RPA-Engine.          | L ỗ i nghiêm tr ọ ng | Có cơ ch ế rollback                   |
| QA- Automation  | Search SwitchConfig    | /switchconfig/search    | Search d ữ li ệ u SwitchConfig trong QA-Automation.   | T ự độ ng retry      | Có cơ ch ế rollback                   |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| BCCS2- Billing     | Export QoS            | /qos/export            | Export d ữ li ệ u QoS trong BCCS2- Billing.              | Đồ ng b ộ d ữ li ệ u   | Theo chu ẩ n ISO 27001       |
|--------------------|-----------------------|------------------------|----------------------------------------------------------|------------------------|------------------------------|
| Infra-Server       | Update Invoice        | /invoice/update        | Update d ữ li ệ u Invoice trong Infra- Server.           | Ghi log đầy đủ         | Có cơ ch ế rollback          |
| BCCS2- Billing     | Monitor VPN           | /vpn/monitor           | Monitor d ữ li ệ u VPN trong BCCS2- Billing.             | Thông báo qua SMS      | D ữ li ệ u backup m ỗ i ngày |
| QA- Automation     | Search SwitchConfig   | /switchconfig/search   | Search d ữ li ệ u SwitchConfig trong QA-Automation.      | Đồ ng b ộ d ữ li ệ u   | Ch ạ y theo l ị ch cron      |
| Security- Firewall | Optimize PackagePlan  | /packageplan/optimize  | Optimize d ữ li ệ u PackagePlan trong Security-Firewall. | Thành công             | Theo quy đị nh Viettel       |
| QA- Automation     | Delete Contact        | /contact/delete        | Delete d ữ li ệ u Contact trong QA- Automation.          | T ự độ ng retry        | Theo chu ẩ n ISO 27001       |
| BCCS2-Core         | Schedule SwitchConfig | /switchconfig/schedule | Schedule d ữ li ệ u SwitchConfig trong BCCS2-Core.       | Thông báo qua SMS      | Có cơ ch ế rollback          |
| IVR-System         | Analyze Promotion     | /promotion/analyze     | Analyze d ữ li ệ u Promotion trong IVR-System.           | Không l ỗ i            | D ữ li ệ u backup m ỗ i ngày |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| QA- Automation     | Import Invoice      | /invoice/import      | Import d ữ li ệ u Invoice trong QA- Automation.      | Thành công          | Tích h ợ p v ớ i CRM             |
|--------------------|---------------------|----------------------|------------------------------------------------------|---------------------|----------------------------------|
| QA- Automation     | Import VPN          | /vpn/import          | Import d ữ li ệ u VPN trong QA- Automation.          | Thông báo qua email | Theo quy đị nh Viettel           |
| IVR-System         | Update SwitchConfig | /switchconfig/update | Update d ữ li ệ u SwitchConfig trong IVR-System.     | Thành công          | Ch ỉ dùng cho admin              |
| BCCS2- Billing     | Insert CDRReport    | /cdrreport/insert    | Insert d ữ li ệ u CDRReport trong BCCS2-Billing.     | Thành công          | Theo quy đị nh Viettel           |
| Security- Firewall | Export Whitelist    | /whitelist/export    | Export d ữ li ệ u Whitelist trong Security-Firewall. | C ả nh báo          | Ch ỉ dùng cho admin              |
| CRM- Platform      | Search DataLake     | /datalake/search     | Search d ữ li ệ u DataLake trong CRM-Platform.       | C ả nh báo          | B ả o m ậ t 2 l ớ p              |
| Infra-Server       | Schedule IVRPrompt  | /ivrprompt/schedule  | Schedule d ữ li ệ u IVRPrompt trong Infra-Server.    | Thông báo qua email | Yêu c ầ u xác th ự c ngườ i dùng |
| Infra-Network      | Analyze Campaign    | /campaign/analyze    | Analyze d ữ li ệ u Campaign trong Infra-Network.     | Thông báo qua SMS   | B ả o m ậ t 2 l ớ p              |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| BCCS2- Billing     | Delete Opportunity      | /opportunity/delete      | Delete d ữ li ệ u Opportunity trong BCCS2-Billing.   | Hi ể n th ị báo cáo   | Yêu c ầ u xác th ự c ngườ i dùng   |
|--------------------|-------------------------|--------------------------|------------------------------------------------------|-----------------------|------------------------------------|
| QA- Automation     | Monitor AccountLock     | /accountlock/monitor     | Monitor d ữ li ệ u AccountLock trong QA-Automation.  | Ghi log đầy đủ        | Ch ạ y theo l ị ch cron            |
| BCCS2-Core         | Monitor Campaign        | /campaign/monitor        | Monitor d ữ li ệ u Campaign trong BCCS2-Core.        | Không l ỗ i           | Ch ỉ dùng cho admin                |
| IVR-System         | Export QoS              | /qos/export              | Export d ữ li ệ u QoS trong IVR-System.              | Ghi log đầy đủ        | Yêu c ầ u xác th ự c ngườ i dùng   |
| Security- Firewall | Config KPIReport        | /kpireport/config        | Config d ữ li ệ u KPIReport trong Security-Firewall. | Hi ể n th ị báo cáo   | Theo chu ẩ n ISO 27001             |
| Infra-Server       | Monitor Blacklist       | /blacklist/monitor       | Monitor d ữ li ệ u Blacklist trong Infra- Server.    | Thông báo qua SMS     | Theo quy đị nh Viettel             |
| BCCS2-Core         | Optimize FirewallPolicy | /firewallpolicy/optimize | Optimize d ữ li ệ u FirewallPolicy trong BCCS2-Core. | L ỗ i nghiêm tr ọ ng  | B ả o m ậ t 2 l ớ p                |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| IPCC- ContactCenter   | Search PackagePlan   | /packageplan/search   | Search d ữ li ệ u PackagePlan trong IPCC- ContactCenter.   | T ự độ ng retry      | Ch ỉ dùng cho admin              |
|-----------------------|----------------------|-----------------------|------------------------------------------------------------|----------------------|----------------------------------|
| IPCC- ContactCenter   | Delete Promotion     | /promotion/delete     | Delete d ữ li ệ u Promotion trong IPCC- ContactCenter.     | Thông báo qua SMS    | Yêu c ầ u xác th ự c ngườ i dùng |
| BCCS2-Core            | Monitor SwitchConfig | /switchconfig/monitor | Monitor d ữ li ệ u SwitchConfig trong BCCS2-Core.          | T ự độ ng retry      | Yêu c ầ u xác th ự c ngườ i dùng |
| IPCC- ContactCenter   | Schedule DataLake    | /datalake/schedule    | Schedule d ữ li ệ u DataLake trong IPCC- ContactCenter.    | Ghi log đầy đủ       | Theo chu ẩ n ISO 27001           |
| IPCC- ContactCenter   | Insert Queue         | /queue/insert         | Insert d ữ li ệ u Queue trong IPCC- ContactCenter.         | Thông báo qua email  | Tích h ợ p v ớ i CRM             |
| RPA-Engine            | Validate APIGateway  | /apigateway/validate  | Validate d ữ li ệ u APIGateway trong RPA-Engine.           | Thông báo qua SMS    | Theo chu ẩ n ISO 27001           |
| Infra-Server          | Schedule AgentStatus | /agentstatus/schedule | Schedule d ữ li ệ u AgentStatus trong Infra-Server.        | Đồ ng b ộ d ữ li ệ u | Theo chu ẩ n ISO 27001           |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| IVR-System          | Optimize Lead         | /lead/optimize         | Optimize d ữ li ệ u Lead trong IVR- System.                | Không l ỗ i          | Ch ỉ dùng cho admin                   |
|---------------------|-----------------------|------------------------|------------------------------------------------------------|----------------------|---------------------------------------|
| BCCS2-Core          | Optimize Promotion    | /promotion/optimize    | Optimize d ữ li ệ u Promotion trong BCCS2-Core.            | Thông báo qua SMS    | K ế t n ố i v ớ i h ệ th ố ng Billing |
| BCCS2- Billing      | Generate Queue        | /queue/generate        | Generate d ữ li ệ u Queue trong BCCS2-Billing.             | Đồ ng b ộ d ữ li ệ u | Yêu c ầ u xác th ự c ngườ i dùng      |
| BCCS2-Core          | Monitor PackagePlan   | /packageplan/monitor   | Monitor d ữ li ệ u PackagePlan trong BCCS2-Core.           | Hi ể n th ị báo cáo  | K ế t n ố i v ớ i h ệ th ố ng Billing |
| Security- Firewall  | Analyze StorageVolume | /storagevolume/analyze | Analyze d ữ li ệ u StorageVolume trong Security- Firewall. | Thông báo qua SMS    | Yêu c ầ u xác th ự c ngườ i dùng      |
| IPCC- ContactCenter | Export Contact        | /contact/export        | Export d ữ li ệ u Contact trong IPCC- ContactCenter.       | Đồ ng b ộ d ữ li ệ u | Ch ạ y theo l ị ch cron               |
| Infra-Network       | Validate QoS          | /qos/validate          | Validate d ữ li ệ u QoS trong Infra-Network.               | Thành công           | Theo quy đị nh Viettel                |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| RPA-Engine          | Search Invoice        | /invoice/search        | Search d ữ li ệ u Invoice trong RPA- Engine.                | Thông báo qua SMS    | Tích h ợ p v ớ i CRM    |
|---------------------|-----------------------|------------------------|-------------------------------------------------------------|----------------------|-------------------------|
| IPCC- ContactCenter | Update FirewallPolicy | /firewallpolicy/update | Update d ữ li ệ u FirewallPolicy trong IPCC- ContactCenter. | T ự độ ng retry      | Theo chu ẩ n ISO 27001  |
| QA- Automation      | Config ClusterNode    | /clusternode/config    | Config d ữ li ệ u ClusterNode trong QA-Automation.          | L ỗ i nghiêm tr ọ ng | Tích h ợ p v ớ i CRM    |
| BCCS2- Billing      | Delete FirewallPolicy | /firewallpolicy/delete | Delete d ữ li ệ u FirewallPolicy trong BCCS2-Billing.       | C ả nh báo           | B ả o m ậ t 2 l ớ p     |
| IVR-System          | Schedule APIGateway   | /apigateway/schedule   | Schedule d ữ li ệ u APIGateway trong IVR-System.            | Hi ể n th ị báo cáo  | Có cơ ch ế rollback     |
| BCCS2-Core          | Config DataLake       | /datalake/config       | Config d ữ li ệ u DataLake trong BCCS2-Core.                | Đồ ng b ộ d ữ li ệ u | Theo quy đị nh Viettel  |
| BCCS2- Billing      | Optimize Whitelist    | /whitelist/optimize    | Optimize d ữ li ệ u Whitelist trong BCCS2-Billing.          | Không l ỗ i          | Ch ạ y theo l ị ch cron |
| Infra-Network       | Search ClusterNode    | /clusternode/search    | Search d ữ li ệ u ClusterNode trong Infra-Network.          | Hi ể n th ị báo cáo  | Có cơ ch ế rollback     |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| IPCC- ContactCenter   | Search Blacklist         | /blacklist/search         | Search d ữ li ệ u Blacklist trong IPCC- ContactCenter.   | Hi ể n th ị báo cáo   | B ả o m ậ t 2 l ớ p                   |
|-----------------------|--------------------------|---------------------------|----------------------------------------------------------|-----------------------|---------------------------------------|
| IPCC- ContactCenter   | Optimize Queue           | /queue/optimize           | Optimize d ữ li ệ u Queue trong IPCC- ContactCenter.     | L ỗ i nghiêm tr ọ ng  | Có cơ ch ế rollback                   |
| Infra-Network         | Schedule IVRPrompt       | /ivrprompt/schedule       | Schedule d ữ li ệ u IVRPrompt trong Infra-Network.       | T ự độ ng retry       | Theo quy đị nh Viettel                |
| RPA-Engine            | Schedule CustomerProfile | /customerprofile/schedule | Schedule d ữ li ệ u CustomerProfile trong RPA-Engine.    | Thông báo qua email   | Tích h ợ p v ớ i CRM                  |
| Infra-Network         | Analyze Queue            | /queue/analyze            | Analyze d ữ li ệ u Queue trong Infra- Network.           | Không l ỗ i           | Theo chu ẩ n ISO 27001                |
| CRM- Platform         | Update DataLake          | /datalake/update          | Update d ữ li ệ u DataLake trong CRM-Platform.           | Thông báo qua SMS     | Ch ỉ dùng cho admin                   |
| QA- Automation        | Export AgentStatus       | /agentstatus/export       | Export d ữ li ệ u AgentStatus trong QA-Automation.       | Đồ ng b ộ d ữ li ệ u  | K ế t n ố i v ớ i h ệ th ố ng Billing |
| BCCS2- Billing        | Schedule SwitchConfig    | /switchconfig/schedule    | Schedule d ữ li ệ u SwitchConfig trong BCCS2-Billing.    | L ỗ i nghiêm tr ọ ng  | Tích h ợ p v ớ i CRM                  |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| IVR-System          | Update Contact        | /contact/update        | Update d ữ li ệ u Contact trong IVR- System.           | Hi ể n th ị báo cáo   | K ế t n ố i v ớ i h ệ th ố ng Billing   |
|---------------------|-----------------------|------------------------|--------------------------------------------------------|-----------------------|-----------------------------------------|
| IVR-System          | Insert ClusterNode    | /clusternode/insert    | Insert d ữ li ệ u ClusterNode trong IVR-System.        | Thông báo qua SMS     | Ch ạ y theo l ị ch cron                 |
| Security- Firewall  | Validate Campaign     | /campaign/validate     | Validate d ữ li ệ u Campaign trong Security-Firewall.  | Hi ể n th ị báo cáo   | Theo chu ẩ n ISO 27001                  |
| IPCC- ContactCenter | Search Queue          | /queue/search          | Search d ữ li ệ u Queue trong IPCC- ContactCenter.     | T ự độ ng retry       | Ch ạ y theo l ị ch cron                 |
| IPCC- ContactCenter | Search Whitelist      | /whitelist/search      | Search d ữ li ệ u Whitelist trong IPCC- ContactCenter. | Ghi log đầy đủ        | Theo quy đị nh Viettel                  |
| IVR-System          | Config FirewallPolicy | /firewallpolicy/config | Config d ữ li ệ u FirewallPolicy trong IVR-System.     | Hi ể n th ị báo cáo   | B ả o m ậ t 2 l ớ p                     |
| QA- Automation      | Validate AccountLock  | /accountlock/validate  | Validate d ữ li ệ u AccountLock trong QA-Automation.   | T ự độ ng retry       | Tích h ợ p v ớ i CRM                    |
| RPA-Engine          | Insert AccountLock    | /accountlock/insert    | Insert d ữ li ệ u AccountLock trong RPA-Engine.        | Thông báo qua SMS     | Yêu c ầ u xác th ự c ngườ i dùng        |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| Infra-Network   | Insert Invoice          | /invoice/insert          | Insert d ữ li ệ u Invoice trong Infra- Network.         | Thông báo qua SMS    | Ch ỉ dùng cho admin                   |
|-----------------|-------------------------|--------------------------|---------------------------------------------------------|----------------------|---------------------------------------|
| RPA-Engine      | Generate Whitelist      | /whitelist/generate      | Generate d ữ li ệ u Whitelist trong RPA-Engine.         | T ự độ ng retry      | Theo quy đị nh Viettel                |
| BCCS2-Core      | Analyze Invoice         | /invoice/analyze         | Analyze d ữ li ệ u Invoice trong BCCS2-Core.            | Thông báo qua email  | K ế t n ố i v ớ i h ệ th ố ng Billing |
| QA- Automation  | Generate FirewallPolicy | /firewallpolicy/generate | Generate d ữ li ệ u FirewallPolicy trong QA-Automation. | T ự độ ng retry      | Theo quy đị nh Viettel                |
| Infra-Server    | Analyze AgentStatus     | /agentstatus/analyze     | Analyze d ữ li ệ u AgentStatus trong Infra-Server.      | Đồ ng b ộ d ữ li ệ u | Yêu c ầ u xác th ự c ngườ i dùng      |
| Infra-Server    | Export DataLake         | /datalake/export         | Export d ữ li ệ u DataLake trong Infra-Server.          | Thành công           | K ế t n ố i v ớ i h ệ th ố ng Billing |
| BCCS2-Core      | Insert PackagePlan      | /packageplan/insert      | Insert d ữ li ệ u PackagePlan trong BCCS2-Core.         | Ghi log đầy đủ       | D ữ li ệ u backup m ỗ i ngày          |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| BCCS2-Core          | Delete DataLake        | /datalake/delete        | Delete d ữ li ệ u DataLake trong BCCS2-Core.            | Ghi log đầy đủ       | D ữ li ệ u backup m ỗ i ngày     |
|---------------------|------------------------|-------------------------|---------------------------------------------------------|----------------------|----------------------------------|
| Infra-Server        | Validate DataLake      | /datalake/validate      | Validate d ữ li ệ u DataLake trong Infra-Server.        | Không l ỗ i          | Ch ạ y theo l ị ch cron          |
| Infra-Server        | Schedule QoS           | /qos/schedule           | Schedule d ữ li ệ u QoS trong Infra- Server.            | T ự độ ng retry      | Yêu c ầ u xác th ự c ngườ i dùng |
| RPA-Engine          | Search CustomerProfile | /customerprofile/search | Search d ữ li ệ u CustomerProfile trong RPA-Engine.     | Hi ể n th ị báo cáo  | D ữ li ệ u backup m ỗ i ngày     |
| Infra-Server        | Update Lead            | /lead/update            | Update d ữ li ệ u Lead trong Infra-Server.              | Không l ỗ i          | Có cơ ch ế rollback              |
| Security- Firewall  | Generate CDRReport     | /cdrreport/generate     | Generate d ữ li ệ u CDRReport trong Security-Firewall.  | Đồ ng b ộ d ữ li ệ u | Ch ỉ dùng cho admin              |
| Security- Firewall  | Monitor PackagePlan    | /packageplan/monitor    | Monitor d ữ li ệ u PackagePlan trong Security-Firewall. | C ả nh báo           | Yêu c ầ u xác th ự c ngườ i dùng |
| IPCC- ContactCenter | Export FirewallPolicy  | /firewallpolicy/export  | Export d ữ li ệ u FirewallPolicy trong                  | Thông báo            | Theo chu ẩ n                     |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

|                     |                      |                       | IPCC- ContactCenter.                                      | qua SMS              | ISO 27001                             |
|---------------------|----------------------|-----------------------|-----------------------------------------------------------|----------------------|---------------------------------------|
| Security- Firewall  | Import Promotion     | /promotion/import     | Import d ữ li ệ u Promotion trong Security-Firewall.      | Ghi log đầy đủ       | D ữ li ệ u backup m ỗ i ngày          |
| BCCS2- Billing      | Delete KPIReport     | /kpireport/delete     | Delete d ữ li ệ u KPIReport trong BCCS2-Billing.          | Thông báo qua SMS    | Yêu c ầ u xác th ự c ngườ i dùng      |
| IPCC- ContactCenter | Import VPN           | /vpn/import           | Import d ữ li ệ u VPN trong IPCC- ContactCenter.          | C ả nh báo           | Tích h ợ p v ớ i CRM                  |
| IPCC- ContactCenter | Monitor Whitelist    | /whitelist/monitor    | Monitor d ữ li ệ u Whitelist trong IPCC- ContactCenter.   | Ghi log đầy đủ       | K ế t n ố i v ớ i h ệ th ố ng Billing |
| QA- Automation      | Optimize DebtControl | /debtcontrol/optimize | Optimize d ữ li ệ u DebtControl trong QA-Automation.      | L ỗ i nghiêm tr ọ ng | K ế t n ố i v ớ i h ệ th ố ng Billing |
| IPCC- ContactCenter | Insert SwitchConfig  | /switchconfig/insert  | Insert d ữ li ệ u SwitchConfig trong IPCC- ContactCenter. | T ự độ ng retry      | K ế t n ố i v ớ i h ệ th ố ng Billing |
| IPCC- ContactCenter | Config CDRReport     | /cdrreport/config     | Config d ữ li ệ u CDRReport trong IPCC- ContactCenter.    | L ỗ i nghiêm tr ọ ng | Theo quy đị nh Viettel                |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| IPCC- ContactCenter   | Config PackagePlan    | /packageplan/config    | Config d ữ li ệ u PackagePlan trong IPCC- ContactCenter.   | Ghi log đầy đủ       | Yêu c ầ u xác th ự c ngườ i dùng   |
|-----------------------|-----------------------|------------------------|------------------------------------------------------------|----------------------|------------------------------------|
| IPCC- ContactCenter   | Config AgentStatus    | /agentstatus/config    | Config d ữ li ệ u AgentStatus trong IPCC- ContactCenter.   | C ả nh báo           | Có cơ ch ế rollback                |
| Security- Firewall    | Monitor IVRPrompt     | /ivrprompt/monitor     | Monitor d ữ li ệ u IVRPrompt trong Security-Firewall.      | Ghi log đầy đủ       | D ữ li ệ u backup m ỗ i ngày       |
| RPA-Engine            | Update FirewallPolicy | /firewallpolicy/update | Update d ữ li ệ u FirewallPolicy trong RPA-Engine.         | Hi ể n th ị báo cáo  | Ch ạ y theo l ị ch cron            |
| Infra-Server          | Delete Contact        | /contact/delete        | Delete d ữ li ệ u Contact trong Infra- Server.             | Thông báo qua SMS    | Theo quy đị nh Viettel             |
| Infra-Network         | Insert Invoice        | /invoice/insert        | Insert d ữ li ệ u Invoice trong Infra- Network.            | Đồ ng b ộ d ữ li ệ u | Tích h ợ p v ớ i CRM               |
| QA- Automation        | Schedule Campaign     | /campaign/schedule     | Schedule d ữ li ệ u Campaign trong QA- Automation.         | Ghi log đầy đủ       | Yêu c ầ u xác th ự c ngườ i dùng   |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| BCCS2- Billing      | Analyze Whitelist     | /whitelist/analyze     | Analyze d ữ li ệ u Whitelist trong BCCS2-Billing.       | Thông báo qua SMS    | Yêu c ầ u xác th ự c ngườ i dùng      |
|---------------------|-----------------------|------------------------|---------------------------------------------------------|----------------------|---------------------------------------|
| Security- Firewall  | Generate CDRReport    | /cdrreport/generate    | Generate d ữ li ệ u CDRReport trong Security-Firewall.  | Thành công           | Có cơ ch ế rollback                   |
| IPCC- ContactCenter | Analyze Whitelist     | /whitelist/analyze     | Analyze d ữ li ệ u Whitelist trong IPCC- ContactCenter. | Không l ỗ i          | D ữ li ệ u backup m ỗ i ngày          |
| QA- Automation      | Export Invoice        | /invoice/export        | Export d ữ li ệ u Invoice trong QA- Automation.         | Hi ể n th ị báo cáo  | Theo chu ẩ n ISO 27001                |
| IPCC- ContactCenter | Export QoS            | /qos/export            | Export d ữ li ệ u QoS trong IPCC- ContactCenter.        | C ả nh báo           | D ữ li ệ u backup m ỗ i ngày          |
| BCCS2-Core          | Insert CDRReport      | /cdrreport/insert      | Insert d ữ li ệ u CDRReport trong BCCS2-Core.           | L ỗ i nghiêm tr ọ ng | K ế t n ố i v ớ i h ệ th ố ng Billing |
| BCCS2-Core          | Update APIGateway     | /apigateway/update     | Update d ữ li ệ u APIGateway trong BCCS2-Core.          | T ự độ ng retry      | Ch ỉ dùng cho admin                   |
| Infra-Server        | Export TransactionLog | /transactionlog/export | Export d ữ li ệ u TransactionLog trong Infra-Server.    | C ả nh báo           | Theo chu ẩ n                          |

<!-- image -->

TD444

L ầ n ban hành: 1

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

|                    |                     |                      |                                                         |                      | ISO 27001               |
|--------------------|---------------------|----------------------|---------------------------------------------------------|----------------------|-------------------------|
| Infra-Server       | Update Contact      | /contact/update      | Update d ữ li ệ u Contact trong Infra- Server.          | C ả nh báo           | Theo quy đị nh Viettel  |
| CRM- Platform      | Insert CDRReport    | /cdrreport/insert    | Insert d ữ li ệ u CDRReport trong CRM-Platform.         | Thành công           | B ả o m ậ t 2 l ớ p     |
| BCCS2-Core         | Export KPIReport    | /kpireport/export    | Export d ữ li ệ u KPIReport trong BCCS2-Core.           | Hi ể n th ị báo cáo  | Tích h ợ p v ớ i CRM    |
| IVR-System         | Monitor APIGateway  | /apigateway/monitor  | Monitor d ữ li ệ u APIGateway trong IVR-System.         | Ghi log đầy đủ       | Theo quy đị nh Viettel  |
| Security- Firewall | Import Queue        | /queue/import        | Import d ữ li ệ u Queue trong Security-Firewall.        | C ả nh báo           | B ả o m ậ t 2 l ớ p     |
| BCCS2-Core         | Import Queue        | /queue/import        | Import d ữ li ệ u Queue trong BCCS2-Core.               | Đồ ng b ộ d ữ li ệ u | Ch ạ y theo l ị ch cron |
| IVR-System         | Analyze Campaign    | /campaign/analyze    | Analyze d ữ li ệ u Campaign trong IVR-System.           | Ghi log đầy đủ       | Ch ỉ dùng cho admin     |
| Security- Firewall | Generate APIGateway | /apigateway/generate | Generate d ữ li ệ u APIGateway trong Security-Firewall. | Đồ ng b ộ d ữ li ệ u | K ế t n ố i v ớ i h ệ   |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

|                     |                    |                     |                                                          |                      | th ố ng Billing                       |
|---------------------|--------------------|---------------------|----------------------------------------------------------|----------------------|---------------------------------------|
| CRM- Platform       | Monitor Promotion  | /promotion/monitor  | Monitor d ữ li ệ u Promotion trong CRM-Platform.         | C ả nh báo           | Tích h ợ p v ớ i CRM                  |
| Security- Firewall  | Monitor Whitelist  | /whitelist/monitor  | Monitor d ữ li ệ u Whitelist trong Security-Firewall.    | Thông báo qua SMS    | Theo chu ẩ n ISO 27001                |
| IPCC- ContactCenter | Delete PackagePlan | /packageplan/delete | Delete d ữ li ệ u PackagePlan trong IPCC- ContactCenter. | Thành công           | Yêu c ầ u xác th ự c ngườ i dùng      |
| IVR-System          | Insert DebtControl | /debtcontrol/insert | Insert d ữ li ệ u DebtControl trong IVR-System.          | L ỗ i nghiêm tr ọ ng | Yêu c ầ u xác th ự c ngườ i dùng      |
| Infra-Server        | Optimize Whitelist | /whitelist/optimize | Optimize d ữ li ệ u Whitelist trong Infra-Server.        | T ự độ ng retry      | D ữ li ệ u backup m ỗ i ngày          |
| Infra-Network       | Monitor Promotion  | /promotion/monitor  | Monitor d ữ li ệ u Promotion trong Infra-Network.        | Hi ể n th ị báo cáo  | K ế t n ố i v ớ i h ệ th ố ng Billing |
| BCCS2-Core          | Import IVRPrompt   | /ivrprompt/import   | Import d ữ li ệ u IVRPrompt trong BCCS2-Core.            | Không l ỗ i          | Theo chu ẩ n ISO 27001                |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| IVR-System     | Validate TransactionLog   | /transactionlog/validate   | Validate d ữ li ệ u TransactionLog trong IVR-System.   | Ghi log đầy đủ       | Ch ạ y theo l ị ch cron      |
|----------------|---------------------------|----------------------------|--------------------------------------------------------|----------------------|------------------------------|
| BCCS2-Core     | Import CustomerProfile    | /customerprofile/import    | Import d ữ li ệ u CustomerProfile trong BCCS2-Core.    | L ỗ i nghiêm tr ọ ng | D ữ li ệ u backup m ỗ i ngày |
| BCCS2- Billing | Optimize QoS              | /qos/optimize              | Optimize d ữ li ệ u QoS trong BCCS2- Billing.          | C ả nh báo           | Theo quy đị nh Viettel       |
| BCCS2-Core     | Schedule Queue            | /queue/schedule            | Schedule d ữ li ệ u Queue trong BCCS2-Core.            | C ả nh báo           | Có cơ ch ế rollback          |
| CRM- Platform  | Optimize ClusterNode      | /clusternode/optimize      | Optimize d ữ li ệ u ClusterNode trong CRM-Platform.    | L ỗ i nghiêm tr ọ ng | Ch ạ y theo l ị ch cron      |
| CRM- Platform  | Delete FirewallPolicy     | /firewallpolicy/delete     | Delete d ữ li ệ u FirewallPolicy trong CRM-Platform.   | T ự độ ng retry      | Ch ỉ dùng cho admin          |
| Infra-Server   | Export Whitelist          | /whitelist/export          | Export d ữ li ệ u Whitelist trong Infra-Server.        | Thành công           | Ch ạ y theo l ị ch cron      |
| Infra-Server   | Import CDRReport          | /cdrreport/import          | Import d ữ li ệ u CDRReport trong Infra-Server.        | Đồ ng b ộ d ữ li ệ u | Tích h ợ p v ớ i CRM         |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| Infra-Server        | Update KPIReport   | /kpireport/update   | Update d ữ li ệ u KPIReport trong Infra-Server.       | T ự độ ng retry      | Có cơ ch ế rollback              |
|---------------------|--------------------|---------------------|-------------------------------------------------------|----------------------|----------------------------------|
| BCCS2- Billing      | Config Lead        | /lead/config        | Config d ữ li ệ u Lead trong BCCS2- Billing.          | Đồ ng b ộ d ữ li ệ u | Có cơ ch ế rollback              |
| CRM- Platform       | Analyze Blacklist  | /blacklist/analyze  | Analyze d ữ li ệ u Blacklist trong CRM-Platform.      | C ả nh báo           | Ch ạ y theo l ị ch cron          |
| QA- Automation      | Update Whitelist   | /whitelist/update   | Update d ữ li ệ u Whitelist trong QA- Automation.     | Thông báo qua SMS    | Tích h ợ p v ớ i CRM             |
| IPCC- ContactCenter | Monitor Invoice    | /invoice/monitor    | Monitor d ữ li ệ u Invoice trong IPCC- ContactCenter. | Ghi log đầy đủ       | B ả o m ậ t 2 l ớ p              |
| CRM- Platform       | Export Invoice     | /invoice/export     | Export d ữ li ệ u Invoice trong CRM- Platform.        | L ỗ i nghiêm tr ọ ng | Yêu c ầ u xác th ự c ngườ i dùng |
| Infra-Server        | Import KPIReport   | /kpireport/import   | Import d ữ li ệ u KPIReport trong Infra-Server.       | T ự độ ng retry      | Ch ạ y theo l ị ch cron          |
| QA- Automation      | Validate Lead      | /lead/validate      | Validate d ữ li ệ u Lead trong QA- Automation.        | Thành công           | Ch ỉ dùng cho admin              |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| Infra-Server       | Update VPN         | /vpn/update         | Update d ữ li ệ u VPN trong Infra-Server.             | Thông báo qua email   | Yêu c ầ u xác th ự c ngườ i dùng      |
|--------------------|--------------------|---------------------|-------------------------------------------------------|-----------------------|---------------------------------------|
| Infra-Network      | Search VPN         | /vpn/search         | Search d ữ li ệ u VPN trong Infra-Network.            | Thông báo qua email   | Ch ạ y theo l ị ch cron               |
| BCCS2- Billing     | Export APIGateway  | /apigateway/export  | Export d ữ li ệ u APIGateway trong BCCS2-Billing.     | Đồ ng b ộ d ữ li ệ u  | Yêu c ầ u xác th ự c ngườ i dùng      |
| Infra-Network      | Import KPIReport   | /kpireport/import   | Import d ữ li ệ u KPIReport trong Infra-Network.      | Thông báo qua email   | K ế t n ố i v ớ i h ệ th ố ng Billing |
| Security- Firewall | Export APIGateway  | /apigateway/export  | Export d ữ li ệ u APIGateway trong Security-Firewall. | T ự độ ng retry       | Theo chu ẩ n ISO 27001                |
| Infra-Server       | Schedule Blacklist | /blacklist/schedule | Schedule d ữ li ệ u Blacklist trong Infra- Server.    | Hi ể n th ị báo cáo   | Yêu c ầ u xác th ự c ngườ i dùng      |
| QA- Automation     | Schedule Blacklist | /blacklist/schedule | Schedule d ữ li ệ u Blacklist trong QA- Automation.   | T ự độ ng retry       | Tích h ợ p v ớ i CRM                  |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| Infra-Server   | Monitor CustomerProfile   | /customerprofile/monitor   | Monitor d ữ li ệ u CustomerProfile trong Infra-Server.   | Đồ ng b ộ d ữ li ệ u   | Ch ỉ dùng cho admin                   |
|----------------|---------------------------|----------------------------|----------------------------------------------------------|------------------------|---------------------------------------|
| IVR-System     | Generate PackagePlan      | /packageplan/generate      | Generate d ữ li ệ u PackagePlan trong IVR-System.        | Thông báo qua SMS      | Có cơ ch ế rollback                   |
| BCCS2-Core     | Optimize IVRPrompt        | /ivrprompt/optimize        | Optimize d ữ li ệ u IVRPrompt trong BCCS2-Core.          | Đồ ng b ộ d ữ li ệ u   | Yêu c ầ u xác th ự c ngườ i dùng      |
| Infra-Network  | Delete Whitelist          | /whitelist/delete          | Delete d ữ li ệ u Whitelist trong Infra-Network.         | L ỗ i nghiêm tr ọ ng   | Theo chu ẩ n ISO 27001                |
| Infra-Server   | Delete PackagePlan        | /packageplan/delete        | Delete d ữ li ệ u PackagePlan trong Infra-Server.        | Không l ỗ i            | Theo chu ẩ n ISO 27001                |
| RPA-Engine     | Update IVRPrompt          | /ivrprompt/update          | Update d ữ li ệ u IVRPrompt trong RPA-Engine.            | Thông báo qua SMS      | Theo quy đị nh Viettel                |
| IVR-System     | Generate Blacklist        | /blacklist/generate        | Generate d ữ li ệ u Blacklist trong IVR- System.         | Thành công             | K ế t n ố i v ớ i h ệ th ố ng Billing |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| RPA-Engine          | Analyze CDRReport      | /cdrreport/analyze      | Analyze d ữ li ệ u CDRReport trong RPA-Engine.         | Hi ể n th ị báo cáo   | Tích h ợ p v ớ i CRM             |
|---------------------|------------------------|-------------------------|--------------------------------------------------------|-----------------------|----------------------------------|
| IPCC- ContactCenter | Search Contact         | /contact/search         | Search d ữ li ệ u Contact trong IPCC- ContactCenter.   | Thành công            | Ch ỉ dùng cho admin              |
| IVR-System          | Analyze FirewallPolicy | /firewallpolicy/analyze | Analyze d ữ li ệ u FirewallPolicy trong IVR-System.    | Không l ỗ i           | Yêu c ầ u xác th ự c ngườ i dùng |
| Infra-Network       | Search IVRPrompt       | /ivrprompt/search       | Search d ữ li ệ u IVRPrompt trong Infra-Network.       | Thông báo qua email   | Yêu c ầ u xác th ự c ngườ i dùng |
| Infra-Network       | Schedule VPN           | /vpn/schedule           | Schedule d ữ li ệ u VPN trong Infra- Network.          | Hi ể n th ị báo cáo   | Ch ỉ dùng cho admin              |
| IVR-System          | Monitor TransactionLog | /transactionlog/monitor | Monitor d ữ li ệ u TransactionLog trong IVR-System.    | T ự độ ng retry       | Yêu c ầ u xác th ự c ngườ i dùng |
| QA- Automation      | Monitor StorageVolume  | /storagevolume/monitor  | Monitor d ữ li ệ u StorageVolume trong QA- Automation. | Thông báo qua email   | Tích h ợ p v ớ i CRM             |

<!-- image -->

## VIETTEL AI RACE

## DANH M Ụ C CH ỨC NĂNG BCCS2

TD444

L ầ n ban hành: 1

| BCCS2- Billing   | Insert FirewallPolicy   | /firewallpolicy/insert   | Insert d ữ li ệ u FirewallPolicy trong BCCS2-Billing.   | Thông báo qua email   | D ữ li ệ u backup m ỗ i ngày   |
|------------------|-------------------------|--------------------------|---------------------------------------------------------|-----------------------|--------------------------------|
| RPA-Engine       | Optimize Campaign       | /campaign/optimize       | Optimize d ữ li ệ u Campaign trong RPA-Engine.          | T ự độ ng retry       | D ữ li ệ u backup m ỗ i ngày   |