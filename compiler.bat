@echo off
echo === Compilando a dissertação... ===

pdflatex dissertacao.tex
bibtex dissertacao
pdflatex dissertacao.tex
pdflatex dissertacao.tex

echo === Compilação concluída ===
pause
