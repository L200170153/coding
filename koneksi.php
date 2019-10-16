<?php 
    $host = 'localhost';
    $user = 'root';
    $password = '1234';

    $conn = mysqli_connect($host, $user, $password);
    if($conn) {
        echo "connection success";
    } else {
        echo "connection fail";
    }
?>