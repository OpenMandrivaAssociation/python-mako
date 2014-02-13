%define		tarname	Mako
%define		name	python-mako
%define		version	0.7.2
%define		rel		1
%define		release	%{rel}

Summary:	Mako template library for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Development/Python 
License:	MIT
URL:		http://www.makotemplates.org/
Source0:	http://www.makotemplates.org/downloads/%{tarname}-%{version}.tar.gz
BuildArch:	noarch
Requires:	python-beaker >= 1.1
Requires:	python-markupsafe >= 0.9.2
BuildRequires:	python-setuptools
BuildRequires:	python-nose
BuildRequires:	python-beaker >= 1.1
BuildRequires:	python-markupsafe >= 0.9.2
BuildRequires:	pkgconfig(python)

%description
Mako is a template library written in Python. It provides a familiar, non-XML
syntax which compiles into Python modules for maximum performance. Mako's
syntax and API borrows from the best ideas of many others, including Django
templates, Cheetah, Myghty, and Genshi. Conceptually, Mako is an embedded
Python (i.e. Python Server Page) language, which refines the familiar ideas of
componentized layout and inheritance to produce one of the most straightforward
and flexible models available, while also maintaining close ties to Python
calling and scoping semantics.

%prep
%setup -q -n %{tarname}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --root %{buildroot}

#check 
#__python setup.py test

%files
%doc CHANGES LICENSE README.rst doc examples
%_bindir/mako-render
%py_sitedir/mako
%py_sitedir/Mako*



%changelog
* Fri Jul 20 2012 Lev Givon <lev@mandriva.org> 0.7.2-1
+ Revision: 810439
- Update to 0.7.2.

* Mon Jul 09 2012 Lev Givon <lev@mandriva.org> 0.7.1-1
+ Revision: 808555
- Update to 0.7.1.

* Thu Feb 02 2012 Lev Givon <lev@mandriva.org> 0.6.2-1
+ Revision: 770765
- Update to 0.6.2.
- Update to 0.6.1.

* Sun Jan 22 2012 Lev Givon <lev@mandriva.org> 0.6.0-1
+ Revision: 764901
- Update to 0.6.0.

* Tue Jan 03 2012 Lev Givon <lev@mandriva.org> 0.5.0-1
+ Revision: 749291
- Update to 0.5.0

* Wed Sep 07 2011 Lev Givon <lev@mandriva.org> 0.4.2-1
+ Revision: 698756
- Update to 0.4.2.

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-2
+ Revision: 667956
- mass rebuild

* Mon Feb 21 2011 Lev Givon <lev@mandriva.org> 0.4.0-1
+ Revision: 639231
- Update to 0.4.0.

* Mon Nov 15 2010 Lev Givon <lev@mandriva.org> 0.3.6-1mdv2011.0
+ Revision: 597741
- Update to 0.3.6.

* Sun Oct 31 2010 John Balcaen <mikala@mandriva.org> 0.3.5-2mdv2011.0
+ Revision: 590960
- Rebuild for python 2.7

* Wed Oct 20 2010 Lev Givon <lev@mandriva.org> 0.3.5-1mdv2011.0
+ Revision: 587007
- Update to 0.3.5.

* Tue Aug 17 2010 Michael Scherer <misc@mandriva.org> 0.3.4-2mdv2011.0
+ Revision: 570998
- add missing Requires

* Sun Jul 11 2010 Lev Givon <lev@mandriva.org> 0.3.4-1mdv2011.0
+ Revision: 551168
- Update to 0.3.4.
- Update to 0.3.3.

* Fri Apr 16 2010 Frederik Himpe <fhimpe@mandriva.org> 0.3.2-1mdv2010.1
+ Revision: 535572
- update to new version 0.3.2

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.5-2mdv2010.1
+ Revision: 523827
- rebuilt for 2010.1

* Wed Jan 27 2010 Frederik Himpe <fhimpe@mandriva.org> 0.2.5-1mdv2010.1
+ Revision: 497465
- update to new version 0.2.5

* Sun Jul 12 2009 Frederik Himpe <fhimpe@mandriva.org> 0.2.4-1mdv2010.0
+ Revision: 395019
- First Mandriva package based on Fedora's SPEC
- create python-mako

