1.Bài báo Lao Động
-Nguồn: https://laodong.vn/<br/>
-Số lượng bài: 10k+<br/>
-Tốc độ: 1500/phút<br/>
-Trạng thái: đã chạy được<br/>
-Thu thập được:link, title, tags, keywords, description, contents<br/>
-Mô tả mã nguồn:<br/>
name :tên của spider<br/>
start_urls:page đầu tiên để crawl rồi từ page này lan sang page khác<br/>
Hàm parse(self,response):hàm gọi để xử lý phản hồi được tải xuống và thực hiện các chức năng:<br/>
Kiểm tra xem link đó có phải là link cần crawl không (tránh crawl các link rác)<br/>
Sau khi kiểm tra thì ghi lại :link, title, tags, keywords, description, contents ra file .tex.<br/>
yield : cho phép chỉ tiến hành crawl trên các bài báo có dạng link tuyệt đối của báo laodong.vn và callback lại parse.<br/>

2.Thu thập trang thương mại điện tử
-Nguồn: https://www.thegioididong.com/
-Số lượng: 400 sản phẩm
-Tốc độ: 15 bài/phút
-Trạng thái:đã chạy được
-Các thông tin:link, name, img link, short description, rate, price, specification
-Mô tả mã nguồn:<br/>
name :tên của spider<br/>
start_urls:page đầu tiên để crawl rồi từ page này lan sang page khác<br/>
Hàm parse(self,response):hàm gọi để xử lý phản hồi được tải xuống và thực hiện các chức năng:<br/>
Kiểm tra xem link đó có phải là link cần crawl không (loại các link không phải là của tgdd và link không phải product)<br/>
Sau khi kiểm tra thì ghi lại :link, name, img link, short description, rate, price, specification.<br/>
yield : cho phép chỉ tiến hành crawl trên các bài báo có dạng link tuyệt đối của báo tgdd và tương đối( có dạng bắt đầu bằng "/") và callback lại parse.<br/>
