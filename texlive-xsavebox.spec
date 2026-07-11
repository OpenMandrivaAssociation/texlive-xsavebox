%global tl_name xsavebox
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.18
Release:	%{tl_revision}.1
Summary:	Saveboxes for repeating content without code replication, based on PDF Form X...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xsavebox
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xsavebox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xsavebox.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xsavebox.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines commands for saving content that can be repeatedly
placed into the document without replicating DVI/PDF code in the output
file, allowing for smaller file size of the final PDF and improved
content caching for faster display in certain PDF viewers. The method
makes use of 'Form XObjects' defined in the PDF specification. The user
commands are modelled after the standard LaTeX commands \savebox, \sbox,
\usebox and the lrbox environment. All common TeX engines and back-ends
are supported: pdfLaTeX, LuaLaTeX LaTeX - dvips - ps2pdf/Distiller
(Xe)LaTeX - (x)dvipdfmx

