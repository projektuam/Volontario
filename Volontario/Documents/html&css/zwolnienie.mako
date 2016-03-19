## -*- coding: utf-8 -*-
<!DOCTYPE html>
<html >
<head>
</head>


<style type="text/css">

* {
margin: 0;
padding: 0;
border: 0;
line-height: 1.4em;
vertical-align: baseline;
text-decoration: none;
outline: 0;
}

p {
	font: 1em arial, sans-serif;
	font-size: 12pt;
	line-height: 0.75cm;
	
}

div.c {
	text-align: left;
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
	font: 18px Serif, sans-serif;
	position: bottom;
}

.right {
	font-size: 12pt;
    position: absolute;
    right: 0px;
    padding: 0px;
}

div.p {
   font-size: 11pt;
   width: 250px;
   position: relative;   
   float: left;
   overflow: auto;
}

div.l {
   font-size: 11pt;
   width: 250px;
   position: relative;   
   float: right;
   overflow: auto;
}


</style>

<page size="A4"></page>

<body>
  
	<div class="right">
	<i>
		UNIWERSYTET IM. ADAMA MICKIEWICZA<br>
		Wydział Studiów Edukacyjnych<br>
		Wydziałowe Centrum Wolontariatu "VOLONTARIO"<br><br><br>
	</i>
	</div>

	<br><br><br><br><br><br><br>
    <!-- Data -->
    <div class="right">
		<p>	
			${place[0]}, dnia ${date[0][8:10]}.${date[0][5:7]}.${date[0][0:4]}r. 
		</p>
	</div>
	<br><br><br><br><br>
  	
  	<center>USPRAWIEDLIWIENIE<br><br>
  	
<p { style="text-align: justify"}>
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Zwracam się z uprzejmą prośbą o usprawiedliwienie nieobecności Pana(-i) <strong>${chart3[0]}</strong>, ${text2[0]} na zajęciach w dniu ${chart[0]}, w godzinach ${chart2[0]}.
<br>
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Powodem nieobecności był aktywny udział Wolontariuszszki(-sza) w organizacji ${text3[0]} w ramach działań Wydziałowego Centrum Wolontariatu VOLONTARIO WSE UAM. 
</p>

	<br><br><br>
	<div class="c">
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Z wyrazami szacunku
	</div>

	</center>
<br><br>
<div>
	<div class="p">
  		${sign1[0]} <br><br><br>
  		${sign2[0]} <br>
	</div>
	<div class="l">
	  	${sign3[0]} <br><br><br>
  		${sign4[0]} <br>
  	</div>
</div>

<footer>

<img src="{% static 'images/logo-wse.png' %}" class="img-responsive">
<div class="right">
	<a>
 		<br><br><br><br><br><br><br><br><br>	
 		ul. Szamarzewskiego 89 pok.24a, 60-568 Poznan<br>
 		Konto: BZ WBK  77 1090 1362 0000 0000 3601 7903 (tytulem: 706.000)<br>
 		tel. 661 254 220 (Agnieszka Bojarczuk), 601 076 771 (Marta Kałużna), 784 037 979 (Marta Wydmuch)<br>
 		volontario.uam@gmail.com<br>
	<b>
 		&nbsp;&nbsp;www.amu.edu.pl&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 	</b>
	</a>
</div>
</footer>

</body>
</html>
