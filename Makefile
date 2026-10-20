# Minimal makefile for Daz Studio Khmer docs

SPHINXOPTS    ?= -W --keep-going
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = docs

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

html:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)
	@touch "$(BUILDDIR)/.nojekyll"

clean:
	rm -rf "$(BUILDDIR)"

.PHONY: help html clean Makefile
