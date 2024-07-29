<?php
session_start();

// 生成一个新的会话密钥
if (!isset($_SESSION['SESSKEY'])) {
    $_SESSION['SESSKEY'] = bin2hex(random_bytes(32));
}

// 获取会话密钥
$sesskey = $_SESSION['SESSKEY'];

echo "Your session key is: $sesskey";
?>
