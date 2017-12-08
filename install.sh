echo "
<?php
/**
 * Created by PhpStorm.
 * User: tudoudou
 * Date: 2017/12/8
 * Time: 上午9:22
 */


$html=<<<html
<!DOCTYPE html>
<html>
<head lang=\"ch\">
    <meta charset=\"UTF-8\">
    <title>欢迎登入后台</title>
</head>
<body>
<form action=\"\" method=\"get\">
    用户名：<input name=\"username\" type=\"text\"/><br>
    密码： <input name=\"password\" type=\"password\"/>
    <input type=\"submit\"/>
</form>
</body>
</html>

html;


if(isset($_GET['username'])&&$_GET['username']){
    $db = new MySQLi(\"localhost\",\"root\",\"\",\"sql_universal_password\");
    mysqli_connect_error()?die(\"连接失败\"):\"\";
    $sql = \"select count(*) from hctf where username='{$_GET['username']}' and password='{$_GET['password']}'\";
    $result = $db->query($sql);
    $n = $result->fetch_row();
    if($n[0]>0)
    {
        echo 'HCTF{UlhgdTSa5cWyM67GPC8EwLfv9juoYI0DKHF4ekt}';
    }
    else
    {
        echo '用户名密码错误';
        echo $html;
    }
}else{

    echo $html;
}

?>
" > /app/index.php
