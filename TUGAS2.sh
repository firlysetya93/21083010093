printf "lakukan perhitungan perkalian "
read perkalian
if [ $perkalian = "iya" ]
then 
	echo "pilih angka b: 1-10 "
	pilih=$RANDOM%10
	let a=$pilih
	echo "a=$a"
	echo "Masukkan angka b: "
	read b
	let kali=$a*$b
	echo "a * b = $kali "
	echo "hasil: "
	read hasil
	if [ $hasil ==  $kali ]
	then 
	 echo "jawabanmu benar"
	else
	 echo "jawabanmu salah" 
	fi
else 
 echo "selesai"
fi
