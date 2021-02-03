# data_processing


cutAndMask Correction

1. Abdullah_Gul & Allyson_Felix & Al_Sharpton 삭제
	- masked와 nonMasked 모두 train에 대한 데이터가 존재하지 않는다.
	  마스크 씌우기 전 총 샘플 데이터 개수 5개

2. nonMaskedOutput/test directory 제거
	

3. nonMaskedOutput/train correction

  > ahn_cheol_soo : 10 (마스크 착용)
  > Alejandro_Toledo : 21 (두사람 겹침), 39 (동일인물 X)
  > Alvaro_Uribe : 35 (동일인물 X)
  > Andre_Agassi : 20 (얼굴 내 장애물)
  > angelina_danilova : 7 (얼굴 존재 X)
  > Angelina_Jolie : 11 (선글라스)
  > anne_hathaway : 7, 15, 20 (얼굴 존재 X)
  > Ariel_Sharon : 61, 68, 72 (얼굴 내 장애물)
  > Arnold_Schwarzenegger : 8, 28 (선글라스), 40 (동일인물 X)
  > Bil_Clinton : 9 (두사람 겹침)
  > billie_eilish : 10 (동일인물 X)
  > Colin_Powell : 36, 46, 220 (동일인물 X)
  > Donald_Rumsfeld : 83 (얼굴 존재 X)
  > elton_john 		==> 선글라스 착용 사진 다수 ==> 제거!
  > eminem : 9, 20 (얼굴 존재 X)
  > George_W_Bush : 21, 22, 453, 530 (얼굴 겹침), 24, 50, 85, 100, 103, 108, 186, 244, 474, 488, 501, 527 (동일 인물 X), 447 (얼굴 내 장애물)
  > Gerhard_Schroeder : 57 (얼굴 겹침), 73, 77, 93 (동일 인물 X)
  > Gray_Davis : 6, 18, 20 (동일 인물 X), 8 (얼굴 내 장애물)
  > Hans_Blix : 26, 39 (동일 인물 X)
  > Hugo_Chavez : 32, 49 (동일 인물 X), 33, 47, 68 (얼굴 겹침), 44, 58 (얼굴 내 장애물)
  > Jacques_Chirac : 23, 46 (동일 인물 X)
  > John_Ashcroft : 17, 35 (얼굴 내 장애물)
  > kim_seon_ho : 2 (얼굴 존재 X)
  > kim_tae_hee : 17 (얼굴 존재 X)
  > kylie_jenner : 9 (얼굴 존재 X)
  > lucas_bravo : 9 (얼굴 존재 X)
  > madonna : 23 (선글라스)
> Mahmoud_Abbas : 7, 8, 10, 18 (선글라스), 12, 21 (동일 인물 X)
> Megawati_Sukarnoputri : 12 (선글라스)
> Michael_Bloomberg : 12 (동일인물 X)
> mindy_kaling : 19 (선글라스)
> Paul_Bremer : 14 (얼굴 내 장애물)
> peter_dinklage : 7, 8 (얼굴 존재 X)
> Recep_Tayyip_Erdogan : 6 (얼굴 불명확), 8 (동일인물 X), 26 (얼굴 내 장애물)
> Serena_Williams : 40, 49 (얼굴 내 장애물)
> Silvio_Berlusconi : 15 (얼굴 내 장애물)
> suzy : 13 (얼굴 존재 X), 24, 25, 28 (얼굴 내 장애물)
> Tiger_Woods : 23 (얼굴 내 장애물)
> Tony_Blair : 69, 143 (동일인물 X), 96 (사진 부정확)


4. maskedOutput/test

> Angelina_Jolie : 4 (사진 부정확)
> elton_john			==> 선글라스 착용 사진 다수 ==> 제거!
> fan_bingbing : 5 (얼굴 미포함)
> lgor_lvanov : 1 (두사람 겹침)
> Jean_Chretien : 5 (동일인물 X)
> Jeremy_Greenstock : 1 (동일인물 X)
> john_legend : 3, 5 (얼굴 미포함)
> John_Negroponte : 4 (두사람 겹침)
> kylie_jenner : 4 (얼굴 미포함)
> Roh_Moo-hyun : 4 (동일인물 X)




5. maskedOutput/train

> Alejandro_Toledo : 21 (두사람 겹침), 39 (동일인물 X)
> Alvaro_Uribe : 6, 18, 33, 34 (선글라스 착용), 35 (동일인물 X)
> angelina_danilova : 7 (얼굴 미포함)
> Angelina_Jolie : 11 (선글라스 착용)
> anne_hathaway : 7, 15, 20 (얼굴 미포함)
> Arnold_Schwarzenegger : 8, 28 (선글라스 착용), 40 (동일인물 X)
> billie_eilish : 10 (동일인물 X)
> Colin_Powell : 36, 220 (동일인물 X)
> elton_john			==> 선글라스 착용 사진 다수 ==> 제거!
> eminem : 9, 20 (얼굴 미포함)
> George_W_Bush : 21, 24, 50, 100, 103, 186, 474, 530 (동일인물 X), 276 (두사람 겹침), 283 (선글라스 착용)
> Gerhard_Schroeder : 93 (동일인물 X)
> Gray_Davis : 6, 18, 20 (동일인물 X)
> Hans_Blix : 11, 39 (동일인물 X)
> Hugo_Chavez : 47 (두사람 겹침), 49 (동일인물 X)
> Jacques_Chirac : 46 (동일인물 X), 23 (사진 부정확)
> Jean_Chretien : 16 (동일인물 X)
> jerry_seinfeld : 21 (동일인물 X)
> kim_seon_ho : 8 (얼굴 미포함)
> kim_tae_hee : 17 (얼굴 미포함)
> kylie_jenner : 9 (얼굴 미포함)
> Laura_Bush : 30 (동일인물 X)
> lucas_bravo : 9 (얼굴 미포함)
> madonna : 23 (선글라스 착용), 16, 21 (사진 부적격)
> Mahmoud_Abbas : 12, 21 (동일인물 X), 7, 8 (선글라스 착용)
> Megawati_Sukarnoputri : 12 (선글라스 착용)
> mindy_kaling : 19 (선글라스 착용)
> peter_dinklage : 7, 8 (얼굴 미포함)
> Recep_Tayyip_Erdogan : 23 (두사람 겹침), 6 (사진 부정확)
> suzy : 13 (얼굴 미포함)
> Tony_Blair : 60, 143 (동일인물 X)
> will_smith : 16, 17 (선글라스 착용)

























