<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Test case</th>
      <th>Mô t ả</th>
      <th>Input</th>
      <th>Expected Output</th>
      <th>Phương pháp</th>
      <th>Ghi chú</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>User login thành công trong <1s</td>
      <td>JMeter script</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>Manual test plan</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Security scan</th>
      <th>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>API call batch 1000 request</th>
      <th>User login thành công trong <1s</th>
      <th>Manual test plan</th>
      <th>G ử i báo cáo PDF hàng ngày</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>Manual test plan</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng,</td>
      <td>network disconnect</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th></th>
      <th>s ự c ố</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công trong <1s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>JMeter script</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>API stress test</th>
      <th>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>invalid data</th>
      <th>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</th>
      <th>Automation Selenium</th>
      <th>Ph ả i log toàn b ộ k ế t qu ả</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>JMeter script</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>User login thành công trong <1s</td>
      <td>JMeter script</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n</td>
      <td>network disconnect</td>
      <td>User login thành công</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>thành công và th ấ t b ạ i.</th>
      <th></th>
      <th>trong <1s</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>Automation Selenium</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>JMeter script</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>API stress</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử</td>
      <td>invalid</td>
      <td>User login</td>
      <td>JMeter</td>
      <td>G ử i báo cáo</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>test</th>
      <th>ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>data</th>
      <th>thành công trong <1s</th>
      <th>script</th>
      <th>PDF hàng ngày</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>Automation Selenium</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>User login thành công trong <1s</td>
      <td>JMeter script</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>Manual test plan</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành</td>
      <td>invalid data</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>công và th ấ t b ạ i.</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công trong <1s</td>
      <td>Automation Selenium</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>Manual test plan</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ</td>
      <td>network disconnect</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không</td>
      <td>K ị ch b ả n Ansible</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th></th>
      <th>gián đoạ n</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>JMeter script</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>JMeter script</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Database</td>
      <td>Th ự c hi ệ n Database</td>
      <td>DB</td>
      <td>H ệ th ố ng</td>
      <td>Automation</td>
      <td>So sánh</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>recovery test</th>
      <th>recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>corruption</th>
      <th>ch ị u t ả i 20k TPS không gián đoạ n</th>
      <th>Selenium</th>
      <th>benchmark v ớ i release trướ c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Manual test plan</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>JMeter script</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>Automation Selenium</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch</td>
      <td>invalid data</td>
      <td>User login thành công</td>
      <td>Manual test plan</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>b ả n thành công và th ấ t b ạ i.</th>
      <th></th>
      <th>trong <1s</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>JMeter script</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>JMeter script</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>Automation Selenium</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>Manual test plan</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ</td>
      <td>network disconnect</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau</td>
      <td>K ị ch b ả n Ansible</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th></th>
      <th>s ự c ố</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>Automation Selenium</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>Automation Selenium</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>API stress</td>
      <td>Th ự c hi ệ n API stress</td>
      <td>network</td>
      <td>Không</td>
      <td>JMeter</td>
      <td>Theo chu ẩ n</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>test</th>
      <th>test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>disconnect</th>
      <th>phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</th>
      <th>script</th>
      <th>ISTQB</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch</td>
      <td>invalid data</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>b ả n thành công và th ấ t b ạ i.</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>K ị ch b ả n Ansible</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công trong <1s</td>
      <td>JMeter script</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>Manual test plan</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Data consistency</td>
      <td>Th ự c hi ệ n Data consistency test để</td>
      <td>network</td>
      <td>H ệ th ố ng ch ị u t ả i</td>
      <td>Manual test</td>
      <td>Ph ả i log toàn</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>test</th>
      <th>ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>disconnect</th>
      <th>20k TPS không gián đoạ n</th>
      <th>plan</th>
      <th>b ộ k ế t qu ả</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>JMeter script</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>User login thành công trong <1s</td>
      <td>Automation Selenium</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>Automation Selenium</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Load test</th>
      <th>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>network disconnect</th>
      <th>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</th>
      <th>JMeter script</th>
      <th>G ử i báo cáo PDF hàng ngày</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>Automation Selenium</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Manual test plan</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công trong <1s</td>
      <td>Automation Selenium</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t</td>
      <td>stress load > 10k TPS</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>b ạ i.</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>User login thành công trong <1s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>Automation Selenium</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>User login thành công trong <1s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>JMeter script</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>Security</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử</td>
      <td>valid data</td>
      <td>D ữ li ệ u đượ c khôi</td>
      <td>Manual test</td>
      <td>Test môi trườ ng Pre-</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>scan</th>
      <th>ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th></th>
      <th>ph ụ c toàn v ẹ n sau s ự c ố</th>
      <th>plan</th>
      <th>Prod</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Manual test plan</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>User login thành công trong <1s</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Failover test</th>
      <th>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>DB corruption</th>
      <th>User login thành công trong <1s</th>
      <th>Manual test plan</th>
      <th>Test môi trườ ng Pre- Prod</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>JMeter script</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>JMeter script</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>Automation Selenium</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành</td>
      <td>invalid data</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau</td>
      <td>Manual test plan</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>công và th ấ t b ạ i.</th>
      <th></th>
      <th>s ự c ố</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>Automation Selenium</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Manual test plan</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>User login thành công trong <1s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Database recovery</td>
      <td>Th ự c hi ệ n Database recovery test để</td>
      <td>valid data</td>
      <td>User login</td>
      <td>JMeter</td>
      <td>Theo chu ẩ n</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>test</th>
      <th>ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th></th>
      <th>thành công trong <1s</th>
      <th>script</th>
      <th>ISTQB</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>JMeter script</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Failover test</th>
      <th>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>DB corruption</th>
      <th>Cluster failover t ự độ ng trong 5s</th>
      <th>Automation Selenium</th>
      <th>G ử i báo cáo PDF hàng ngày</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>User login thành công trong <1s</td>
      <td>JMeter script</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>User login thành công trong <1s</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng,</td>
      <td>valid data</td>
      <td>User login thành công</td>
      <td>Automation Selenium</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th></th>
      <th>trong <1s</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Manual test plan</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>JMeter script</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>Manual test plan</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Data</td>
      <td>Th ự c hi ệ n Data</td>
      <td>DB</td>
      <td>User</td>
      <td>K ị ch b ả n</td>
      <td>Test môi</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>consistency test</th>
      <th>consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>corruption</th>
      <th>login thành công trong <1s</th>
      <th>Ansible</th>
      <th>trườ ng Pre- Prod</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Manual test plan</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Automation Selenium</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Automation Selenium</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành</td>
      <td>network disconnect</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>công và th ấ t b ạ i.</th>
      <th></th>
      <th>Top 10</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>JMeter script</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành</td>
      <td>valid data</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP</td>
      <td>Manual test plan</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>công và th ấ t b ạ i.</th>
      <th></th>
      <th>Top 10</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>User login thành công trong <1s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>Automation Selenium</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>User login thành công trong <1s</td>
      <td>JMeter script</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công</td>
      <td>JMeter script</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th></th>
      <th>trong <1s</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>JMeter script</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>JMeter script</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>JMeter script</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng</td>
      <td>stress load > 10k</td>
      <td>Không phát hi ệ n l ỗ h ổ ng</td>
      <td>JMeter script</td>
      <td>So sánh benchmark v ớ i</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>TPS</th>
      <th>b ả om ậ t OWASP Top 10</th>
      <th></th>
      <th>release trướ c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>User login thành công trong <1s</td>
      <td>JMeter script</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>User login thành công trong <1s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Data</td>
      <td>Th ự c hi ệ n Data</td>
      <td>invalid</td>
      <td>User</td>
      <td>Automation</td>
      <td>So sánh</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>consistency test</th>
      <th>consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>data</th>
      <th>login thành công trong <1s</th>
      <th>Selenium</th>
      <th>benchmark v ớ i release trướ c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>Automation Selenium</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>JMeter script</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành</td>
      <td>stress load > 10k TPS</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>công và th ấ t b ạ i.</th>
      <th></th>
      <th>Top 10</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>JMeter script</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>Manual test plan</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>User login thành công trong <1s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Database recovery</td>
      <td>Th ự c hi ệ n Database recovery test để</td>
      <td>network</td>
      <td>Cluster failover</td>
      <td>Manual test</td>
      <td>So sánh benchmark v ớ i</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>test</th>
      <th>ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>disconnect</th>
      <th>t ự độ ng trong 5s</th>
      <th>plan</th>
      <th>release trướ c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>JMeter script</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>Automation Selenium</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>K ị ch b ả n Ansible</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t</td>
      <td>API call batch 1000 request</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>b ạ i.</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>User login thành công trong <1s</td>
      <td>JMeter script</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Automation Selenium</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công trong <1s</td>
      <td>JMeter script</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng</td>
      <td>invalid data</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn</td>
      <td>JMeter script</td>
      <td>Test môi trườ ng Pre-</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th></th>
      <th>v ẹ n sau s ự c ố</th>
      <th></th>
      <th>Prod</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>Manual test plan</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Automation Selenium</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>JMeter script</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Data consistency</td>
      <td>Th ự c hi ệ n Data consistency test để</td>
      <td>API call batch</td>
      <td>Không phát hi ệ n</td>
      <td>K ị ch b ả n</td>
      <td>Theo chu ẩ n</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>test</th>
      <th>ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>1000 request</th>
      <th>l ỗ h ổ ng b ả om ậ t OWASP Top 10</th>
      <th>Ansible</th>
      <th>ISTQB</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>JMeter script</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công trong <1s</td>
      <td>Automation Selenium</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>Manual test plan</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Data consistency test</th>
      <th>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>stress load > 10k TPS</th>
      <th>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</th>
      <th>K ị ch b ả n Ansible</th>
      <th>Ph ả i log toàn b ộ k ế t qu ả</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Manual test plan</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>Manual test plan</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Manual test plan</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch</td>
      <td>invalid data</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau</td>
      <td>JMeter script</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>b ả n thành công và th ấ t b ạ i.</th>
      <th></th>
      <th>s ự c ố</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>JMeter script</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Manual test plan</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>User login thành công trong <1s</td>
      <td>JMeter script</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Failover</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử</td>
      <td>DB</td>
      <td>Không phát hi ệ n</td>
      <td>Automation</td>
      <td>Theo chu ẩ n</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>test</th>
      <th>ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>corruption</th>
      <th>l ỗ h ổ ng b ả om ậ t OWASP Top 10</th>
      <th>Selenium</th>
      <th>ISTQB</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>Automation Selenium</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>JMeter script</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>Manual test plan</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t</td>
      <td>network disconnect</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>b ạ i.</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>User login thành công trong <1s</td>
      <td>JMeter script</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>JMeter script</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>Manual test plan</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Database recovery</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng</td>
      <td>network disconnect</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Test môi trườ ng Pre-</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>test</th>
      <th>và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th></th>
      <th>v ẹ n sau s ự c ố</th>
      <th></th>
      <th>Prod</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>K ị ch b ả n Ansible</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>JMeter script</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>JMeter script</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Load test</th>
      <th>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>valid data</th>
      <th>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</th>
      <th>Automation Selenium</th>
      <th>G ử i báo cáo PDF hàng ngày</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công trong <1s</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>JMeter script</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>Manual test plan</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành</td>
      <td>stress load > 10k TPS</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>công và th ấ t b ạ i.</th>
      <th></th>
      <th>Top 10</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>User login thành công trong <1s</td>
      <td>JMeter script</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>JMeter script</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>JMeter script</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Manual test plan</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u</td>
      <td>network disconnect</td>
      <td>Cluster failover t ự độ ng</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark v ớ i</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th></th>
      <th>trong 5s</th>
      <th></th>
      <th>release trướ c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>K ị ch b ả n Ansible</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>K ị ch b ả n Ansible</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và</td>
      <td>API call batch 1000 request</td>
      <td>User login thành công trong <1s</td>
      <td>Automation Selenium</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>th ấ t b ạ i.</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Automation Selenium</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>JMeter script</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>Automation Selenium</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Security</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử</td>
      <td>invalid</td>
      <td>H ệ th ố ng ch ị u t ả i</td>
      <td>K ị ch b ả n</td>
      <td>Test môi trườ ng Pre-</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>scan</th>
      <th>ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>data</th>
      <th>20k TPS không gián đoạ n</th>
      <th>Ansible</th>
      <th>Prod</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>User login thành công trong <1s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>JMeter script</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>JMeter script</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và</td>
      <td>network disconnect</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>th ấ t b ạ i.</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>JMeter script</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>Manual test plan</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ</td>
      <td>valid data</td>
      <td>User login thành công</td>
      <td>Manual test plan</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th></th>
      <th>trong <1s</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>JMeter script</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Automation Selenium</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Manual test plan</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Login test</th>
      <th>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>DB corruption</th>
      <th>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</th>
      <th>Manual test plan</th>
      <th>So sánh benchmark v ớ i release trướ c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>JMeter script</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>Automation Selenium</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>Automation Selenium</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành</td>
      <td>invalid data</td>
      <td>User login thành công trong <1s</td>
      <td>Automation Selenium</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>công và th ấ t b ạ i.</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>JMeter script</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng</td>
      <td>stress load > 10k</td>
      <td>User login thành</td>
      <td>JMeter script</td>
      <td>So sánh benchmark v ớ i</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>TPS</th>
      <th>công trong <1s</th>
      <th></th>
      <th>release trướ c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>Manual test plan</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>JMeter script</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>User login thành công trong <1s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Load test</th>
      <th>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>stress load > 10k TPS</th>
      <th>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</th>
      <th>JMeter script</th>
      <th>Theo chu ẩ n ISTQB</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>Manual test plan</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>K ị ch b ả n Ansible</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và</td>
      <td>invalid data</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Automation Selenium</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>th ấ t b ạ i.</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>Manual test plan</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>K ị ch b ả n Ansible</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>K ị ch b ả n Ansible</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Manual test plan</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u</td>
      <td>API call batch 1000</td>
      <td>User login thành</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>request</th>
      <th>công trong <1s</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Automation Selenium</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Automation Selenium</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Automation Selenium</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Load test</th>
      <th>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>network disconnect</th>
      <th>Cluster failover t ự độ ng trong 5s</th>
      <th>Manual test plan</th>
      <th>G ử i báo cáo PDF hàng ngày</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>K ị ch b ả n Ansible</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>User login thành công trong <1s</td>
      <td>Automation Selenium</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t</td>
      <td>invalid data</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>b ạ i.</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Manual test plan</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>Automation Selenium</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c</td>
      <td>stress load > 10k</td>
      <td>H ệ th ố ng ch ị u t ả i</td>
      <td>Automation</td>
      <td>Ph ả i log toàn</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>TPS</th>
      <th>20k TPS không gián đoạ n</th>
      <th>Selenium</th>
      <th>b ộ k ế t qu ả</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>K ị ch b ả n Ansible</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>JMeter script</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>JMeter script</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Login test</th>
      <th>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>stress load > 10k TPS</th>
      <th>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</th>
      <th>JMeter script</th>
      <th>Ph ả i log toàn b ộ k ế t qu ả</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>Automation Selenium</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và</td>
      <td>invalid data</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>JMeter script</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>th ấ t b ạ i.</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>JMeter script</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>Manual test plan</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c</td>
      <td>invalid</td>
      <td>H ệ th ố ng ch ị u t ả i</td>
      <td>K ị ch b ả n</td>
      <td>Ph ả i log toàn</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>data</th>
      <th>20k TPS không gián đoạ n</th>
      <th>Ansible</th>
      <th>b ộ k ế t qu ả</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Manual test plan</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>JMeter script</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>K ị ch b ả n Ansible</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Login test</th>
      <th>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>network disconnect</th>
      <th>User login thành công trong <1s</th>
      <th>JMeter script</th>
      <th>G ử i báo cáo PDF hàng ngày</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>Automation Selenium</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>Manual test plan</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công trong <1s</td>
      <td>Automation Selenium</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n</td>
      <td>invalid data</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP</td>
      <td>K ị ch b ả n Ansible</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>thành công và th ấ t b ạ i.</th>
      <th></th>
      <th>Top 10</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>JMeter script</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>User login thành công trong <1s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>JMeter script</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c</td>
      <td>API call batch</td>
      <td>Cluster failover</td>
      <td>K ị ch b ả n</td>
      <td>So sánh benchmark v ớ i</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>1000 request</th>
      <th>t ự độ ng trong 5s</th>
      <th>Ansible</th>
      <th>release trướ c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>K ị ch b ả n Ansible</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Manual test plan</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>JMeter script</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và</td>
      <td>network disconnect</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>th ấ t b ạ i.</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Manual test plan</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>User login thành công trong <1s</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>User login thành công trong <1s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u</td>
      <td>valid data</td>
      <td>Không phát hi ệ n l ỗ h ổ ng</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark v ớ i</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th></th>
      <th>b ả om ậ t OWASP Top 10</th>
      <th></th>
      <th>release trướ c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công trong <1s</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công trong <1s</td>
      <td>JMeter script</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và</td>
      <td>network disconnect</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>JMeter script</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>th ấ t b ạ i.</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>JMeter script</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>User login thành công trong <1s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>Manual test plan</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Security</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử</td>
      <td>API call batch</td>
      <td>H ệ th ố ng ch ị u t ả i</td>
      <td>Manual test</td>
      <td>So sánh benchmark v ớ i</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>scan</th>
      <th>ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>1000 request</th>
      <th>20k TPS không gián đoạ n</th>
      <th>plan</th>
      <th>release trướ c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>Manual test plan</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>JMeter script</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>User login thành công trong <1s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>API stress</td>
      <td>Th ự c hi ệ n API stress</td>
      <td>invalid</td>
      <td>Không</td>
      <td>K ị ch b ả n</td>
      <td>G ử i báo cáo</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>test</th>
      <th>test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>data</th>
      <th>phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</th>
      <th>Ansible</th>
      <th>PDF hàng ngày</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>Manual test plan</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>User login thành công trong <1s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Th ự c hi ệ n Data consistency test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và</td>
      <td>valid data</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>Manual test plan</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>th ấ t b ạ i.</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>invalid data</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>JMeter script</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>JMeter script</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>Automation Selenium</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t</td>
      <td>invalid data</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP</td>
      <td>JMeter script</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>b ạ i.</th>
      <th></th>
      <th>Top 10</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Security scan</td>
      <td>Th ự c hi ệ n Security scan để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>K ị ch b ả n Ansible</td>
      <td>So sánh benchmark v ớ i release trướ c</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>Manual test plan</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>DB corruption</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>Cluster failover t ự độ ng trong 5s</td>
      <td>Automation Selenium</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Database recovery</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng</td>
      <td>valid data</td>
      <td>Cluster failover t ự độ ng</td>
      <td>K ị ch b ả n Ansible</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>test</th>
      <th>và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th></th>
      <th>trong 5s</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>API call batch 1000 request</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Test môi trườ ng Pre- Prod</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Th ự c hi ệ n Database recovery test để ki ể mth ử ch ức năng và hi ệu năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công trong <1s</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>Manual test plan</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Th ự c hi ệ n API stress test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>stress load > 10k TPS</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>Manual test plan</td>
      <td>G ử i báo cáo PDF hàng ngày</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## K Ị CH B Ả N KI Ể M TH Ử QA

TD447

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Load test</th>
      <th>Th ự c hi ệ n Load test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</th>
      <th>invalid data</th>
      <th>User login thành công trong <1s</th>
      <th>K ị ch b ả n Ansible</th>
      <th>Theo chu ẩ n ISTQB</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>H ệ th ố ng ch ị u t ả i 20k TPS không gián đoạ n</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>valid data</td>
      <td>Không phát hi ệ n l ỗ h ổ ng b ả om ậ t OWASP Top 10</td>
      <td>K ị ch b ả n Ansible</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Th ự c hi ệ n Failover test để ki ể mth ử ch ức năng và hiệ u năng củ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>D ữ li ệ u đượ c khôi ph ụ c toàn v ẹ n sau s ự c ố</td>
      <td>JMeter script</td>
      <td>Ph ả i log toàn b ộ k ế t qu ả</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Th ự c hi ệ n Login test để ki ể mth ử ch ứ c năng và hiệu năng c ủ a h ệ th ố ng, bao g ồ mk ị ch b ả n thành công và th ấ t b ạ i.</td>
      <td>network disconnect</td>
      <td>User login thành công trong <1s</td>
      <td>Automation Selenium</td>
      <td>Theo chu ẩ n ISTQB</td>
    </tr>
  </tbody>
</table>
<!-- image -->

