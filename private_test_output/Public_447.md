<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| Test case              | Mô t ả                                                                                                                                          | Input                       | Expected Output                                      | Phương pháp      | Ghi chú                                |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|------------------------------------------------------|------------------|----------------------------------------|
| Login test             | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.            | API call batch 1000 request | User login thành công trong <1s                      | JMeter script    | Test môi trườ ng Pre- Prod             |
| Load test              | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.             | stress load > 10k TPS       | User login thành công trong <1s                      | Manual test plan | Ph ả i log toàn b ộ k ế t qu ả         |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | network disconnect          | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | Manual test plan | So sánh benchmark v ớ i release trướ c |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | stress load > 10k TPS       | Cluster failover t ự độ ng trong 5s                  | Manual test plan | Theo chu ẩ n ISTQB                     |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| Security scan          | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.          | API call batch 1000 request   | User login thành công trong <1s                      | Manual test plan     | G ử i báo cáo PDF hàng ngày            |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|------------------------------------------------------|----------------------|----------------------------------------|
| Security scan          | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.          | DB corruption                 | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố  | K ị ch b ả n Ansible | Test môi trườ ng Pre- Prod             |
| API stress test        | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.        | valid data                    | User login thành công trong <1s                      | Manual test plan     | So sánh benchmark v ớ i release trướ c |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | valid data                    | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | Manual test plan     | Test môi trườ ng Pre- Prod             |
| Failover test          | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng,                                                            | network disconnect            | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau          | Manual test plan     | So sánh benchmark v ớ i release trướ c |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                        | bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                                                                                               |                       | s ự c ố                                              |                      |                                        |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|------------------------------------------------------|----------------------|----------------------------------------|
| API stress test        | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.        | DB corruption         | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | K ị ch b ả n Ansible | Test môi trườ ng Pre- Prod             |
| Data consistency test  | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.  | stress load > 10k TPS | Cluster failover t ự độ ng trong 5s                  | K ị ch b ả n Ansible | So sánh benchmark v ớ i release trướ c |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | stress load > 10k TPS | User login thành công trong <1s                      | K ị ch b ả n Ansible | G ử i báo cáo PDF hàng ngày            |
| Failover test          | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.          | stress load > 10k TPS | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố  | JMeter script        | Ph ả i log toàn b ộ k ế t qu ả         |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| API stress test   | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | invalid data       | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố   | Automation Selenium   | Ph ả i log toàn b ộ k ế t qu ả         |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------|-----------------------|----------------------------------------|
| Load test         | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.        | network disconnect | Cluster failover t ự độ ng trong 5s                   | JMeter script         | Ph ả i log toàn b ộ k ế t qu ả         |
| Security scan     | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.     | invalid data       | User login thành công trong <1s                       | JMeter script         | So sánh benchmark v ớ i release trướ c |
| Failover test     | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.     | valid data         | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10  | K ị ch b ả n Ansible  | Theo chu ẩ n ISTQB                     |
| Failover test     | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n                                 | network disconnect | User login thành công                                 | K ị ch b ả n Ansible  | Test môi trườ ng Pre- Prod             |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                       | thành công và th ấ t b ạ i.                                                                                                                    |                    | trong <1s                                         |                     |                                        |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|---------------------------------------------------|---------------------|----------------------------------------|
| Failover test         | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.         | invalid data       | User login thành công trong <1s                   | Manual test plan    | G ử i báo cáo PDF hàng ngày            |
| API stress test       | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.       | valid data         | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n | Automation Selenium | Test môi trườ ng Pre- Prod             |
| Data consistency test | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | network disconnect | Cluster failover t ự độ ng trong 5s               | JMeter script       | So sánh benchmark v ớ i release trướ c |
| Load test             | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.            | valid data         | User login thành công trong <1s                   | Manual test plan    | Ph ả i log toàn b ộ k ế t qu ả         |
| API stress            | Th ự c hi ệ n API stress test để ki ể mth ử                                                                                                    | invalid            | User login                                        | JMeter              | G ử i báo cáo                          |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| test                   | ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                                                    | data               | thành công trong <1s                | script              | PDF hàng ngày               |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------|---------------------|-----------------------------|
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | invalid data       | Cluster failover t ự độ ng trong 5s | Automation Selenium | Test môi trườ ng Pre- Prod  |
| Security scan          | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.          | valid data         | User login thành công trong <1s     | JMeter script       | G ử i báo cáo PDF hàng ngày |
| Security scan          | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.          | network disconnect | Cluster failover t ự độ ng trong 5s | Manual test plan    | G ử i báo cáo PDF hàng ngày |
| Login test             | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành                                  | invalid data       | User login thành công trong <1s     | Manual test plan    | Theo chu ẩ n ISTQB          |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                       | công và th ấ t b ạ i.                                                                                                                    |                             |                                                   |                      |                                        |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|---------------------------------------------------|----------------------|----------------------------------------|
| Load test             | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.      | stress load > 10k TPS       | User login thành công trong <1s                   | Automation Selenium  | Ph ả i log toàn b ộ k ế t qu ả         |
| API stress test       | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | API call batch 1000 request | Cluster failover t ự độ ng trong 5s               | K ị ch b ả n Ansible | Ph ả i log toàn b ộ k ế t qu ả         |
| Load test             | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.      | stress load > 10k TPS       | Cluster failover t ự độ ng trong 5s               | K ị ch b ả n Ansible | Test môi trườ ng Pre- Prod             |
| API stress test       | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | network disconnect          | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n | Manual test plan     | Ph ả i log toàn b ộ k ế t qu ả         |
| Data consistency test | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ                                                      | network disconnect          | H ệ th ố ng ch ị u t ả i 20k TPS không            | K ị ch b ả n Ansible | So sánh benchmark v ớ i release trướ c |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                        | th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                                                                                      |                    | gián đoạ n                                           |                      |                                        |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|------------------------------------------------------|----------------------|----------------------------------------|
| Load test              | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.             | DB corruption      | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố  | K ị ch b ả n Ansible | Test môi trườ ng Pre- Prod             |
| Data consistency test  | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.  | network disconnect | User login thành công trong <1s                      | Manual test plan     | Theo chu ẩ n ISTQB                     |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | DB corruption      | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | JMeter script        | So sánh benchmark v ớ i release trướ c |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | network disconnect | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | JMeter script        | Test môi trườ ng Pre- Prod             |
| Database               | Th ự c hi ệ n Database                                                                                                                          | DB                 | H ệ th ố ng                                          | Automation           | So sánh                                |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| recovery test          | recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                        | corruption            | ch ị u t ả i 20k TPS không gián đoạ n               | Selenium            | benchmark v ớ i release trướ c   |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|-----------------------------------------------------|---------------------|----------------------------------|
| Data consistency test  | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.  | valid data            | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | Manual test plan    | Ph ả i log toàn b ộ k ế t qu ả   |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | stress load > 10k TPS | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | JMeter script       | G ử i báo cáo PDF hàng ngày      |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | valid data            | Cluster failover t ự độ ng trong 5s                 | Automation Selenium | Ph ả i log toàn b ộ k ế t qu ả   |
| Data consistency test  | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch                                    | invalid data          | User login thành công                               | Manual test plan    | Test môi trườ ng Pre- Prod       |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                       | b ả n thành công và th ấ t b ạ i.                                                                                                      |                       | trong <1s                                            |                      |                             |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------|------------------------------------------------------|----------------------|-----------------------------|
| Failover test         | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | stress load > 10k TPS | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | JMeter script        | G ử i báo cáo PDF hàng ngày |
| Login test            | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | stress load > 10k TPS | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | JMeter script        | Theo chu ẩ n ISTQB          |
| Login test            | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | invalid data          | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | Automation Selenium  | Test môi trườ ng Pre- Prod  |
| Login test            | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | valid data            | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n    | Manual test plan     | Theo chu ẩ n ISTQB          |
| Data consistency test | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ                                                    | network disconnect    | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau          | K ị ch b ả n Ansible | G ử i báo cáo PDF hàng ngày |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                 | th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                                                                               |                             | s ự c ố                                              |                      |                                        |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|------------------------------------------------------|----------------------|----------------------------------------|
| Login test      | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.     | network disconnect          | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n    | Automation Selenium  | So sánh benchmark v ớ i release trướ c |
| API stress test | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | network disconnect          | Cluster failover t ự độ ng trong 5s                  | K ị ch b ả n Ansible | Test môi trườ ng Pre- Prod             |
| Failover test   | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | API call batch 1000 request | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | Automation Selenium  | Test môi trườ ng Pre- Prod             |
| API stress test | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | invalid data                | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | Automation Selenium  | Test môi trườ ng Pre- Prod             |
| API stress      | Th ự c hi ệ n API stress                                                                                                                 | network                     | Không                                                | JMeter               | Theo chu ẩ n                           |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| test                   | test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                                 | disconnect   | phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10      | script              | ISTQB                                  |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|--------------|-----------------------------------------------------|---------------------|----------------------------------------|
| Data consistency test  | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.  | invalid data | Cluster failover t ự độ ng trong 5s                 | Manual test plan    | So sánh benchmark v ớ i release trướ c |
| Failover test          | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.          | valid data   | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | Automation Selenium | So sánh benchmark v ớ i release trướ c |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | valid data   | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n   | Manual test plan    | So sánh benchmark v ớ i release trướ c |
| Data consistency test  | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch                                    | invalid data | Cluster failover t ự độ ng trong 5s                 | Automation Selenium | So sánh benchmark v ớ i release trướ c |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                        | b ả n thành công và th ấ t b ạ i.                                                                                                               |                       |                                                   |                      |                                        |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|---------------------------------------------------|----------------------|----------------------------------------|
| Load test              | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.             | DB corruption         | User login thành công trong <1s                   | Manual test plan     | So sánh benchmark v ớ i release trướ c |
| API stress test        | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.        | DB corruption         | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n | K ị ch b ả n Ansible | So sánh benchmark v ớ i release trướ c |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | stress load > 10k TPS | User login thành công trong <1s                   | JMeter script        | Theo chu ẩ n ISTQB                     |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | valid data            | Cluster failover t ự độ ng trong 5s               | Manual test plan     | Test môi trườ ng Pre- Prod             |
| Data consistency       | Th ự c hi ệ n Data consistency test để                                                                                                          | network               | H ệ th ố ng ch ị u t ả i                          | Manual test          | Ph ả i log toàn                        |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| test          | ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                                | disconnect         | 20k TPS không gián đoạ n                          | plan                | b ộ k ế t qu ả                         |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------|--------------------|---------------------------------------------------|---------------------|----------------------------------------|
| Failover test | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | network disconnect | Cluster failover t ự độ ng trong 5s               | JMeter script       | Theo chu ẩ n ISTQB                     |
| Failover test | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | valid data         | Cluster failover t ự độ ng trong 5s               | Automation Selenium | So sánh benchmark v ớ i release trướ c |
| Load test     | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.    | invalid data       | User login thành công trong <1s                   | Automation Selenium | Theo chu ẩ n ISTQB                     |
| Login test    | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | valid data         | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n | Automation Selenium | Theo chu ẩ n ISTQB                     |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| Load test             | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.            | network disconnect    | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố   | JMeter script        | G ử i báo cáo PDF hàng ngày    |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|-------------------------------------------------------|----------------------|--------------------------------|
| Login test            | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.           | valid data            | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10  | Automation Selenium  | Theo chu ẩ n ISTQB             |
| API stress test       | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.       | DB corruption         | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố   | Manual test plan     | Ph ả i log toàn b ộ k ế t qu ả |
| Data consistency test | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | stress load > 10k TPS | User login thành công trong <1s                       | Automation Selenium  | Test môi trườ ng Pre- Prod     |
| Security scan         | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t                | stress load > 10k TPS | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n     | K ị ch b ả n Ansible | Theo chu ẩ n ISTQB             |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                       | b ạ i.                                                                                                                                         |                             |                                                   |                      |                                        |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|---------------------------------------------------|----------------------|----------------------------------------|
| Data consistency test | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | DB corruption               | User login thành công trong <1s                   | K ị ch b ả n Ansible | Ph ả i log toàn b ộ k ế t qu ả         |
| Data consistency test | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | API call batch 1000 request | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n | Automation Selenium  | G ử i báo cáo PDF hàng ngày            |
| Failover test         | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.         | API call batch 1000 request | User login thành công trong <1s                   | K ị ch b ả n Ansible | So sánh benchmark v ớ i release trướ c |
| API stress test       | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.       | API call batch 1000 request | Cluster failover t ự độ ng trong 5s               | JMeter script        | Theo chu ẩ n ISTQB                     |
| Security              | Th ự c hi ệ n Security scan để ki ể mth ử                                                                                                      | valid data                  | D ữ li ệ u đượ c khôi                             | Manual test          | Test môi trườ ng Pre-                  |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| scan          | ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                                           |                             | ph ụ c toàn v ẹ n sau s ự c ố                        | plan                 | Prod                                   |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|------------------------------------------------------|----------------------|----------------------------------------|
| Failover test | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | network disconnect          | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | K ị ch b ả n Ansible | Ph ả i log toàn b ộ k ế t qu ả         |
| Load test     | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.    | DB corruption               | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố  | Manual test plan     | Test môi trườ ng Pre- Prod             |
| Failover test | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | API call batch 1000 request | Cluster failover t ự độ ng trong 5s                  | K ị ch b ả n Ansible | So sánh benchmark v ớ i release trướ c |
| Load test     | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.    | DB corruption               | User login thành công trong <1s                      | Automation Selenium  | So sánh benchmark v ớ i release trướ c |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| Failover test          | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.          | DB corruption      | User login thành công trong <1s                     | Manual test plan    | Test môi trườ ng Pre- Prod             |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------|---------------------|----------------------------------------|
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | network disconnect | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n   | JMeter script       | So sánh benchmark v ớ i release trướ c |
| Login test             | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.            | network disconnect | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | JMeter script       | Test môi trườ ng Pre- Prod             |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | valid data         | Cluster failover t ự độ ng trong 5s                 | Automation Selenium | Test môi trườ ng Pre- Prod             |
| Login test             | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành                                  | invalid data       | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau         | Manual test plan    | G ử i báo cáo PDF hàng ngày            |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                        | công và th ấ t b ạ i.                                                                                                                           |               | s ự c ố                                              |                      |                                        |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|---------------|------------------------------------------------------|----------------------|----------------------------------------|
| Security scan          | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.          | DB corruption | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | Automation Selenium  | Test môi trườ ng Pre- Prod             |
| Failover test          | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.          | invalid data  | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố  | Manual test plan     | Test môi trườ ng Pre- Prod             |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | valid data    | User login thành công trong <1s                      | K ị ch b ả n Ansible | Test môi trườ ng Pre- Prod             |
| API stress test        | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.        | invalid data  | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n    | Manual test plan     | So sánh benchmark v ớ i release trướ c |
| Database recovery      | Th ự c hi ệ n Database recovery test để                                                                                                         | valid data    | User login                                           | JMeter               | Theo chu ẩ n                           |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| test            | ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                                  |                             | thành công trong <1s                                | script               | ISTQB                                  |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-----------------------------------------------------|----------------------|----------------------------------------|
| Failover test   | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | API call batch 1000 request | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n   | Automation Selenium  | So sánh benchmark v ớ i release trướ c |
| Load test       | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.      | API call batch 1000 request | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | Automation Selenium  | So sánh benchmark v ớ i release trướ c |
| Load test       | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.      | API call batch 1000 request | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | JMeter script        | G ử i báo cáo PDF hàng ngày            |
| API stress test | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | network disconnect          | Cluster failover t ự độ ng trong 5s                 | K ị ch b ả n Ansible | Ph ả i log toàn b ộ k ế t qu ả         |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| Failover test   | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | DB corruption               | Cluster failover t ự độ ng trong 5s                 | Automation Selenium   | G ử i báo cáo PDF hàng ngày            |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-----------------------------------------------------|-----------------------|----------------------------------------|
| Security scan   | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | DB corruption               | User login thành công trong <1s                     | JMeter script         | G ử i báo cáo PDF hàng ngày            |
| Security scan   | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | API call batch 1000 request | User login thành công trong <1s                     | Automation Selenium   | So sánh benchmark v ớ i release trướ c |
| API stress test | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | invalid data                | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | Manual test plan      | So sánh benchmark v ớ i release trướ c |
| Failover test   | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng,                                                     | valid data                  | User login thành công                               | Automation Selenium   | Theo chu ẩ n ISTQB                     |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                       | bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                                                                                              |                       | trong <1s                                           |                      |                             |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|-----------------------------------------------------|----------------------|-----------------------------|
| API stress test       | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.       | invalid data          | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | Manual test plan     | G ử i báo cáo PDF hàng ngày |
| Data consistency test | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | network disconnect    | Cluster failover t ự độ ng trong 5s                 | K ị ch b ả n Ansible | G ử i báo cáo PDF hàng ngày |
| API stress test       | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.       | stress load > 10k TPS | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | JMeter script        | Test môi trườ ng Pre- Prod  |
| Login test            | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.           | stress load > 10k TPS | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n   | Manual test plan     | Test môi trườ ng Pre- Prod  |
| Data                  | Th ự c hi ệ n Data                                                                                                                             | DB                    | User                                                | K ị ch b ả n         | Test môi                    |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| consistency test       | consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                     | corruption                  | login thành công trong <1s                          | Ansible              | trườ ng Pre- Prod              |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-----------------------------------------------------|----------------------|--------------------------------|
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | API call batch 1000 request | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | Manual test plan     | G ử i báo cáo PDF hàng ngày    |
| API stress test        | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.        | valid data                  | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | Automation Selenium  | Theo chu ẩ n ISTQB             |
| Data consistency test  | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.  | network disconnect          | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | Automation Selenium  | G ử i báo cáo PDF hàng ngày    |
| Login test             | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành                                  | network disconnect          | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP       | K ị ch b ả n Ansible | Ph ả i log toàn b ộ k ế t qu ả |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|               | công và th ấ t b ạ i.                                                                                                                  |                             | Top 10                                              |                      |                                        |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-----------------------------------------------------|----------------------|----------------------------------------|
| Load test     | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.    | DB corruption               | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | JMeter script        | Ph ả i log toàn b ộ k ế t qu ả         |
| Load test     | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.    | valid data                  | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | K ị ch b ả n Ansible | Ph ả i log toàn b ộ k ế t qu ả         |
| Load test     | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.    | stress load > 10k TPS       | User login thành công trong <1s                     | Manual test plan     | So sánh benchmark v ớ i release trướ c |
| Security scan | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | API call batch 1000 request | Cluster failover t ự độ ng trong 5s                 | K ị ch b ả n Ansible | Test môi trườ ng Pre- Prod             |
| Load test     | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành                          | valid data                  | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP       | Manual test plan     | Test môi trườ ng Pre- Prod             |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                 | công và th ấ t b ạ i.                                                                                                                    |                       | Top 10                              |                      |                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|-------------------------------------|----------------------|--------------------------------|
| Failover test   | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | valid data            | User login thành công trong <1s     | K ị ch b ả n Ansible | Ph ả i log toàn b ộ k ế t qu ả |
| API stress test | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | network disconnect    | Cluster failover t ự độ ng trong 5s | K ị ch b ả n Ansible | G ử i báo cáo PDF hàng ngày    |
| Login test      | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.     | invalid data          | Cluster failover t ự độ ng trong 5s | Automation Selenium  | Ph ả i log toàn b ộ k ế t qu ả |
| Load test       | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.      | valid data            | User login thành công trong <1s     | JMeter script        | Ph ả i log toàn b ộ k ế t qu ả |
| Load test       | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao                                                    | stress load > 10k TPS | User login thành công               | JMeter script        | G ử i báo cáo PDF hàng ngày    |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                        | g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                                                                                                   |                   | trong <1s                                            |                      |                                |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|------------------------------------------------------|----------------------|--------------------------------|
| Login test             | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.            | valid data        | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n    | JMeter script        | Theo chu ẩ n ISTQB             |
| Data consistency test  | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.  | DB corruption     | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | JMeter script        | G ử i báo cáo PDF hàng ngày    |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | DB corruption     | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n    | JMeter script        | Theo chu ẩ n ISTQB             |
| Load test              | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.             | valid data        | Cluster failover t ự độ ng trong 5s                  | K ị ch b ả n Ansible | Ph ả i log toàn b ộ k ế t qu ả |
| Load test              | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng                                                                                  | stress load > 10k | Không phát hi ệ n l ỗ h ổ ng                         | JMeter script        | So sánh benchmark v ớ i        |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                       | c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                                                                           | TPS                         | b ả om ậ t OWASP Top 10                             |                      | release trướ c                         |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-----------------------------------------------------|----------------------|----------------------------------------|
| Security scan         | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.         | API call batch 1000 request | User login thành công trong <1s                     | JMeter script        | Test môi trườ ng Pre- Prod             |
| Data consistency test | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | API call batch 1000 request | User login thành công trong <1s                     | K ị ch b ả n Ansible | G ử i báo cáo PDF hàng ngày            |
| Load test             | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.            | valid data                  | User login thành công trong <1s                     | Manual test plan     | So sánh benchmark v ớ i release trướ c |
| Security scan         | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.         | stress load > 10k TPS       | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | Automation Selenium  | So sánh benchmark v ớ i release trướ c |
| Data                  | Th ự c hi ệ n Data                                                                                                                             | invalid                     | User                                                | Automation           | So sánh                                |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| consistency test      | consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                    | data                  | login thành công trong <1s                          | Selenium            | benchmark v ớ i release trướ c         |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|-----------------------------------------------------|---------------------|----------------------------------------|
| Data consistency test | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | valid data            | User login thành công trong <1s                     | Manual test plan    | Ph ả i log toàn b ộ k ế t qu ả         |
| Data consistency test | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | invalid data          | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n   | Automation Selenium | Ph ả i log toàn b ộ k ế t qu ả         |
| Failover test         | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.         | DB corruption         | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | JMeter script       | G ử i báo cáo PDF hàng ngày            |
| Login test            | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành                                 | stress load > 10k TPS | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP       | Manual test plan    | So sánh benchmark v ớ i release trướ c |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                       | công và th ấ t b ạ i.                                                                                                                          |                             | Top 10                                              |                      |                                        |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-----------------------------------------------------|----------------------|----------------------------------------|
| Security scan         | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.         | stress load > 10k TPS       | Cluster failover t ự độ ng trong 5s                 | Manual test plan     | So sánh benchmark v ớ i release trướ c |
| Data consistency test | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | API call batch 1000 request | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | JMeter script        | Ph ả i log toàn b ộ k ế t qu ả         |
| Security scan         | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.         | DB corruption               | Cluster failover t ự độ ng trong 5s                 | Manual test plan     | G ử i báo cáo PDF hàng ngày            |
| Failover test         | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.         | valid data                  | User login thành công trong <1s                     | K ị ch b ả n Ansible | G ử i báo cáo PDF hàng ngày            |
| Database recovery     | Th ự c hi ệ n Database recovery test để                                                                                                        | network                     | Cluster failover                                    | Manual test          | So sánh benchmark v ớ i                |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| test            | ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                                | disconnect                  | t ự độ ng trong 5s                                   | plan                 | release trướ c                         |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|------------------------------------------------------|----------------------|----------------------------------------|
| Security scan   | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | API call batch 1000 request | Cluster failover t ự độ ng trong 5s                  | JMeter script        | Theo chu ẩ n ISTQB                     |
| Failover test   | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | network disconnect          | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | Automation Selenium  | Ph ả i log toàn b ộ k ế t qu ả         |
| Load test       | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.    | valid data                  | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | K ị ch b ả n Ansible | G ử i báo cáo PDF hàng ngày            |
| API stress test | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t      | API call batch 1000 request | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố  | Automation Selenium  | So sánh benchmark v ớ i release trướ c |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                        | b ạ i.                                                                                                                                          |                             |                                                     |                      |                                |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-----------------------------------------------------|----------------------|--------------------------------|
| API stress test        | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.        | API call batch 1000 request | User login thành công trong <1s                     | JMeter script        | Ph ả i log toàn b ộ k ế t qu ả |
| Failover test          | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.          | invalid data                | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | Automation Selenium  | Ph ả i log toàn b ộ k ế t qu ả |
| Load test              | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.             | stress load > 10k TPS       | User login thành công trong <1s                     | JMeter script        | Test môi trườ ng Pre- Prod     |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | API call batch 1000 request | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n   | K ị ch b ả n Ansible | Theo chu ẩ n ISTQB             |
| Load test              | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng                                                                                  | invalid data                | D ữ li ệ u đượ c khôi ph ụ c toàn                   | JMeter script        | Test môi trườ ng Pre-          |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                  | c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                                                                     |                             | v ẹ n sau s ự c ố                                   |                      | Prod                                   |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-----------------------------------------------------|----------------------|----------------------------------------|
| Load test        | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.      | stress load > 10k TPS       | Cluster failover t ự độ ng trong 5s                 | Manual test plan     | G ử i báo cáo PDF hàng ngày            |
| Login test       | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.     | invalid data                | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | K ị ch b ả n Ansible | Theo chu ẩ n ISTQB                     |
| API stress test  | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | API call batch 1000 request | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | Automation Selenium  | G ử i báo cáo PDF hàng ngày            |
| API stress test  | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | stress load > 10k TPS       | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n   | JMeter script        | So sánh benchmark v ớ i release trướ c |
| Data consistency | Th ự c hi ệ n Data consistency test để                                                                                                   | API call batch              | Không phát hi ệ n                                   | K ị ch b ả n         | Theo chu ẩ n                           |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| test                   | ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                                         | 1000 request          | l ỗ h ổ ng b ả om ậ t OWASP Top 10                   | Ansible             | ISTQB                                  |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|------------------------------------------------------|---------------------|----------------------------------------|
| Login test             | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.            | valid data            | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố  | JMeter script       | Theo chu ẩ n ISTQB                     |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | stress load > 10k TPS | User login thành công trong <1s                      | Manual test plan    | So sánh benchmark v ớ i release trướ c |
| Load test              | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.             | stress load > 10k TPS | User login thành công trong <1s                      | Automation Selenium | Theo chu ẩ n ISTQB                     |
| Security scan          | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.          | stress load > 10k TPS | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | Manual test plan    | Theo chu ẩ n ISTQB                     |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| Data consistency test   | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | stress load > 10k TPS   | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n    | K ị ch b ả n Ansible   | Ph ả i log toàn b ộ k ế t qu ả   |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|------------------------------------------------------|------------------------|----------------------------------|
| Login test              | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.             | stress load > 10k TPS   | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố  | Manual test plan       | Ph ả i log toàn b ộ k ế t qu ả   |
| Data consistency test   | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | invalid data            | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | Manual test plan       | Test môi trườ ng Pre- Prod       |
| API stress test         | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.         | network disconnect      | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố  | Manual test plan       | G ử i báo cáo PDF hàng ngày      |
| Database recovery test  | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch                                    | invalid data            | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau          | JMeter script          | Theo chu ẩ n ISTQB               |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                        | b ả n thành công và th ấ t b ạ i.                                                                                                               |                             | s ự c ố                                             |                  |                                |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-----------------------------------------------------|------------------|--------------------------------|
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | API call batch 1000 request | User login thành công trong <1s                     | Manual test plan | Test môi trườ ng Pre- Prod     |
| Login test             | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.            | API call batch 1000 request | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n   | JMeter script    | G ử i báo cáo PDF hàng ngày    |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | invalid data                | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | Manual test plan | Ph ả i log toàn b ộ k ế t qu ả |
| Security scan          | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.          | network disconnect          | User login thành công trong <1s                     | JMeter script    | Ph ả i log toàn b ộ k ế t qu ả |
| Failover               | Th ự c hi ệ n Failover test để ki ể mth ử                                                                                                       | DB                          | Không phát hi ệ n                                   | Automation       | Theo chu ẩ n                   |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| test            | ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                                           | corruption                  | l ỗ h ổ ng b ả om ậ t OWASP Top 10                   | Selenium            | ISTQB                                  |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|------------------------------------------------------|---------------------|----------------------------------------|
| Load test       | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.    | stress load > 10k TPS       | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | Automation Selenium | Theo chu ẩ n ISTQB                     |
| Failover test   | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | valid data                  | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | JMeter script       | So sánh benchmark v ớ i release trướ c |
| Security scan   | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | API call batch 1000 request | Cluster failover t ự độ ng trong 5s                  | Manual test plan    | Test môi trườ ng Pre- Prod             |
| API stress test | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t      | network disconnect          | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | Manual test plan    | So sánh benchmark v ớ i release trướ c |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                   | b ạ i.                                                                                                                                   |                             |                                                      |                      |                                |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|------------------------------------------------------|----------------------|--------------------------------|
| API stress test   | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | API call batch 1000 request | User login thành công trong <1s                      | JMeter script        | G ử i báo cáo PDF hàng ngày    |
| Failover test     | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | API call batch 1000 request | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố  | JMeter script        | Ph ả i log toàn b ộ k ế t qu ả |
| Failover test     | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | API call batch 1000 request | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố  | K ị ch b ả n Ansible | Theo chu ẩ n ISTQB             |
| Login test        | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.     | valid data                  | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | Manual test plan     | Test môi trườ ng Pre- Prod     |
| Database recovery | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng                                                                            | network disconnect          | D ữ li ệ u đượ c khôi ph ụ c toàn                    | K ị ch b ả n Ansible | Test môi trườ ng Pre-          |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| test                   | và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                                                               |                    | v ẹ n sau s ự c ố                                   |                      | Prod                                   |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------|----------------------|----------------------------------------|
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | network disconnect | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n   | K ị ch b ả n Ansible | G ử i báo cáo PDF hàng ngày            |
| Security scan          | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.          | invalid data       | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n   | JMeter script        | So sánh benchmark v ớ i release trướ c |
| Load test              | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.             | network disconnect | Cluster failover t ự độ ng trong 5s                 | K ị ch b ả n Ansible | Ph ả i log toàn b ộ k ế t qu ả         |
| Security scan          | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.          | valid data         | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | JMeter script        | Test môi trườ ng Pre- Prod             |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| Load test              | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.             | valid data            | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n    | Automation Selenium   | G ử i báo cáo PDF hàng ngày            |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|------------------------------------------------------|-----------------------|----------------------------------------|
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | stress load > 10k TPS | User login thành công trong <1s                      | Automation Selenium   | So sánh benchmark v ớ i release trướ c |
| API stress test        | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.        | valid data            | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố  | JMeter script         | So sánh benchmark v ớ i release trướ c |
| Failover test          | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.          | stress load > 10k TPS | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | Manual test plan      | Test môi trườ ng Pre- Prod             |
| Load test              | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành                                   | stress load > 10k TPS | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP        | K ị ch b ả n Ansible  | Ph ả i log toàn b ộ k ế t qu ả         |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                        | công và th ấ t b ạ i.                                                                                                                           |                             | Top 10                                              |                  |                                        |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-----------------------------------------------------|------------------|----------------------------------------|
| Data consistency test  | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.  | invalid data                | User login thành công trong <1s                     | JMeter script    | Ph ả i log toàn b ộ k ế t qu ả         |
| Load test              | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.             | network disconnect          | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | JMeter script    | Theo chu ẩ n ISTQB                     |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | network disconnect          | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | JMeter script    | So sánh benchmark v ớ i release trướ c |
| Security scan          | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.          | API call batch 1000 request | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | Manual test plan | Ph ả i log toàn b ộ k ế t qu ả         |
| Failover test          | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u                                                                                   | network disconnect          | Cluster failover t ự độ ng                          | Manual test plan | So sánh benchmark v ớ i                |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                        | năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                                                                       |                             | trong 5s                                             |                      | release trướ c                         |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|------------------------------------------------------|----------------------|----------------------------------------|
| Data consistency test  | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | network disconnect          | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n    | Automation Selenium  | So sánh benchmark v ớ i release trướ c |
| Failover test          | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.         | network disconnect          | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố  | K ị ch b ả n Ansible | G ử i báo cáo PDF hàng ngày            |
| Data consistency test  | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | invalid data                | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | K ị ch b ả n Ansible | So sánh benchmark v ớ i release trướ c |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và              | API call batch 1000 request | User login thành công trong <1s                      | Automation Selenium  | Test môi trườ ng Pre- Prod             |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                        | th ấ t b ạ i.                                                                                                                                   |                             |                                                      |                     |                                        |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|------------------------------------------------------|---------------------|----------------------------------------|
| Security scan          | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.          | valid data                  | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố  | Automation Selenium | Theo chu ẩ n ISTQB                     |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | API call batch 1000 request | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n    | JMeter script       | G ử i báo cáo PDF hàng ngày            |
| Failover test          | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.          | network disconnect          | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | Automation Selenium | Test môi trườ ng Pre- Prod             |
| Data consistency test  | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.  | network disconnect          | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố  | Manual test plan    | So sánh benchmark v ớ i release trướ c |
| Security               | Th ự c hi ệ n Security scan để ki ể mth ử                                                                                                       | invalid                     | H ệ th ố ng ch ị u t ả i                             | K ị ch b ả n        | Test môi trườ ng Pre-                  |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| scan                   | ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                                             | data                  | 20k TPS không gián đoạ n                             | Ansible              | Prod                                   |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|------------------------------------------------------|----------------------|----------------------------------------|
| Security scan          | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | DB corruption         | User login thành công trong <1s                      | K ị ch b ả n Ansible | Test môi trườ ng Pre- Prod             |
| Login test             | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.     | stress load > 10k TPS | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n    | JMeter script        | Test môi trườ ng Pre- Prod             |
| API stress test        | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | stress load > 10k TPS | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | JMeter script        | So sánh benchmark v ớ i release trướ c |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và        | network disconnect    | Cluster failover t ự độ ng trong 5s                  | K ị ch b ả n Ansible | Ph ả i log toàn b ộ k ế t qu ả         |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                        | th ấ t b ạ i.                                                                                                                          |                             |                                                      |                      |                                        |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|------------------------------------------------------|----------------------|----------------------------------------|
| Failover test          | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | API call batch 1000 request | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | JMeter script        | So sánh benchmark v ớ i release trướ c |
| Login test             | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | DB corruption               | Cluster failover t ự độ ng trong 5s                  | Manual test plan     | Test môi trườ ng Pre- Prod             |
| Security scan          | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | stress load > 10k TPS       | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n    | K ị ch b ả n Ansible | Test môi trườ ng Pre- Prod             |
| Login test             | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | stress load > 10k TPS       | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố  | Automation Selenium  | So sánh benchmark v ớ i release trướ c |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ                                                   | valid data                  | User login thành công                                | Manual test plan     | Ph ả i log toàn b ộ k ế t qu ả         |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                 | th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                                                                               |                             | trong <1s                                           |                      |                                        |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-----------------------------------------------------|----------------------|----------------------------------------|
| API stress test | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | invalid data                | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n   | JMeter script        | So sánh benchmark v ớ i release trướ c |
| Security scan   | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | network disconnect          | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | Automation Selenium  | G ử i báo cáo PDF hàng ngày            |
| Failover test   | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | invalid data                | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n   | K ị ch b ả n Ansible | Theo chu ẩ n ISTQB                     |
| Login test      | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.     | API call batch 1000 request | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | Manual test plan     | Theo chu ẩ n ISTQB                     |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| Login test             | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.            | DB corruption         | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố   | Manual test plan    | So sánh benchmark v ớ i release trướ c   |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|-------------------------------------------------------|---------------------|------------------------------------------|
| Login test             | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.            | DB corruption         | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố   | JMeter script       | Ph ả i log toàn b ộ k ế t qu ả           |
| Security scan          | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.          | network disconnect    | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10  | Automation Selenium | G ử i báo cáo PDF hàng ngày              |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | stress load > 10k TPS | Cluster failover t ự độ ng trong 5s                   | Automation Selenium | G ử i báo cáo PDF hàng ngày              |
| Login test             | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành                                  | invalid data          | User login thành công trong <1s                       | Automation Selenium | Ph ả i log toàn b ộ k ế t qu ả           |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                       | công và th ấ t b ạ i.                                                                                                                          |                       |                                                      |                      |                                        |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|------------------------------------------------------|----------------------|----------------------------------------|
| Data consistency test | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | network disconnect    | User login thành công trong <1s                      | Manual test plan     | Ph ả i log toàn b ộ k ế t qu ả         |
| Data consistency test | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | valid data            | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n    | K ị ch b ả n Ansible | Test môi trườ ng Pre- Prod             |
| Load test             | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.            | stress load > 10k TPS | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố  | JMeter script        | So sánh benchmark v ớ i release trướ c |
| Failover test         | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.         | DB corruption         | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | K ị ch b ả n Ansible | Test môi trườ ng Pre- Prod             |
| Load test             | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng                                                                                 | stress load > 10k     | User login thành                                     | JMeter script        | So sánh benchmark v ớ i                |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                 | c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                                                                     | TPS                | công trong <1s                                       |                      | release trướ c                 |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------|--------------------|------------------------------------------------------|----------------------|--------------------------------|
| Security scan   | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | network disconnect | Cluster failover t ự độ ng trong 5s                  | Manual test plan     | Ph ả i log toàn b ộ k ế t qu ả |
| Login test      | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.     | DB corruption      | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | JMeter script        | G ử i báo cáo PDF hàng ngày    |
| Failover test   | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | invalid data       | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | K ị ch b ả n Ansible | Theo chu ẩ n ISTQB             |
| API stress test | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | network disconnect | User login thành công trong <1s                      | K ị ch b ả n Ansible | Test môi trườ ng Pre- Prod     |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| Load test              | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.             | stress load > 10k TPS       | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n    | JMeter script        | Theo chu ẩ n ISTQB             |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|------------------------------------------------------|----------------------|--------------------------------|
| Load test              | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.             | API call batch 1000 request | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | Manual test plan     | G ử i báo cáo PDF hàng ngày    |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | stress load > 10k TPS       | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố  | K ị ch b ả n Ansible | G ử i báo cáo PDF hàng ngày    |
| Data consistency test  | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.  | valid data                  | Cluster failover t ự độ ng trong 5s                  | K ị ch b ả n Ansible | Ph ả i log toàn b ộ k ế t qu ả |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và               | invalid data                | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố  | Automation Selenium  | Test môi trườ ng Pre- Prod     |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                        | th ấ t b ạ i.                                                                                                                                   |                             |                                                      |                      |                                |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|------------------------------------------------------|----------------------|--------------------------------|
| API stress test        | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.        | valid data                  | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | Manual test plan     | Test môi trườ ng Pre- Prod     |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | valid data                  | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n    | K ị ch b ả n Ansible | G ử i báo cáo PDF hàng ngày    |
| Data consistency test  | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.  | API call batch 1000 request | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n    | K ị ch b ả n Ansible | G ử i báo cáo PDF hàng ngày    |
| Login test             | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.            | valid data                  | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố  | Manual test plan     | Ph ả i log toàn b ộ k ế t qu ả |
| Security scan          | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u                                                                                   | API call batch 1000         | User login thành                                     | K ị ch b ả n Ansible | Ph ả i log toàn b ộ k ế t qu ả |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                       | năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                                                                       | request                     | công trong <1s                                      |                     |                                        |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-----------------------------------------------------|---------------------|----------------------------------------|
| Failover test         | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.         | DB corruption               | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | Automation Selenium | Ph ả i log toàn b ộ k ế t qu ả         |
| API stress test       | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.       | valid data                  | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | Automation Selenium | Test môi trườ ng Pre- Prod             |
| Load test             | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.            | API call batch 1000 request | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | Automation Selenium | Test môi trườ ng Pre- Prod             |
| Data consistency test | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | API call batch 1000 request | Cluster failover t ự độ ng trong 5s                 | Automation Selenium | So sánh benchmark v ớ i release trướ c |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| Load test              | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.             | network disconnect    | Cluster failover t ự độ ng trong 5s                  | Manual test plan     | G ử i báo cáo PDF hàng ngày            |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|------------------------------------------------------|----------------------|----------------------------------------|
| API stress test        | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.        | stress load > 10k TPS | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n    | K ị ch b ả n Ansible | G ử i báo cáo PDF hàng ngày            |
| Login test             | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.            | stress load > 10k TPS | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | Automation Selenium  | So sánh benchmark v ớ i release trướ c |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | valid data            | User login thành công trong <1s                      | Automation Selenium  | Test môi trườ ng Pre- Prod             |
| API stress test        | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t               | invalid data          | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n    | K ị ch b ả n Ansible | Ph ả i log toàn b ộ k ế t qu ả         |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                        | b ạ i.                                                                                                                                          |                       |                                                     |                      |                                        |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|-----------------------------------------------------|----------------------|----------------------------------------|
| Data consistency test  | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.  | valid data            | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | K ị ch b ả n Ansible | Test môi trườ ng Pre- Prod             |
| API stress test        | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.        | DB corruption         | Cluster failover t ự độ ng trong 5s                 | Manual test plan     | So sánh benchmark v ớ i release trướ c |
| Data consistency test  | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.  | DB corruption         | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | Manual test plan     | Theo chu ẩ n ISTQB                     |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | stress load > 10k TPS | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n   | Automation Selenium  | Ph ả i log toàn b ộ k ế t qu ả         |
| Load test              | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c                                                                                                    | stress load > 10k     | H ệ th ố ng ch ị u t ả i                            | Automation           | Ph ả i log toàn                        |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                        | năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                                                          | TPS                | 20k TPS không gián đoạ n                             | Selenium             | b ộ k ế t qu ả                 |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|------------------------------------------------------|----------------------|--------------------------------|
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | network disconnect | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố  | K ị ch b ả n Ansible | G ử i báo cáo PDF hàng ngày    |
| Load test              | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.             | DB corruption      | Cluster failover t ự độ ng trong 5s                  | JMeter script        | Ph ả i log toàn b ộ k ế t qu ả |
| Failover test          | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.          | DB corruption      | Cluster failover t ự độ ng trong 5s                  | K ị ch b ả n Ansible | G ử i báo cáo PDF hàng ngày    |
| Login test             | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.            | valid data         | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | JMeter script        | Ph ả i log toàn b ộ k ế t qu ả |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| Login test             | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.            | stress load > 10k TPS   | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n   | JMeter script        | Ph ả i log toàn b ộ k ế t qu ả   |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------|----------------------|----------------------------------|
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | stress load > 10k TPS   | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | K ị ch b ả n Ansible | Test môi trườ ng Pre- Prod       |
| Login test             | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.            | valid data              | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n   | Automation Selenium  | Ph ả i log toàn b ộ k ế t qu ả   |
| Load test              | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.             | valid data              | User login thành công trong <1s                     | Manual test plan     | Theo chu ẩ n ISTQB               |
| Data consistency test  | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và                | invalid data            | Cluster failover t ự độ ng trong 5s                 | JMeter script        | Theo chu ẩ n ISTQB               |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                        | th ấ t b ạ i.                                                                                                                                   |                             |                                                      |                      |                                |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|------------------------------------------------------|----------------------|--------------------------------|
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | stress load > 10k TPS       | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố  | JMeter script        | Theo chu ẩ n ISTQB             |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | API call batch 1000 request | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | K ị ch b ả n Ansible | Ph ả i log toàn b ộ k ế t qu ả |
| API stress test        | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.        | invalid data                | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố  | K ị ch b ả n Ansible | Ph ả i log toàn b ộ k ế t qu ả |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | valid data                  | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n    | Manual test plan     | Ph ả i log toàn b ộ k ế t qu ả |
| Load test              | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c                                                                                                    | invalid                     | H ệ th ố ng ch ị u t ả i                             | K ị ch b ả n         | Ph ả i log toàn                |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                        | năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                                                          | data                        | 20k TPS không gián đoạ n                            | Ansible              | b ộ k ế t qu ả                         |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-----------------------------------------------------|----------------------|----------------------------------------|
| API stress test        | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.        | DB corruption               | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n   | K ị ch b ả n Ansible | Ph ả i log toàn b ộ k ế t qu ả         |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | DB corruption               | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | Manual test plan     | G ử i báo cáo PDF hàng ngày            |
| Login test             | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.            | network disconnect          | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n   | JMeter script        | Theo chu ẩ n ISTQB                     |
| Load test              | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.             | API call batch 1000 request | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | K ị ch b ả n Ansible | So sánh benchmark v ớ i release trướ c |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| Login test      | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.     | network disconnect    | User login thành công trong <1s                   | JMeter script        | G ử i báo cáo PDF hàng ngày            |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|---------------------------------------------------|----------------------|----------------------------------------|
| API stress test | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | valid data            | Cluster failover t ự độ ng trong 5s               | Automation Selenium  | Ph ả i log toàn b ộ k ế t qu ả         |
| Failover test   | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | DB corruption         | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n | Manual test plan     | Test môi trườ ng Pre- Prod             |
| Failover test   | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | stress load > 10k TPS | User login thành công trong <1s                   | Automation Selenium  | Ph ả i log toàn b ộ k ế t qu ả         |
| Security scan   | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n                               | invalid data          | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP     | K ị ch b ả n Ansible | So sánh benchmark v ớ i release trướ c |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                       | thành công và th ấ t b ạ i.                                                                                                                    |                             | Top 10                                              |                      |                                        |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-----------------------------------------------------|----------------------|----------------------------------------|
| Data consistency test | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | API call batch 1000 request | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n   | JMeter script        | So sánh benchmark v ớ i release trướ c |
| Data consistency test | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | network disconnect          | User login thành công trong <1s                     | K ị ch b ả n Ansible | So sánh benchmark v ớ i release trướ c |
| Failover test         | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.         | invalid data                | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | JMeter script        | G ử i báo cáo PDF hàng ngày            |
| Load test             | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.            | valid data                  | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n   | Manual test plan     | So sánh benchmark v ớ i release trướ c |
| Login test            | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c                                                                                                  | API call batch              | Cluster failover                                    | K ị ch b ả n         | So sánh benchmark v ớ i                |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                        | năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                                                          | 1000 request                | t ự độ ng trong 5s                                  | Ansible              | release trướ c                         |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-----------------------------------------------------|----------------------|----------------------------------------|
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | network disconnect          | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n   | K ị ch b ả n Ansible | So sánh benchmark v ớ i release trướ c |
| Failover test          | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.          | valid data                  | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | Manual test plan     | G ử i báo cáo PDF hàng ngày            |
| Security scan          | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.          | API call batch 1000 request | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n   | JMeter script        | Ph ả i log toàn b ộ k ế t qu ả         |
| Data consistency test  | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và                | network disconnect          | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n   | K ị ch b ả n Ansible | Test môi trườ ng Pre- Prod             |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                        | th ấ t b ạ i.                                                                                                                                   |                             |                                                      |                      |                                        |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|------------------------------------------------------|----------------------|----------------------------------------|
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | stress load > 10k TPS       | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố  | Manual test plan     | G ử i báo cáo PDF hàng ngày            |
| Data consistency test  | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.  | valid data                  | User login thành công trong <1s                      | Automation Selenium  | So sánh benchmark v ớ i release trướ c |
| Login test             | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.            | invalid data                | User login thành công trong <1s                      | K ị ch b ả n Ansible | So sánh benchmark v ớ i release trướ c |
| Security scan          | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.          | API call batch 1000 request | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | K ị ch b ả n Ansible | Theo chu ẩ n ISTQB                     |
| Failover test          | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u                                                                                   | valid data                  | Không phát hi ệ n l ỗ h ổ ng                         | Manual test plan     | So sánh benchmark v ớ i                |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                        | năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                                                                        |                       | b ả om ậ t OWASP Top 10                             |                     | release trướ c                         |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|-----------------------------------------------------|---------------------|----------------------------------------|
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | invalid data          | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | Manual test plan    | So sánh benchmark v ớ i release trướ c |
| Failover test          | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.          | stress load > 10k TPS | User login thành công trong <1s                     | Automation Selenium | So sánh benchmark v ớ i release trướ c |
| API stress test        | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.        | stress load > 10k TPS | User login thành công trong <1s                     | JMeter script       | Test môi trườ ng Pre- Prod             |
| Data consistency test  | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và                | network disconnect    | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n   | JMeter script       | So sánh benchmark v ớ i release trướ c |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                 | th ấ t b ạ i.                                                                                                                            |                             |                                                     |                      |                                        |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-----------------------------------------------------|----------------------|----------------------------------------|
| Security scan   | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | API call batch 1000 request | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | JMeter script        | G ử i báo cáo PDF hàng ngày            |
| Failover test   | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | invalid data                | User login thành công trong <1s                     | K ị ch b ả n Ansible | So sánh benchmark v ớ i release trướ c |
| API stress test | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | valid data                  | Cluster failover t ự độ ng trong 5s                 | Manual test plan     | Test môi trườ ng Pre- Prod             |
| Failover test   | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | invalid data                | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n   | K ị ch b ả n Ansible | Ph ả i log toàn b ộ k ế t qu ả         |
| Security        | Th ự c hi ệ n Security scan để ki ể mth ử                                                                                                | API call batch              | H ệ th ố ng ch ị u t ả i                            | Manual test          | So sánh benchmark v ớ i                |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| scan            | ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                                             | 1000 request   | 20k TPS không gián đoạ n                            | plan                 | release trướ c                         |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------|----------------|-----------------------------------------------------|----------------------|----------------------------------------|
| Load test       | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.      | valid data     | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n   | Manual test plan     | Theo chu ẩ n ISTQB                     |
| Load test       | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.      | valid data     | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | Automation Selenium  | So sánh benchmark v ớ i release trướ c |
| API stress test | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | DB corruption  | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố | JMeter script        | So sánh benchmark v ớ i release trướ c |
| Load test       | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.      | valid data     | User login thành công trong <1s                     | K ị ch b ả n Ansible | Ph ả i log toàn b ộ k ế t qu ả         |
| API stress      | Th ự c hi ệ n API stress                                                                                                                 | invalid        | Không                                               | K ị ch b ả n         | G ử i báo cáo                          |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| test                   | test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                                 | data                        | phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10       | Ansible              | PDF hàng ngày                          |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|------------------------------------------------------|----------------------|----------------------------------------|
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | API call batch 1000 request | Cluster failover t ự độ ng trong 5s                  | Manual test plan     | Test môi trườ ng Pre- Prod             |
| Load test              | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.             | network disconnect          | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | Automation Selenium  | So sánh benchmark v ớ i release trướ c |
| Security scan          | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.          | network disconnect          | User login thành công trong <1s                      | K ị ch b ả n Ansible | Test môi trườ ng Pre- Prod             |
| Data consistency test  | Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và                | valid data                  | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố  | Manual test plan     | Test môi trườ ng Pre- Prod             |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|               | th ấ t b ạ i.                                                                                                                        |               |                                                      |                      |                                        |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------|---------------|------------------------------------------------------|----------------------|----------------------------------------|
| Login test    | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | invalid data  | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | JMeter script        | So sánh benchmark v ớ i release trướ c |
| Load test     | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.  | DB corruption | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | K ị ch b ả n Ansible | Ph ả i log toàn b ộ k ế t qu ả         |
| Login test    | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | DB corruption | Cluster failover t ự độ ng trong 5s                  | JMeter script        | Test môi trườ ng Pre- Prod             |
| Load test     | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.  | valid data    | Cluster failover t ự độ ng trong 5s                  | Automation Selenium  | G ử i báo cáo PDF hàng ngày            |
| Security scan | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t      | invalid data  | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP        | JMeter script        | Ph ả i log toàn b ộ k ế t qu ả         |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

|                        | b ạ i.                                                                                                                                          |                       | Top 10                                            |                      |                                        |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|---------------------------------------------------|----------------------|----------------------------------------|
| Security scan          | Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.          | valid data            | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n | K ị ch b ả n Ansible | So sánh benchmark v ớ i release trướ c |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | valid data            | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n | Manual test plan     | Test môi trườ ng Pre- Prod             |
| Load test              | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.             | DB corruption         | User login thành công trong <1s                   | Manual test plan     | Test môi trườ ng Pre- Prod             |
| API stress test        | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.        | stress load > 10k TPS | Cluster failover t ự độ ng trong 5s               | Automation Selenium  | G ử i báo cáo PDF hàng ngày            |
| Database recovery      | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng                                                                                   | valid data            | Cluster failover t ự độ ng                        | K ị ch b ả n Ansible | G ử i báo cáo PDF hàng ngày            |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| test                   | và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.                                                               |                             | trong 5s                                             |                      |                                |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|------------------------------------------------------|----------------------|--------------------------------|
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | API call batch 1000 request | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố  | K ị ch b ả n Ansible | Test môi trườ ng Pre- Prod     |
| Database recovery test | Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | stress load > 10k TPS       | User login thành công trong <1s                      | K ị ch b ả n Ansible | Ph ả i log toàn b ộ k ế t qu ả |
| Load test              | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.             | valid data                  | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | Manual test plan     | Theo chu ẩ n ISTQB             |
| API stress test        | Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.        | stress load > 10k TPS       | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | Manual test plan     | G ử i báo cáo PDF hàng ngày    |

<!-- image -->

## VIETTEL AI RACE

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

| Load test     | Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.    | invalid data       | User login thành công trong <1s                      | K ị ch b ả n Ansible   | Theo chu ẩ n ISTQB             |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------|--------------------|------------------------------------------------------|------------------------|--------------------------------|
| Login test    | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | valid data         | H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n    | K ị ch b ả n Ansible   | Theo chu ẩ n ISTQB             |
| Login test    | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | valid data         | Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10 | K ị ch b ả n Ansible   | Theo chu ẩ n ISTQB             |
| Failover test | Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i. | network disconnect | D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố  | JMeter script          | Ph ả i log toàn b ộ k ế t qu ả |
| Login test    | Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.   | network disconnect | User login thành công trong <1s                      | Automation Selenium    | Theo chu ẩ n ISTQB             |

<!-- image -->

| VIETTEL AI RACE   | TD447   |
|-------------------|---------|