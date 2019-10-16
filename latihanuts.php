<html>
    <head>
        <title>coba</title>
    </head>
    <body>
        <center>
            <?php 
                error_reporting(E_ALL ^ E_NOTICE);
                $conn = mysqli_connect("localhost", "root", "1234", "informatika");
                
                $NIMLAMA = $_POST["NIMLAMA"];
                $NIM = $_POST["NIM"];
                $Nama = $_POST["Nama"];
                $Kelas = $_POST["Kelas"];
                $Alamat = $_POST["Alamat"];

                $SUBMIT = $_POST["Submit"];
                $UBAH = $_POST["Ubah"];

                if ($SUBMIT) {
                    if ($NIM == "") {
                        echo "NGGAK BOLEH KOSONG";
                    } elseif ($Nama == "") {
                        echo "NGGAK BOLEH KOSONG";
                    } elseif ($Kelas == "") {
                        echo "NGGAK BOLEH KOSONG";
                    } elseif ($Alamat == "") {
                        echo "NGGAK BOLEH KOSONG";
                    } else {
                        $insert = "INSERT INTO mahasiswa VALUES ('$NIM', '$Nama', '$Kelas', '$Alamat')";
                        mysqli_query($conn, $insert);
                        echo "<h3>INSERTED</h3>";
                    }
                } elseif ($UBAH) {
                    if ($NIM == "") {
                        echo "NGGAK BOLEH KOSONG";
                    } elseif ($Nama == "") {
                        echo "NGGAK BOLEH KOSONG";
                    } elseif ($Kelas == "") {
                        echo "NGGAK BOLEH KOSONG";
                    } elseif ($Alamat == "") {
                        echo "NGGAK BOLEH KOSONG";
                    } else {
                        $update = "UPDATE mahasiswa 
                                    SET NIM='$NIM', Nama='$Nama', Kelas='$Kelas', Alamat='$Alamat'
                                    WHERE NIM= '$NIMLAMA'";
                        mysqli_query($conn, $update);
                        echo "updated";
                    }
                }

                if($_GET["hps"]) {
                    $NIM = $_GET["hps"];
                    $delete = "DELETE FROM mahasiswa WHERE NIM = '$NIM'";
                    mysqli_query($conn, $delete);
                    echo "deleted";
                } elseif ($_GET["ubh"]) {
                    $NIM = $_GET["ubh"];
                    $cari = "SELECT * FROM mahasiswa WHERE NIM='$NIM'";
                    $hasil = mysqli_query($conn, $cari);
                    $dataMahasiswa = mysqli_fetch_row($hasil);
                }
            ?>

            <form method="post" action="latihanuts.php">
			<table>
				<tr>
					<td>NIM</td>
					<td>:</td>
					<td> 
						<input type="text" name="NIM" value="<?php echo $dataMahasiswa[0] ?>">
						<!-- Membuat input baru dengan type hidden untuk mengirimkan NIM lama atau NIM yang belum di ubah sebagai acuan untuk men-select data -->
						<input type="hidden" name="NIMLAMA" value="<?php echo $dataMahasiswa[0] ?>">
					</td>
				</tr>
				<tr>
					<td>Nama</td>
					<td>:</td>
					<td>
						<input type="text" name="Nama" value="<?php echo $dataMahasiswa[1] ?>">
					</td>
				</tr>
				<tr>
					<td>Kelas</td>
					<td>:</td>
					<td>
						<input type="radio" name="Kelas" value="A" <?php if ($dataMahasiswa[2]=="A") { echo "checked"; } ?> >A
						<input type="radio" name="Kelas" value="B" <?php if ($dataMahasiswa[2]=="B") { echo "checked"; } ?> >B
						<input type="radio" name="Kelas" value="C" <?php if ($dataMahasiswa[2]=="C") { echo "checked"; } ?> >C
					</td>
				</tr>
				<tr>
					<td>Alamat</td>
					<td>:</td>
					<td>
						<input type="text" name="Alamat" value="<?php echo $dataMahasiswa[3] ?>">
					</td>
				</tr>
				<tr>
					<td></td>
					<td></td>
					<td>
						<?php
							// Cek apakah dataMahasiswa ada atau tidak
							if ($dataMahasiswa) {
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
        <table border="1">
			<tr>
				<td>NIM</td>
				<td>Nama</td>
				<td>Kelas</td>
				<td>Alamat</td>
				<td>Aksi</td>
			</tr>
			<?php
				$cari = "SELECT * FROM mahasiswa";
				$hasil = mysqli_query($conn, $cari);
				while ($data = mysqli_fetch_row($hasil)){
					// Tambahkan tombol ubah dan hapus dengan link menuju file ini dan dengan mengirim data $_GET dengan value NIM
					echo "
						<tr>
							<td>$data[0]</td>
							<td>$data[1]</td>
							<td>$data[2]</td>
							<td>$data[3]</td>
							<td>
								<a href='latihanuts.php?ubh=$data[0]'>Ubah</a>
								<a href='latihanuts.php?hps=$data[0]'>Hapus</a>
							</td>
						</tr>
					";
				}
			?>
		</table>
        
        </center>
    </body>
</html>