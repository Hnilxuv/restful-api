# restful-api
ex1:
Bước 1: Chạy script SQL ex1 trong file SQL Script với SQL server. (em tạo kết nối với SQL server)

Bước 2: Chạy file app.py trong ex1

<img width="148" alt="image" src="https://user-images.githubusercontent.com/89204878/164365830-e9ae8dc1-a5d0-494d-9b62-6e22ccca6d17.png">

Bước 3:
- chạy các api với post man trong app.py 

<img width="562" alt="image" src="https://user-images.githubusercontent.com/89204878/164366038-838bf344-2395-46cc-82b6-cc1edae072f5.png">

- với api add :
  + body json gồm:
  
  <img width="523" alt="image" src="https://user-images.githubusercontent.com/89204878/164366764-1d219ede-681c-4d52-a6aa-3f2a931f5ab6.png">
  
  + validate: name: string, no empty, maxlength = 50, regex: chữ hoa chữ thường ko số có dấu cách
              acc_no: string, no empty, regex:  giới hạn 9 chữ số
              balance: int, no empty
 
 - với api deposit, withdraw 
   + url: ...../(acc_id)/(deposit/withdraw)
   + body: "amount": (int)
   + validate: int, no empty
   + condition: api withdraw: amount < balanace + fee withdraw
   
   
