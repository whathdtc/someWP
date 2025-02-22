# HTTP Basics  

## 魔法数字是什么  
1. 随便填，然后抓包  
![alt text](image.png)  
![alt text](image-2.png)  
2. POST传的第一个参数就是，填进去点go  
![alt text](image-3.png)

# HTTP Proxies

![alt text](image-7.png)  

1. burpsuit开启拦截，然后点击Submit
![alt text](image-8.png)  
![alt text](image-9.png)  

2. 按照要求修改  
- Change the Method to GET  
![alt text](image-10.png)  

- Add a header 'x-request-intercepted:true'  
![alt text](image-11.png)  

- Remove the request body and instead send 'changeMe' as a query string parameter and set the value to 'Requests are tampered easily' (without the single quotes)
![alt text](image-12.png)  
把最后一行删除  
3. 但是发现有问题，警觉空格要用url编码  
![alt text](image-13.png)  
并且最后一行不能删除  
![alt text](image-14.png)  
4. 改好之后发送，响应很好  
![alt text](image-15.png)  



# Developer Tools  


## Using the console  
要调用一个函数，然后填入一个随机数，该数字会被输出  
![alt text](image-17.png)  
直接调用  
![alt text](image-18.png)


## 找一个特殊HTTP请求，然后找networkNum  
![alt text](image-4.png)  
1. 题目要用Network tab来完成，F12，html代码一点点找，找到了对应位置form标签，想必这就是要发送的请求，里面有一个input标签，名字是networkNum，后面有值。  
![alt text](image-16.png)  

2. 也可以拦截请求，按照要求点一下GO按钮，拦截查看  
![alt text](image-5.png)  


# CIA Triad  
CIA三要素：机密性，完整性，可用性(confidentiality, integrity, availability)。  

# Writing new lesson  

怎么在webgoat中添加新课程，我就不看了。  

