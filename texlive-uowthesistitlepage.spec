Name:		texlive-uowthesistitlepage
Version:	3.0.1
Release:	1
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
%{_texmfdistdir}/tex/latex/uowthesistitlepage
%doc %{_texmfdistdir}/doc/latex/uowthesistitlepage

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
