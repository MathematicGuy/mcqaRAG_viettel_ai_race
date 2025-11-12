<!-- image -->

## QU Ả N LÝ API &amp; LOG

TD448

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>API</th>
      <th>Phương th ứ c</th>
      <th>Hành độ ng</th>
      <th>Mô t ả chi ti ế t</th>
      <th>K ế t qu ả</th>
      <th>Ghi chú</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/customer/update</td>
      <td>PATCH</td>
      <td>Thêm b ả n ghi</td>
      <td>API /customer/update s ử d ụng phương thứ c PATCH để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PATCH</td>
      <td>Xóa thông tin</td>
      <td>API /invoice/export s ử d ụng phương thứ c PATCH để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>GET</td>
      <td>Xóa thông tin</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c GET để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>POST</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PUT</td>
      <td>Export d ữ li ệ u</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
  </tbody>
</table>
<!-- image -->

/rpa/task/execute    <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>POST</th>
      <th>C ậ p nh ậ t c ấ u hình</th>
      <th>API /rpa/task/execute s ử d ụng phương thứ c POST để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>Log đầ y đủ</th>
      <th>Tích h ợ p v ớ i API Gateway</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/customer/update</td>
      <td>GET</td>
      <td>Thêm b ả n ghi</td>
      <td>API /customer/update s ử d ụng phương thứ c GET để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>POST</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>POST</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /invoice/export s ử d ụng phương thứ c POST để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>GET</td>
      <td>Export d ữ li ệ u</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c GET để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
  </tbody>
</table>
<!-- image -->

/rpa/task/execute         <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>POST</th>
      <th>Export d ữ li ệ u</th>
      <th>API /rpa/task/execute s ử d ụng phương thứ c POST để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>Log đầ y đủ</th>
      <th>Gi ớ i h ạ n rate-limit 1000 req/min</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>Export d ữ li ệ u</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c PATCH để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>POST</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /invoice/export s ử d ụng phương thứ c POST để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>GET</td>
      <td>Xóa thông tin</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c GET để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>DELETE</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
  </tbody>
</table>
<!-- image -->

/ivr/callflow             <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>POST</th>
      <th>Xóa thông tin</th>
      <th>API /ivr/callflow s ử d ụng phương thứ c POST để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>Thành công <1s</th>
      <th>Theo chu ẩ n RESTful</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/security/firewall/config</td>
      <td>POST</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>GET</td>
      <td>Thêm b ả n ghi</td>
      <td>API /invoice/export s ử d ụng phương thứ c GET để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PATCH</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /invoice/export s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PUT</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c PUT để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PUT</td>
      <td>Thêm b ả n</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c PUT</td>
      <td>Log đầ y</td>
      <td>Tích h ợ p v ớ i API</td>
    </tr>
  </tbody>
</table>
<!-- image -->

ghi                     <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>đủ</th>
      <th>Gateway</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/rpa/task/execute</td>
      <td>POST</td>
      <td>Thêm b ả n ghi</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c POST để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>DELETE</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>DELETE</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c DELETE để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>DELETE</td>
      <td>Thêm b ả n ghi</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c DELETE để Thêm b ả n</td>
      <td>Thành công <1s</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
  </tbody>
</table>
<!-- image -->

ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                                                                                 <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/crm/lead/import</td>
      <td>DELETE</td>
      <td>Thêm b ả n ghi</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c DELETE để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PATCH</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c PATCH để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>GET</td>
      <td>Export d ữ li ệ u</td>
      <td>API /invoice/export s ử d ụng phương thứ c GET để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>POST</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>POST</td>
      <td>Ki ể m tra tr ạ ng</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c</td>
      <td>Log đầ y đủ</td>
      <td>Có versioning v1/v2</td>
    </tr>
  </tbody>
</table>
<!-- image -->

thái                    <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/security/firewall/config</td>
      <td>GET</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c GET để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>GET</td>
      <td>Thêm b ả n ghi</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c GET để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>POST</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c POST để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>GET</td>
      <td>Export d ữ li ệ u</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c GET để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>DELETE</td>
      <td>Thêm b ả n ghi</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c DELETE để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
  </tbody>
</table>
<!-- image -->

d ị ch chi ti ế t.                                                                                                                  <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/invoice/export</td>
      <td>PUT</td>
      <td>Export d ữ li ệ u</td>
      <td>API /invoice/export s ử d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PATCH</td>
      <td>Export d ữ li ệ u</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c PATCH để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PUT</td>
      <td>Export d ữ li ệ u</td>
      <td>API /invoice/export s ử d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>DELETE</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /customer/update s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>DELETE</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c DELETE để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>PUT</td>
      <td>Export</td>
      <td>API</td>
      <td>Rollback</td>
      <td>Tích h ợ p</td>
    </tr>
  </tbody>
</table>
<!-- image -->

d ữ li ệ u        <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>/security/firewall/config s ử d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>khi l ỗ i</th>
      <th>v ớ i API Gateway</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PUT</td>
      <td>Export d ữ li ệ u</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>PUT</td>
      <td>Thêm b ả n ghi</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c PUT để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>DELETE</td>
      <td>Export d ữ li ệ u</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c DELETE để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PATCH</td>
      <td>Thêm b ả n ghi</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c PATCH để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>GET</td>
      <td>Xóa thông</td>
      <td>API /invoice/export s ử d ụng phương thứ c GET</td>
      <td>Rollback</td>
      <td>Gi ớ i h ạ n rate-limit</td>
    </tr>
  </tbody>
</table>
<!-- image -->

tin                     <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>khi l ỗ i</th>
      <th>1000 req/min</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PATCH</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c PATCH để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>DELETE</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>DELETE</td>
      <td>Thêm b ả n ghi</td>
      <td>API /invoice/export s ử d ụng phương thứ c DELETE để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>GET</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c GET để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>DELETE</td>
      <td>C ậ p nh ậ t c ấ u</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c DELETE để C ậ p nh ậ t c ấ u hình, có xác th ự c</td>
      <td>Thành công <1s</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
  </tbody>
</table>
<!-- image -->

hình                    <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/crm/lead/import</td>
      <td>PUT</td>
      <td>Xóa thông tin</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c PUT để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>POST</td>
      <td>Thêm b ả n ghi</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c POST để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PATCH</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PATCH</td>
      <td>Xóa thông tin</td>
      <td>API /customer/update s ử d ụng phương thứ c PATCH để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>POST</td>
      <td>Export d ữ li ệ u</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c POST để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao</td>
      <td>Log đầ y đủ</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
  </tbody>
</table>
<!-- image -->

d ị ch chi ti ế t.                                                                                                                       <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/security/firewall/config</td>
      <td>PUT</td>
      <td>Thêm b ả n ghi</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c PUT để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>GET</td>
      <td>Export d ữ li ệ u</td>
      <td>API /invoice/export s ử d ụng phương thứ c GET để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>POST</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>GET</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /customer/update s ử d ụng phương thứ c GET để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>POST</td>
      <td>Xóa thông tin</td>
      <td>API /customer/update s ử d ụng phương thứ c POST để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
  </tbody>
</table>
<!-- image -->

/network/qos/monitor      <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>PUT</th>
      <th>Thêm b ả n ghi</th>
      <th>API /network/qos/monitor s ử d ụng phương thứ c PUT để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>Retry t ố i đa 3 lầ n</th>
      <th>Có versioning v1/v2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/ivr/callflow</td>
      <td>DELETE</td>
      <td>Export d ữ li ệ u</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c DELETE để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>GET</td>
      <td>Xóa thông tin</td>
      <td>API /invoice/export s ử d ụng phương thứ c GET để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>GET</td>
      <td>Export d ữ li ệ u</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c GET để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>POST</td>
      <td>Xóa thông tin</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c POST để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>DELETE</td>
      <td>Xóa thông</td>
      <td>API /customer/update s ử d ụng phương thứ c DELETE để Xóa thông</td>
      <td>Rollback khi l ỗ i</td>
      <td>Gi ớ i h ạ n rate-limit 1000</td>
    </tr>
  </tbody>
</table>
<!-- image -->

tin                     <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th></th>
      <th>req/min</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/security/firewall/config</td>
      <td>POST</td>
      <td>Thêm b ả n ghi</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c POST để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>GET</td>
      <td>Thêm b ả n ghi</td>
      <td>API /invoice/export s ử d ụng phương thứ c GET để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PUT</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /customer/update s ử d ụng phương thứ c PUT để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>POST</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /customer/update s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>POST</td>
      <td>Export d ữ li ệ u</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c POST để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao</td>
      <td>Thành công <1s</td>
      <td>Có versioning v1/v2</td>
    </tr>
  </tbody>
</table>
<!-- image -->

d ị ch chi ti ế t.                                                                                                                  <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/invoice/export</td>
      <td>DELETE</td>
      <td>Export d ữ li ệ u</td>
      <td>API /invoice/export s ử d ụng phương thứ c DELETE để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>GET</td>
      <td>Export d ữ li ệ u</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c GET để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>Xóa thông tin</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c PATCH để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>POST</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>DELETE</td>
      <td>Thêm b ả n ghi</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c DELETE để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao</td>
      <td>Log đầ y đủ</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
  </tbody>
</table>
<!-- image -->

d ị ch chi ti ế t.                                                                                                                  <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/crm/lead/import</td>
      <td>PUT</td>
      <td>Export d ữ li ệ u</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>POST</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>GET</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /customer/update s ử d ụng phương thứ c GET để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PUT</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c PUT để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PUT</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c PUT để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao</td>
      <td>Thành công <1s</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## QU Ả N LÝ API &amp; LOG

TD448

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>d ị ch chi ti ế t.</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/security/firewall/config</td>
      <td>GET</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c GET để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>GET</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c GET để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>POST</td>
      <td>Thêm b ả n ghi</td>
      <td>API /invoice/export s ử d ụng phương thứ c POST để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>DELETE</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>GET</td>
      <td>C ậ p nh ậ t c ấ u</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Tích h ợ p v ớ i API</td>
    </tr>
  </tbody>
</table>
<!-- image -->

hình                    <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>GET để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th></th>
      <th>Gateway</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PATCH</td>
      <td>Export d ữ li ệ u</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c PATCH để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PUT</td>
      <td>Xóa thông tin</td>
      <td>API /customer/update s ử d ụng phương thứ c PUT để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PUT</td>
      <td>Thêm b ả n ghi</td>
      <td>API /customer/update s ử d ụng phương thứ c PUT để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>GET</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c GET để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PUT</td>
      <td>Export d ữ li ệ u</td>
      <td>API /invoice/export s ử d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
  </tbody>
</table>
<!-- image -->

/security/firewall/config   <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>DELETE</th>
      <th>Xóa thông tin</th>
      <th>API /security/firewall/config s ử d ụng phương thứ c DELETE để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>Rollback khi l ỗ i</th>
      <th>Tích h ợ p v ớ i API Gateway</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/network/qos/monitor</td>
      <td>DELETE</td>
      <td>Export d ữ li ệ u</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c DELETE để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>Xóa thông tin</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c PATCH để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>POST</td>
      <td>Thêm b ả n ghi</td>
      <td>API /invoice/export s ử d ụng phương thứ c POST để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>POST</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c POST để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
  </tbody>
</table>
<!-- image -->

/crm/lead/import     <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>GET</th>
      <th>Ki ể m tra tr ạ ng thái</th>
      <th>API /crm/lead/import s ử d ụng phương thứ c GET để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>Retry t ố i đa 3 lầ n</th>
      <th>Theo chu ẩ n RESTful</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PUT</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c PUT để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>POST</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /customer/update s ử d ụng phương thứ c POST để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PUT</td>
      <td>Thêm b ả n ghi</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c PUT để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>POST</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
  </tbody>
</table>
<!-- image -->

/customer/update   <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>PATCH</th>
      <th>C ậ p nh ậ t c ấ u hình</th>
      <th>API /customer/update s ử d ụng phương thứ c PATCH để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>Log đầ y đủ</th>
      <th>Tích h ợ p v ớ i API Gateway</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/invoice/export</td>
      <td>POST</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /invoice/export s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c PATCH để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>GET</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /customer/update s ử d ụng phương thứ c GET để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c PATCH để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
  </tbody>
</table>
<!-- image -->

/crm/lead/import          <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>GET</th>
      <th>Thêm b ả n ghi</th>
      <th>API /crm/lead/import s ử d ụng phương thứ c GET để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>Thành công <1s</th>
      <th>Tích h ợ p v ớ i API Gateway</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/security/firewall/config</td>
      <td>GET</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c GET để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>Export d ữ li ệ u</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c PATCH để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>GET</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c GET để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>POST</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
  </tbody>
</table>
<!-- image -->

d ị ch chi ti ế t.                                                                                                                  <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/customer/update</td>
      <td>POST</td>
      <td>Export d ữ li ệ u</td>
      <td>API /customer/update s ử d ụng phương thứ c POST để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>DELETE</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>GET</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c GET để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PUT</td>
      <td>Export d ữ li ệ u</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PATCH</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao</td>
      <td>Rollback khi l ỗ i</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
  </tbody>
</table>
<!-- image -->

d ị ch chi ti ế t.                                                                                                              <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/crm/lead/import</td>
      <td>PUT</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c PUT để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>POST</td>
      <td>Xóa thông tin</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c POST để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PATCH</td>
      <td>Export d ữ li ệ u</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c PATCH để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PUT</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c PUT để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>GET</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c GET để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>Thêm</td>
      <td>API /crm/lead/import</td>
      <td>Thông</td>
      <td>Theo</td>
    </tr>
  </tbody>
</table>
<!-- image -->

b ả n ghi               <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>s ử d ụng phương thứ c PATCH để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>báo s ự ki ệ n qua Kafka</th>
      <th>chu ẩ n RESTful</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PATCH</td>
      <td>Thêm b ả n ghi</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c PATCH để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PATCH</td>
      <td>Export d ữ li ệ u</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c PATCH để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PUT</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /invoice/export s ử d ụng phương thứ c PUT để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>DELETE</td>
      <td>Export d ữ li ệ u</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c DELETE để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PUT</td>
      <td>C ậ p nh ậ t</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c</td>
      <td>Rollback</td>
      <td>Theo chu ẩ n</td>
    </tr>
  </tbody>
</table>
<!-- image -->

c ấ u hình              <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>PUT để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>khi l ỗ i</th>
      <th>RESTful</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/rpa/task/execute</td>
      <td>POST</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c POST để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>DELETE</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>POST</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>GET</td>
      <td>Xóa thông tin</td>
      <td>API /customer/update s ử d ụng phương thứ c GET để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>POST</td>
      <td>Ki ể m tra tr ạ ng</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c POST để Ki ể mtra</td>
      <td>Thành công</td>
      <td>Gi ớ i h ạ n rate-limit 1000</td>
    </tr>
  </tbody>
</table>
<!-- image -->

thái                    <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th><1s</th>
      <th>req/min</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/security/firewall/config</td>
      <td>DELETE</td>
      <td>Thêm b ả n ghi</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c DELETE để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>DELETE</td>
      <td>Xóa thông tin</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c DELETE để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PATCH</td>
      <td>Xóa thông tin</td>
      <td>API /customer/update s ử d ụng phương thứ c PATCH để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>PATCH</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c PATCH để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>GET</td>
      <td>C ậ p nh ậ t c ấ u</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c</td>
      <td>Rollback khi l ỗ i</td>
      <td>Tích h ợ p v ớ i API</td>
    </tr>
  </tbody>
</table>
<!-- image -->

hình                    <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>GET để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th></th>
      <th>Gateway</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/customer/update</td>
      <td>PUT</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /customer/update s ử d ụng phương thứ c PUT để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>POST</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c POST để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>POST</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>POST</td>
      <td>Export d ữ li ệ u</td>
      <td>API /invoice/export s ử d ụng phương thứ c POST để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>POST</td>
      <td>Xóa thông</td>
      <td>API /security/firewall/config</td>
      <td>Retry t ố i</td>
      <td>H ỗ tr ợ JSON và</td>
    </tr>
  </tbody>
</table>
<!-- image -->

tin                     <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>s ử d ụng phương thứ c POST để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>đa 3 lầ n</th>
      <th>XML</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/crm/lead/import</td>
      <td>POST</td>
      <td>Thêm b ả n ghi</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c POST để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>DELETE</td>
      <td>Thêm b ả n ghi</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c DELETE để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>DELETE</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PATCH</td>
      <td>Export d ữ li ệ u</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c PATCH để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
  </tbody>
</table>
<!-- image -->

/rpa/task/execute   <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>PATCH</th>
      <th>C ậ p nh ậ t c ấ u hình</th>
      <th>API /rpa/task/execute s ử d ụng phương thứ c PATCH để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>Retry t ố i đa 3 lầ n</th>
      <th>Tích h ợ p v ớ i API Gateway</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/crm/lead/import</td>
      <td>GET</td>
      <td>Thêm b ả n ghi</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c GET để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>DELETE</td>
      <td>Xóa thông tin</td>
      <td>API /invoice/export s ử d ụng phương thứ c DELETE để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>GET</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /customer/update s ử d ụng phương thứ c GET để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>POST</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>POST</td>
      <td>Xóa thông</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c POST để Xóa thông tin,</td>
      <td>Thành công</td>
      <td>Tích h ợ p v ớ i API</td>
    </tr>
  </tbody>
</table>
<!-- image -->

tin               <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th><1s</th>
      <th>Gateway</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PATCH</td>
      <td>Thêm b ả n ghi</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c PATCH để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>GET</td>
      <td>Xóa thông tin</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c GET để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PATCH</td>
      <td>Export d ữ li ệ u</td>
      <td>API /customer/update s ử d ụng phương thứ c PATCH để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>POST</td>
      <td>Export d ữ li ệ u</td>
      <td>API /invoice/export s ử d ụng phương thứ c POST để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PUT</td>
      <td>Xóa thông tin</td>
      <td>API /invoice/export s ử d ụng phương thứ c PUT để Xóa thông tin, có xác th ự c OAuth2 và log</td>
      <td>Log đầ y đủ</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
  </tbody>
</table>
<!-- image -->

giao d ị ch chi ti ế t.                                                                                                          <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PATCH</td>
      <td>Thêm b ả n ghi</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c PATCH để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>GET</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c GET để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PATCH</td>
      <td>Xóa thông tin</td>
      <td>API /customer/update s ử d ụng phương thứ c PATCH để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>DELETE</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /invoice/export s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PUT</td>
      <td>Thêm b ả n ghi</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c PUT để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Có versioning v1/v2</td>
    </tr>
  </tbody>
</table>
<!-- image -->

/invoice/export      <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>PATCH</th>
      <th>Xóa thông tin</th>
      <th>API /invoice/export s ử d ụng phương thứ c PATCH để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>Thành công <1s</th>
      <th>Tích h ợ p v ớ i API Gateway</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/ivr/callflow</td>
      <td>DELETE</td>
      <td>Thêm b ả n ghi</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c DELETE để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>GET</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c GET để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>DELETE</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PATCH</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c PATCH để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
  </tbody>
</table>
<!-- image -->

/ivr/callflow     <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>POST</th>
      <th>Export d ữ li ệ u</th>
      <th>API /ivr/callflow s ử d ụng phương thứ c POST để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>Rollback khi l ỗ i</th>
      <th>H ỗ tr ợ JSON và XML</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/ivr/callflow</td>
      <td>DELETE</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c DELETE để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>GET</td>
      <td>Xóa thông tin</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c GET để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PUT</td>
      <td>Xóa thông tin</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c PUT để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>Thêm b ả n ghi</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c PATCH để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PUT</td>
      <td>Ki ể m tra tr ạ ng</td>
      <td>API /invoice/export s ử d ụng phương thứ c PUT để Ki ể mtra tr ạ ng thái,</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Theo chu ẩ n</td>
    </tr>
  </tbody>
</table>
<!-- image -->

thái                    <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th></th>
      <th>RESTful</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/ivr/callflow</td>
      <td>PATCH</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>GET</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /invoice/export s ử d ụng phương thứ c GET để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PATCH</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c PATCH để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>GET</td>
      <td>Xóa thông tin</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c GET để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>POST</td>
      <td>Export d ữ li ệ u</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c POST để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
  </tbody>
</table>
<!-- image -->

d ị ch chi ti ế t.                                                                                                                 <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/invoice/export</td>
      <td>PUT</td>
      <td>Xóa thông tin</td>
      <td>API /invoice/export s ử d ụng phương thứ c PUT để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>DELETE</td>
      <td>Thêm b ả n ghi</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c DELETE để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PATCH</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /invoice/export s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>DELETE</td>
      <td>Export d ữ li ệ u</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c DELETE để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PATCH</td>
      <td>Export d ữ li ệ u</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c PATCH để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
  </tbody>
</table>
<!-- image -->

d ị ch chi ti ế t.                                                                                                                <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c PATCH để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>POST</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PATCH</td>
      <td>Xóa thông tin</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c PATCH để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>DELETE</td>
      <td>Xóa thông tin</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c DELETE để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>DELETE</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao</td>
      <td>Rollback khi l ỗ i</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
  </tbody>
</table>
<!-- image -->

d ị ch chi ti ế t.                                                                                                                 <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/customer/update</td>
      <td>DELETE</td>
      <td>Xóa thông tin</td>
      <td>API /customer/update s ử d ụng phương thứ c DELETE để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>GET</td>
      <td>Thêm b ả n ghi</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c GET để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>DELETE</td>
      <td>Export d ữ li ệ u</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c DELETE để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>POST</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /invoice/export s ử d ụng phương thứ c POST để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>GET</td>
      <td>Export d ữ li ệ u</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c GET để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
  </tbody>
</table>
<!-- image -->

/security/firewall/config   <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>PATCH</th>
      <th>Xóa thông tin</th>
      <th>API /security/firewall/config s ử d ụng phương thứ c PATCH để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>Log đầ y đủ</th>
      <th>H ỗ tr ợ JSON và XML</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/network/qos/monitor</td>
      <td>POST</td>
      <td>Export d ữ li ệ u</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c POST để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>DELETE</td>
      <td>Thêm b ả n ghi</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c DELETE để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PUT</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c PUT để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PUT</td>
      <td>Thêm b ả n ghi</td>
      <td>API /invoice/export s ử d ụng phương thứ c PUT để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
  </tbody>
</table>
<!-- image -->

/ivr/callflow        <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>PATCH</th>
      <th>C ậ p nh ậ t c ấ u hình</th>
      <th>API /ivr/callflow s ử d ụng phương thứ c PATCH để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>Retry t ố i đa 3 lầ n</th>
      <th>Gi ớ i h ạ n rate-limit 1000 req/min</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/network/qos/monitor</td>
      <td>DELETE</td>
      <td>Export d ữ li ệ u</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c DELETE để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PUT</td>
      <td>Xóa thông tin</td>
      <td>API /customer/update s ử d ụng phương thứ c PUT để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PATCH</td>
      <td>Xóa thông tin</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c PATCH để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>POST</td>
      <td>Xóa thông tin</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c POST để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>Xóa thông</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c</td>
      <td>Thông báo s ự</td>
      <td>Theo chu ẩ n</td>
    </tr>
  </tbody>
</table>
<!-- image -->

tin                     <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>PATCH để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>ki ệ n qua Kafka</th>
      <th>RESTful</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c PATCH để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PUT</td>
      <td>Xóa thông tin</td>
      <td>API /customer/update s ử d ụng phương thứ c PUT để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>POST</td>
      <td>Export d ữ li ệ u</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c POST để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>PATCH</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c PATCH để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>GET</td>
      <td>Thêm b ả n ghi</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c GET để Thêm b ả n ghi, có xác th ự c OAuth2 và</td>
      <td>Log đầ y đủ</td>
      <td>Có versioning v1/v2</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## QU Ả N LÝ API &amp; LOG

TD448

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>log giao d ị ch chi ti ế t.</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/network/qos/monitor</td>
      <td>POST</td>
      <td>Xóa thông tin</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c POST để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>POST</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /customer/update s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PATCH</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c PATCH để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PUT</td>
      <td>Thêm b ả n ghi</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c PUT để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>GET</td>
      <td>Xóa thông tin</td>
      <td>API /invoice/export s ử d ụng phương thứ c GET để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PUT</td>
      <td>Export</td>
      <td>API /ivr/callflow s ử</td>
      <td>Thông</td>
      <td>H ỗ tr ợ</td>
    </tr>
  </tbody>
</table>
<!-- image -->

d ữ li ệ u              <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>báo s ự ki ệ n qua Kafka</th>
      <th>JSON và XML</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/rpa/task/execute</td>
      <td>POST</td>
      <td>Xóa thông tin</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c POST để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>DELETE</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c DELETE để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PATCH</td>
      <td>Thêm b ả n ghi</td>
      <td>API /invoice/export s ử d ụng phương thứ c PATCH để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>PUT</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c PUT để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>POST</td>
      <td>C ậ p nh ậ t c ấ u</td>
      <td>API /invoice/export s ử d ụng phương thứ c POST để C ậ p nh ậ t c ấ u</td>
      <td>Thông báo s ự ki ệ n qua</td>
      <td>Theo chu ẩ n</td>
    </tr>
  </tbody>
</table>
<!-- image -->

hình                    <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>Kafka</th>
      <th>RESTful</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PUT</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c PUT để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PUT</td>
      <td>Thêm b ả n ghi</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c PUT để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>PUT</td>
      <td>Thêm b ả n ghi</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c PUT để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PUT</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c PUT để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>GET</td>
      <td>Export d ữ li ệ u</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c GET để Export d ữ li ệ u,</td>
      <td>Rollback khi l ỗ i</td>
      <td>Có versioning v1/v2</td>
    </tr>
  </tbody>
</table>
<!-- image -->

có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.                                                                                <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/rpa/task/execute</td>
      <td>DELETE</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>POST</td>
      <td>Thêm b ả n ghi</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c POST để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>DELETE</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c DELETE để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>DELETE</td>
      <td>Export d ữ li ệ u</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c DELETE để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>PUT</td>
      <td>Export d ữ li ệ u</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
  </tbody>
</table>
<!-- image -->

log giao d ị ch chi ti ế t.                                                                                                      <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/crm/lead/import</td>
      <td>POST</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c POST để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PATCH</td>
      <td>Xóa thông tin</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c PATCH để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PATCH</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /invoice/export s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>GET</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c GET để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>GET</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /customer/update s ử d ụng phương thứ c GET để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
  </tbody>
</table>
<!-- image -->

/rpa/task/execute         <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>GET</th>
      <th>Thêm b ả n ghi</th>
      <th>API /rpa/task/execute s ử d ụng phương thứ c GET để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>Rollback khi l ỗ i</th>
      <th>Theo chu ẩ n RESTful</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/invoice/export</td>
      <td>GET</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /invoice/export s ử d ụng phương thứ c GET để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PATCH</td>
      <td>Thêm b ả n ghi</td>
      <td>API /invoice/export s ử d ụng phương thứ c PATCH để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>DELETE</td>
      <td>Thêm b ả n ghi</td>
      <td>API /invoice/export s ử d ụng phương thứ c DELETE để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>DELETE</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c DELETE để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PUT</td>
      <td>Xóa thông</td>
      <td>API /invoice/export s ử d ụng phương thứ c PUT</td>
      <td>Retry t ố i</td>
      <td>Theo chu ẩ n</td>
    </tr>
  </tbody>
</table>
<!-- image -->

tin                     <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>đa 3 lầ n</th>
      <th>RESTful</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/crm/lead/import</td>
      <td>POST</td>
      <td>Thêm b ả n ghi</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c POST để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>GET</td>
      <td>Thêm b ả n ghi</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c GET để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PUT</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c PUT để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>DELETE</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PUT</td>
      <td>Thêm b ả n ghi</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c PUT để Thêm b ả n ghi, có xác th ự c OAuth2 và</td>
      <td>Thành công <1s</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
  </tbody>
</table>
<!-- image -->

log giao d ị ch chi ti ế t.                                                                                                      <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PATCH</td>
      <td>Xóa thông tin</td>
      <td>API /customer/update s ử d ụng phương thứ c PATCH để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>POST</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>GET</td>
      <td>Xóa thông tin</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c GET để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>DELETE</td>
      <td>Xóa thông tin</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c DELETE để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PUT</td>
      <td>Export</td>
      <td>API /ivr/callflow s ử</td>
      <td>Retry t ố i</td>
      <td>Theo</td>
    </tr>
  </tbody>
</table>
<!-- image -->

d ữ li ệ u              <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>đa 3 lầ n</th>
      <th>chu ẩ n RESTful</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PATCH</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PATCH</td>
      <td>Export d ữ li ệ u</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c PATCH để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PUT</td>
      <td>Xóa thông tin</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c PUT để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PATCH</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>GET</td>
      <td>Export d ữ li ệ u</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c GET để Export d ữ li ệ u, có xác th ự c OAuth2 và</td>
      <td>Log đầ y đủ</td>
      <td>Có versioning v1/v2</td>
    </tr>
  </tbody>
</table>
<!-- image -->

log giao d ị ch chi ti ế t.                                                                                                   <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/rpa/task/execute</td>
      <td>DELETE</td>
      <td>Export d ữ li ệ u</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c DELETE để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PATCH</td>
      <td>Thêm b ả n ghi</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c PATCH để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>GET</td>
      <td>Export d ữ li ệ u</td>
      <td>API /invoice/export s ử d ụng phương thứ c GET để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>DELETE</td>
      <td>Export d ữ li ệ u</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c DELETE để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>PATCH</td>
      <td>Xóa thông tin</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c PATCH để Xóa thông tin, có xác th ự c OAuth2</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
  </tbody>
</table>
<!-- image -->

và log giao d ị ch chi ti ế t.                                                                                                      <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/customer/update</td>
      <td>PUT</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /customer/update s ử d ụng phương thứ c PUT để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>DELETE</td>
      <td>Xóa thông tin</td>
      <td>API /invoice/export s ử d ụng phương thứ c DELETE để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PUT</td>
      <td>Export d ữ li ệ u</td>
      <td>API /customer/update s ử d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>POST</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PUT</td>
      <td>Xóa thông tin</td>
      <td>API /invoice/export s ử d ụng phương thứ c PUT để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>GET</td>
      <td>Export</td>
      <td>API</td>
      <td>Retry t ố i</td>
      <td>Tích h ợ p</td>
    </tr>
  </tbody>
</table>
<!-- image -->

d ữ li ệ u              <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>/network/qos/monitor s ử d ụng phương thứ c GET để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>đa 3 lầ n</th>
      <th>v ớ i API Gateway</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/ivr/callflow</td>
      <td>GET</td>
      <td>Thêm b ả n ghi</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c GET để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>POST</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>POST</td>
      <td>Export d ữ li ệ u</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c POST để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>POST</td>
      <td>Export d ữ li ệ u</td>
      <td>API /invoice/export s ử d ụng phương thứ c POST để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
  </tbody>
</table>
<!-- image -->

/crm/lead/import   <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>PATCH</th>
      <th>Ki ể m tra tr ạ ng thái</th>
      <th>API /crm/lead/import s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>Retry t ố i đa 3 lầ n</th>
      <th>H ỗ tr ợ JSON và XML</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PUT</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c PUT để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PUT</td>
      <td>Thêm b ả n ghi</td>
      <td>API /invoice/export s ử d ụng phương thứ c PUT để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>DELETE</td>
      <td>Thêm b ả n ghi</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c DELETE để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PUT</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c PUT để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PATCH</td>
      <td>Thêm b ả n</td>
      <td>API /invoice/export s ử d ụng phương thứ c PATCH để Thêm b ả n</td>
      <td>Thành công</td>
      <td>Có versioning</td>
    </tr>
  </tbody>
</table>
<!-- image -->

ghi                     <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th><1s</th>
      <th>v1/v2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PUT</td>
      <td>Export d ữ li ệ u</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>DELETE</td>
      <td>Thêm b ả n ghi</td>
      <td>API /invoice/export s ử d ụng phương thứ c DELETE để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>POST</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /invoice/export s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PUT</td>
      <td>Thêm b ả n ghi</td>
      <td>API /customer/update s ử d ụng phương thứ c PUT để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PATCH</td>
      <td>Thêm b ả n ghi</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c PATCH để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
  </tbody>
</table>
<!-- image -->

d ị ch chi ti ế t.                                                                                                                 <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PUT</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c PUT để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>DELETE</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /invoice/export s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PATCH</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PUT</td>
      <td>Thêm b ả n ghi</td>
      <td>API /customer/update s ử d ụng phương thứ c PUT để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>DELETE</td>
      <td>Xóa thông tin</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c DELETE để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
  </tbody>
</table>
<!-- image -->

/crm/lead/import          <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>DELETE</th>
      <th>Thêm b ả n ghi</th>
      <th>API /crm/lead/import s ử d ụng phương thứ c DELETE để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>Retry t ố i đa 3 lầ n</th>
      <th>Gi ớ i h ạ n rate-limit 1000 req/min</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/crm/lead/import</td>
      <td>PUT</td>
      <td>Export d ữ li ệ u</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>POST</td>
      <td>Export d ữ li ệ u</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c POST để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>POST</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c POST để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PUT</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c PUT để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
  </tbody>
</table>
<!-- image -->

/crm/lead/import          <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>DELETE</th>
      <th>C ậ p nh ậ t c ấ u hình</th>
      <th>API /crm/lead/import s ử d ụng phương thứ c DELETE để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>Retry t ố i đa 3 lầ n</th>
      <th>Tích h ợ p v ớ i API Gateway</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/ivr/callflow</td>
      <td>DELETE</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c DELETE để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>GET</td>
      <td>Thêm b ả n ghi</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c GET để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>PATCH</td>
      <td>Export d ữ li ệ u</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c PATCH để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PUT</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c PUT để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Rollback khi l ỗ i</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>DELETE</td>
      <td>Ki ể m tra</td>
      <td>API /network/qos/monitor</td>
      <td>Rollback</td>
      <td>H ỗ tr ợ JSON và</td>
    </tr>
  </tbody>
</table>
<!-- image -->

tr ạ ng thái            <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>khi l ỗ i</th>
      <th>XML</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/invoice/export</td>
      <td>DELETE</td>
      <td>Xóa thông tin</td>
      <td>API /invoice/export s ử d ụng phương thứ c DELETE để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>POST</td>
      <td>Thêm b ả n ghi</td>
      <td>API /network/qos/monitor s ử d ụng phương thứ c POST để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>DELETE</td>
      <td>Xóa thông tin</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c DELETE để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>DELETE</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /invoice/export s ử d ụng phương thứ c DELETE để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PATCH</td>
      <td>Xóa thông</td>
      <td>API /customer/update s ử d ụng phương thứ c</td>
      <td>Rollback</td>
      <td>Tích h ợ p v ớ i API</td>
    </tr>
  </tbody>
</table>
<!-- image -->

tin                     <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>PATCH để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th>khi l ỗ i</th>
      <th>Gateway</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/ivr/callflow</td>
      <td>POST</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c POST để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>DELETE</td>
      <td>C ậ p nh ậ t c ấ u hình</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c DELETE để C ậ p nh ậ t c ấ u hình, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>DELETE</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /customer/update s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PATCH</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /customer/update s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Theo chu ẩ n RESTful</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>POST</td>
      <td>Export d ữ</td>
      <td>API /security/firewall/config s ử d ụng phương thứ c</td>
      <td>Log đầ y đủ</td>
      <td>Tích h ợ p v ớ i API</td>
    </tr>
  </tbody>
</table>
<!-- image -->

li ệ u                  <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>POST để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</th>
      <th></th>
      <th>Gateway</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/crm/lead/import</td>
      <td>DELETE</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c DELETE để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>Ki ể m tra tr ạ ng thái</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Log đầ y đủ</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PUT</td>
      <td>Export d ữ li ệ u</td>
      <td>API /customer/update s ử d ụng phương thứ c PUT để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>GET</td>
      <td>Export d ữ li ệ u</td>
      <td>API /invoice/export s ử d ụng phương thứ c GET để Export d ữ li ệ u, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thông báo s ự ki ệ n qua Kafka</td>
      <td>Gi ớ i h ạ n rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>POST</td>
      <td>Thêm b ả n ghi</td>
      <td>API /customer/update s ử d ụng phương thứ c POST để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>H ỗ tr ợ JSON và XML</td>
    </tr>
  </tbody>
</table>
<!-- image -->

d ị ch chi ti ế t.                                                                                                               <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/crm/lead/import</td>
      <td>DELETE</td>
      <td>Xóa thông tin</td>
      <td>API /crm/lead/import s ử d ụng phương thứ c DELETE để Xóa thông tin, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Thành công <1s</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>GET</td>
      <td>Thêm b ả n ghi</td>
      <td>API /rpa/task/execute s ử d ụng phương thứ c GET để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>POST</td>
      <td>Thêm b ả n ghi</td>
      <td>API /ivr/callflow s ử d ụng phương thứ c POST để Thêm b ả n ghi, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t.</td>
      <td>Retry t ố i đa 3 lầ n</td>
      <td>Tích h ợ p v ớ i API Gateway</td>
    </tr>
  </tbody>
</table>| /customer/update  | PATCH  | Ki ể m tra tr ạ ng thái | API /customer/update s ử d ụng phương thứ c PATCH để Ki ể mtra tr ạ ng thái, có xác th ự c OAuth2 và log giao d ị ch chi ti ế t. | Thành công <1s        | H ỗ tr ợ JSON và XML         |