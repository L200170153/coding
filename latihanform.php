<html>
    <head>
        <title>Data Mahasiswa</title>
    </head>
    <?php
        $conn = mysqli_connect('localhost', 'root', '1234', 'informatika')
    ?>
    <body>
        <h3>Form Mahasiswa</h3>
        <table>
            <form method='post' action='latihanform.php'>
                <tr>
                    <td> NIM </td>
                    <td> : </td>
                    <td> <input type='text' name='nim' size='10'></td>
                </tr>
                <tr>
                    <td> Nama </td>
                    <td> : </td>
                    <td> <input type='text' name='nama' size='30'></td>
                </tr>       
                <tr>
                    <td> Kelas </td>
                    <td> : </td>
                    <td> 
                        <input type='radio' name='kelas' value='A' checked>A
                        <input type='radio' name='kelas' value='B'>B
                        <input type='radio' name='kelas' value='C'>C
                    </td>
                </tr>
                <tr>
                    <td> Alamat </td>
                    <td> : </td>
                    <td> <input type='text' name='alamat' size='40'></td>
                </tr>
                <tr>
                    <td> <input type='submit' name='submit' value='KIRIMKAN'></td>
                </tr>
            </form>
        </table>
        <?php
            error_reporting(E_ALL^E_NOTICE);
            $nim = $_POST['nim'];
            $nama = $_POST['nama'];
            $kelas = $_POST['kelas'];
            $alamat = $_POST['alamat'];
            $submit = $_POST['submit'];
            $input = "insert into mahasiswa (nim, nama, kelas, alamat) values 
            ('$nim','$nama', '$kelas', '$alamat')";
            if($submit) {
                if($nim = '') {
                    echo "NIM tidak boleh kosong";
                } elseif ($nama = '') {
                    echo "Nama tidak boleh kosong";
                } elseif ($alamat = '') {
                    echo "Alamat tidak boleh kosong";
                } else {
                    mysqli_query($conn, $input);
                    echo "Data berhasil dimasukkan";
                }
            }
        ?>
    </body>
</html>