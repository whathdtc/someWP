# 身份绕过  



# 2  
题目说，我更换了密码并且更换了设备，登录需要回答我设置的问题，问题的答案在服务器上，并且我忘了，我提供了用户名和电子邮件  

1. 抓包  
![alt text](image.png)  

2. 我尝试了把verifyMethod的值改为NULL，删除secQuestion0和secQuestion1，但是都没什么用，找了一篇答案，把secQuestion0和secQuestion1改成secQuestion2和secQuestion3，然后就过了，我试了试，果然是对的  
![alt text](image-1.png)  
