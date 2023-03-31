Name:		texlive-xsavebox
Version:	64049
Release:	2
Summary:	Saveboxes for repeating content without code replication, based on PDF Form XObjects
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xsavebox
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xsavebox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xsavebox.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xsavebox.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines commands for saving content that can be
repeatedly placed into the document without replicating DVI/PDF
code in the output file, allowing for smaller file size of the
final PDF and improved content caching for faster display in
certain PDF viewers. The method makes use of 'Form XObjects'
defined in the PDF specification. The user commands are
modelled after the standard LaTeX commands \savebox, \sbox,
\usebox and the lrbox environment. All common TeX engines and
back-ends are supported: pdfLaTeX, LuaLaTeX LaTeX - dvips -
ps2pdf/Distiller (Xe)LaTeX - (x)dvipdfmx

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/xsavebox
%{_texmfdistdir}/tex/latex/xsavebox
%doc %{_texmfdistdir}/doc/latex/xsavebox

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
