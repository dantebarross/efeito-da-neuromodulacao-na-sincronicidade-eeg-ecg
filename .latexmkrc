$pdf_mode = 1;
$bibtex_use = 2;  # Garante que BibTeX rode quando necessário
$pdflatex = "pdflatex -interaction=nonstopmode -synctex=1 %O %S";
$pdflatex .= " && bibtex %B && pdflatex %O %S && pdflatex %O %S";
