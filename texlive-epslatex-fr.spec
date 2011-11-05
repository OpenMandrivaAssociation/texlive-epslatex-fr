# revision 19440
# category Package
# catalog-ctan /info/epslatex/french
# catalog-date 2007-02-08 01:16:19 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-epslatex-fr
Version:	20070208
Release:	1
Summary:	French version of "graphics in LaTeX"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/epslatex/french
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epslatex-fr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epslatex-fr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This is the French translation of epslatex, and describes how
to use imported graphics in LaTeX(2e) documents.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/Ball.eps
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/CHAP2.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/Construction.eps
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/Franc-chap.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/README
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/README.TEXLIVE
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/Warning.eps
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/alltex.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/auteurs.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/bases.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/block.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/box1.eps
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/box2.eps
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/boxes.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/btxdoc.bib
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/cm.eps
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/cm.ps
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/danger.eps
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/divers.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/ebnf.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/export.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/fepslatex.pdf
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/fepslatex.tex
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/fill.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/fmparhack.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/foot.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/fr.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/franc.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/frnew.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/g_toc_entry.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/graphic.eps
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/hands.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/header.tex
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/indentondemand.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/makecmds.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/makerobust.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/mass.eps
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/mypatches.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/myvarioref.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/nrfoot.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/origin.eps
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/overlay.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/pale.eps
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/pend.eps
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/pretzel.eps
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/pretzel.ps
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/rdanger.eps
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/rosette.eps
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/rosette.ps
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/sgte.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/smaller.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/square.eps
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/topcapt.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/topfig.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/warn.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/wdesc.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/whitecdp.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/wide.eps
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/widecenter.sty
%doc %{_texmfdistdir}/doc/latex/epslatex-fr/xb.sty
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
