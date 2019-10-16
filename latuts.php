<html>
    <head>
    </head>
    <body>
        <?php 
            error_reporting(E_ALL ^ E_NOTICE);

            $conn = mysqli_connect("localhost","root","1234","toko");

            $id = $_POST["id"];
            $idawal = $_POST["idawal"];
            $nama = $_POST["nama"];
            $jenis = $_POST["jenis"];
            $harga = $_POST["harga"];
            $submit = $_POST["submit"];
            $ubah = $_POST["ubah"];

            if($submit) {
                if($id == "") {
                    echo "nggak boleh";
                } elseif($nama == "") {
                    echo "nggak boleh";
                } elseif($jenis == "") {
                    echo "nggak boleh";
                } elseif($harga == "") {
                    echo "nggak boleh";
                } else {
                    $insert = "INSERT INTO barang values ('$id', '$nama', '$jenis', '$harga')";
                    mysqli_query($conn, $insert);
                    echo "INSERTED";
                }
            } elseif($ubah) {
                if($id == "") {
                    echo "nggak boleh";
                } elseif($nama == "") {
                    echo "nggak boleh";
                } elseif($jenis == "") {
                    echo "nggak boleh";
                } elseif($harga == "") {
                    echo "nggak boleh";
                } else {
                    $update = "UPDATE barang
                                SET id='$id', nama='$nama', jenis='$jenis', harga='$harga'
                                where id='$idawal'";
                    mysqli_query($conn, $update);
                    echo "updated";
                }
            }

            if($_GET["hps"]) {
                $id = $_GET["hps"];
                $delete = "DELETE FROM barang WHERE id='$id'";
                mysqli_query($conn, $delete);
                echo "deleted";
            } elseif($_GET["ubh"]) {
                $id = $_GET["ubh"];
                $cari = "SELECT * FROM barang WHERE id='$id'";
                $hasil = mysqli_query($conn, $cari);
                $dataBarang = mysqli_fetch_row($hasil);
            }
        ?>

        <form action='latuts.php' method='post'>
            <table>
                <tr>
                    <td>id</td>
                    <td>:</td>
                    <td><input type=text name='id' value="<?php echo $dataBarang[0] ?>">
                    <input type=hidden name='idawal' value="<?php echo $dataBarang[0] ?>">
                    </td>
                </tr>
                <tr>
                    <td>nama</td>
                    <td>:</td>
                    <td><input type=text name='nama' value="<?php echo $dataBarang[1] ?>"></td>
                </tr>
                <tr>
                    <td>jenis</td>
                    <td>:</td>
                    <td><input type=radio name='jenis' value='A'<?php if($dataBarang[2]=='A') {echo "checked";}?>>A
                    <input type=radio name='jenis' value='B'<?php if($dataBarang[2]=='B') {echo "checked";}?>>B
                    <input type=radio name='jenis' value='B'<?php if($dataBarang[2]=='C') {echo "checked";}?>>C
                    </td>
                </tr>
                <tr>
                    <td>harga</td>
                    <td>:</td>
                    <td><input type=text name='harga' value="<?php echo $dataBarang[3] ?>"></td>
                </tr>
                <tr>
                    <td></td>
                    <td></td>
                    <td>
                        <?php 
                            if($dataBarang) {
                                echo "<input type='submit' name='ubah' value='ubah'>";
                            } else {
                                echo "<input type='submit' name='submit' value='submit'>";
                            }
                        ?>
                    </td>
                </tr>
            </table>
        </form>

        <hr>

        <table border='1'>
            <tr>
                <td>ID</td>
                <td>NAMA</td>
                <td>JENIS</td>
                <td>HARGA</td>
                <td>AKSI</td>
            </tr>
            
            <?php 
                $cari = "SELECT * FROM barang";
                $hasil = mysqli_query($conn,$cari);
                while($data = mysqli_fetch_row($hasil)) {
                    echo "
                        <tr>
                            <td>$data[0]</td>
                            <td>$data[1]</td>
                            <td>$data[2]</td>
                            <td>$data[3]</td>
                            <td>
                                <a href='latuts.php?ubh=$data[0]'>ubah</a>
                                <a href='latuts.php?hps=$data[0]'>hapus</a>
                            </td>
                        </tr>
                    ";
                }
            ?>
        </table>
    </body>
</html>