%define		tarname	Mako
%define		name	python-mako
%define		version	0.7.2
%define		rel		1
%if %mdkversion < 201100
%define		release	%mkrel %{rel}
%else
%define		release	%{rel}
%endif

Summary:	Mako template library for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Development/Python 
License:	MIT
URL:		http://www.makotemplates.org/
Source0:	http://www.makotemplates.org/downloads/%{tarname}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch
Requires:	python-beaker >= 1.1
Requires:	python-markupsafe >= 0.9.2
BuildRequires:	python-setuptools
BuildRequires:	python-nose
BuildRequires:	python-beaker >= 1.1
BuildRequires:	python-markupsafe >= 0.9.2
%py_requires -d

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
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --root %{buildroot}

%check 
%__python setup.py test

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGES LICENSE README.rst doc examples
%_bindir/mako-render
%py_sitedir/mako
%py_sitedir/Mako*

