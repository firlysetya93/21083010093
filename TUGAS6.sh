echo -n "input: "
read semester

declare -a IPSMhs 
i=0
let jumlah=$semester-1 

while [ $i -le $jumlah ];
do
	let nilai=$i+1
	printf " " $nilai;
	read nilaiIPS;
	IPSMhs[$i]=$nilaiIPS;
	let total=total+$nilaiIPS;
	let i=$i+1;
done

let IPK=$total/$semester
echo "IPS mhs = " $total "/" $semester
echo "IPK mhs = " $IPK

