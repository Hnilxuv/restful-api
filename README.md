# restful-api

# ex1:

Bước 1: Chạy script SQL ex1 trong file SQL Script với SQL server. (em tạo kết nối với SQL server)

Bước 2: Sửa tên server name trong file db.py trong ex1 và chạy file app.py trong ex1

<img width="148" alt="image" src="https://user-images.githubusercontent.com/89204878/164365830-e9ae8dc1-a5d0-494d-9b62-6e22ccca6d17.png">

Bước 3: chạy các api với post man trong app.py 

ví dụ

<img width="562" alt="image" src="https://user-images.githubusercontent.com/89204878/164366038-838bf344-2395-46cc-82b6-cc1edae072f5.png">

<img width="896" alt="image" src="https://user-images.githubusercontent.com/89204878/164387050-513c9ccd-c10a-414b-b38a-e2323ca3afac.png">

<img width="897" alt="image" src="https://user-images.githubusercontent.com/89204878/164387118-b22ec982-b616-4201-9e13-80e17136f14a.png">

- với api add :
    + body json gồm:

    <img width="523" alt="image" src="https://user-images.githubusercontent.com/89204878/164366764-1d219ede-681c-4d52-a6aa-3f2a931f5ab6.png">

    + validate: 
            
            name: string, no empty, maxlength = 50, regex: chữ hoa chữ thường ko số có dấu cách
            
            acc_no: string, no empty, regex:  giới hạn 9 chữ số
            
            balance: int, no empty
 
- với api deposit, withdraw 
     + url: ...../(acc_id)/(deposit/withdraw)
     + body: "amount": (int)
     + validate: int, no empty
     + condition: > 0 , api withdraw: amount < balanace + fee withdraw

# ex3:
 
Bước 1: Chạy script SQL ex3 trong file SQL Script với SQL server. (em tạo kết nối với SQL server)

Bước 2: Sửa tên server name trong file db.py trong ex3 và chạy file app.py trong ex3 

Bước 3: chạy các api theo comment
  
  - customer add    
      + body, validate: 
      
              name: string, not empty, maxlength = 50, regex: chữ ko số có cách.
                      
              phone: string, not empty, regex: chỉ số, giới hạn 10
  
  - product add
      + body, validate: 
              
              name: string, not empty, maxlengt = 50, regex: số, chữ hoa, thường, có cách. condition: not exist in db.
                        
              category: string, not empty, maxlengt = 50, regex: số, chữ hoa, thường, có cách.

              brand: string, not empty, maxlengt = 50, regex: số, chữ hoa, thường, có cách.

              price: int, not empty.
                      
  - bill add
      + body, validate: 
            
            customer_id: string, not empty, regex: định dạng theo id sinh tự động. condition: exist in db.
      
  - bill detail add
      + body, validate: 
            
            product_id: int, not empty. condition: exist in PRODUCT.
            
            amount: int, not empty
  
  - với các api theo customer id --> url: .../customer/(customer_id)/.... tương tự với product (product_id), bill (bill_id)

ví dụ:

<img width="887" alt="image" src="https://user-images.githubusercontent.com/89204878/164392331-6f4bd516-d3c8-43b4-b128-b0dc32b8cdcd.png">

<img width="885" alt="image" src="https://user-images.githubusercontent.com/89204878/164392471-3c46c42a-ab4f-4cfe-8bf0-4da0483af5bf.png">



# ex4:
Bước 1: Chạy script SQL ex4 trong file SQL Script với SQL server. (em tạo kết nối với SQL server) 

Bước 2: Sửa tên server name trong file db.py trong ex4 và chạy file app.py trong ex4 

Bước 3: chạy các api theo comment 
  
  - customer add
      + body, validate: 
            
            name: string, not empty, maxlength = 50, regex: số, chữ hoa, thường, có cách.
  
  - saving/checking acount add
      + body, validate: 
      
            customer_id: int, not empty
            
            acc_no: string, not empty, regex: chỉ số, giới hạn 10
            
            balance: int, not empty
            
            link_code: int, not empty
  - với các api theo customer id --> url: .../customer/(customer_id)/....
