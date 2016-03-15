<!DOCTYPE html>
<html>
<head>
</head>

<style type="text/css">
p {
	font: 1em verdana, sans-serif;
	
}

a {
	font: 0.7em times, sans-serif;
	position: bottom;
}

b{
	color: white;
	background:black;
	border-style: solid;
	border-color: black;
}

i{
	font: 18px verdana, sans-serif;
	position: bottom;
}

.right {
    position: absolute;
    right: 0px;
    padding: 0px;

}



</style>

<page size="A4"></page>

<body>
  
	<div class="right">
	<i>
		UNIWERSYTET IM. ADAMA MICKIEWICZA<br>
		Wydzial Studiow Edukacyjnych<br>
		Wydzialowe Centrum Wolontariatu "VOLONTARIO"<br><br><br>
	</i>
	</div>

	<br><br><br><br><br><br><br><br><br>
    <!-- Data -->
    <div class="right">
		<p>	
			${place[0]}, dnia ${date[0][8:10]}.${date[0][5:7]}.${date[0][0:4]}r. 
		</p>
	</div>
	<br><br><br><br><br><br><br><br><br>
  	<br>${title[0]}<br><br><br>
  	
	${text[0]}<br><br>
  	${sign1[0]} <br>
<footer>

<img src="{% static 'images/logo-wse.png' %}" class="img-responsive">
<div class="right">
	<a>
 		<br><br><br><br><br><br><br><br><br>	
 		ul. Szamarzewskiego 89 pok.24a, 60-568 Poznan<br>
 		Konto: BZ WBK  77 1090 1362 0000 0000 3601 7903 (tytulem: 706.000)<br>
 		tel. 661 254 220 (Agnieszka Bojarczuk), 601 076 771 (Marta Kaluzna), 784 037 979 (Marta Wydmuch)<br>
 		volontario.uam@gmail.com<br>
	<b>
 		&nbsp;&nbsp;www.amu.edu.pl&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 	</b>
	</a>
</div>
</footer>

</body>
</html>
