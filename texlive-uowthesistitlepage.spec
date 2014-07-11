# revision 32626
# category Package
# catalog-ctan /macros/latex/contrib/uowthesistitlepage
# catalog-date 2014-01-10 08:34:25 +0100
# catalog-license lppl1.3
# catalog-version 2.0
Name:		texlive-uowthesistitlepage
Version:	2.0
Release:	3
Summary:	Title page for dissertations at the University of Wollongong
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/uowthesistitlepage
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uowthesistitlepage.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uowthesistitlepage.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package redefines \maketitle to generate a title page for a
University of Wollongong thesis, in accordance with the UoW
branding guidelines. The package should be used with the book
class to typeset a thesis. The package also defines a
\declaration command that typesets the declaration that this
thesis is your own work, etc., which is required in the front
of each PhD Thesis.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/uowthesistitlepage/uowthesistitlepage.sty
%doc %{_texmfdistdir}/doc/latex/uowthesistitlepage/README
%doc %{_texmfdistdir}/doc/latex/uowthesistitlepage/uowthesistitlepage_doc.pdf
%doc %{_texmfdistdir}/doc/latex/uowthesistitlepage/uowthesistitlepage_doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
