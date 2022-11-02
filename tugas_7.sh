panjang() {
 echo "Masukkan panjang : "
 read panjang
}
lebar() {
 echo "Masukkan lebar : "
 read lebar
}
luas() {
 let persegi=$panjang*$lebar
 echo "luas persegi : 
$persegi "
 read luas persegi
}
panjang
lebar
luas
