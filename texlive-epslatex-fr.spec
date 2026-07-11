%global tl_name epslatex-fr
%global tl_revision 19440

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	French version of graphics in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/epslatex/french
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/epslatex-fr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/epslatex-fr.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is the French translation of epslatex, and describes how to use
imported graphics in LaTeX(2e) documents.

