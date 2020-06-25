mkdir Tolima
cd Tolima
cp ../DatosTolima.dat DatosTolima.dat
cp ../PlotsTolima.py PlotsTolima.py

awk '{ split($1,array, " ");
	if (array[1]=="March")
	   print $4" "$6 
	 

	 split ($2,array, " ");
	if (array[1]=="March")
	   print $5" "$7  }' DatosTolima.dat > DatosMarzo.txt



awk '{ split ($1,array, " ");
	if (array[1]=="March" || array[1]=="April" || array[1]=="May" || array[1]=="June" || array[1]=="July" || array[1]=="August" || array[1]=="September" || array[1]=="October" || array[1]=="November" || array[1]=="December" || array[1]=="January"|| array[1]=="February")

	   print $4" "$6


	 split ($2,array, " ");


	if (array[1]=="March" || array[1]=="April" || array[1]=="May" || array[1]=="June" || array[1]=="July" || array[1]=="August" || array[1]=="September" || array[1]=="October" || array[1]=="November" || array[1]=="December" || array[1]=="January" || array[1]=="February")
	   print $5" "$7}' DatosTolima.dat > GRF_vs_EQ.txt



python PlotsTolima.py

rm DatosTolima.dat

