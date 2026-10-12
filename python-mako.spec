%define module mako

Summary:	Mako template library for Python
Name:		python-mako
Version:	1.3.12
Release:	2
Group:		Development/Python
License:	MIT
Url:		https://www.makotemplates.org/
Source0:	https://files.pythonhosted.org/packages/source/m/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(beaker)
BuildRequires:	python%{pyver}dist(markupsafe)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
Requires:	python%{pyver}dist(beaker) >= 1.1
%rename		python3-mako

%description
Mako is a template library written in Python. It provides a familiar, non-XML
syntax which compiles into Python modules for maximum performance. Mako's
syntax and API borrows from the best ideas of many others, including Django
templates, Cheetah, Myghty, and Genshi. Conceptually, Mako is an embedded
Python (i.e. Python Server Page) language, which refines the familiar ideas of
componentized layout and inheritance to produce one of the most straightforward
and flexible models available, while also maintaining close ties to Python
calling and scoping semantics.

%files
%{_bindir}/mako-render
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
