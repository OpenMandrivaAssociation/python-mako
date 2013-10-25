%define		tarname	Mako

Summary:	Mako template library for Python
Name:		python-mako
Version:	0.9.0
Release:	1
Group:		Development/Python
License:	MIT
URL:		http://www.makotemplates.org/
Source0:	http://www.makotemplates.org/downloads/Mako-%{version}.tar.gz
BuildArch:	noarch
Requires:	python-beaker >= 1.1
Requires:	python-markupsafe >= 0.9.2
BuildRequires:	python-setuptools
BuildRequires:	python-nose
BuildRequires:	python-beaker >= 1.1
BuildRequires:	python-markupsafe >= 0.9.2
BuildRequires:	python-devel

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
%{_bindir}/mako-render
%{py_puresitedir}/mako
%{py_puresitedir}/Mako*
