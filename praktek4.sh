echo -n "masukkan angka ganjil: "
read angka
i=0

until [ ! $angka -gt $i ]
do
 echo "$angka adalah  ganjil"
 angka=$((angka - 2))
done
