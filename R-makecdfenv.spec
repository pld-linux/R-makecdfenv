%define		packname	makecdfenv

Summary:	CDF Environment Maker
Name:		R-%{packname}
Version:	1.38.0
Release:	1
License:	LGPL v2+
Group:		Applications/Engineering
Source0:	http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	3f2338fe3351eaa7d8a86faa5223de0c
Patch0:		bogus-deps.patch
URL:		http://bioconductor.org/packages/release/bioc/html/makecdfenv.html
BuildRequires:	R
BuildRequires:	R-Biobase
BuildRequires:	R-affy
BuildRequires:	R-affyio
BuildRequires:	texlive-latex
BuildRequires:	zlib-devel
Requires:	R
Requires:	R-Biobase
Requires:	R-affy
Requires:	R-affyio
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package has two functions. One reads a Affymetrix chip
description file (CDF) and creates a hash table environment containing
the location/probe set membership mapping. The other creates a package
that automatically loads that environment.

%prep
%setup -q -c -n %{packname}
%patch0 -p1

%build
R CMD build %{packname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Code
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/extdata
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%dir %{_libdir}/R/library/%{packname}/libs
%attr(755,root,root) %{_libdir}/R/library/%{packname}/libs/makecdfenv.so
