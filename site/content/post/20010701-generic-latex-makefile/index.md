+++
title = "Generic LaTeX Makefile"
date = "2001-07-01"
tags = ['LaTeX', 'Make', 'Programming']
categories = ['Programming']
+++

https://gist.github.com/vfilby/43983dbe9e36814a7afa7b4b2ab08adc

{{< highlight make >}}
# Generic LaTeX Makefile.
#
# $ID$
#
# This makefile is to be specifically used for LaTeX documents only.
# makeindx and BiBTeX extensions are supported.  
#
# To use this makefile you must be using GNU make.  If you are
# not sure what make is installed ask your system administrator.
# You can also try running GNU make explicitly by running gmake.
#
# REQUIRED FILES, these are common on most linuxy systems.
#  - latex
#  - bibtex
#  - makeindex
#  - dvips
#  - ps2pdf
#  - echo
#  - grep
# 
# Vincent Filby Copyright (c) 2001
# 
# CONFIGURATION SECTION
#
# The base latex program and latex commandline flags
LATEX=latex
LATEXFLAGS=--interaction=nonstopmode
#
# The BiBTeX extensions.
BIBTEX=bibtex
#
# makeindex
MAKEINDEX=makeindex
#
# DVI to postscript converter, if you are
# using a different converter you will have to 
# change the syntax in the %.ps rule and the %.all rule.
DVIPS=dvips
#
# Postscript to pdf converter, if you are
# using a different converter you will have to change
# the syntax in the %.pdf rule and the %.all rule.
PS2PDF=ps2pdf
#
# Other programs
GREP=grep
ECHO=echo
#
# End of CONFIGURATION SECTION
.PHONY: clean
.SUFFIXES:

all:
	@echo "Please specify a rule."
	@echo "Here are the rules using 'file.tex' as an example."
	@echo " 'file' to run LaTeX"
	@echo " 'file.bib' to run BiBTeX"
	@echo " 'file.ind' to run makeindex"
	@echo " 'file.ps' to generate post-script"
	@echo " 'file.pdf' to generate portable document format"
	@echo " 'file.all' to itelligently run LaTeX, makeindex and BiBTeX"
	@echo " 'clean' to remove temporary, dvi, ps and pdf files" 

%: %.tex
	$(LATEX) $*.tex

%.bib: %.aux
	$(BIBTEX) $<

%.ind: %.idx
	$(MAKEINDEX) $*
	

%.pdf: %.ps
	$(PS2PDF) $< $@

%.ps: %.dvi
	$(DVIPS) -f $< > $@

clean:
	rm -f *.ps *.pdf *.ind *.ilg *.dvi *.xref *.toc\
	      *.idx *.log *.aux

# This is a special rule which will process the LaTeX
# files and bibtex or makeindex if necessary.
%.all: %.tex
#	Process the tex file
	@echo "Processing $<..."
	@$(LATEX) $(LATEXFLAGS) $< > /dev/null
	@echo "================================================================================"
	@echo "Warnings: see $*.log for more details"
	@echo "================================================================================"
	-@grep "Warning" $*.log

#	Process index if present
	$(if $(wildcard $*.idx), \
		@echo "================================================================================";\
		echo "$*.idx is present --  Generating index."; \
		echo "================================================================================";\
		$(MAKEINDEX) $*;\
		echo ">>> Re-running LaTeX silently to update index (See $*.log for errors).";\
		$(LATEX) $(LATEXFLAGS) $< > /dev/null;,\
		@echo "================================================================================";\
		echo "$*.idx is not present -- INDEX NOT GENERATED"; \
		echo "================================================================================";\
	)
	
#	Process bibtex if present
	$(if $(wildcard $*.bib), \
		@echo "================================================================================";\
		echo "$*.bib is present -- Generating bibliography"; \
		echo "================================================================================";\
		$(BIBTEX) $*.bib;\
		echo ">>> Re-running LaTeX silently to update bibliography (See $*.log for errors).";\
		$(LATEX) $(LATEXFLAGS) $< > /dev/null;,\
		@echo "================================================================================";\
		echo "$*.bib is not present -- BIBLIOGRAPHY NOT GENERATED"; \
		echo "================================================================================";\
	)

{{< /highlight >}}