filename=main

pdf: .images
	pdflatex ${filename}.tex
	bibtex ${filename}||true
	pdflatex ${filename}.tex
	pdflatex ${filename}.tex
	#ps2pdf ${filename}.ps

pdf-clean: pdf
	rm -f ${filename}.log
	rm -f ${filename}.aux
	rm -f ${filename}.out
	rm -f ${filename}.dvi
	rm -f ${filename}.bbl
	rm -f ${filename}.blg
	rm -f ${filename}.toc
	rm -f ${filename}.ps

.images:
	cd images && make 

#pdf-print: ps
#	ps2pdf -dColorConversionStrategy=/LeaveColorUnchanged -dPDFSETTINGS=/printer ${filename}.ps
#
#text: html
#	html2text -width 100 -style pretty ${filename}/${filename}.html | sed -n '/./,$$p' | head -n-2 >${filename}.txt
#
#html:
#	@#latex2html -split +0 -info "" -no_navigation ${filename}
#	htlatex ${filename}
#
#ps:	dvi
#	dvips -t letter ${filename}.dvi
#
#dvi:
#	latex ${filename}
#	bibtex ${filename}||true
#	latex ${filename}
#	latex ${filename}

read:
	evince ${filename}.pdf &

aread:
	acroread ${filename}.pdf

clean:
	rm -f ${filename}.{ps,pdf,log,aux,out,dvi,bbl,blg}
	rm -f ${filename}.log
	rm -f ${filename}.aux
	rm -f ${filename}.out
	rm -f ${filename}.dvi
	rm -f ${filename}.bbl
	rm -f ${filename}.blg
	rm -f ${filename}.toc
	rm -f ${filename}.ps
	rm -f ${filename}.pdf
