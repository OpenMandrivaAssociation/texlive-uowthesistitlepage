%global tl_name uowthesistitlepage
%global tl_revision 54512

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0.1
Release:	%{tl_revision}.1
Summary:	Title page for dissertations at the University of Wollongong
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/uowthesistitlepage
License:	lppl1.3c cc-by-sa-4
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uowthesistitlepage.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uowthesistitlepage.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package redefines \maketitle to generate a title page for a
University of Wollongong thesis, in accordance with the UoW branding
guidelines. The package should be used with the book class to typeset a
thesis. The package also defines a \declaration command that typesets
the declaration that this thesis is your own work, etc., which is
required in the front of each PhD Thesis.

