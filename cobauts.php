<html>
    <head>
    </head>
    <body>
        <center>
            <?php 
                error_reporting(E_ALL ^ E_NOTICE);

                //buat koneksi
                $conn = mysqli_connect("localhost","root","1234","informatika");

                //deklarasi 
                $NIMLAMA = $_POST["NIMLAMA"];
                $NIM = $_POST["NIM"];
                $Nama = $_POST["Nama"];
                $Kelas = $_POST["Kelas"];
                $Alamat = $_POST["Alamat"];
                $Submit = $_POST["Submit"];
                $Ubah = $_POST["Ubah"];
                
                //button event
                if($Submit) {
                    if($NIM == "") {
                        echo "NGGAK BOLEH";
                    } elseif($Nama == "") {
                        echo "NGGAK BOLEH";
                    } elseif($Kelas == "") {
                        echo "NGGAK BOLEH";
                    } elseif($Alamat == "") {
                        echo "NGGAK BOLEH";
                    } else {
                        $insert = "INSERT INTO mahasiswa VALUES ('$NIM', '$Nama', '$Kelas', '$Alamat')";
                        mysqli_query($conn,$insert);
                        echo "<h3>INSERTED</h3>";
                    }
                } elseif ($Ubah) {
                    if($NIM == "") {
                        echo "NGGAK BOLEH";
                    } elseif($Nama == "") {
                        echo "NGGAK BOLEH";
                    } elseif($Kelas == "") {
                        echo "NGGAK BOLEH";
                    } elseif($Alamat == "") {
                        echo "NGGAK BOLEH";
                    } else {
                        $update = "UPDATE mahasiswa 
                        SET NIM='$NIM', Nama='$Nama', Kelas='$Kelas', Alamat='$Alamat'
                        WHERE NIM= '$NIMLAMA'";
                        mysqli_query($conn,$update);
                        echo "<h3>UPDATED</h3>";
                    }
                }
                
                //linking hapus dan ubah
                if($_GET["hps"]) {
                    $NIM = $_GET["hps"];
                    $delete = "DELETE FROM mahasiswa where nim='$NIM'";
                    mysqli_query($conn,$delete);
                    echo "<h3>DELETED</h3>";
                } elseif($_GET["ubh"]) {
                    $NIM = $_GET["ubh"];
                    $cari = "SELECT * from mahasiswa where nim='$NIM'";
                    $hasil = mysqli_query($conn,$cari);
                    $dataMahasiswa = mysqli_fetch_row($hasil);
                }
            ?>


            <!--membuat input-->
            <form action="cobauts.php" method="POST">
                <table border='0'>
                    <tr>
                        <td> NIM </td>
                        <td> : </td>
                        <td> <input type="text" name="NIM" value="<?php echo $dataMahasiswa[0] ?>">
                            <input type="hidden" name="NIMLAMA" value="<?php echo $dataMahasiswa[0] ?>"> </td>
                    </tr>
                    <tr>
                        <td> Nama </td>
                        <td> : </td>
                        <td> <input type="text" name="Nama" value="<?php echo $dataMahasiswa[1] ?>">
                    </tr>
                    <tr>
                        <td> Kelas </td>
                        <td> : </td>
                        <td> <input type="radio" name="Kelas" value="A" <?php if($dataMahasiswa[2] == "A") {echo "checked"; } ?>>A
                        <input type="radio" name="Kelas" value="B" <?php if($dataMahasiswa[2] == "B") {echo "checked"; } ?>>B
                        <input type="radio" name="Kelas" value="C" <?php if($dataMahasiswa[2] == "C") {echo "checked"; } ?>>C </td>
                    </tr>
                    <tr>
                        <td> Alamat </td>
                        <td> : </td>
                        <td> <input type="text" name="Alamat" value="<?php echo $dataMahasiswa[3]; ?>">
                    </tr>
                    <tr>
                        <td></td>
                        <td></td>
                        <td>
                            <?php 
                                if($dataMahasiswa) {
                                    echo "<input type='submit' name='Ubah' value='Ubah'>";
                                } else {
                                    echo "<input type='submit' name='Submit' value='Submit'>";
                                }
                            ?>
                        </td>
                    </tr>
                </table>
            </form>
            
            <hr>
            <table border='1'>
                <tr>
                    <td> NIM </td>
                    <td> Nama </td>
                    <td> Kelas </td>
                    <td> Alamat </td>
                    <td> Aksi </td>
                </tr>
                <?php 
                    $cari = "SELECT * from mahasiswa";
                    $hasil = mysqli_query($conn, $cari);
                    while ($data = mysqli_fetch_row($hasil)) {
                        echo "<tr> 
                            <td> $data[0] </td>
                            <td> $data[1] </td>
                            <td> $data[2] </td>
                            <td> $data[3] </td>
                            <td> 
                                <a href='cobauts.php?ubh=$data[0]'> ubah </a>
                                <a href='cobauts.php?hps=$data[0]'> hapus </a>
                            </td>
                        </tr>";
                    }
                ?>
            </table>
            
        </center>
    </body>
</html>