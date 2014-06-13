%define		tarname	Mako

Summary:	Mako template library for Python
Name:		python-mako
Version:	0.9.1
Release:	2
Group:		Development/Python
License:	MIT
Url:		http://www.makotemplates.org/
Source0:	http://www.makotemplates.org/downloads/Mako-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-beaker
BuildRequires:	python-markupsafe
BuildRequires:	python-nose
BuildRequires:	python-setuptools
BuildRequires:	python3-distribute
BuildRequires:	python3-beaker
BuildRequires:	python3-markupsafe
BuildRequires:	python3-nose
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(python3)
Requires:	python-beaker >= 1.1
Requires:	python-markupsafe >= 0.9.2

%description
Mako is a template library written in Python. It provides a familiar, non-XML
syntax which compiles into Python modules for maximum performance. Mako's
syntax and API borrows from the best ideas of many others, including Django
templates, Cheetah, Myghty, and Genshi. Conceptually, Mako is an embedded
Python (i.e. Python Server Page) language, which refines the familiar ideas of
componentized layout and inheritance to produce one of the most straightforward
and flexible models available, while also maintaining close ties to Python
calling and scoping semantics.

%package -n python3-mako
Summary:	Mako template library for Python3
Group:		Development/Python
Requires:	python3-beaker >= 1.1
Requires:	python3-markupsafe >= 0.9.2

%description -n python3-mako
Mako is a template library written in Python. It provides a familiar, non-XML
syntax which compiles into Python modules for maximum performance. Mako's
syntax and API borrows from the best ideas of many others, including Django
templates, Cheetah, Myghty, and Genshi. Conceptually, Mako is an embedded
Python (i.e. Python Server Page) language, which refines the familiar ideas of
componentized layout and inheritance to produce one of the most straightforward
and flexible models available, while also maintaining close ties to Python
calling and scoping semantics

%prep
%setup -q -c

mv %{tarname}-%{version} python2
cp -r python2 python3

%install
pushd python3
PYTHONDONTWRITEBYTECODE=  python3 setup.py install --root %{buildroot}
mv %{buildroot}/%{_bindir}/mako-render %{buildroot}/%{_bindir}/python3-mako-render
popd

pushd python2
PYTHONDONTWRITEBYTECODE=  python setup.py install --root %{buildroot}
popd

#check
#__python setup.py test

%files
%doc python2/CHANGES python2/LICENSE python2/README.rst python2/doc python2/examples
%{_bindir}/mako-render
%{py_puresitedir}/mako
%{py_puresitedir}/Mako*

%files -n python3-mako
%doc python3/CHANGES python3/LICENSE python3/README.rst python3/doc python3/examples
%{py3_puresitedir}/mako
%{py3_puresitedir}/Mako*
%{_bindir}/python3-mako-render 

