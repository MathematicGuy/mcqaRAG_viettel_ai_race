<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Module</th>
      <th>Lo ạ i log</th>
      <th>M ức độ</th>
      <th>Hành độ ng</th>
      <th>Mô t ả chi ti ế t</th>
      <th>K ế t qu ả</th>
      <th>Ghi chú</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>RPA</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng RPA Xu ấ t log lo ạ i TransactionLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng CRM Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>PerformanceLog</td>
      <td>Error</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng Billing Phân tích log lo ạ i PerformanceLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng Infra Xóa log lo ạ i TransactionLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AuditLog</td>
      <td>Warning</td>
      <td>Xu ấ t</td>
      <td>H ệ th ố ng QA Xu ấ t</td>
      <td>Không</td>
      <td>Có dashboard</td>
    </tr>
  </tbody>
</table>
<!-- image -->

log                 <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>log lo ạ i AuditLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</th>
      <th>m ấ t mát d ữ li ệ u</th>
      <th>Grafana</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>IPCC</td>
      <td>PerformanceLog</td>
      <td>Fatal</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng IPCC Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>ErrorLog</td>
      <td>Info</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng IPCC Xóa log lo ạ i ErrorLog v ớ im ứ c Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>ErrorLog</td>
      <td>Warning</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng Billing Xóa log lo ạ i ErrorLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>AuditLog</td>
      <td>Error</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng CRM G ử i log sang SIEM lo ạ i AuditLog v ớ i m ứ c Error, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AuditLog</td>
      <td>Error</td>
      <td>G ử i log</td>
      <td>H ệ th ố ng Infra G ử i log sang SIEM lo ạ i</td>
      <td>Không m ấ t mát</td>
      <td>Theo chu ẩ n syslog</td>
    </tr>
  </tbody>
</table>
<!-- image -->

sang SIEM           <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>AuditLog v ớ im ứ c Error, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</th>
      <th>d ữ li ệ u</th>
      <th>RFC5424</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>RPA</td>
      <td>PerformanceLog</td>
      <td>Fatal</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng RPA Xu ấ t log lo ạ i PerformanceLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AccessLog</td>
      <td>Info</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng QA Nén và lưu trữ log lo ạ i AccessLog v ớ i m ứ c Info, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>ErrorLog</td>
      <td>Info</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng Billing Xu ấ t log lo ạ i ErrorLog v ớ im ứ c Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng IVR Xóa log lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>PerformanceLog</td>
      <td>Error</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng IVR Xóa log lo ạ i PerformanceLog</td>
      <td>Có ch ỉ s ố th ố ng</td>
      <td>G ử i log sang ELK</td>
    </tr>
  </tbody>
</table>
<!-- image -->

v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                                                       <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>kê</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>IPCC</td>
      <td>AuditLog</td>
      <td>Error</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng IPCC Nén và lưu trữ log lo ạ i AuditLog v ớ i m ứ c Error, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AccessLog</td>
      <td>Warning</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng Infra Xu ấ t log lo ạ i AccessLog v ớ i m ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AccessLog</td>
      <td>Warning</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng QA Nén và lưu trữ log lo ạ i AccessLog v ớ i m ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>ErrorLog</td>
      <td>Critical</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng Infra Xu ấ t log lo ạ i ErrorLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AuditLog</td>
      <td>Error</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng QA Xóa log lo ạ i AuditLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i</td>
      <td>Tích h ợ p c ả nh báo</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>thi ể u 90 ngày.</th>
      <th>realtime</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CRM</td>
      <td>AuditLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng CRM Xóa log lo ạ i AuditLog v ớ im ứ c Fatal, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>PerformanceLog</td>
      <td>Warning</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng CRM Xu ấ t log lo ạ i PerformanceLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng Infra Xu ấ t log lo ạ i TransactionLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng IPCC Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>PerformanceLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng IPCC Xóa log lo ạ i PerformanceLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>thi ể u 90 ngày.</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Billing</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng Billing Phân tích log lo ạ i AccessLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>ErrorLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng RPA Xóa log lo ạ i ErrorLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>TransactionLog</td>
      <td>Info</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng Infra Xu ấ t log lo ạ i TransactionLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>ErrorLog</td>
      <td>Warning</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng IVR Xu ấ t log lo ạ i ErrorLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AuditLog</td>
      <td>Warning</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng QA G ử i log sang SIEM lo ạ i AuditLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>PerformanceLog</td>
      <td>Critical</td>
      <td>Phân</td>
      <td>H ệ th ố ng Infra</td>
      <td>Có ch ỉ</td>
      <td>Theo chu ẩ n</td>
    </tr>
  </tbody>
</table>
<!-- image -->

tích log            <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Phân tích log lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</th>
      <th>s ố th ố ng kê</th>
      <th>syslog RFC5424</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>QA</td>
      <td>AuditLog</td>
      <td>Critical</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng QA Xu ấ t log lo ạ i AuditLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng IPCC Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>PerformanceLog</td>
      <td>Critical</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng RPA Phân tích log lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AuditLog</td>
      <td>Info</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng Infra Xóa log lo ạ i AuditLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>ErrorLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng RPA Xóa log lo ạ i ErrorLog v ớ im ứ c Fatal, d ữ</td>
      <td>Tích h ợ p c ả nh</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
  </tbody>
</table>
<!-- image -->

li ệu lưu trữ t ố i thi ể u 90 ngày.                                                                                    <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>báo realtime</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Billing</td>
      <td>ErrorLog</td>
      <td>Info</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng Billing G ử i log sang SIEM lo ạ i ErrorLog v ớ i m ứ c Info, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>PerformanceLog</td>
      <td>Critical</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng CRM G ử i log sang SIEM lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng Billing Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng CRM Phân tích log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>AuditLog</td>
      <td>Critical</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng IVR Xu ấ t log lo ạ i AuditLog v ớ im ứ c Critical,</td>
      <td>Không m ấ t mát</td>
      <td>G ử i log sang ELK</td>
    </tr>
  </tbody>
</table>
<!-- image -->

d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                                                                                <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>d ữ li ệ u</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CRM</td>
      <td>ErrorLog</td>
      <td>Info</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng CRM Xu ấ t log lo ạ i ErrorLog v ớ im ứ c Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>ErrorLog</td>
      <td>Fatal</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng IPCC Phân tích log lo ạ i ErrorLog v ớ im ứ c Fatal, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AuditLog</td>
      <td>Error</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng QA Nén và lưu trữ log lo ạ i AuditLog v ớ im ứ c Error, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng CRM G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>ErrorLog</td>
      <td>Warning</td>
      <td>Nén và lưu tr ữ</td>
      <td>H ệ th ố ng Infra Nén và lưu trữ log lo ạ i ErrorLog v ớ im ứ c Warning, d ữ li ệ u</td>
      <td>Log đượ c mã hóa AES-</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>log</th>
      <th>lưu trữ t ố i thi ể u 90 ngày.</th>
      <th>256</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>RPA</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng RPA G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>ErrorLog</td>
      <td>Error</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng QA Xu ấ t log lo ạ i ErrorLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AccessLog</td>
      <td>Info</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng QA Xu ấ t log lo ạ i AccessLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng CRM G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>PerformanceLog</td>
      <td>Warning</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng Billing Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>Có dashboard Grafana</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>thi ể u 90 ngày.</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>IPCC</td>
      <td>AccessLog</td>
      <td>Error</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng IPCC G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Error, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AuditLog</td>
      <td>Warning</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng Billing Xu ấ t log lo ạ i AuditLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AuditLog</td>
      <td>Error</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng Billing Xu ấ t log lo ạ i AuditLog v ớ im ứ c Error, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng Billing Nén và lưu trữ log lo ạ i AccessLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>AccessLog</td>
      <td>Warning</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng CRM Nén và lưu trữ log lo ạ i AccessLog v ớ i m ứ c Warning, d ữ li ệu lưu trữ t ố i</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>thi ể u 90 ngày.</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Infra</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng Infra Phân tích log lo ạ i AccessLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>TransactionLog</td>
      <td>Info</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng IPCC Xóa log lo ạ i TransactionLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AccessLog</td>
      <td>Error</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng QA Nén và lưu trữ log lo ạ i AccessLog v ớ i m ứ c Error, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>ErrorLog</td>
      <td>Error</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng IPCC Phân tích log lo ạ i ErrorLog v ớ im ứ c Error, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>ErrorLog</td>
      <td>Critical</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng Infra Phân tích log lo ạ i ErrorLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>ngày.</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>IVR</td>
      <td>AccessLog</td>
      <td>Warning</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng IVR Phân tích log lo ạ i AccessLog v ớ i m ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng IVR Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>ErrorLog</td>
      <td>Error</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng QA G ử i log sang SIEM lo ạ i ErrorLog v ớ im ứ c Error, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng RPA Phân tích log lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng Billing G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>ngày.</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CRM</td>
      <td>TransactionLog</td>
      <td>Info</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng CRM Phân tích log lo ạ i TransactionLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>ErrorLog</td>
      <td>Info</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng Billing Nén và lưu trữ log lo ạ i ErrorLog v ớ i m ứ c Info, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng RPA Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>ErrorLog</td>
      <td>Info</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng Infra Xóa log lo ạ i ErrorLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>ErrorLog</td>
      <td>Info</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng IVR Nén và lưu trữ log lo ạ i ErrorLog v ớ im ứ c Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>IPCC</th>
      <th>AuditLog</th>
      <th>Error</th>
      <th>G ử i log sang SIEM</th>
      <th>H ệ th ố ng IPCC G ử i log sang SIEM lo ạ i AuditLog v ớ i m ứ c Error, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</th>
      <th>Tích h ợ p c ả nh báo realtime</th>
      <th>Phân quy ề n chi ti ế t</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>QA</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng QA G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AuditLog</td>
      <td>Warning</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng Infra Xóa log lo ạ i AuditLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>ErrorLog</td>
      <td>Warning</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng IVR G ử i log sang SIEM lo ạ i ErrorLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>AuditLog</td>
      <td>Fatal</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng IVR Xu ấ t log lo ạ i AuditLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>PerformanceLog</td>
      <td>Info</td>
      <td>Nén và lưu</td>
      <td>H ệ th ố ng Infra Nén và lưu trữ log lo ạ i PerformanceLog</td>
      <td>Không m ấ t mát</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>tr ữ log</th>
      <th>v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</th>
      <th>d ữ li ệ u</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Billing</td>
      <td>PerformanceLog</td>
      <td>Error</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng Billing Xu ấ t log lo ạ i PerformanceLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng CRM Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng QA Xu ấ t log lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng RPA G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>Phân tích</td>
      <td>H ệ th ố ng QA Phân tích log lo ạ i TransactionLog</td>
      <td>Có ch ỉ s ố th ố ng</td>
      <td>Theo chu ẩ n syslog</td>
    </tr>
  </tbody>
</table>
<!-- image -->

log                 <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</th>
      <th>kê</th>
      <th>RFC5424</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CRM</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng CRM G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>PerformanceLog</td>
      <td>Critical</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng Billing Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng QA Xu ấ t log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AccessLog</td>
      <td>Info</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng Billing Xóa log lo ạ i AccessLog v ớ i m ứ c Info, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>AuditLog</td>
      <td>Warning</td>
      <td>Nén và lưu</td>
      <td>H ệ th ố ng CRM Nén và lưu trữ log lo ạ i AuditLog v ớ i</td>
      <td>Có ch ỉ s ố th ố ng</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
  </tbody>
</table>
<!-- image -->

tr ữ log            <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>m ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</th>
      <th>kê</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Billing</td>
      <td>AccessLog</td>
      <td>Info</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng Billing Xóa log lo ạ i AccessLog v ớ i m ứ c Info, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>AccessLog</td>
      <td>Error</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng IVR Xóa log lo ạ i AccessLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>AccessLog</td>
      <td>Error</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng IVR Xóa log lo ạ i AccessLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>TransactionLog</td>
      <td>Info</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng Billing Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng Billing Xóa log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i</td>
      <td>Log đượ c mã hóa AES-</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>thi ể u 90 ngày.</th>
      <th>256</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Infra</td>
      <td>AccessLog</td>
      <td>Info</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng Infra Xóa log lo ạ i AccessLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>ErrorLog</td>
      <td>Critical</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng RPA Xóa log lo ạ i ErrorLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>TransactionLog</td>
      <td>Warning</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng Billing Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>PerformanceLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng Infra Xóa log lo ạ i PerformanceLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>TransactionLog</td>
      <td>Warning</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng Infra G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>IPCC</th>
      <th>PerformanceLog</th>
      <th>Critical</th>
      <th>Nén và lưu tr ữ log</th>
      <th>H ệ th ố ng IPCC Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</th>
      <th>Tích h ợ p c ả nh báo realtime</th>
      <th>Phân quy ề n chi ti ế t</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>IPCC</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng IPCC G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng RPA G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>AccessLog</td>
      <td>Critical</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng IVR Phân tích log lo ạ i AccessLog v ớ i m ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AuditLog</td>
      <td>Critical</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng Billing Xóa log lo ạ i AuditLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>G ử i log sang ELK</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>ngày.</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>QA</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng QA G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>TransactionLog</td>
      <td>Info</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng Billing G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AccessLog</td>
      <td>Warning</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng Billing Nén và lưu trữ log lo ạ i AccessLog v ớ i m ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>ErrorLog</td>
      <td>Error</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng IPCC Xóa log lo ạ i ErrorLog v ớ im ứ c Error, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng RPA Phân tích log lo ạ i TransactionLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>G ử i log sang ELK</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>thi ể u 90 ngày.</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Billing</td>
      <td>AuditLog</td>
      <td>Error</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng Billing Phân tích log lo ạ i AuditLog v ớ im ứ c Error, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>TransactionLog</td>
      <td>Info</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng QA Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>AuditLog</td>
      <td>Info</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng CRM Phân tích log lo ạ i AuditLog v ớ im ứ c Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>TransactionLog</td>
      <td>Warning</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng QA Phân tích log lo ạ i TransactionLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng Billing Xu ấ t log lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>G ử i log sang ELK</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>thi ể u 90 ngày.</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Infra</td>
      <td>AccessLog</td>
      <td>Warning</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng Infra Xóa log lo ạ i AccessLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>TransactionLog</td>
      <td>Info</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng Billing G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>AccessLog</td>
      <td>Critical</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng CRM Nén và lưu trữ log lo ạ i AccessLog v ớ i m ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>ErrorLog</td>
      <td>Warning</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng QA Xóa log lo ạ i ErrorLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng Infra Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>IPCC</th>
      <th>AuditLog</th>
      <th>Error</th>
      <th>Nén và lưu tr ữ log</th>
      <th>H ệ th ố ng IPCC Nén và lưu trữ log lo ạ i AuditLog v ớ i m ứ c Error, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</th>
      <th>Có th ể truy xu ấ t khi c ầ n</th>
      <th>G ử i log sang ELK</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>QA</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng QA Nén và lưu trữ log lo ạ i AccessLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>PerformanceLog</td>
      <td>Error</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng CRM G ử i log sang SIEM lo ạ i PerformanceLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng RPA Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>AuditLog</td>
      <td>Warning</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng CRM Phân tích log lo ạ i AuditLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Infra</th>
      <th>ErrorLog</th>
      <th>Critical</th>
      <th>Nén và lưu tr ữ log</th>
      <th>H ệ th ố ng Infra Nén và lưu trữ log lo ạ i ErrorLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</th>
      <th>Không m ấ t mát d ữ li ệ u</th>
      <th>G ử i log sang ELK</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>RPA</td>
      <td>PerformanceLog</td>
      <td>Critical</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng RPA Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>AuditLog</td>
      <td>Warning</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng IPCC Phân tích log lo ạ i AuditLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AccessLog</td>
      <td>Info</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng Billing Xu ấ t log lo ạ i AccessLog v ớ i m ứ c Info, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AccessLog</td>
      <td>Warning</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng Billing Xu ấ t log lo ạ i AccessLog v ớ i m ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
  </tbody>
</table>
<!-- image -->

QA    <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>TransactionLog</th>
      <th>Warning</th>
      <th>Xu ấ t log</th>
      <th>H ệ th ố ng QA Xu ấ t log lo ạ i TransactionLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</th>
      <th>Có ch ỉ s ố th ố ng kê</th>
      <th>T ự độ ng xóa log sau 180 ngày</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>IVR</td>
      <td>AccessLog</td>
      <td>Warning</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng IVR G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>ErrorLog</td>
      <td>Warning</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng IVR Xóa log lo ạ i ErrorLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>AuditLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng IPCC Xóa log lo ạ i AuditLog v ớ im ứ c Fatal, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng Infra Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AuditLog</td>
      <td>Error</td>
      <td>Nén và</td>
      <td>H ệ th ố ng Infra Nén và lưu trữ log lo ạ i</td>
      <td>Tích h ợ p</td>
      <td>Theo chu ẩ n syslog</td>
    </tr>
  </tbody>
</table>
<!-- image -->

lưu tr ữ log        <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>AuditLog v ớ im ứ c Error, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</th>
      <th>c ả nh báo realtime</th>
      <th>RFC5424</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>IPCC</td>
      <td>PerformanceLog</td>
      <td>Critical</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng IPCC G ử i log sang SIEM lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>PerformanceLog</td>
      <td>Warning</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng Infra Phân tích log lo ạ i PerformanceLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng Infra Xóa log lo ạ i AccessLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>PerformanceLog</td>
      <td>Critical</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng QA Phân tích log lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>PerformanceLog</td>
      <td>Critical</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng Infra Xóa log lo ạ i PerformanceLog</td>
      <td>Có th ể truy xu ấ t khi</td>
      <td>Theo chu ẩ n syslog</td>
    </tr>
  </tbody>
</table>
<!-- image -->

v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                                                      <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>c ầ n</th>
      <th>RFC5424</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>QA</td>
      <td>PerformanceLog</td>
      <td>Fatal</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng QA Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>ErrorLog</td>
      <td>Warning</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng RPA Nén và lưu trữ log lo ạ i ErrorLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>ErrorLog</td>
      <td>Critical</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng IPCC Xóa log lo ạ i ErrorLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng QA Xóa log lo ạ i AccessLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>AuditLog</td>
      <td>Warning</td>
      <td>Nén và lưu tr ữ</td>
      <td>H ệ th ố ng RPA Nén và lưu trữ log lo ạ i AuditLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90</td>
      <td>Log đượ c mã hóa AES-</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>log</th>
      <th>ngày.</th>
      <th>256</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>QA</td>
      <td>AuditLog</td>
      <td>Fatal</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng QA G ử i log sang SIEM lo ạ i AuditLog v ớ im ứ c Fatal, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>PerformanceLog</td>
      <td>Warning</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng CRM G ử i log sang SIEM lo ạ i PerformanceLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng RPA G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AuditLog</td>
      <td>Warning</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng Billing Nén và lưu trữ log lo ạ i AuditLog v ớ i m ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>AuditLog</td>
      <td>Error</td>
      <td>Nén và lưu tr ữ</td>
      <td>H ệ th ố ng IPCC Nén và lưu trữ log lo ạ i AuditLog v ớ i m ứ c Error, d ữ li ệ u lưu trữ t ố i thi ể u 90</td>
      <td>Log đượ c mã hóa AES-</td>
      <td>G ử i log sang ELK</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>log</th>
      <th>ngày.</th>
      <th>256</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>IPCC</td>
      <td>PerformanceLog</td>
      <td>Warning</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng IPCC Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>TransactionLog</td>
      <td>Warning</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng IPCC G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>PerformanceLog</td>
      <td>Warning</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng IVR Phân tích log lo ạ i PerformanceLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AccessLog</td>
      <td>Critical</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng Infra Phân tích log lo ạ i AccessLog v ớ i m ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>PerformanceLog</td>
      <td>Warning</td>
      <td>Nén và lưu tr ữ</td>
      <td>H ệ th ố ng Billing Nén và lưu trữ log lo ạ i PerformanceLog</td>
      <td>Có th ể truy xu ấ t khi</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>log</th>
      <th>v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</th>
      <th>c ầ n</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>QA</td>
      <td>AccessLog</td>
      <td>Warning</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng QA G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>PerformanceLog</td>
      <td>Warning</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng QA G ử i log sang SIEM lo ạ i PerformanceLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>PerformanceLog</td>
      <td>Fatal</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng IPCC Xu ấ t log lo ạ i PerformanceLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng Infra G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>ErrorLog</td>
      <td>Error</td>
      <td>G ử i log sang</td>
      <td>H ệ th ố ng IPCC G ử i log sang SIEM lo ạ i ErrorLog v ớ i m ứ c Error, d ữ li ệ u</td>
      <td>Có th ể truy xu ấ t khi</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>SIEM</th>
      <th>lưu trữ t ố i thi ể u 90 ngày.</th>
      <th>c ầ n</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>IVR</td>
      <td>AuditLog</td>
      <td>Critical</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng IVR Nén và lưu trữ log lo ạ i AuditLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng Billing G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>PerformanceLog</td>
      <td>Critical</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng RPA Phân tích log lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng IPCC G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AuditLog</td>
      <td>Critical</td>
      <td>Nén và lưu tr ữ</td>
      <td>H ệ th ố ng Infra Nén và lưu trữ log lo ạ i AuditLog v ớ im ứ c Critical, d ữ li ệu lưu</td>
      <td>Tích h ợ p c ả nh báo</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>log</th>
      <th>tr ữ t ố i thi ể u 90 ngày.</th>
      <th>realtime</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Billing</td>
      <td>AccessLog</td>
      <td>Error</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng Billing Xóa log lo ạ i AccessLog v ớ i m ứ c Error, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AuditLog</td>
      <td>Critical</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng QA Xu ấ t log lo ạ i AuditLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>PerformanceLog</td>
      <td>Warning</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng QA G ử i log sang SIEM lo ạ i PerformanceLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>ErrorLog</td>
      <td>Error</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng Infra Xóa log lo ạ i ErrorLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>AccessLog</td>
      <td>Info</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng CRM Xóa log lo ạ i AccessLog v ớ i m ứ c Info, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
  </tbody>
</table>
<!-- image -->

IPCC   <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>AccessLog</th>
      <th>Fatal</th>
      <th>G ử i log sang SIEM</th>
      <th>H ệ th ố ng IPCC G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</th>
      <th>Tích h ợ p c ả nh báo realtime</th>
      <th>G ử i log sang ELK</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>QA</td>
      <td>AuditLog</td>
      <td>Fatal</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng QA Nén và lưu trữ log lo ạ i AuditLog v ớ im ứ c Fatal, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>ErrorLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng RPA Xóa log lo ạ i ErrorLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>TransactionLog</td>
      <td>Info</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng CRM Xu ấ t log lo ạ i TransactionLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>PerformanceLog</td>
      <td>Info</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng Infra Xu ấ t log lo ạ i PerformanceLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>TransactionLog</td>
      <td>Warning</td>
      <td>G ử i log</td>
      <td>H ệ th ố ng Infra G ử i log sang SIEM lo ạ i</td>
      <td>Tích h ợ p</td>
      <td>Theo chu ẩ n syslog</td>
    </tr>
  </tbody>
</table>
<!-- image -->

sang SIEM           <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>TransactionLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</th>
      <th>c ả nh báo realtime</th>
      <th>RFC5424</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>IVR</td>
      <td>AuditLog</td>
      <td>Warning</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng IVR Xu ấ t log lo ạ i AuditLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>ErrorLog</td>
      <td>Warning</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng Billing Xóa log lo ạ i ErrorLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>PerformanceLog</td>
      <td>Critical</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng IPCC Phân tích log lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>ErrorLog</td>
      <td>Error</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng RPA Nén và lưu trữ log lo ạ i ErrorLog v ớ im ứ c Error, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng RPA Xu ấ t log lo ạ i TransactionLog v ớ im ứ c Critical,</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Có dashboard Grafana</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>RPA</td>
      <td>AuditLog</td>
      <td>Critical</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng RPA Nén và lưu trữ log lo ạ i AuditLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>ErrorLog</td>
      <td>Fatal</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng QA Phân tích log lo ạ i ErrorLog v ớ im ứ c Fatal, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng RPA G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>ErrorLog</td>
      <td>Warning</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng RPA Phân tích log lo ạ i ErrorLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>PerformanceLog</td>
      <td>Info</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng CRM Xóa log lo ạ i PerformanceLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>thi ể u 90 ngày.</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Infra</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng Infra Nén và lưu trữ log lo ạ i AccessLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>ErrorLog</td>
      <td>Critical</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng IVR Phân tích log lo ạ i ErrorLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>PerformanceLog</td>
      <td>Error</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng Infra Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>TransactionLog</td>
      <td>Info</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng IPCC G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>ErrorLog</td>
      <td>Error</td>
      <td>Nén và lưu tr ữ</td>
      <td>H ệ th ố ng IPCC Nén và lưu trữ log lo ạ i ErrorLog v ớ i m ứ c Error, d ữ li ệ u lưu trữ t ố i thi ể u 90</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>log</th>
      <th>ngày.</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>RPA</td>
      <td>PerformanceLog</td>
      <td>Error</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng RPA G ử i log sang SIEM lo ạ i PerformanceLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>ErrorLog</td>
      <td>Critical</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng Infra Xóa log lo ạ i ErrorLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>PerformanceLog</td>
      <td>Critical</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng IVR G ử i log sang SIEM lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AuditLog</td>
      <td>Error</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng Infra G ử i log sang SIEM lo ạ i AuditLog v ớ im ứ c Error, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>ErrorLog</td>
      <td>Critical</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng IVR Xóa log lo ạ i ErrorLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>PerformanceLog</td>
      <td>Fatal</td>
      <td>Nén</td>
      <td>H ệ th ố ng QA Nén</td>
      <td>Có th ể</td>
      <td>T ự độ ng xóa</td>
    </tr>
  </tbody>
</table>
<!-- image -->

và lưu tr ữ log   <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</th>
      <th>truy xu ấ t khi c ầ n</th>
      <th>log sau 180 ngày</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>RPA</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng RPA Phân tích log lo ạ i TransactionLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>PerformanceLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng RPA Xóa log lo ạ i PerformanceLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>ErrorLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng Billing Xóa log lo ạ i ErrorLog v ớ im ứ c Fatal, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng RPA Xóa log lo ạ i AccessLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>AccessLog</td>
      <td>Warning</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng CRM Xu ấ t log lo ạ i AccessLog v ớ i</td>
      <td>Có th ể truy xu ấ t khi</td>
      <td>G ử i log sang ELK</td>
    </tr>
  </tbody>
</table>
<!-- image -->

m ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.                                                                <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>c ầ n</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>IVR</td>
      <td>PerformanceLog</td>
      <td>Warning</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng IVR G ử i log sang SIEM lo ạ i PerformanceLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>PerformanceLog</td>
      <td>Error</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng IPCC Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng QA Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AccessLog</td>
      <td>Error</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng QA Phân tích log lo ạ i AccessLog v ớ i m ứ c Error, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>AuditLog</td>
      <td>Info</td>
      <td>Phân tích</td>
      <td>H ệ th ố ng RPA Phân tích log lo ạ i AuditLog v ớ im ứ c</td>
      <td>Có th ể truy xu ấ t khi</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
  </tbody>
</table>
<!-- image -->

log                 <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</th>
      <th>c ầ n</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Billing</td>
      <td>ErrorLog</td>
      <td>Fatal</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng Billing Nén và lưu trữ log lo ạ i ErrorLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>TransactionLog</td>
      <td>Info</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng CRM Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng Billing Xóa log lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng CRM Xu ấ t log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AccessLog</td>
      <td>Warning</td>
      <td>G ử i log sang</td>
      <td>H ệ th ố ng Infra G ử i log sang SIEM lo ạ i AccessLog v ớ i</td>
      <td>Có ch ỉ s ố th ố ng</td>
      <td>Có dashboard Grafana</td>
    </tr>
  </tbody>
</table>
<!-- image -->

SIEM                <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>m ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</th>
      <th>kê</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>IPCC</td>
      <td>AuditLog</td>
      <td>Fatal</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng IPCC G ử i log sang SIEM lo ạ i AuditLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>TransactionLog</td>
      <td>Warning</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng CRM Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>AccessLog</td>
      <td>Error</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng IVR Xu ấ t log lo ạ i AccessLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng CRM Xóa log lo ạ i TransactionLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>Nén và lưu tr ữ</td>
      <td>H ệ th ố ng Infra Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>log</th>
      <th>li ệu lưu trữ t ố i thi ể u 90 ngày.</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>IPCC</td>
      <td>PerformanceLog</td>
      <td>Critical</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng IPCC Xu ấ t log lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng Billing Xóa log lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng Infra Xóa log lo ạ i AccessLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>TransactionLog</td>
      <td>Info</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng IPCC G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>AccessLog</td>
      <td>Error</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng IPCC Phân tích log lo ạ i AccessLog v ớ i m ứ c Error, d ữ li ệ u lưu trữ t ố i thi ể u 90</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>G ử i log sang ELK</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>ngày.</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Infra</td>
      <td>PerformanceLog</td>
      <td>Warning</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng Infra G ử i log sang SIEM lo ạ i PerformanceLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>PerformanceLog</td>
      <td>Warning</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng IPCC G ử i log sang SIEM lo ạ i PerformanceLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AccessLog</td>
      <td>Error</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng Billing Nén và lưu trữ log lo ạ i AccessLog v ớ i m ứ c Error, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>PerformanceLog</td>
      <td>Info</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng Billing G ử i log sang SIEM lo ạ i PerformanceLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>ErrorLog</td>
      <td>Fatal</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng CRM Xu ấ t log lo ạ i ErrorLog v ớ im ứ c Fatal, d ữ li ệu lưu</td>
      <td>Có ch ỉ s ố th ố ng</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>tr ữ t ố i thi ể u 90 ngày.</th>
      <th>kê</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Billing</td>
      <td>ErrorLog</td>
      <td>Critical</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng Billing Nén và lưu trữ log lo ạ i ErrorLog v ớ i m ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>ErrorLog</td>
      <td>Critical</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng CRM Phân tích log lo ạ i ErrorLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AuditLog</td>
      <td>Fatal</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng QA G ử i log sang SIEM lo ạ i AuditLog v ớ im ứ c Fatal, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>PerformanceLog</td>
      <td>Fatal</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng QA Phân tích log lo ạ i PerformanceLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng Infra Xu ấ t log lo ạ i TransactionLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>thi ể u 90 ngày.</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CRM</td>
      <td>AuditLog</td>
      <td>Critical</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng CRM Phân tích log lo ạ i AuditLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AuditLog</td>
      <td>Warning</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng Billing Xu ấ t log lo ạ i AuditLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>AccessLog</td>
      <td>Warning</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng IPCC Phân tích log lo ạ i AccessLog v ớ i m ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>PerformanceLog</td>
      <td>Critical</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng Billing Xu ấ t log lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>AuditLog</td>
      <td>Critical</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng RPA Xu ấ t log lo ạ i AuditLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>Có dashboard Grafana</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>ngày.</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CRM</td>
      <td>AuditLog</td>
      <td>Critical</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng CRM Nén và lưu trữ log lo ạ i AuditLog v ớ i m ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>AuditLog</td>
      <td>Info</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng RPA Xu ấ t log lo ạ i AuditLog v ớ im ứ c Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>ErrorLog</td>
      <td>Critical</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng RPA Xu ấ t log lo ạ i ErrorLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>ErrorLog</td>
      <td>Error</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng RPA Xu ấ t log lo ạ i ErrorLog v ớ im ứ c Error, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AuditLog</td>
      <td>Critical</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng QA Xóa log lo ạ i AuditLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>IVR</th>
      <th>AccessLog</th>
      <th>Info</th>
      <th>G ử i log sang SIEM</th>
      <th>H ệ th ố ng IVR G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Info, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</th>
      <th>Có th ể truy xu ấ t khi c ầ n</th>
      <th>Phân quy ề n chi ti ế t</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>QA</td>
      <td>TransactionLog</td>
      <td>Warning</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng QA G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AccessLog</td>
      <td>Critical</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng Infra Phân tích log lo ạ i AccessLog v ớ i m ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>ErrorLog</td>
      <td>Info</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng RPA G ử i log sang SIEM lo ạ i ErrorLog v ớ im ứ c Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>AccessLog</td>
      <td>Warning</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng CRM G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Có dashboard Grafana</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>RPA</th>
      <th>TransactionLog</th>
      <th>Error</th>
      <th>Xóa log</th>
      <th>H ệ th ố ng RPA Xóa log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</th>
      <th>Không m ấ t mát d ữ li ệ u</th>
      <th>Phân quy ề n chi ti ế t</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>RPA</td>
      <td>ErrorLog</td>
      <td>Fatal</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng RPA G ử i log sang SIEM lo ạ i ErrorLog v ớ im ứ c Fatal, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>AuditLog</td>
      <td>Critical</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng RPA Xóa log lo ạ i AuditLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>ErrorLog</td>
      <td>Warning</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng CRM Nén và lưu trữ log lo ạ i ErrorLog v ớ i m ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>TransactionLog</td>
      <td>Info</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng Infra Xóa log lo ạ i TransactionLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>PerformanceLog</td>
      <td>Info</td>
      <td>Nén và</td>
      <td>H ệ th ố ng Billing Nén và lưu trữ log</td>
      <td>Không m ấ t mát</td>
      <td>G ử i log sang</td>
    </tr>
  </tbody>
</table>
<!-- image -->

lưu tr ữ log   <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>lo ạ i PerformanceLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</th>
      <th>d ữ li ệ u</th>
      <th>ELK</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Infra</td>
      <td>PerformanceLog</td>
      <td>Fatal</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng Infra Phân tích log lo ạ i PerformanceLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng IPCC Xóa log lo ạ i TransactionLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>PerformanceLog</td>
      <td>Error</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng IPCC Xóa log lo ạ i PerformanceLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>ErrorLog</td>
      <td>Warning</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng Billing Xóa log lo ạ i ErrorLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>ErrorLog</td>
      <td>Fatal</td>
      <td>G ử i log</td>
      <td>H ệ th ố ng IVR G ử i log sang SIEM lo ạ i</td>
      <td>Log đượ c</td>
      <td>Có dashboard</td>
    </tr>
  </tbody>
</table>
<!-- image -->

sang SIEM           <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>ErrorLog v ớ im ứ c Fatal, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</th>
      <th>mã hóa AES- 256</th>
      <th>Grafana</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CRM</td>
      <td>PerformanceLog</td>
      <td>Error</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng CRM Xu ấ t log lo ạ i PerformanceLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng Billing Xóa log lo ạ i TransactionLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>ErrorLog</td>
      <td>Fatal</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng QA Phân tích log lo ạ i ErrorLog v ớ im ứ c Fatal, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AuditLog</td>
      <td>Fatal</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng Infra G ử i log sang SIEM lo ạ i AuditLog v ớ im ứ c Fatal, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AuditLog</td>
      <td>Critical</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng QA Xu ấ t log lo ạ i AuditLog v ớ im ứ c Critical,</td>
      <td>Có ch ỉ s ố th ố ng</td>
      <td>Theo chu ẩ n syslog</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</th>
      <th>kê</th>
      <th>RFC5424</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>QA</td>
      <td>PerformanceLog</td>
      <td>Error</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng QA G ử i log sang SIEM lo ạ i PerformanceLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>TransactionLog</td>
      <td>Info</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng Infra Xóa log lo ạ i TransactionLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>PerformanceLog</td>
      <td>Fatal</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng IVR Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>TransactionLog</td>
      <td>Info</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng CRM Xóa log lo ạ i TransactionLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>AccessLog</td>
      <td>Critical</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng CRM Phân tích log lo ạ i AccessLog v ớ i m ứ c Critical, d ữ li ệu lưu trữ t ố i</td>
      <td>Log đượ c mã hóa AES-</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>thi ể u 90 ngày.</th>
      <th>256</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>RPA</td>
      <td>AccessLog</td>
      <td>Error</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng RPA Xóa log lo ạ i AccessLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>AuditLog</td>
      <td>Info</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng RPA Xu ấ t log lo ạ i AuditLog v ớ im ứ c Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>ErrorLog</td>
      <td>Warning</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng Infra Phân tích log lo ạ i ErrorLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>PerformanceLog</td>
      <td>Info</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng CRM Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AuditLog</td>
      <td>Error</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng Billing Nén và lưu trữ log lo ạ i AuditLog v ớ i m ứ c Error, d ữ li ệ u lưu trữ t ố i thi ể u 90</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>ngày.</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>IVR</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng IVR Phân tích log lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng QA Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AuditLog</td>
      <td>Warning</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng Infra Xu ấ t log lo ạ i AuditLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>PerformanceLog</td>
      <td>Info</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng IPCC Phân tích log lo ạ i PerformanceLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>PerformanceLog</td>
      <td>Critical</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng IVR Phân tích log lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>thi ể u 90 ngày.</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Infra</td>
      <td>ErrorLog</td>
      <td>Critical</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng Infra Nén và lưu trữ log lo ạ i ErrorLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>ErrorLog</td>
      <td>Info</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng QA G ử i log sang SIEM lo ạ i ErrorLog v ớ im ứ c Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>ErrorLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng IVR Xóa log lo ạ i ErrorLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>ErrorLog</td>
      <td>Info</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng Billing G ử i log sang SIEM lo ạ i ErrorLog v ớ i m ứ c Info, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng Infra Xóa log lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Billing</th>
      <th>TransactionLog</th>
      <th>Fatal</th>
      <th>Xu ấ t log</th>
      <th>H ệ th ố ng Billing Xu ấ t log lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</th>
      <th>Không m ấ t mát d ữ li ệ u</th>
      <th>G ử i log sang ELK</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>IPCC</td>
      <td>ErrorLog</td>
      <td>Warning</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng IPCC Xóa log lo ạ i ErrorLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>AccessLog</td>
      <td>Error</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng IVR G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Error, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>PerformanceLog</td>
      <td>Fatal</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng Infra Phân tích log lo ạ i PerformanceLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AuditLog</td>
      <td>Error</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng Infra G ử i log sang SIEM lo ạ i AuditLog v ớ im ứ c Error, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Infra</th>
      <th>AccessLog</th>
      <th>Warning</th>
      <th>Xóa log</th>
      <th>H ệ th ố ng Infra Xóa log lo ạ i AccessLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</th>
      <th>Có ch ỉ s ố th ố ng kê</th>
      <th>G ử i log sang ELK</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>IVR</td>
      <td>ErrorLog</td>
      <td>Error</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng IVR G ử i log sang SIEM lo ạ i ErrorLog v ớ im ứ c Error, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>ErrorLog</td>
      <td>Info</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng Infra Nén và lưu trữ log lo ạ i ErrorLog v ớ im ứ c Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng QA Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>AccessLog</td>
      <td>Info</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng RPA Xóa log lo ạ i AccessLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>ErrorLog</td>
      <td>Error</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng RPA Xu ấ t log lo ạ i ErrorLog v ớ im ứ c</td>
      <td>Có ch ỉ s ố th ố ng</td>
      <td>Theo chu ẩ n syslog</td>
    </tr>
  </tbody>
</table>
<!-- image -->

Error, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.                                                                         <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>kê</th>
      <th>RFC5424</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Infra</td>
      <td>ErrorLog</td>
      <td>Critical</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng Infra Nén và lưu trữ log lo ạ i ErrorLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng IPCC G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>PerformanceLog</td>
      <td>Info</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng Infra G ử i log sang SIEM lo ạ i PerformanceLog v ớ im ứ c Info, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>PerformanceLog</td>
      <td>Fatal</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng RPA Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AuditLog</td>
      <td>Critical</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng Billing Xu ấ t log lo ạ i AuditLog v ớ im ứ c</td>
      <td>Có ch ỉ s ố th ố ng</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
  </tbody>
</table>
<!-- image -->

Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.                                                            <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>kê</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>IVR</td>
      <td>AuditLog</td>
      <td>Info</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng IVR G ử i log sang SIEM lo ạ i AuditLog v ớ im ứ c Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>AuditLog</td>
      <td>Warning</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng RPA Xu ấ t log lo ạ i AuditLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>AuditLog</td>
      <td>Info</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng IPCC Phân tích log lo ạ i AuditLog v ớ im ứ c Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng IVR Xu ấ t log lo ạ i AccessLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>ErrorLog</td>
      <td>Warning</td>
      <td>Nén và lưu tr ữ</td>
      <td>H ệ th ố ng RPA Nén và lưu trữ log lo ạ i ErrorLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90</td>
      <td>Tích h ợ p c ả nh báo</td>
      <td>G ử i log sang ELK</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>log</th>
      <th>ngày.</th>
      <th>realtime</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>QA</td>
      <td>AuditLog</td>
      <td>Warning</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng QA Xóa log lo ạ i AuditLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>ErrorLog</td>
      <td>Info</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng IPCC Phân tích log lo ạ i ErrorLog v ớ im ứ c Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>ErrorLog</td>
      <td>Warning</td>
      <td>Phân tích log</td>
      <td>H ệ th ố ng IVR Phân tích log lo ạ i ErrorLog v ớ im ứ c Warning, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>TransactionLog</td>
      <td>Warning</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng Infra Xu ấ t log lo ạ i TransactionLog v ớ im ứ c Warning, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng RPA G ử i log sang SIEM lo ạ i AccessLog v ớ i m ứ c Fatal, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>G ử i log sang ELK</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>CRM</th>
      <th>ErrorLog</th>
      <th>Fatal</th>
      <th>Xóa log</th>
      <th>H ệ th ố ng CRM Xóa log lo ạ i ErrorLog v ớ im ứ c Fatal, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</th>
      <th>Log đượ c mã hóa AES- 256</th>
      <th>T ự độ ng xóa log sau 180 ngày</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>IPCC</td>
      <td>ErrorLog</td>
      <td>Critical</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng IPCC Xu ấ t log lo ạ i ErrorLog v ớ im ứ c Critical, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Không m ấ t mát d ữ li ệ u</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>AuditLog</td>
      <td>Info</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng RPA Nén và lưu trữ log lo ạ i AuditLog v ớ im ứ c Info, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Có th ể truy xu ấ t khi c ầ n</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>PerformanceLog</td>
      <td>Critical</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng Billing Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>G ử i log sang ELK</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AccessLog</td>
      <td>Critical</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng Infra Xu ấ t log lo ạ i AccessLog v ớ i m ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Phân quy ề n chi ti ế t</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>IVR</th>
      <th>AccessLog</th>
      <th>Critical</th>
      <th>Xu ấ t log</th>
      <th>H ệ th ố ng IVR Xu ấ t log lo ạ i AccessLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</th>
      <th>Không m ấ t mát d ữ li ệ u</th>
      <th>G ử i log sang ELK</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Billing</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng Billing G ử i log sang SIEM lo ạ i TransactionLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Log đượ c mã hóa AES- 256</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>AccessLog</td>
      <td>Info</td>
      <td>Xu ấ t log</td>
      <td>H ệ th ố ng CRM Xu ấ t log lo ạ i AccessLog v ớ i m ứ c Info, d ữ li ệ u lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>PerformanceLog</td>
      <td>Critical</td>
      <td>Xóa log</td>
      <td>H ệ th ố ng CRM Xóa log lo ạ i PerformanceLog v ớ im ứ c Critical, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Tích h ợ p c ả nh báo realtime</td>
      <td>Theo chu ẩ n syslog RFC5424</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>PerformanceLog</td>
      <td>Fatal</td>
      <td>Nén và lưu tr ữ log</td>
      <td>H ệ th ố ng CRM Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>T ự độ ng xóa log sau 180 ngày</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## BÁO CÁO H Ệ TH Ố NG &amp; LOG

TD449

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Billing</th>
      <th>TransactionLog</th>
      <th>Fatal</th>
      <th>Nén và lưu tr ữ log</th>
      <th>H ệ th ố ng Billing Nén và lưu trữ log lo ạ i TransactionLog v ớ im ứ c Fatal, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.</th>
      <th>Không m ấ t mát d ữ li ệ u</th>
      <th>T ự độ ng xóa log sau 180 ngày</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Infra</td>
      <td>AuditLog</td>
      <td>Fatal</td>
      <td>G ử i log sang SIEM</td>
      <td>H ệ th ố ng Infra G ử i log sang SIEM lo ạ i AuditLog v ớ im ứ c Fatal, d ữ li ệu lưu tr ữ t ố i thi ể u 90 ngày.</td>
      <td>Có ch ỉ s ố th ố ng kê</td>
      <td>Có dashboard Grafana</td>
    </tr>
  </tbody>
</table>| CRM       | PerformanceLog   | Error   | Nén và lưu tr ữ log   | H ệ th ố ng CRM Nén và lưu trữ log lo ạ i PerformanceLog v ớ im ứ c Error, d ữ li ệu lưu trữ t ố i thi ể u 90 ngày.       | Tích h ợ p c ả nh báo realtime | Theo chu ẩ n syslog RFC5424      |