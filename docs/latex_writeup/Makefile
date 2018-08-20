LATEX       = pdflatex
BASH        = bash -c
ECHO        = echo
RM          = rm -rf
RM_TMP      = ${RM} $(foreach suff, ${TMP_SUFFS}, ${NAME}.${suff})

TMP_SUFFS   = aux bbl blg log dvi ps eps out
SUFF        = pdf

CHECK_RERUN = grep Rerun $*.log

NAME    = pipeline
DOC_OUT = ${NAME}.${SUFF}

default: ${DOC_OUT}

%.pdf: %.tex
	${LATEX} $<
	( ${CHECK_RERUN} && ${LATEX} $< ) || echo "Done."
	( ${CHECK_RERUN} && ${LATEX} $< ) || echo "Done."

clean:
	${RM_TMP}