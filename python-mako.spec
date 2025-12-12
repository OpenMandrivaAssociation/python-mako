%define tarname Mako

Summary:	Mako template library for Python
Name:		python-mako
Version:	1.3.10
Release:	2
Group:		Development/Python
License:	MIT
Url:		https://www.makotemplates.org/
Source0:	https://files.pythonhosted.org/packages/source/m/mako/mako-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-beaker
BuildRequires:	python-markupsafe
# Nose looks like abandonware without support for new python
#BuildRequires:	python-nose
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
BuildRequires:	python-pkg-resources
Requires:	python-beaker >= 1.1
Requires:	python-markupsafe >= 0.9.2
%rename		python3-mako
BuildSystem:  python

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
%{python_sitelib}/mako-%{version}.dist-info
%{python_sitelib}/mako/
