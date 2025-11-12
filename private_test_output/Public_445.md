<!-- image -->

Nghi ệ p v ụ   <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Lo ạ i ch ỉ tiêu</th>
      <th>Hành độ ng</th>
      <th>API/Action</th>
      <th>Mô t ả chi ti ế t</th>
      <th>Phương pháp đo</th>
      <th>K ế t qu ả mong mu ố n</th>
      <th>Ghi chú</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Xóa</td>
      <td>/crm/lead/add</td>
      <td>Xóa d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/lead/export</td>
      <td>G ắ n th ẻ d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

và ghi log đầ y đủ .                                                                                                            <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>trướ c khi t ả i.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Xóa</td>
      <td>/crm/lead/export</td>
      <td>Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/lead/export</td>
      <td>G ắ n th ẻ d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/lead/add</td>
      <td>C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Không l ỗ i, log đầy đủ trong</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                             <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>AuditLog, SLA đáp ứ ng 99.99%.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Xóa</td>
      <td>/crm/campaign/import</td>
      <td>Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/lead/add</td>
      <td>Chuy ển đổ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

và ghi log đầ y đủ .                                                                                                            <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Import</td>
      <td>/crm/campaign/import</td>
      <td>Import d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/campaign/import</td>
      <td>Chuy ển đổ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Lead</th>
      <th>Ch ỉ tiêu ch ứ c năng</th>
      <th>Chuy ể n đổ i</th>
      <th>/crm/opportunity/delete</th>
      <th>Chuy ển đổ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử ch ứ c năng</th>
      <th>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</th>
      <th>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/campaign/import</td>
      <td>Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Export</td>
      <td>/crm/contact/update</td>
      <td>Export d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                             <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>b ộ sang h ệ th ố ng Billing.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/contact/update</td>
      <td>G ắ n th ẻ d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/contact/update</td>
      <td>C ậ p nh ậ t d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Lead</th>
      <th>Ch ỉ tiêu ch ứ c năng</th>
      <th>Chuy ể n đổ i</th>
      <th>/crm/contact/update</th>
      <th>Chuy ển đổ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử b ả o m ậ t</th>
      <th>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</th>
      <th>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/lead/add</td>
      <td>Chuy ển đổ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Import</td>
      <td>/crm/opportunity/delete</td>
      <td>Import d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                   <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>hai l ớ p trướ c khi t ả i.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Xóa</td>
      <td>/crm/contact/update</td>
      <td>Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Xóa</td>
      <td>/crm/lead/export</td>
      <td>Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Campaign</th>
      <th>Ch ỉ tiêu ch ứ c năng</th>
      <th>Xóa</th>
      <th>/crm/opportunity/delete</th>
      <th>Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử hi ệ u năng</th>
      <th>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</th>
      <th>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Import</td>
      <td>/crm/lead/add</td>
      <td>Import d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/lead/add</td>
      <td>G ắ n th ẻ d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog,</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                               <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>SLA đáp ứ ng 99.99%.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/campaign/import</td>
      <td>Chuy ển đổ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Import</td>
      <td>/crm/campaign/import</td>
      <td>Import d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Lead</th>
      <th>Ch ỉ tiêu hi ệu năng</th>
      <th>Thêm m ớ i</th>
      <th>/crm/contact/update</th>
      <th>Thêmm ớ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử hi ệ u năng</th>
      <th>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</th>
      <th>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/opportunity/delete</td>
      <td>Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/lead/export</td>
      <td>C ậ p nh ậ t d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                         <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>ứ ng 99.99%.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Export</td>
      <td>/crm/lead/export</td>
      <td>Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/lead/export</td>
      <td>G ắ n th ẻ d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Contact</th>
      <th>Ch ỉ tiêu ch ứ c năng</th>
      <th>G ắ n th ẻ</th>
      <th>/crm/contact/update</th>
      <th>G ắ n th ẻ d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử ch ứ c năng</th>
      <th>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</th>
      <th>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/contact/update</td>
      <td>G ắ n th ẻ d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Xóa</td>
      <td>/crm/lead/add</td>
      <td>Xóa d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s,</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

và ghi log đầ y đủ .                                                                                                              <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>t ự độ ng retry khi l ỗ i.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Import</td>
      <td>/crm/opportunity/delete</td>
      <td>Import d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/lead/add</td>
      <td>C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Lead</th>
      <th>Ch ỉ tiêu b ả om ậ t</th>
      <th>Chuy ể n đổ i</th>
      <th>/crm/opportunity/delete</th>
      <th>Chuy ển đổ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử ch ứ c năng</th>
      <th>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</th>
      <th>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Thêm m ớ i</td>
      <td>/crm/lead/add</td>
      <td>Thêmm ớ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Export</td>
      <td>/crm/contact/update</td>
      <td>Export d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                           <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>rollback giao d ị ch.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/lead/add</td>
      <td>Chuy ển đổ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Import</td>
      <td>/crm/opportunity/delete</td>
      <td>Import d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Campaign</th>
      <th>Ch ỉ tiêu b ả om ậ t</th>
      <th>Xóa</th>
      <th>/crm/campaign/import</th>
      <th>Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử b ả o m ậ t</th>
      <th>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</th>
      <th>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/campaign/import</td>
      <td>C ậ p nh ậ t d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/lead/export</td>
      <td>Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                           <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>vòng 5s, t ự độ ng retry khi l ỗ i.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/opportunity/delete</td>
      <td>Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Xóa</td>
      <td>/crm/campaign/import</td>
      <td>Xóa d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

Contact     <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Ch ỉ tiêu b ả om ậ t</th>
      <th>Thêm m ớ i</th>
      <th>/crm/lead/add</th>
      <th>Thêmm ớ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử b ả o m ậ t</th>
      <th>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</th>
      <th>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Import</td>
      <td>/crm/opportunity/delete</td>
      <td>Import d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/lead/add</td>
      <td>C ậ p nh ậ t d ữ li ệ u Opportunity trong CRM, bao g ồ m</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                              <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>xác th ự c hai l ớ p trướ c khi t ả i.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Xóa</td>
      <td>/crm/contact/update</td>
      <td>Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Import</td>
      <td>/crm/opportunity/delete</td>
      <td>Import d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>và ghi log đầ y đủ .</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/campaign/import</td>
      <td>C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/opportunity/delete</td>
      <td>Chuy ển đổ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Contact</th>
      <th>Ch ỉ tiêu hi ệu năng</th>
      <th>Thêm m ớ i</th>
      <th>/crm/campaign/import</th>
      <th>Thêmm ớ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử ch ứ c năng</th>
      <th>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</th>
      <th>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Thêm m ớ i</td>
      <td>/crm/contact/update</td>
      <td>Thêmm ớ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Xóa</td>
      <td>/crm/opportunity/delete</td>
      <td>Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                          <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>vòng 5s, t ự độ ng retry khi l ỗ i.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/campaign/import</td>
      <td>G ắ n th ẻ d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/campaign/import</td>
      <td>C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Opportunity</th>
      <th>Ch ỉ tiêu hi ệu năng</th>
      <th>G ắ n th ẻ</th>
      <th>/crm/contact/update</th>
      <th>G ắ n th ẻ d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử b ả o m ậ t</th>
      <th>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</th>
      <th>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/campaign/import</td>
      <td>G ắ n th ẻ d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Xóa</td>
      <td>/crm/lead/add</td>
      <td>Xóa d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                        <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>rollback giao d ị ch.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/contact/update</td>
      <td>G ắ n th ẻ d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/opportunity/delete</td>
      <td>Chuy ển đổ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/opportunity/delete</td>
      <td>G ắ n th ẻ d ữ li ệ u Campaign trong CRM,</td>
      <td>Ki ể m th ử</td>
      <td>C ả nh báo n ế u thi ế u trườ ng</td>
      <td>D ữ li ệu đượ c backup hàng ngày,</td>
    </tr>
  </tbody>
</table>
<!-- image -->

bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                             <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>hi ệ u năng</th>
      <th>b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</th>
      <th>lưu giữ t ố i thi ể u 30 ngày.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/opportunity/delete</td>
      <td>Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/lead/add</td>
      <td>C ậ p nh ậ t d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

và ghi log đầ y đủ .                                                                                                              <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>h ệ th ố ng Billing.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Xóa</td>
      <td>/crm/opportunity/delete</td>
      <td>Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/lead/add</td>
      <td>C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Contact</th>
      <th>Ch ỉ tiêu ch ứ c năng</th>
      <th>Xóa</th>
      <th>/crm/lead/export</th>
      <th>Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử b ả o m ậ t</th>
      <th>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</th>
      <th>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/lead/add</td>
      <td>G ắ n th ẻ d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/opportunity/delete</td>
      <td>G ắ n th ẻ d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s,</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

và ghi log đầ y đủ .                                                                                                               <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>t ự độ ng retry khi l ỗ i.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Thêm m ớ i</td>
      <td>/crm/contact/update</td>
      <td>Thêmm ớ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/lead/add</td>
      <td>C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Opportunity</th>
      <th>Ch ỉ tiêu b ả om ậ t</th>
      <th>Export</th>
      <th>/crm/lead/export</th>
      <th>Export d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử ch ứ c năng</th>
      <th>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</th>
      <th>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Export</td>
      <td>/crm/lead/add</td>
      <td>Export d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Thêm m ớ i</td>
      <td>/crm/contact/update</td>
      <td>Thêmm ớ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                      <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>li ệu đồ ng b ộ sang h ệ th ố ng Billing.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/campaign/import</td>
      <td>G ắ n th ẻ d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Export</td>
      <td>/crm/lead/export</td>
      <td>Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Contact</th>
      <th>Ch ỉ tiêu hi ệu năng</th>
      <th>C ậ p nh ậ t</th>
      <th>/crm/lead/export</th>
      <th>C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử hi ệ u năng</th>
      <th>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</th>
      <th>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Import</td>
      <td>/crm/lead/export</td>
      <td>Import d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/opportunity/delete</td>
      <td>G ắ n th ẻ d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog,</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                      <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>SLA đáp ứ ng 99.99%.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/opportunity/delete</td>
      <td>G ắ n th ẻ d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Export</td>
      <td>/crm/lead/export</td>
      <td>Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Contact</th>
      <th>Ch ỉ tiêu ch ứ c năng</th>
      <th>Thêm m ớ i</th>
      <th>/crm/campaign/import</th>
      <th>Thêmm ớ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử hi ệ u năng</th>
      <th>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</th>
      <th>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Xóa</td>
      <td>/crm/opportunity/delete</td>
      <td>Xóa d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Xóa</td>
      <td>/crm/lead/add</td>
      <td>Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                     <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>vòng 5s, t ự độ ng retry khi l ỗ i.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Export</td>
      <td>/crm/campaign/import</td>
      <td>Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Import</td>
      <td>/crm/contact/update</td>
      <td>Import d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

Opportunity   <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Ch ỉ tiêu ch ứ c năng</th>
      <th>Thêm m ớ i</th>
      <th>/crm/lead/export</th>
      <th>Thêmm ớ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử ch ứ c năng</th>
      <th>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</th>
      <th>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Xóa</td>
      <td>/crm/campaign/import</td>
      <td>Xóa d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Xóa</td>
      <td>/crm/opportunity/delete</td>
      <td>Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u</td>
      <td>Ki ể m th ử</td>
      <td>Thành công v ớ i th ờ i gian x ử lý <</td>
      <td>D ữ li ệu đượ c backup hàng ngày,</td>
    </tr>
  </tbody>
</table>
<!-- image -->

đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                    <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>hi ệ u năng</th>
      <th>1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</th>
      <th>lưu giữ t ố i thi ể u 30 ngày.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Import</td>
      <td>/crm/lead/export</td>
      <td>Import d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Import</td>
      <td>/crm/contact/update</td>
      <td>Import d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

và ghi log đầ y đủ .                                                                                                               <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Export</td>
      <td>/crm/contact/update</td>
      <td>Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/lead/export</td>
      <td>C ậ p nh ậ t d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Opportunity</th>
      <th>Ch ỉ tiêu ch ứ c năng</th>
      <th>Thêm m ớ i</th>
      <th>/crm/contact/update</th>
      <th>Thêmm ớ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử hi ệ u năng</th>
      <th>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</th>
      <th>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Export</td>
      <td>/crm/contact/update</td>
      <td>Export d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Xóa</td>
      <td>/crm/opportunity/delete</td>
      <td>Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u</td>
      <td>Ki ể m th ử</td>
      <td>Thành công v ớ i th ờ i gian x ử lý <</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                       <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>ch ứ c năng</th>
      <th>1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/opportunity/delete</td>
      <td>C ậ p nh ậ t d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/lead/export</td>
      <td>Chuy ển đổ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Campaign</th>
      <th>Ch ỉ tiêu b ả om ậ t</th>
      <th>Export</th>
      <th>/crm/lead/add</th>
      <th>Export d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử ch ứ c năng</th>
      <th>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</th>
      <th>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/lead/export</td>
      <td>C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/opportunity/delete</td>
      <td>G ắ n th ẻ d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog,</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                           <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>SLA đáp ứ ng 99.99%.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/contact/update</td>
      <td>Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Import</td>
      <td>/crm/opportunity/delete</td>
      <td>Import d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Campaign</th>
      <th>Ch ỉ tiêu hi ệu năng</th>
      <th>Thêm m ớ i</th>
      <th>/crm/opportunity/delete</th>
      <th>Thêmm ớ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử hi ệ u năng</th>
      <th>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</th>
      <th>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Xóa</td>
      <td>/crm/campaign/import</td>
      <td>Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Export</td>
      <td>/crm/lead/export</td>
      <td>Export d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                            <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>vòng 5s, t ự độ ng retry khi l ỗ i.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/lead/add</td>
      <td>G ắ n th ẻ d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/campaign/import</td>
      <td>G ắ n th ẻ d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Lead</th>
      <th>Ch ỉ tiêu hi ệu năng</th>
      <th>C ậ p nh ậ t</th>
      <th>/crm/contact/update</th>
      <th>C ậ p nh ậ t d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử hi ệ u năng</th>
      <th>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</th>
      <th>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Import</td>
      <td>/crm/lead/export</td>
      <td>Import d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Export</td>
      <td>/crm/opportunity/delete</td>
      <td>Export d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog,</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                  <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>SLA đáp ứ ng 99.99%.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Xóa</td>
      <td>/crm/lead/add</td>
      <td>Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Export</td>
      <td>/crm/lead/export</td>
      <td>Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Lead</th>
      <th>Ch ỉ tiêu b ả om ậ t</th>
      <th>C ậ p nh ậ t</th>
      <th>/crm/contact/update</th>
      <th>C ậ p nh ậ t d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử hi ệ u năng</th>
      <th>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</th>
      <th>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/lead/add</td>
      <td>C ậ p nh ậ t d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Thêm m ớ i</td>
      <td>/crm/opportunity/delete</td>
      <td>Thêmm ớ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                            <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>hai l ớ p trướ c khi t ả i.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/lead/add</td>
      <td>Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Thêm m ớ i</td>
      <td>/crm/lead/add</td>
      <td>Thêmm ớ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Contact</th>
      <th>Ch ỉ tiêu ch ứ c năng</th>
      <th>Export</th>
      <th>/crm/opportunity/delete</th>
      <th>Export d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử ch ứ c năng</th>
      <th>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</th>
      <th>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Import</td>
      <td>/crm/opportunity/delete</td>
      <td>Import d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/lead/add</td>
      <td>Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                           <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>b ộ sang h ệ th ố ng Billing.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Import</td>
      <td>/crm/campaign/import</td>
      <td>Import d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/lead/add</td>
      <td>Chuy ển đổ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Opportunity</th>
      <th>Ch ỉ tiêu ch ứ c năng</th>
      <th>Xóa</th>
      <th>/crm/lead/add</th>
      <th>Xóa d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử ch ứ c năng</th>
      <th>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</th>
      <th>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Xóa</td>
      <td>/crm/contact/update</td>
      <td>Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/lead/export</td>
      <td>C ậ p nh ậ t d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                    <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>b ộ sang h ệ th ố ng Billing.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Import</td>
      <td>/crm/lead/export</td>
      <td>Import d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Export</td>
      <td>/crm/opportunity/delete</td>
      <td>Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Lead</th>
      <th>Ch ỉ tiêu ch ứ c năng</th>
      <th>Thêm m ớ i</th>
      <th>/crm/campaign/import</th>
      <th>Thêmm ớ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử hi ệ u năng</th>
      <th>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</th>
      <th>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/campaign/import</td>
      <td>C ậ p nh ậ t d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Export</td>
      <td>/crm/opportunity/delete</td>
      <td>Export d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                          <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>rollback giao d ị ch.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/contact/update</td>
      <td>C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Import</td>
      <td>/crm/campaign/import</td>
      <td>Import d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

Campaign   <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Ch ỉ tiêu hi ệu năng</th>
      <th>Xóa</th>
      <th>/crm/campaign/import</th>
      <th>Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử ch ứ c năng</th>
      <th>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</th>
      <th>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Thêm m ớ i</td>
      <td>/crm/lead/export</td>
      <td>Thêmm ớ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Thêm m ớ i</td>
      <td>/crm/opportunity/delete</td>
      <td>Thêmm ớ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog,</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                           <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>SLA đáp ứ ng 99.99%.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Import</td>
      <td>/crm/lead/add</td>
      <td>Import d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/campaign/import</td>
      <td>Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Lead</th>
      <th>Ch ỉ tiêu hi ệu năng</th>
      <th>C ậ p nh ậ t</th>
      <th>/crm/contact/update</th>
      <th>C ậ p nh ậ t d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử ch ứ c năng</th>
      <th>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</th>
      <th>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/lead/add</td>
      <td>Chuy ển đổ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Xóa</td>
      <td>/crm/campaign/import</td>
      <td>Xóa d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                      <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>hai l ớ p trướ c khi t ả i.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Export</td>
      <td>/crm/lead/add</td>
      <td>Export d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Export</td>
      <td>/crm/opportunity/delete</td>
      <td>Export d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Opportunity</th>
      <th>Ch ỉ tiêu ch ứ c năng</th>
      <th>Xóa</th>
      <th>/crm/contact/update</th>
      <th>Xóa d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử ch ứ c năng</th>
      <th>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</th>
      <th>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Import</td>
      <td>/crm/opportunity/delete</td>
      <td>Import d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Xóa</td>
      <td>/crm/lead/export</td>
      <td>Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                            <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>rollback giao d ị ch.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Thêm m ớ i</td>
      <td>/crm/campaign/import</td>
      <td>Thêmm ớ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Import</td>
      <td>/crm/opportunity/delete</td>
      <td>Import d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

Lead    <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Ch ỉ tiêu hi ệu năng</th>
      <th>Thêm m ớ i</th>
      <th>/crm/lead/add</th>
      <th>Thêmm ớ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử b ả o m ậ t</th>
      <th>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</th>
      <th>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/lead/add</td>
      <td>G ắ n th ẻ d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/lead/export</td>
      <td>Chuy ển đổ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                      <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>hai l ớ p trướ c khi t ả i.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Import</td>
      <td>/crm/opportunity/delete</td>
      <td>Import d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Xóa</td>
      <td>/crm/lead/add</td>
      <td>Xóa d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

Lead     <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Ch ỉ tiêu b ả om ậ t</th>
      <th>Chuy ể n đổ i</th>
      <th>/crm/lead/add</th>
      <th>Chuy ển đổ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử b ả o m ậ t</th>
      <th>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</th>
      <th>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/campaign/import</td>
      <td>C ậ p nh ậ t d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/contact/update</td>
      <td>C ậ p nh ậ t d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                            <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>ứ ng 99.99%.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Thêm m ớ i</td>
      <td>/crm/contact/update</td>
      <td>Thêmm ớ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/lead/add</td>
      <td>G ắ n th ẻ d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

Lead        <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Ch ỉ tiêu b ả om ậ t</th>
      <th>Xóa</th>
      <th>/crm/lead/export</th>
      <th>Xóa d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử hi ệ u năng</th>
      <th>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</th>
      <th>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/campaign/import</td>
      <td>C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/campaign/import</td>
      <td>Chuy ển đổ i d ữ li ệ u Opportunity trong CRM, bao g ồ m</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                   <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>vòng 5s, t ự độ ng retry khi l ỗ i.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/campaign/import</td>
      <td>C ậ p nh ậ t d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Export</td>
      <td>/crm/lead/export</td>
      <td>Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

retry khi l ỗ i.                                                                 <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Import</td>
      <td>/crm/campaign/import</td>
      <td>Import d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Export</td>
      <td>/crm/lead/add</td>
      <td>Export d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/lead/add</td>
      <td>Chuy ển đổ i d ữ li ệ u Lead trong CRM, bao g ồ m</td>
      <td>Ki ể m th ử</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                          <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>ch ứ c năng</th>
      <th>d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/opportunity/delete</td>
      <td>Chuy ển đổ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Xóa</td>
      <td>/crm/contact/update</td>
      <td>Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>và ghi log đầ y đủ .</th>
      <th></th>
      <th>h ệ th ố ng Billing.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/campaign/import</td>
      <td>Chuy ển đổ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/contact/update</td>
      <td>G ắ n th ẻ d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Thêm m ớ i</td>
      <td>/crm/campaign/import</td>
      <td>Thêmm ớ i d ữ li ệ u Contact</td>
      <td>Ki ể m th ử</td>
      <td>C ả nh báo n ế u thi ế u</td>
      <td>D ữ li ệu đượ c backup hàng ngày,</td>
    </tr>
  </tbody>
</table>
<!-- image -->

trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                              <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>hi ệ u năng</th>
      <th>trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</th>
      <th>lưu giữ t ố i thi ể u 30 ngày.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Thêm m ớ i</td>
      <td>/crm/contact/update</td>
      <td>Thêmm ớ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Export</td>
      <td>/crm/contact/update</td>
      <td>Export d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

và ghi log đầ y đủ .                                                                                                           <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>h ệ th ố ng Billing.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Thêm m ớ i</td>
      <td>/crm/opportunity/delete</td>
      <td>Thêmm ớ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Export</td>
      <td>/crm/lead/export</td>
      <td>Export d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Import</td>
      <td>/crm/contact/update</td>
      <td>Import d ữ li ệ u Lead trong</td>
      <td>Ki ể m th ử</td>
      <td>C ả nh báo n ế u thi ế u</td>
      <td>D ữ li ệu đượ c backup hàng ngày,</td>
    </tr>
  </tbody>
</table>
<!-- image -->

CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                              <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>hi ệ u năng</th>
      <th>trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</th>
      <th>lưu giữ t ố i thi ể u 30 ngày.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Import</td>
      <td>/crm/lead/export</td>
      <td>Import d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/lead/export</td>
      <td>Chuy ển đổ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

và ghi log đầ y đủ .                                                                                                           <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>ứ ng 99.99%.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/lead/add</td>
      <td>G ắ n th ẻ d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/opportunity/delete</td>
      <td>C ậ p nh ậ t d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Export</td>
      <td>/crm/lead/export</td>
      <td>Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c,</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                     <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>h ệ th ố ng rollback giao d ị ch.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Xóa</td>
      <td>/crm/contact/update</td>
      <td>Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Export</td>
      <td>/crm/lead/export</td>
      <td>Export d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Contact</th>
      <th>Ch ỉ tiêu ch ứ c năng</th>
      <th>Import</th>
      <th>/crm/campaign/import</th>
      <th>Import d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử hi ệ u năng</th>
      <th>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</th>
      <th>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Thêm m ớ i</td>
      <td>/crm/lead/export</td>
      <td>Thêmm ớ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/lead/export</td>
      <td>G ắ n th ẻ d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                            <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>rollback giao d ị ch.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Export</td>
      <td>/crm/campaign/import</td>
      <td>Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/lead/export</td>
      <td>Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Contact</th>
      <th>Ch ỉ tiêu ch ứ c năng</th>
      <th>Thêm m ớ i</th>
      <th>/crm/contact/update</th>
      <th>Thêmm ớ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử hi ệ u năng</th>
      <th>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</th>
      <th>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/contact/update</td>
      <td>C ậ p nh ậ t d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Xóa</td>
      <td>/crm/lead/export</td>
      <td>Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                             <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>trong vòng 5s, t ự độ ng retry khi l ỗ i.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Xóa</td>
      <td>/crm/lead/export</td>
      <td>Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/campaign/import</td>
      <td>Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

và ghi log đầ y đủ .                                                                                                                  <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>h ệ th ố ng Billing.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Thêm m ớ i</td>
      <td>/crm/campaign/import</td>
      <td>Thêmm ớ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/campaign/import</td>
      <td>C ậ p nh ậ t d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Contact</th>
      <th>Ch ỉ tiêu ch ứ c năng</th>
      <th>C ậ p nh ậ t</th>
      <th>/crm/opportunity/delete</th>
      <th>C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử hi ệ u năng</th>
      <th>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</th>
      <th>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Xóa</td>
      <td>/crm/campaign/import</td>
      <td>Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/lead/export</td>
      <td>G ắ n th ẻ d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                            <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>li ệu đồ ng b ộ sang h ệ th ố ng Billing.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/lead/add</td>
      <td>Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/lead/add</td>
      <td>G ắ n th ẻ d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Contact</th>
      <th>Ch ỉ tiêu b ả om ậ t</th>
      <th>Import</th>
      <th>/crm/lead/add</th>
      <th>Import d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử b ả o m ậ t</th>
      <th>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</th>
      <th>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Thêm m ớ i</td>
      <td>/crm/campaign/import</td>
      <td>Thêmm ớ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Xóa</td>
      <td>/crm/lead/add</td>
      <td>Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                            <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>vòng 5s, t ự độ ng retry khi l ỗ i.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/lead/export</td>
      <td>Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Xóa</td>
      <td>/crm/campaign/import</td>
      <td>Xóa d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

Lead     <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Ch ỉ tiêu hi ệu năng</th>
      <th>Xóa</th>
      <th>/crm/contact/update</th>
      <th>Xóa d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử ch ứ c năng</th>
      <th>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</th>
      <th>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Export</td>
      <td>/crm/lead/add</td>
      <td>Export d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Export</td>
      <td>/crm/lead/add</td>
      <td>Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                            <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>li ệu đồ ng b ộ sang h ệ th ố ng Billing.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/lead/add</td>
      <td>Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/campaign/import</td>
      <td>Chuy ển đổ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

và ghi log đầ y đủ .                                                                                                                  <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/opportunity/delete</td>
      <td>C ậ p nh ậ t d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/campaign/import</td>
      <td>G ắ n th ẻ d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Campaign</th>
      <th>Ch ỉ tiêu hi ệu năng</th>
      <th>C ậ p nh ậ t</th>
      <th>/crm/campaign/import</th>
      <th>C ậ p nh ậ t d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử b ả o m ậ t</th>
      <th>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</th>
      <th>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Import</td>
      <td>/crm/campaign/import</td>
      <td>Import d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Import</td>
      <td>/crm/lead/export</td>
      <td>Import d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

và ghi log đầ y đủ .                                                                                                           <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>hai l ớ p trướ c khi t ả i.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Thêm m ớ i</td>
      <td>/crm/lead/add</td>
      <td>Thêmm ớ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/lead/export</td>
      <td>C ậ p nh ậ t d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Lead</th>
      <th>Ch ỉ tiêu ch ứ c năng</th>
      <th>G ắ n th ẻ</th>
      <th>/crm/contact/update</th>
      <th>G ắ n th ẻ d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử hi ệ u năng</th>
      <th>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</th>
      <th>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Thêm m ớ i</td>
      <td>/crm/lead/export</td>
      <td>Thêmm ớ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Export</td>
      <td>/crm/lead/add</td>
      <td>Export d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s,</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                     <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>t ự độ ng retry khi l ỗ i.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Xóa</td>
      <td>/crm/opportunity/delete</td>
      <td>Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Thêm m ớ i</td>
      <td>/crm/lead/add</td>
      <td>Thêmm ớ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Campaign</th>
      <th>Ch ỉ tiêu b ả om ậ t</th>
      <th>Export</th>
      <th>/crm/contact/update</th>
      <th>Export d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử ch ứ c năng</th>
      <th>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</th>
      <th>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/contact/update</td>
      <td>Chuy ển đổ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Xóa</td>
      <td>/crm/lead/export</td>
      <td>Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                        <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>xác th ự c hai l ớ p trướ c khi t ả i.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/opportunity/delete</td>
      <td>G ắ n th ẻ d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Import</td>
      <td>/crm/campaign/import</td>
      <td>Import d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Contact</th>
      <th>Ch ỉ tiêu b ả om ậ t</th>
      <th>G ắ n th ẻ</th>
      <th>/crm/campaign/import</th>
      <th>G ắ n th ẻ d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử ch ứ c năng</th>
      <th>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</th>
      <th>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/opportunity/delete</td>
      <td>C ậ p nh ậ t d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Export</td>
      <td>/crm/opportunity/delete</td>
      <td>Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

và ghi log đầ y đủ .                                                                                                               <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>hai l ớ p trướ c khi t ả i.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Thêm m ớ i</td>
      <td>/crm/opportunity/delete</td>
      <td>Thêmm ớ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Thêm m ớ i</td>
      <td>/crm/lead/export</td>
      <td>Thêmm ớ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Contact</th>
      <th>Ch ỉ tiêu ch ứ c năng</th>
      <th>C ậ p nh ậ t</th>
      <th>/crm/lead/add</th>
      <th>C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử ch ứ c năng</th>
      <th>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</th>
      <th>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/campaign/import</td>
      <td>Chuy ển đổ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Import</td>
      <td>/crm/lead/export</td>
      <td>Import d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

và ghi log đầ y đủ .                                                                                                           <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>rollback giao d ị ch.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/contact/update</td>
      <td>C ậ p nh ậ t d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Export</td>
      <td>/crm/lead/add</td>
      <td>Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/campaign/import</td>
      <td>G ắ n th ẻ d ữ li ệ u Opportunity trong CRM, bao g ồ m</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Thành công v ớ i th ờ i gian x ử lý <</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                             <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Export</td>
      <td>/crm/opportunity/delete</td>
      <td>Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Xóa</td>
      <td>/crm/opportunity/delete</td>
      <td>Xóa d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

và ghi log đầ y đủ .                                                                                                             <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>h ệ th ố ng Billing.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Thêm m ớ i</td>
      <td>/crm/opportunity/delete</td>
      <td>Thêmm ớ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/lead/export</td>
      <td>G ắ n th ẻ d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Opportunity</th>
      <th>Ch ỉ tiêu b ả om ậ t</th>
      <th>Thêm m ớ i</th>
      <th>/crm/contact/update</th>
      <th>Thêmm ớ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử ch ứ c năng</th>
      <th>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</th>
      <th>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/opportunity/delete</td>
      <td>Chuy ển đổ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/lead/export</td>
      <td>C ậ p nh ậ t d ữ li ệ u Campaign trong CRM,</td>
      <td>Ki ể m th ử</td>
      <td>Đồ ng b ộ d ữ li ệ u sang</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA</td>
    </tr>
  </tbody>
</table>
<!-- image -->

bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                           <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>hi ệ u năng</th>
      <th>DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</th>
      <th>để t ự độ ng hóa quy trình.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/lead/add</td>
      <td>G ắ n th ẻ d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Xóa</td>
      <td>/crm/contact/update</td>
      <td>Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

và ghi log đầ y đủ .                                                                                                         <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>ứ ng 99.99%.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/contact/update</td>
      <td>G ắ n th ẻ d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Import</td>
      <td>/crm/opportunity/delete</td>
      <td>Import d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Xóa</td>
      <td>/crm/opportunity/delete</td>
      <td>Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c,</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>h ệ th ố ng rollback giao d ị ch.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Xóa</td>
      <td>/crm/lead/export</td>
      <td>Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Thêm m ớ i</td>
      <td>/crm/lead/export</td>
      <td>Thêmm ớ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Contact</th>
      <th>Ch ỉ tiêu hi ệu năng</th>
      <th>Thêm m ớ i</th>
      <th>/crm/contact/update</th>
      <th>Thêmm ớ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử b ả o m ậ t</th>
      <th>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</th>
      <th>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Xóa</td>
      <td>/crm/lead/add</td>
      <td>Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Import</td>
      <td>/crm/contact/update</td>
      <td>Import d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                           <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>hai l ớ p trướ c khi t ả i.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Import</td>
      <td>/crm/contact/update</td>
      <td>Import d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/lead/add</td>
      <td>C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Contact</th>
      <th>Ch ỉ tiêu ch ứ c năng</th>
      <th>G ắ n th ẻ</th>
      <th>/crm/lead/export</th>
      <th>G ắ n th ẻ d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử b ả o m ậ t</th>
      <th>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</th>
      <th>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/contact/update</td>
      <td>G ắ n th ẻ d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Xóa</td>
      <td>/crm/opportunity/delete</td>
      <td>Xóa d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                               <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>rollback giao d ị ch.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/campaign/import</td>
      <td>C ậ p nh ậ t d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Export</td>
      <td>/crm/opportunity/delete</td>
      <td>Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

Lead     <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Ch ỉ tiêu hi ệu năng</th>
      <th>Xóa</th>
      <th>/crm/opportunity/delete</th>
      <th>Xóa d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử ch ứ c năng</th>
      <th>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</th>
      <th>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Import</td>
      <td>/crm/lead/export</td>
      <td>Import d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Import</td>
      <td>/crm/contact/update</td>
      <td>Import d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                        <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>rollback giao d ị ch.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Thêm m ớ i</td>
      <td>/crm/opportunity/delete</td>
      <td>Thêmm ớ i d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Export</td>
      <td>/crm/lead/add</td>
      <td>Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Contact</th>
      <th>Ch ỉ tiêu hi ệu năng</th>
      <th>Xóa</th>
      <th>/crm/contact/update</th>
      <th>Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử b ả o m ậ t</th>
      <th>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</th>
      <th>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Export</td>
      <td>/crm/opportunity/delete</td>
      <td>Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/lead/add</td>
      <td>C ậ p nh ậ t d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                     <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>rollback giao d ị ch.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Import</td>
      <td>/crm/opportunity/delete</td>
      <td>Import d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Xóa</td>
      <td>/crm/lead/add</td>
      <td>Xóa d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Campaign</th>
      <th>Ch ỉ tiêu b ả om ậ t</th>
      <th>Thêm m ớ i</th>
      <th>/crm/lead/add</th>
      <th>Thêmm ớ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử hi ệ u năng</th>
      <th>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</th>
      <th>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Thêm m ớ i</td>
      <td>/crm/campaign/import</td>
      <td>Thêmm ớ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Thêm m ớ i</td>
      <td>/crm/campaign/import</td>
      <td>Thêmm ớ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s,</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

và ghi log đầ y đủ .                                                                                                                  <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>t ự độ ng retry khi l ỗ i.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/lead/export</td>
      <td>Chuy ển đổ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Xóa</td>
      <td>/crm/lead/add</td>
      <td>Xóa d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

Opportunity   <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Ch ỉ tiêu hi ệu năng</th>
      <th>Chuy ể n đổ i</th>
      <th>/crm/lead/add</th>
      <th>Chuy ển đổ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử ch ứ c năng</th>
      <th>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</th>
      <th>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/lead/add</td>
      <td>C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Export</td>
      <td>/crm/lead/export</td>
      <td>Export d ữ li ệ u Opportunity trong CRM, bao g ồ m</td>
      <td>Ki ể m th ử</td>
      <td>Không l ỗ i, log đầy đủ trong</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                      <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>hi ệ u năng</th>
      <th>AuditLog, SLA đáp ứ ng 99.99%.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/contact/update</td>
      <td>C ậ p nh ậ t d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/opportunity/delete</td>
      <td>Chuy ển đổ i d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

retry khi l ỗ i.                                                             <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Xóa</td>
      <td>/crm/campaign/import</td>
      <td>Xóa d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Thêm m ớ i</td>
      <td>/crm/lead/export</td>
      <td>Thêmm ớ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Lead</th>
      <th>Ch ỉ tiêu hi ệu năng</th>
      <th>Xóa</th>
      <th>/crm/contact/update</th>
      <th>Xóa d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử ch ứ c năng</th>
      <th>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</th>
      <th>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/opportunity/delete</td>
      <td>Chuy ển đổ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/lead/add</td>
      <td>C ậ p nh ậ t d ữ li ệ u Campaign trong CRM, bao g ồ m</td>
      <td>Ki ể m th ử</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                    <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>hi ệ u năng</th>
      <th>trong vòng 5s, t ự độ ng retry khi l ỗ i.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Import</td>
      <td>/crm/lead/add</td>
      <td>Import d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/lead/export</td>
      <td>G ắ n th ẻ d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

và ghi log đầ y đủ .                                                                                                            <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>C ậ p nh ậ t</td>
      <td>/crm/lead/add</td>
      <td>C ậ p nh ậ t d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Import</td>
      <td>/crm/lead/export</td>
      <td>Import d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Xóa</td>
      <td>/crm/contact/update</td>
      <td>Xóa d ữ li ệ u Contact trong</td>
      <td>Ki ể m th ử</td>
      <td>C ả nh báo n ế u thi ế u</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho</td>
    </tr>
  </tbody>
</table>
<!-- image -->

CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                              <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>hi ệ u năng</th>
      <th>trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</th>
      <th>qu ả n tr ị viên ph ụ trách.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Import</td>
      <td>/crm/opportunity/delete</td>
      <td>Import d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/lead/add</td>
      <td>G ắ n th ẻ d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

và ghi log đầ y đủ .                                                                                                            <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>h ệ th ố ng Billing.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/lead/export</td>
      <td>G ắ n th ẻ d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Thêm m ớ i</td>
      <td>/crm/campaign/import</td>
      <td>Thêmm ớ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Opportunity</th>
      <th>Ch ỉ tiêu b ả om ậ t</th>
      <th>Chuy ể n đổ i</th>
      <th>/crm/opportunity/delete</th>
      <th>Chuy ển đổ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử b ả o m ậ t</th>
      <th>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</th>
      <th>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Export</td>
      <td>/crm/opportunity/delete</td>
      <td>Export d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Xóa</td>
      <td>/crm/campaign/import</td>
      <td>Xóa d ữ li ệ u Opportunity trong CRM, bao g ồ m</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho</td>
    </tr>
  </tbody>
</table>
<!-- image -->

validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                 <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>trong vòng 5s, t ự độ ng retry khi l ỗ i.</th>
      <th>qu ả n tr ị viên ph ụ trách.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Xóa</td>
      <td>/crm/lead/add</td>
      <td>Xóa d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Export</td>
      <td>/crm/contact/update</td>
      <td>Export d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có xác th ự c hai l ớ p trướ c khi t ả i.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Campaign</th>
      <th>Ch ỉ tiêu ch ứ c năng</th>
      <th>Chuy ể n đổ i</th>
      <th>/crm/contact/update</th>
      <th>Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử b ả o m ậ t</th>
      <th>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</th>
      <th>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/lead/export</td>
      <td>Chuy ển đổ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Thêm m ớ i</td>
      <td>/crm/lead/add</td>
      <td>Thêmm ớ i d ữ li ệ u Campaign trong CRM, bao g ồ m</td>
      <td>Ki ể m th ử</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho</td>
    </tr>
  </tbody>
</table>
<!-- image -->

validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                     <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>ch ứ c năng</th>
      <th>trong vòng 5s, t ự độ ng retry khi l ỗ i.</th>
      <th>qu ả n tr ị viên ph ụ trách.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Export</td>
      <td>/crm/contact/update</td>
      <td>Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>Ph ả i ki ể m th ử v ới ≥ 10.000 b ản ghi để đả mb ả o hi ệu năng.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/contact/update</td>
      <td>G ắ n th ẻ d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Contact</th>
      <th>Ch ỉ tiêu ch ứ c năng</th>
      <th>Xóa</th>
      <th>/crm/lead/add</th>
      <th>Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử b ả o m ậ t</th>
      <th>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</th>
      <th>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Import</td>
      <td>/crm/campaign/import</td>
      <td>Import d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong vòng 5s, t ự độ ng retry khi l ỗ i.</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Export</td>
      <td>/crm/lead/export</td>
      <td>Export d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Xu ấ t báo cáo chi ti ết dướ i d ạ ng CSV, có</td>
      <td>Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                                             <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>xác th ự c hai l ớ p trướ c khi t ả i.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>G ắ n th ẻ</td>
      <td>/crm/contact/update</td>
      <td>G ắ n th ẻ d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Import</td>
      <td>/crm/lead/export</td>
      <td>Import d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử b ả o m ậ t</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

## CH Ỉ TIÊU CRM - RPA

TD445

L ầ n ban hành: 1

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Contact</th>
      <th>Ch ỉ tiêu hi ệu năng</th>
      <th>Xóa</th>
      <th>/crm/opportunity/delete</th>
      <th>Xóa d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</th>
      <th>Ki ể m th ử ch ứ c năng</th>
      <th>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</th>
      <th>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Thêm m ớ i</td>
      <td>/crm/lead/export</td>
      <td>Thêmm ớ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Thêm m ớ i</td>
      <td>/crm/opportunity/delete</td>
      <td>Thêmm ớ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u</td>
      <td>Ki ể m th ử hi ệ u năng</td>
      <td>Đồ ng b ộ d ữ li ệ u sang DataLake trong</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .                                                                           <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
      <th>vòng 5s, t ự độ ng retry khi l ỗ i.</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Opportunity</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Thêm m ớ i</td>
      <td>/crm/lead/export</td>
      <td>Thêmm ớ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang h ệ th ố ng Billing.</td>
      <td>D ữ li ệu đượ c backup hàng ngày, lưu giữ t ố i thi ể u 30 ngày.</td>
    </tr>
    <tr>
      <td>Lead</td>
      <td>Ch ỉ tiêu hi ệu năng</td>
      <td>Export</td>
      <td>/crm/opportunity/delete</td>
      <td>Export d ữ li ệ u Lead trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Thành công v ớ i th ờ i gian x ử lý < 1s, d ữ li ệu đồ ng b ộ sang</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

h ệ th ố ng Billing.                                         <table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu b ả om ậ t</td>
      <td>Xóa</td>
      <td>/crm/lead/add</td>
      <td>Xóa d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>K ế t qu ả đượ c g ử i mail và SMS cho qu ả n tr ị viên ph ụ trách.</td>
    </tr>
    <tr>
      <td>Campaign</td>
      <td>Ch ỉ tiêu ch ứ c năng</td>
      <td>Chuy ể n đổ i</td>
      <td>/crm/opportunity/delete</td>
      <td>Chuy ển đổ i d ữ li ệ u Campaign trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .</td>
      <td>Ki ể m th ử ch ứ c năng</td>
      <td>Không l ỗ i, log đầy đủ trong AuditLog, SLA đáp ứ ng 99.99%.</td>
      <td>Theo chu ẩ n ISO 27001 và quy đị nh b ả om ậ t Viettel.</td>
    </tr>
  </tbody>
</table>
<!-- image -->

Contact     | Ch ỉ tiêu hi ệu năng   | Export     | /crm/lead/add    | Export d ữ li ệ u Contact trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ .        | Ki ể m th ử b ả o m ậ t   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.   | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.   |
|-------------|------------------------|------------|------------------|------------------------------------------------------------------------------------------------------------------------------------|---------------------------|------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Opportunity | Ch ỉ tiêu hi ệu năng   | Thêm m ớ i | /crm/lead/export | Thêmm ớ i d ữ li ệ u Opportunity trong CRM, bao g ồ m validate d ữ li ệ u đầ u vào, x ử lý logic nghi ệ p v ụ và ghi log đầ y đủ . | Ki ể m th ử hi ệ u năng   | C ả nh báo n ế u thi ế u trườ ng b ắ t bu ộ c, h ệ th ố ng rollback giao d ị ch.   | Yêu c ầ u tích h ợ p v ớ i h ệ th ố ng RPA để t ự độ ng hóa quy trình.   |