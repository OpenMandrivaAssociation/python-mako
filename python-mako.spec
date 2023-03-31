%define tarname Mako
%bcond_with python2

Summary:	Mako template library for Python
Name:		python-mako
Version:	1.2.4
Release:	2
Group:		Development/Python
License:	MIT
Url:		http://www.makotemplates.org/
Source0:	https://files.pythonhosted.org/packages/source/M/Mako/Mako-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-beaker
BuildRequires:	python-markupsafe
BuildRequires:	python-nose
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
BuildRequires:	python-pkg-resources
Requires:	python-beaker >= 1.1
Requires:	python-markupsafe >= 0.9.2
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

%if %{with python2}
%package -n python2-mako
Summary:	Mako template library for Python3
Group:		Development/Python
Requires:	python-beaker >= 1.1
Requires:	python2-markupsafe >= 0.9.2
BuildRequires:	python2-markupsafe
BuildRequires:	python2-distribute
BuildRequires:	python2-pkg-resources
BuildRequires:	python2-beaker
BuildRequires:	python2-nose
BuildRequires:	pkgconfig(python2)

%description -n python2-mako
Mako is a template library written in Python. It provides a familiar, non-XML
syntax which compiles into Python modules for maximum performance. Mako's
syntax and API borrows from the best ideas of many others, including Django
templates, Cheetah, Myghty, and Genshi. Conceptually, Mako is an embedded
Python (i.e. Python Server Page) language, which refines the familiar ideas of
componentized layout and inheritance to produce one of the most straightforward
and flexible models available, while also maintaining close ties to Python
calling and scoping semantics
%endif

%prep
%setup -q -c

mv %{tarname}-%{version} python2
cp -r python2 python3

%install
%if %{with python2}
cd python2
PYTHONDONTWRITEBYTECODE=yes python2 setup.py install --root %{buildroot}
mv %{buildroot}/%{_bindir}/mako-render %{buildroot}/%{_bindir}/python2-mako-render
cd ..
%endif

cd python3
PYTHONDONTWRITEBYTECODE=yes python setup.py install --root %{buildroot}
cd ..

#check
#__python setup.py test

%files
%doc python3/CHANGES python3/LICENSE python3/README.rst python3/doc python3/examples
%{_bindir}/mako-render
%{py_puresitedir}/mako
%{py_puresitedir}/Mako*

%if %{with python2}
%files -n python2-mako
%doc python2/CHANGES python2/LICENSE python2/README.rst python2/doc python2/examples
%{py2_puresitedir}/mako
%{py2_puresitedir}/Mako*
%{_bindir}/python2-mako-render 
%endif
